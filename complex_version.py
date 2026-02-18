# complex_version.py
import os
from typing import Annotated, Sequence, TypedDict, Literal
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import StateGraph, END, START
from langgraph.graph.message import add_messages
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
from dotenv import load_dotenv

load_dotenv()

from langchain_ollama import ChatOllama
llm = ChatOllama(model="llama3.2", temperature=0)

class AgentState(TypedDict):
    """State of the agent."""
    messages: Annotated[Sequence[BaseMessage], add_messages]

@tool
def get_current_weather(location: str) -> str:
    """Get the current weather in a given location."""
    return f"The current weather in {location} is sunny with a temperature of 25°C."

def create_weather_agent():
    """Create an agent that can fetch weather data."""
    
    tools = [get_current_weather]
    llm_with_tools = llm.bind_tools(tools)

    """tool nodes will automatically call the tools 
    and add the tool calls to the messages, so we can 
    check for those to determine whether to continue calling 
    tools or end the agent's execution.
    """
    # Define the function to call the model
    def call_model(state: AgentState):
        """Call the model with the current messages."""
        response = llm_with_tools.invoke(state["messages"])
        return {"messages": [response]}
    
    # Define the function to determine whether to continue calling tools or end
    def should_continue(state: AgentState) -> Literal["tools", END]:
        """Determine whether the agent should continue calling tools or end."""
        last_message = state["messages"][-1]
        if hasattr(last_message, "tool_calls") and last_message.tool_calls:
            return "tools"
        return END
    
    # Build the graph
    workflow = StateGraph(AgentState)
    workflow.add_node("agent", call_model)
    workflow.add_node("tools", ToolNode(tools))
    workflow.add_edge(START, "agent")
    workflow.add_conditional_edges("agent", should_continue)
    workflow.add_edge("tools", "agent")

    # Compile and return the agent
    agent = workflow.compile()
    return agent

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
            response = weather_agent.invoke({
                "messages": [HumanMessage(content=query)]
            })
            final_message = response["messages"][-1].content
            print(f"Response: {final_message}")
        except Exception as e:            
            print(f"Error: {e}")

if __name__ == "__main__":
    main()