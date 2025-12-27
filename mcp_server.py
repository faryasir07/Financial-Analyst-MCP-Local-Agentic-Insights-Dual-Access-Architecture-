from fastmcp import FastMCP
import subprocess
import os

# Initialize the MCP Server
mcp = FastMCP(name="FinancialAnalyst")

@mcp.tool()
def save_and_run_finance_code(python_code: str) -> str:
    """
    Saves the provided code to 'analytics.py' and runs it.
    The script must use yfinance and matplotlib, and save its plot to 'plot.png'.
    """
    file_path = "analytics.py"
    
    # Write the code to a file
    with open(file_path, "w") as f:
        f.write(python_code)
    
    # Run the script
    try:
        # We use 'python' to execute the newly created file
        result = subprocess.run(
            ["python", file_path], 
            capture_output=True, 
            text=True, 
            timeout=30
        )
        
        if result.returncode == 0:
            return f"Success! Output: {result.stdout}. Chart saved as plot.png"
        else:
            return f"Code Error: {result.stderr}"
            
    except Exception as e:
        return f"System Error: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8000)
    