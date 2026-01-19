import time
import asyncio
import random
from app.services.base_service import BaseService


class WeatherService(BaseService):
    def __init__(self, delay: float = 1.0):
        super().__init__(name="weather", delay=delay)

    
    def fetch_sync(self, city: str):
        time.sleep(self.delay) 
        return {                                                                        
          "city": city,                                                               
          "temperature": random.randint(15, 35),                                      
          "unit": "celsius"                                                           
        } 

    async def fetch_async(self, city: str):
        await asyncio.sleep(self.delay) 
        return {                                                                        
          "city": city,                                                               
          "temperature": random.randint(15, 35),                                      
          "unit": "celsius"                                                           
        }