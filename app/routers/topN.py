from fastapi import APIRouter, status

from app.schemas.data import Input, Output
from app.services.topN import topNService
from app.utils.exception import InvalidParameter, InvalidLengthOfArray

router = APIRouter(
    tags=["top_n"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)

@router.post("/top_n", response_model=Output)
async def create_task(input: Input):
    if input.n <= 0:
        raise InvalidParameter()
    if len(input.arr) < input.n:
        raise InvalidLengthOfArray()

    arr = topNService.search_top_n(input.arr, input.n)
    return {"arr": arr}

