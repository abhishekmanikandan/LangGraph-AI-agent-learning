from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent, tool
import requests

load_dotenv()

@tool()
def get_weather(city: str):
    '''
    This is a tool which accept the city as a parameter to this function and return the weather details and which can 
    be used for the llm agent calls.
    '''
    print("🔨 Tool Called: get_weather", city)
    
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}."
    return "Something went wrong"

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
agent = initialize_agent(tools=[get_weather], llm=llm, agent="zero-shot-react-description", verbose=True)
agent.invoke("Give me a tweet about today's weather in chennai")

# result = llm.invoke("Give me a tweet about today's weather in Chennai")
# print(result)