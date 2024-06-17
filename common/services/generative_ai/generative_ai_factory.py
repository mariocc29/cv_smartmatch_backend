from app.initializers.generative_ai import GENERATIVE_AI_ENGINE
from common.services.generative_ai.generative_ai_repository import GenerativeAIRepository
from common.services.generative_ai.google_generative_ai_repository import GoogleGenerativeAIRepository

class GenerativeAIFactory():
  @staticmethod
  def create() -> GenerativeAIRepository:
    if GENERATIVE_AI_ENGINE == 'google_generativeai':
      return GoogleGenerativeAIRepository()
    else:
      raise ValueError(f"Unsupported summary generation type: {GENERATIVE_AI_ENGINE}")