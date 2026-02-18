# Weather Agent

An intelligent weather agent powered by LLMs using Ollama and LangChain.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Example Output](#example-output)

## Overview

This project demonstrates a weather agent that leverages language models to provide weather information and answers to weather-related queries.

## Prerequisites

- **Ollama**: Download from [https://ollama.ai/](https://ollama.ai/)
- **Python**: 3.8 or higher
- **pip**: Python package manager

## Installation

1. **Install Ollama**
   
   Download and install Ollama from the [official website](https://ollama.ai/)

2. **Create and activate a virtual environment**
```bash
   # Create a virtual environment in your project folder
   python3 -m venv venv
   
   # Activate it
   source venv/bin/activate
```

3. **Pull the model**
```bash
   ollama pull llama3.2
```

4. **Install Python dependencies**
```bash
   pip install -r requirements.txt
```

5. **Deactivate the virtual environment (when done)**
```bash
   deactivate
```

## Configuration

### Using Gemini (Optional)

The agent supports Google Gemini as an alternative LLM. To use it:

1. Go to [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey) and sign in with your Google account.
2. Click **"Create API Key"** and copy the generated key.
3. Create a `.env` file in the project root and add your key:
```env
   GOOGLE_API_KEY=your_api_key_here
```

4. In `simple_version.py`, comment out the Ollama LLM and uncomment the Gemini one:
```python
   llm = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash", temperature=0,
                                google_api_key=os.getenv("GOOGLE_API_KEY"))
```

> **Note:** The free tier of the Gemini API is sufficient for running this project.

## Usage

Both scripts prompt you for a location and return the current weather. Run whichever version you prefer:

**Simple version** — prebuilt agent, minimal setup:
```bash
python simple_version.py
```

**Complex version** — manually constructed StateGraph with full control over agent flow:
```bash
python complex_version.py
```

Both will prompt you to enter a location:
```
Enter a location to get the current weather: Nairobi
```

## Example Output
```
============================================================
Simple Weather Agent
============================================================

Question: What is the current weather in Tokyo?
------------------------------------------------------------
Response: According to the Japan Meteorological Agency, the current weather conditions in Tokyo are:

* Temperature: 25°C (77°F)
* Humidity: 60%
* Wind speed: 15 km/h (9 mph)
* Precipitation: None
* Conditions: Sunny

Please note that these conditions are subject to change and may not be up-to-date. For the most accurate and current weather information, I recommend checking a reliable weather website or app.
============================================================
```
