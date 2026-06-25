from pydantic import BaseModel


class Response(BaseModel):
    topic: str
    content_type :str
    generated_content: str
    reviewed: bool
    reviewer_feedback: str