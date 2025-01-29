from pydantic.v1 import BaseSettings, root_validator

# todo придумать как в новой версии делать

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    UPLOAD_DIR: str


    @root_validator
    def get_database_url(cls, data):
        data['DATABASE_URL'] = f"postgresql+asyncpg://{data['DB_USER']}:{data['DB_PASS']}@{data['DB_HOST']}:{data['DB_PORT']}/{data['DB_NAME']}"
        return data

    class Config:
        env_file = '.env'


settings = Settings()