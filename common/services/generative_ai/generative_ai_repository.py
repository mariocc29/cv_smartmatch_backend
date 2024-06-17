from abc import ABC, abstractmethod

class GenerativeAIRepository(ABC):
  @abstractmethod
  def send(self, prompt: str) -> str:
    pass