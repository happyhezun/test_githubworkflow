from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, field_validator, ValidationError

def check_name(v: str) -> str:
    if not v.startswith("小"):
        raise ValueError("must be startswith 小")
    return v


class User(BaseModel):
    id: int
    name: str = "小懒蛋"
    age: int
    email: EmailStr
    signup_ts: Optional[datetime] = None
    friends: List[str] = []
    validate_fields = field_validator("name")(check_name)
    @field_validator("age")
    @classmethod
    def check_age(cls, age):
        if age < 18:
            raise ValueError("用户年龄必须大于18岁")
        return age


if __name__ == '__main__':
    user_data = {
        "id": 123,
        "name": "懒蛋",
        "age": 20,
        "email": "aaa@aaa.com",
        "signup_tsl": '2024-07-19 00:22',
        "friends": ["公号号：海哥python", "小天才", b''],
    }
    try:
        user = User(**user_data)
    except ValidationError as e:
        print(f"Validation error: {e.json()}")
