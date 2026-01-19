import time
import asyncio

from app.services.weather_service import WeatherService                             
from app.services.stock_service import StockService                                 
from app.services.news_service import NewsService  

class Aggregator:                                                                   
    def __init__(self, delay: float = 1.0):                                         
        # Create instances of all 3 services                                        
        self.weather = WeatherService(delay=delay)                                  
        self.stock = StockService(delay=delay)                                      
        self.news = NewsService(delay=delay)                                        
                                                                                    
    def fetch_all_sync(self, city: str, company: str, query: str):                  
        """Fetch from all APIs sequentially"""                                      
        start = time.time()                                                         
                                                                                    
        weather_data = self.weather.fetch_sync(city)                                              
        stock_data = self.stock.fetch_sync(company)                   
        news_data = self.news.fetch_sync(query)                                         
                                                                                    
        end = time.time()                                                           
                                                                                    
        return {                                                                    
            "weather": weather_data,                                                
            "stock": stock_data,                                                    
            "news": news_data,                                                      
            "total_time": round(end - start, 2)                                     
        }                                                                           
                                                                                    
    async def fetch_all_async(self, city: str, company: str, query: str):           
        """Fetch from all APIs concurrently"""                                      
        start = time.time()                                                         
                                                                                    
        weather_data, stock_data, news_data = await asyncio.gather(                                   
        self.weather.fetch_async(city),                                                         
        self.stock.fetch_async(company),                                                         
        self.news.fetch_async(query)                                                          
        )                                                               
                                                                                    
        end = time.time()                                                           
                                                                                    
        return {                                                                    
            "weather": weather_data,                                                
            "stock": stock_data,                                                    
            "news": news_data,                                                      
            "total_time": round(end - start, 2)                                     
        }                   