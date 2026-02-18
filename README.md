# 🌤️ Weather Agent - LangGraph Learning Project

> Building AI agents from simple helpers to custom state graphs with conversation memory.

**Framework:** LangGraph + LangChain  
**Models:** Ollama (llama3.2) + Google Gemini  
**Built:** February 2026

---

## 🎯 Two Implementations

This project demonstrates the progression from LangGraph's prebuilt helpers 
to custom StateGraph implementation with conversation memory.

### Simple Version
**File:** `simple_version.py`

Quick setup using `create_react_agent` helper.

**Features:**
- Single weather tool
- Prebuilt ReAct agent
- Basic invoke pattern
- Dual LLM support (Ollama/Gemini)

**Best for:** Quick prototypes, learning basics

---

### Complex Version  
**File:** `complex_version.py`

Custom StateGraph with conversation memory and multi-turn dialogue.

**Features:**
- ✅ Custom StateGraph workflow
- ✅ Conversation memory (remembers context)
- ✅ Multi-turn dialogue support
- ✅ Interactive chat mode
- ✅ Demo mode showing memory in action
- ✅ History viewer
- ✅ Clean, focused implementation

**Best for:** Understanding LangGraph internals, production patterns

---

## 🚀 Quick Start

### Prerequisites

```bash
# 1. Install Ollama
# Download: https://ollama.ai

# 2. Pull model
ollama pull llama3.2

# 3. Install dependencies
pip install -r requirements.txt

# 4. (Optional) For Gemini - create .env:
GOOGLE_API_KEY=your_key_here
```

### Run Simple Version

```bash
python simple_version.py
```

### Run Complex Version

**Interactive mode:**
```bash
python complex_version.py
```

**Demo mode:**
```bash
python complex_version.py --demo
```

---

## 💬 Example: Multi-Turn Conversation

The complex version remembers conversation context:

```
👤 You: What's the weather in Paris?
🤖 Agent: The current weather in Paris is sunny with 
          a temperature of 25°C.

👤 You: What about London?
🤖 Agent: The current weather in London is sunny with 
          a temperature of 25°C.

👤 You: Which city is warmer?
          ↑ Agent remembers we discussed Paris and London!
🤖 Agent: Based on our conversation, both Paris and London 
          have the same temperature of 25°C.
```

**The agent maintains context across turns** using LangGraph's 
MemorySaver checkpointing.

---

## 🏗️ Architecture

### Simple Version
```
User Input
    ↓
create_react_agent (prebuilt)
    ↓
Ollama LLM + Tool
    ↓
Response
```

### Complex Version
```
User Input
    ↓
StateGraph
    ├─ Agent Node (call model)
    ├─ Should Continue? (conditional)
    │   ├─ Tools Node (if tool calls)
    │   └─ END (if done)
    └─ MemorySaver (checkpointing)
    ↓
Response (with context preserved)
```

---

## 🧠 Key Concepts

### From Simple Version:
- LangGraph prebuilt helpers
- Tool definitions with `@tool` decorator
- Basic agent invocation
- LLM model switching

### From Complex Version:
- **StateGraph** - Custom workflow graphs
- **TypedDict** - Typed state management
- **add_messages** - Message list annotations
- **MemorySaver** - Conversation checkpointing
- **Thread IDs** - Multiple conversation support
- **Conditional Edges** - Dynamic routing
- **Multi-turn dialogue** - Context across turns

---

## 🔧 Switching LLMs

Both versions support easy LLM switching:

```python
# Ollama (local, free)
from langchain_ollama import ChatOllama
llm = ChatOllama(model="llama3.2", temperature=0)

# Google Gemini (cloud, needs API key)
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
```

---

## 🌍 Production Integration

Replace the dummy weather function with a real API:

```python
import requests

@tool
def get_current_weather(location: str) -> str:
    """Get real weather from OpenWeatherMap."""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    response = requests.get(url, params={
        "q": location,
        "appid": api_key,
        "units": "metric"
    })
    
    data = response.json()
    return f"Weather in {location}: {data['weather'][0]['description']}, {data['main']['temp']}°C"
```

**Free Weather APIs:**
- [OpenWeatherMap](https://openweathermap.org/api)
- [WeatherAPI](https://www.weatherapi.com/)
- [Open-Meteo](https://open-meteo.com/)

---

## 📦 Project Structure

```
weather-agent/
├── simple_version.py       # Prebuilt helper
├── complex_version.py      # Custom StateGraph + memory
├── requirements.txt        # Dependencies
├── .env.example           # Config template
└── README.md              # This file
```

---

## 🎓 Learning Progression

```
Step 1: simple_version.py
        ↓
      Learn prebuilt helpers
        ↓
Step 2: complex_version.py
        ↓
      Learn StateGraph, memory, multi-turn
```

**Key insight:** The complex version is only ~100 lines but demonstrates 
production patterns - StateGraph, memory persistence, and proper 
conversation flow.

---

## 🔗 Related Projects

- **RAG System** - Document Q&A with retrieval
- **HuggingFace Experiments** - Model inference patterns

---

## 📊 Comparison

| Feature | Simple | Complex            |
|---------|--------|--------------------
| Setup   | Prebuilt| Custom StateGraph |
| Memory  | ❌     | ✅ MemorySaver |
| Multi-turn | ❌ | ✅ |
| History View | ❌ | ✅ |
| Demo Mode | ❌ | ✅ |
| Code Lines | ~40 | ~100 |

---

## 🧪 Testing

**Simple version:**
```bash
python simple_version.py
# Enter: London
# See single response
```

**Complex version - Interactive:**
```bash
python complex_version.py
# Ask about multiple cities
# Ask comparison questions
# See conversation context maintained
```

**Complex version - Demo:**
```bash
python complex_version.py --demo
# Watch automated multi-turn conversation
# Observe memory in action
```

---

## 💡 When To Use Each

**Use Simple Version:**
- Quick prototypes
- Learning LangGraph basics
- Single-turn interactions
- No memory needed

**Use Complex Version:**
- Multi-turn conversations
- Context-aware responses
- Production applications
- Learning LangGraph internals

---

## 👤 Author

**Steven**  
Learning progression: Prebuilt helpers → Custom state graphs

**Technologies:**
- LangGraph for agent orchestration
- LangChain for tool integration  
- Ollama for local inference
- Google Gemini for cloud inference

---

## 📝 Notes

This project shows learning progression in building AI agents.
The complex version demonstrates that production patterns (StateGraph,
memory, multi-turn) can be implemented cleanly in ~100 lines.

Both versions are suitable for their respective use cases.
The key is understanding when to use prebuilt helpers vs. 
custom implementations.