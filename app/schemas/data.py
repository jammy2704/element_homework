from pydantic import BaseModel, PositiveInt, validator


class Input(BaseModel):
    n: PositiveInt
    arr: list[int]

    @validator("arr")
    def check_arr_length(cls, v, values):
        if values.get("n") and len(v) < values["n"]:
            raise ValueError("length of array should be more than n")
        return v


class Output(BaseModel):
    arr: list[int]
