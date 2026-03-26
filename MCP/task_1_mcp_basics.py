"""
Advanced MCP Concepts: Extend LangGraph with External Tools
What is MCP?
Model Context Protocol (MCP) is an open protocol for connecting AI to external tools. Think of it as a USB port for AI - a standardized way for models to interact with databases, APIs, and services.

Build on Your LangGraph Knowledge
Extend your LangGraph agents with MCP servers - from simple calculator tools to orchestrating multiple services.

Your 3-Step MCP Journey
📡
MCP Basics
Create server
🔌
Integration
Connect to LangGraph
🌐
Multi-Server
Orchestrate tools
From simple tools to multi-server orchestration - Master MCP!
"""

"""
Understanding MCP Architecture
THE MCP ECOSYSTEM
MCP creates a bridge between AI and external tools:

🤖
AI Assistant
(LangGraph)
MCP Protocol
stdio • SSE • HTTP
🔧
MCP Server
(Your Tools)
📦 MCP Server
• Exposes tools
• Defines schemas
• Handles requests
🔧 Tools
• Functions with @tool
• Input parameters
• Structured responses
🔌 Integration
• Bind to LLMs
• Route queries
• Handle responses
🎯 Naming
• mcp__server__tool
• Consistent pattern
• Clear hierarchy
🎯 SIMPLE EXAMPLE
Think of MCP like USB devices:
1. USB Port (MCP Protocol) = Standard connection
2. Device (MCP Server) = Calculator, Weather, etc.
3. Functions (Tools) = What the device can do
4. Computer (LangGraph) = Uses the devices!
"""

"""
📡 Task 1: Understanding MCP Basics
🎯 Create Your First MCP Server
📁 Select task_1_mcp_basics.py from the explorer

✏️ Complete the TODOs:

Line 65: Initialize FastMCP server: "Calculator"
Line 78: Add tool decorator: @mcp.tool()
💡 Key Learning: MCP servers expose tools via decorators, tools are tested directly, production servers run with mcp.run()
🚀 Run Command (Terminal 1)
python3 /root/code/task_1_mcp_basics.py
📋
⚠️ IMPORTANT: Server Runs Continuously for clients to communicate in production environments
After running the command above, the MCP server will start and run continuously. This is normal behavior for MCP servers!

✅ Keep Terminal 1 open - The server must stay running
✅ You'll see "Server ready! Waiting for client connections..."
✅ Task 1 is marked complete automatically before server starts
✅ Open a new terminal (Terminal 2) for the next tasks
❌ Press Ctrl+C after you finish this MCP task as the next task will call the server automatically!
"""


#!/usr/bin/env python3
"""Task 1: Understanding MCP Basics - Your first MCP server"""

import os
import asyncio
from typing import Any

# ╔════════════════════════════════════════╗
# ║     Model Context Protocol (MCP)      ║
# ╚════════════════════════════════════════╝
#
# What is MCP?
# ------------
# MCP is like a USB port for AI - a standard way for
# AI models to connect to external tools and data sources.
#
# ┌─────────────────┐     MCP Protocol    ┌─────────────────┐
# │   AI Assistant  │◄────────────────────►│   MCP Server    │
# │   (LangGraph)   │   stdio/SSE/HTTP    │  (Your Tools)   │
# └─────────────────┘                      └─────────────────┘
#
# MCP Server Components:
# ┌──────────────────────────────────────┐
# │          MCP Server                  │
# ├──────────────────────────────────────┤
# │ 1. Tools (Functions)                 │
# │    └─ add, multiply, divide          │
# │ 2. Resources (Optional)              │
# │    └─ Files, data, configs           │
# │ 3. Prompts (Optional)                │
# │    └─ Pre-defined templates          │
# └──────────────────────────────────────┘

print("📡 Task 1: Understanding MCP Basics\n")

# Import MCP SDK components
try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print("⚠️ Creating mock FastMCP for learning (install 'pip install mcp' for real implementation)")

    # Mock implementation for learning purposes
    class FastMCP:
        """Mock FastMCP server for learning"""
        def __init__(self, name):
            self.name = name
            self.tools = []

        def tool(self):
            """Mock tool decorator"""
            def decorator(func):
                self.tools.append({
                    'name': func.__name__,
                    'function': func
                })
                return func
            return decorator

        def run(self, transport="stdio"):
            print(f"🚀 {self.name} MCP Server would run with {transport} transport")
            print(f"📦 Available tools: {[t['name'] for t in self.tools]}")

# TODO 1: Initialize the MCP server
# Hint: Pass server name to FastMCP with double quotes
mcp = FastMCP("Calculator")  # Replace ___ with Calculator

# Create calculator tools using FastMCP decorators
@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together"""
    result = a + b
    print(f"  🔧 Tool 'add' called with a={a}, b={b}")
    print(f"  ➕ Result: {result}")
    return result

# TODO 2: Create the multiply tool
# Hint: Use @mcp.tool() decorator
@mcp.tool()  # Replace ___ with @mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    result = a * b
    print(f"  🔧 Tool 'multiply' called with a={a}, b={b}")
    print(f"  ✖️ Result: {result}")
    return result

@mcp.tool()
def divide(a: float, b: float) -> str:
    """Divide two numbers with zero check"""
    print(f"  🔧 Tool 'divide' called with a={a}, b={b}")

    if b == 0:
        print("  ❌ Error: Division by zero!")
        return "Error: Cannot divide by zero"

    result = a / b
    print(f"  ➗ Result: {result}")
    return f"{a} ÷ {b} = {result}"

# Test the tools directly (simulating MCP calls)
print("\n" + "=" * 60)
print("TESTING MCP TOOLS:")
print("=" * 60)

def test_tools():
    """Test our MCP tools directly"""

    # Test addition
    print("\nTest 1: Addition")
    result = add(5, 3)
    print(f"Response: {result}")

    # Test multiplication
    print("\nTest 2: Multiplication")
    result = multiply(4, 7)
    print(f"Response: {result}")

    # Test division
    print("\nTest 3: Division")
    result = divide(10, 2)
    print(f"Response: {result}")

    # Test division by zero
    print("\nTest 4: Division by zero")
    result = divide(5, 0)
    print(f"Response: {result}")

# Run the tests
test_tools()

if __name__ == "__main__":
    # Create marker file (must happen before server starts)
    os.makedirs("/root/markers", exist_ok=True)
    with open("/root/markers/task1_mcp_basics_complete.txt", "w") as f:
        f.write("TASK1_COMPLETE")

    print("\n" + "=" * 60)
    print("💡 KEY CONCEPTS:")
    print("- FastMCP creates MCP servers easily")
    print("- @mcp.tool() decorator exposes functions")
    print("- Tools have type hints for parameters")
    print("- Servers can run via stdio, SSE, or HTTP")
    print("- AI models call tools through MCP protocol")
    print("=" * 60)

    print("\n✅ Task 1 complete! MCP tools tested successfully.")
    print("\n" + "=" * 60)
    print("🚀 STARTING MCP SERVER")
    print("=" * 60)
    print("The calculator MCP server is now starting...")
    print("Keep this terminal open - the server will run continuously.")
    print("Use Ctrl+C to stop the server when you're done.")
    print("\nServer ready! Waiting for client connections...")
    print("=" * 60 + "\n")

    # Start the MCP server (blocks indefinitely)
    # This is the production pattern - servers run continuously
    mcp.run(transport="stdio")