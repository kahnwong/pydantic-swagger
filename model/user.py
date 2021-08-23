from datetime import datetime
from typing import List
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


class UserResponse(BaseModel):
    status: int
