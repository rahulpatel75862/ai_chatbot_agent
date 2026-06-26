from app.services.llm_services import LLMService
from app.prompts.research_prompts import research_prompt


research_chain = research_prompt | LLMService.get_llm()