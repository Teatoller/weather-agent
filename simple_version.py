# weather.py
# A simple version of the weather program that just prints the current weather for a given location.
import os
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

 # Load environment variables from .env file
load_dotenv()

# ── Pick ONE of the two LLM blocks below ───────────────────────────────────
# Initialize the language model
# 1) Ollama (local, no API key needed)
from langchain_ollama import ChatOllama
llm = ChatOllama(model="llama3.2", temperature=0)

# 2) Google Gemini
# from langchain_google_genai import ChatGoogleGenerativeAI
# llm = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash", temperature=0,
#                              google_api_key=os.getenv("GOOGLE_API_KEY"))

# ─────────────────────────────────────────────────────────────────────────────



@tool
def get_current_weather(location: str) -> str:
    """Get the current weather in a given location."""
    # In a real implementation, you would use an API to get the weather data.
    return f"The current weather in {location} is sunny with a temperature of 25°C."


def create_weather_agent():
    """Create an agent that can fetch weather data."""
    # This function is a placeholder for creating an agent that can fetch weather data.
    # In a real implementation, you would set up the agent with the necessary tools and APIs.
    # Create the agent with the tool to get current weather.
    agent_tools = create_react_agent(
        model=llm,
        tools=[get_current_weather],
    )
    
    return agent_tools


def main():
    """Main function to run the weather agent."""
    location = input("Enter a location to get the current weather: ")
    weather_agent = create_weather_agent()

    queries = [
        f"What is the current weather in {location}?",
    ]

    for query in queries:
        print(f"\n{'='*50}")
        print(f"Question: {query}")
        print(f"{'='*50}")

        try:
            response = weather_agent.invoke({"messages": [("user", query)]})
            # The response is expected to be a dictionary with a "messages" key, where the last message contains the final answer.
            final_message = response["messages"][-1].content
            print(f"Response: {final_message}")
        except Exception as e:            
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
