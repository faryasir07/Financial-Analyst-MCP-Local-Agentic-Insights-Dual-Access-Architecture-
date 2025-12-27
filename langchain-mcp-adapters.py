from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from mcp_server import mcp

from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY=os.getenv('GROQ_API_KEY')

# 1. Setup the Model (Groq)
llm = ChatGroq(
    model="openai/gpt-oss-120b", # Use the specific Groq ID
    temperature=0,
    api_key=GROQ_API_KEY
)

async def run_agent():
    # 1. Connect to your local MCP server
    # Note: Use the full path to your finance_server.py
    client = MultiServerMCPClient({
        "FinancialAnalyst": {
            "command": "python",
            "args": ["mcp_server.py"],
            "transport": "stdio"
        }
    })

    # 2. Grab the tools from the MCP server
    async with client.session(server_name='FinancialAnalyst') as session:
        mcp_tools = await client.get_tools()

        # 4. Create the Graph Agent
        agent = create_react_agent(llm, mcp_tools)

        # 5. Execute
        query = "Plot the price of Bitcoin (BTC-USD) over the last 30 days."
        async for event in agent.astream({"messages": [("user", query)]}):
            print(event)

# Run the async loop
import asyncio
if __name__ == "__main__":
    asyncio.run(run_agent())