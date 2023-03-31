from fastapi import APIRouter, status

from app.schemas.data import Input, Output
from app.services.top_n import TopNService

router = APIRouter(
    tags=["top_n"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.post("/top_n", response_model=Output)
async def create_task(input: Input):
    arr = TopNService.search_top_n(input.arr, input.n)
    return {"arr": arr}
