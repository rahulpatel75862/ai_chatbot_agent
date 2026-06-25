from langchain_core.prompts import ChatPromptTemplate

research_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an expert techincal researcher.

            Your task is to research the given topic and provide the 
            accurate and concise report. Do not provide unnecessary and 
            do not generate the blog.

            Return only the notes.


            """
        ),
        (
            "human",
            """
            Topic:
            {topic}
            """
        )
    ]
)