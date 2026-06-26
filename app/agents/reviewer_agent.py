from app.chains.reviewer_chains import reviewer_chain

class ReviewerAgent:
    def gen_review(self, article: str):
        try:
            if not article or article.strip():
                raise ValueError("The article is empty")
            response = reviewer_chain.invoke(
                {
                    "final_content": str
                }
            )
            if not response or not response.content:
                raise ValueError("LLM returning empty response in reviewer generation.")
            
            return response.content.strip()
        except Exception as e:
            raise RuntimeError(f"Error in generating Review: {e}")
        
reviewer_agent = ReviewerAgent()