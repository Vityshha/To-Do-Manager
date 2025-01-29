from fastapi import APIRouter, HTTPException, status, Response
from app.users.dao import UsersDAO
from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.schemas import SUserLogin, SUserRegister
from datetime import date

router = APIRouter(
    prefix='/auth',
    tags=['Auth'],
)


@router.post('/register', operation_id="register_user")
async def register_user(user_data: SUserRegister):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists.")

    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(
        email=user_data.email,
        hashed_password=hashed_password,
        first_name=user_data.first_name or "",
        last_name=user_data.last_name or "",
        image_id=user_data.image_id if user_data.image_id is not None else 0,
        created_at=date.today()
    )
    return {"detail": "User successfully registered"}


@router.post('/login')
async def login_user(response: Response, user_data: SUserLogin):
    user = await authenticate_user(user_data.email, user_data.hashed_password)
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
async def update_user(user_id: int, user_data: SUserRegister):
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
