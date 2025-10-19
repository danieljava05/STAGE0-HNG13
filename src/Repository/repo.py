from datetime import datetime, timezone
import httpx
from src.Config import Config
import logging as log

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
