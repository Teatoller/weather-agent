# Weather Agent

An intelligent weather agent powered by LLMs using Ollama and LangChain.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
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

## Usage

Run the simple version of the agent:

```bash
python simple_version.py
```

## Example Output

```
============================================================
Simple Weather Agent
============================================================

Question: What is the current weather in Nairobi?
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