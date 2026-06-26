from app.services.llm_services import LLMService
from app.prompts.writer_prompts import writer_prompt


writer_chain = writer_prompt | LLMService.get_llm()