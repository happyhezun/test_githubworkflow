from enum import Enum

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, EmailStr
from pydantic import constr, conint


class GenderEnum(str, Enum):
    """
    性别枚举
    """
    male = "男"
    femalee = "女"


class User(BaseModel):
    id: int
    name: str = "小懒蛋"
    age: conint(ge=0, le=99)
    email: EmailStr
    signup_ts: Optional[datetime] = None
    friends: List[str] = []
    password: constr(min_length=6, max_length=10)
    phone: constr(pattern=r'^1\d{10}$')
    sex: GenderEnum


if __name__ == '__main__':
    user_data = {
       "id": 123,
        "name": "小懒蛋",
        "age": 20,
        "email": "aaa@aaa.com",
        "signup_ts": '2024-07-19 00:22',
        "friends": ["公众号:海哥Python", "小天才"],
        "password": '123456',
        "phone": '13800000000',
        "sex": "男",
    }

    try:
        user = User(**user_data)
        print(f"User id: {user.id}, User name: {user.name}")
    except ValidationError as e:
        print(f"Validation error: {e.json()}")
