
from typing import Annotated, Literal
from pydantic import BaseModel, Field

class IncomingRequests(BaseModel):
    topic: Annotated[
        str,
        Field(min_length = 3, max_length = 200, description="The Topic you want to know.")
    ]

    content_ype: Literal[
        "Linkedin",
        "Instagram",
        "FaceBook"
    ]

    about: Literal[
        "professional",
        "casual",
        "Technical"
    ] = "professional"

    max_words: Annotated[
        int,
        Field(ge=500, le=2000, description="Maximum number of words")
    ]=500

