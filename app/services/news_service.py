import time
import asyncio
import random
from app.services.base_service import BaseService


class NewsService(BaseService):
    def __init__(self, delay: float = 1.0):
        super().__init__(name="news", delay=delay)

    def fetch_sync(self, query: str):                                                   
        time.sleep(self.delay)                                                          
        headlines = [                                                                   
            f"Breaking: {query} is trending today",                                     
            f"New developments in {query}",                                             
            f"Experts discuss the future of {query}"                                    
        ]                                                                               
        return {                                                                        
            "query": query,                                                             
            "headlines": headlines                                                      
        }                                                                               
                                                                                        
    async def fetch_async(self, query: str):                                            
        await asyncio.sleep(self.delay)                                                 
        headlines = [                                                                   
            f"Breaking: {query} is trending today",                                     
            f"New developments in {query}",                                             
            f"Experts discuss the future of {query}"                                    
        ]                                                                               
        return {                                                                        
            "query": query,                                                             
            "headlines": headlines                                                      
        }              