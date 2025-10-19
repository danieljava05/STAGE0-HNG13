from fastapi import FastAPI,Request
from contextlib import asynccontextmanager
from src.route.route import factRouter
from slowapi.middleware import SlowAPIMiddleware
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded
from fastapi.middleware.cors import CORSMiddleware
from src.limiter_setup import limiter as lt





@asynccontextmanager
async def life_span(app:FastAPI):
    print("server started .....")
    yield
    print("Server is shuting down!!!")

version ="v1"
app = FastAPI(
    title ="STAGE0-HNG13",
    description ="An API that get data from external API(FACT)",
    version=version,
    lifespan= life_span
)
app.state.limiter = lt

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_middleware(SlowAPIMiddleware)

@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": "Too many requests, please try again later."}
    )




app.include_router(factRouter,prefix=f"/api/{version}/fact")

