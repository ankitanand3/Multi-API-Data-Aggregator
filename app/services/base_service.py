from abc import ABC, abstractmethod

class BaseService(ABC):
    def __init__(self, name: str, delay: float = 1.0):
        self.name = name
        self.delay = delay

    @abstractmethod
    def fetch_sync(self):
        """Synchronous fetch - child must implement"""
        pass

    @abstractmethod
    async def fetch_async(self):
        """Asynchronous fetch - child must implement"""
        pass