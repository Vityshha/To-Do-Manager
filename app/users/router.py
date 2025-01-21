from fastapi import APIRouter, HTTPException, status, Response
from app.users.dao import UsersDAO
from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.schemas import SUserAuth, SUserCreate

router = APIRouter(
    prefix='/auth',
    tags=['Auth'],
)


@router.post('/register')
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500, detail="User already exists.")
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, password=hashed_password)
    return {"detail": "User successfully registered"}



@router.post('/login')
async def login_user(response: Response, user_data: SUserCreate):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password."
        )
    access_token = create_access_token({'sub': user.id})
    response.set_cookie(
        'access_token', access_token, httponly=True, secure=True)
    return {'access_token': access_token}


@router.get('/users')
async def get_users():
    users = await UsersDAO.find_all()
    return users

@router.get('/users/{user_id}')
async def get_user(user_id: int):
    user = await UsersDAO.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put('/users/{user_id}')
async def update_user(user_id: int, user_data: SUserCreate):
    existing_user = await UsersDAO.find_by_id(user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = await UsersDAO.update(
        model_id=user_id,
        email=user_data.email,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        image_id=user_data.image_id,
    )
    return updated_user

@router.delete('/users/{user_id}')
async def delete_user(user_id: int):
    existing_user = await UsersDAO.find_by_id(user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    await UsersDAO.delete(user_id)
    return {"detail": "User successfully deleted"}
