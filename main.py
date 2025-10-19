from fastapi import FastAPI,Request
from contextlib import asynccontextmanager
from slowapi.middleware import SlowAPIMiddleware
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter,status
from pydantic import BaseModel
from datetime import datetime, timezone
import httpx
from Config import Config
import logging as log
# rate limiting
from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi.responses import JSONResponse
# from starlette.requests import Request

limiter = Limiter(key_func=get_remote_address)



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
app.state.limiter = limiter

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

#schema



class userData(BaseModel):
    email : str
    name : str
    stack: str

class factResponse(BaseModel):
    status : str
    user : userData
    timestamp : str
    fact : str 

    class Config():
        from_atttributes = True

# repository


log.basicConfig(
            filename="etl.log",
            level=log.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
    )
    

class factRepo() :

    def __log(self,message,level="INFO"):
        if level == "INFO" :
            log.info(message)
        elif level == "WARNING":
            log.warning(message)
        elif level == "ERROR":
            log.error(message)
        print(f"[INFO] {message}")
        return self
    

    async def fetch_fact_data(self,timeout : float = 5.0) -> str:

        try :
            async with httpx.AsyncClient(timeout=timeout) as client:
                fact_url = Config.FACT_URL
                resp = await client.get(fact_url)
                resp.raise_for_status()
                data = resp.json()
                self.__log("Successfully fetch the data")
                return data.get("fact","No fact found")
        except Exception :
            self.__log("Unable to fetch Data","ERROR")
            return  "Unable to fetch data from fact at this moment (Try again later)"

    def current_utc_iso(self)-> str:
        dt = datetime.now(timezone.utc)

        iso = dt.isoformat(timespec="milliseconds").replace("+00:00","Z")
        self.__log("Converted date to iso format")
        return iso

    async def get_profile(self):
        data = await self.fetch_fact_data()
        response = {
            "status": "success",
            "user":{
                "email": Config.EMAIL,
                "name": Config.NAME,
                "stack": Config.STACK
            },
            "timestamp": self.current_utc_iso(),
            "fact": data
        }
        self.__log("Successfully returning the structured JSON Data")

        return response


# route

fact = factRepo()
factRouter = APIRouter(
    tags=["FACT"]
)
@factRouter.get("/me",response_model=factResponse, status_code=status.HTTP_200_OK)
@limiter.limit("5/minute")
async def getFact(request: Request):
    data = await fact.get_profile()
    return data

app.include_router(factRouter,prefix=f"/api/{version}/fact")
