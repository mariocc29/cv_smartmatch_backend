import google.generativeai as genai

from app.initializers.generative_ai import GENERATIVE_AI_API_KEY, GENERATIVE_AI_MODEL
from common.services.generative_ai.generative_ai_repository import GenerativeAIRepository

class GoogleGenerativeAIRepository(GenerativeAIRepository):
  def send(self, prompt: str) -> str:
    genai.configure(api_key=GENERATIVE_AI_API_KEY)
    model = genai.GenerativeModel(GENERATIVE_AI_MODEL)
    response = model.generate_content(prompt)
    return response.text