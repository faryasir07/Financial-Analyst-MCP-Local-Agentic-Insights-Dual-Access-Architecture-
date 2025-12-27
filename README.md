# 📈 Financial Analyst MCP: 

### Local Agentic Insights:

A powerful Model Context Protocol (MCP) server that enables LLMs to perform live financial analysis and data visualization on your local machine. This project bridges the gap between high-speed cloud intelligence (Groq / OpenAI) and local Python execution.


## 🌟 Key Features :

1)Dual-Access Architecture:Runs seamlessly with LangGraph (local client) and the ChatGPT Desktop app (remote client via ngrok).

2)Agentic Code Execution: The agent doesn't just "talk" about stocks; it writes, saves, and executes real Python code using yfinance and matplotlib.

3)Standardized Protocol: Built on the FastMCP framework for reliable, typed tool-calling.

4)Zero-UI Visualization: Automatically generates and saves visual charts (```plot.png```) directly to your workspace.


## 🏗️ Architecture

1)The system operates using a Server-Client model:

2)The Server (```mcp_server.py```): A FastMCP instance that exposes a save_and_run_finance_code tool. It listens on port 8000 using the SSE (Server-Sent Events) transport.

3)The Bridge (ngrok): Tunnels the local SSE port to a public URL so ChatGPT Desktop can safely reach your local tools.

4)The Client (LangGraph): A local stateful agent that uses Groq (gpt-oss-120b) to reason and decide when to trigger the financial tools.


## 🚀 Getting Started

1. Installation

```bash
pip install -r requirements.txt
```

### 2. Environment Setup

Create a ```.env``` file in the root directory:
```bash
GROQ_API_KEY=your_groq_api_key_here
```
### 3.  Running the MCP Server
Start the server in SSE mode to support both local and remote connections:

```bash
python mcp_server.py
```

### 4. Connecting to ChatGPT Desktop (Optional)

To use this as a "Custom Connector" in ChatGPT:

1)Start an ngrok tunnel: ```ngrok http 8000```

2)Copy the ```http``` URL.

In ChatGPT Desktop: Settings > Apps > Create App.

URL: ```https://your-ngrok-url.app/sse``` (Important: add /sse at the end).

## 🛠️ Usage Example
Once the server is live, you can ask your agent:

"Plot the price of Nvidia (NVDA) vs AMD (AMD) over the last 6 months and calculate the moving average."

The agent will:

->Generate a Python script (```analytics.py```).

->Fetch data via ```yfinance```.

->Execute the script locally.

->Produce a file named ```plot.png``` in your folder.


## 🔒 Security Note

This server allows the LLM to execute Python code on your machine via ```subprocess```. While powerful, always run this in a trusted environment. For production use, consider wrapping the execution in a Docker container to isolate the script from your main OS.

## Project Structure

```mcp_server.py```: The FastMCP server definition and tool logic.

```mcp_client.py```: The LangGraph orchestration script.

```analytics.py```: (Generated) The latest script created by the AI.

```plot.png```: (Generated) The visual output of the analysis.

```requirements.txt```:Required libraries to install.

