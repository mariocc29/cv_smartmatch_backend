from django.http import HttpResponse
from abc import ABC, abstractmethod

class DocumentGenerator(ABC):
    @abstractmethod
    def generate_document(self) -> str:
        pass
    
    @abstractmethod
    def generate_document(self, rendered_html: str) -> HttpResponse:
        pass