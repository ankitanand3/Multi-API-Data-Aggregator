import time
import asyncio
import random
from app.services.base_service import BaseService


class StockService(BaseService):
    def __init__(self, delay: float = 1.0):
        super().__init__(name="stock", delay=delay)

    def fetch_sync(self, company: str):
        time.sleep(self.delay) 
        return {                                                                        
          "company": company,                                                               
          "stock": random.randint(15, 35),                                      
          "unit": "dollar"                                                           
        } 

    async def fetch_async(self, company: str):
        await asyncio.sleep(self.delay) 
        return {                                                                        
          "company": company,                                                               
          "stock": random.randint(15, 35),                                      
          "unit": "dollar"                                                            
        }