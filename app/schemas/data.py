from pydantic import BaseModel
from typing import List

class Input(BaseModel):
    n: int
    arr: List[int]


class Output(BaseModel):
    arr: List[int]
