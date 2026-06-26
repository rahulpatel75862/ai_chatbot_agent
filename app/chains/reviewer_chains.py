from app.services.llm_services import LLMService
from app.prompts.reviewer_prompts import reviewer_prompt

reviewer_chain = reviewer_prompt | LLMService.get_llm()