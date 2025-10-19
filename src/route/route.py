from fastapi import APIRouter,status,Request
from src.Schema.schema import factResponse
from src.Repository.repo import factRepo
# rate limiting
from fastapi.responses import JSONResponse
from src.limiter_setup import limiter
# from starlette.requests import Request




fact = factRepo()
factRouter = APIRouter(
    tags=["FACT"]
)
@factRouter.get("/me",response_model=factResponse, status_code=status.HTTP_200_OK)
@limiter.limit("5/minute")
async def getFact(request: Request):
    data = await fact.get_profile()
    return data