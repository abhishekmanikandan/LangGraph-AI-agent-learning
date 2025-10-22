from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class CountryInfo(BaseModel):
    country: str = Field(..., description="Name of the country")
    capital: str = Field(..., description="Capital city of the country")
    population: int = Field(..., description="Population of the country")
    area: float = Field(..., description="Area of the country in square kilometers")
    languages: list[str] = Field(..., description="List of official languages spoken in the country")

structured_llm = llm.with_structured_output(CountryInfo)

response = structured_llm.invoke("Provide details about Japan")

print(response)