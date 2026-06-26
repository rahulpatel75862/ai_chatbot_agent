from app.chains.research_chains import research_chain

class ResearchAgent:
    """
    Handles the research generation using research chain
    """

    def generate_research(self, topic: str) -> str:
        
        try:
            response = research_chain.invoke(
                {
                    "topic": str
                }
            )
            if not response or not response.content:
                raise ValueError("LLm sent empty response")
            
            return response.content.strip()
        except Exception as e:
            raise ValueError(f"failed in generating research: {e}")
        

research_agent = ResearchAgent()
