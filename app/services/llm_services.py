from langchain_openai import ChatOpenAI
from app.config.settings import settings

class LLMService():
    def __init__(self):
        self.llm = ChatOpenAI(
            model=settings.MODEL_NAME,
            api_key=settings.GEMINI_API_KEY,
            base_url=settings.BASE_URL,
            temperature=settings.TEMPERATURE,
            
        )

    def get_llm(self):
        """
        Returns the initialized llm model.
        """
    
llm_service = LLMService()