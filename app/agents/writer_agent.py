from app.chains.writer_chains import writer_chain
from app.agents.research_agent import research_agent


class writer_agent:

    def GenArticle(self, research_notes):
        try:
            if not research_notes or not research_notes.strip():
                raise ValueError("Research Notes Can not be empty.")
            response = writer_chain.invoke(
                {
                    "research_notes": research_notes
                }
            )
            if not response or not response.content:
                raise ValueError("LLM returning empty response in article generation.")
            
            return response.content.strip()
        except Exception as e:
            raise ValueError(f"Error in generating article: {e}")
        
gen_article = writer_agent()