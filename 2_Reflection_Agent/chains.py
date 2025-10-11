from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

generation_prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a worldclass twitter content creator. You create engaging and trendy tweets on a variety of topics."
        "Generate the best twitter post possible on the given topic by the user. Make sure it is trendy and engaging. "
        "If the user provied a critique, respond with a revised tweet of your previous response."),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

reflection_prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a worldclass twitter influence grading a tweet."
        "Generate critique on the tweet given by the user and suggest improvements. "
        "Always provide with detailed recommendations to improve the tweet including hashtags, emojis, and trends, length and"
        "engagement, style etc. If the tweet is perfect, respond with 'No critique needed'."),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm