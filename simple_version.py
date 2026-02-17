# weather.py
# A simple version of the weather program that just prints the current weather for a given location.
import os
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent


def get_current_weather(location):
    # This is a placeholder for the actual weather fetching logic.
    # In a real implementation, you would use an API to get the weather data.
    return f"The current weather in {location} is sunny with a temperature of 25°C."


def create_weather_agent():
    # This function is a placeholder for creating an agent that can fetch weather data.
    # In a real implementation, you would set up the agent with the necessary tools and APIs.
    llm = ChatOllama(model="llama3.2",
                     temperature=0,
                     )
    agent_tools = create_react_agent(
        llm=llm,
        tools=get_agent_tools())
    return agent_tools


def main():
    location = input("Enter a location to get the current weather: ")
    weather = get_current_weather(location)
    print(weather)


if __name__ == "__main__":
    main()
