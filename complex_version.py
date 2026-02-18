#complex_version.py
"""Multi-turn weather agent using LangGraph.
   
   A learning project demonstrating:
   - Conversation memory across turns
   - Tool calling for weather data
   - Interactive and demo modes
   
   Usage:
     python complex_version.py        # Interactive mode
     python complex_version.py --demo # Run demo
"""

import os
import sys
from typing import Annotated, Sequence, TypedDict, Literal
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import StateGraph, END, START
from langgraph.graph.message import add_messages
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv

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

class AgentState(TypedDict):
    """State of the agent - just the message history."""
    messages: Annotated[Sequence[BaseMessage], add_messages]

@tool
def get_current_weather(location: str) -> str:
    """Get the current weather in a given location."""
    return f"The current weather in {location} is sunny with a temperature of 25°C."

def create_weather_agent():
    """Create an agent that can fetch weather data."""
    
    tools = [get_current_weather]
    llm_with_tools = llm.bind_tools(tools)

    def call_model(state: AgentState):
        """Call the model with the current messages."""
        response = llm_with_tools.invoke(state["messages"])
        return {"messages": [response]}
    
    def should_continue(state: AgentState) -> Literal["tools", END]:
        """Check if we need to call tools or can respond directly."""
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

    # Add memory for conversation persistence
    memory = MemorySaver()

    # Compile and return the agent
    agent = workflow.compile(checkpointer=memory)
    return agent

def run_conversation_turn(agent, query: str, thread_id: str = "1"):
    """Run a single turn of the conversation."""
    try:
        config = {"configurable": {"thread_id": thread_id}}
        response = agent.invoke({
            "messages": [HumanMessage(content=query)]
        }, config=config)
        return response["messages"][-1].content
    except Exception as e:            
        print(f"Error: {e}")
        return "Sorry, I encountered an error."

def view_conversation_history(agent, thread_id: str):
    """View the conversation history for a thread."""
    try:
        state = agent.get_state({"configurable": {"thread_id": thread_id}})
        
        print("\nConversation History:")
        for i, msg in enumerate(state.values["messages"]):
            role = "Human" if isinstance(msg, HumanMessage) else "AI"
            content = msg.content[:100] + "..." if len(msg.content) > 100 else msg.content
            print(f"{i+1}. {role}: {content}")
    except Exception as e:
        print(f"Could not retrieve history: {e}")

def main():
    """Interactive mode with multi-turn conversation."""
    weather_agent = create_weather_agent()
    
    # Use a consistent thread_id for the whole conversation
    thread_id = "user_session_1"
    
    print("\n  Weather Agent (Multi-turn conversation enabled)")
    print("="*60)
    print("Ask about weather in different cities. Type 'quit' to exit.")
    print()
    
    while True:
        user_input = input("\n👤 You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if not user_input:
            continue
        
        try:
            response = run_conversation_turn(
                weather_agent, 
                user_input, 
                thread_id=thread_id
            )
            print(f"\nAgent: {response}")
            
            show_history = input("\nShow conversation history? (y/n): ").lower()
            if show_history == 'y':
                view_conversation_history(weather_agent, thread_id)
                
        except Exception as e:
            print(f"Error: {e}")

def demo_multi_turn():
    """Run a pre-defined demo showing multi-turn capabilities."""
    weather_agent = create_weather_agent()
    thread_id = "demo_conversation"
    
    print("\n📞 DEMO: Multi-turn conversation")
    print("="*60)
    
    queries = [
        "What's the weather in Paris?",
        "What about London?",
        "Which city is warmer?"
    ]
    
    for i, query in enumerate(queries, 1):
        print(f"\nQ{i}: {query}")
        response = run_conversation_turn(weather_agent, query, thread_id)
        print(f"A{i}: {response}")
    
    print("\n" + "="*60)
    print("...Agent remembered the conversation context!")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        demo_multi_turn()
    else:
        main()