"""
LangGraph Basics: Build Stateful AI Workflows
What is LangGraph?
LangGraph is a framework for building stateful, multi-step AI workflows using graphs. Unlike simple LLM chains, LangGraph gives you explicit control over how data flows through your application, enabling complex decision-making, loops, and conditional routing.

Master the Fundamentals Step by Step
Learn LangGraph progressively - from basic imports to building a complete research assistant with multiple tools.

Your 7-Step Learning Journey
1️⃣
Imports
Foundation setup
2️⃣
Nodes
State functions
3️⃣
Edges
Connect nodes
4️⃣
Complete Flow
Multi-step
5️⃣
Routing
Conditionals
6️⃣
Calculator
LLM tool
7️⃣
Research Agent
Complete AI
Build progressively: Start with imports → End with a complete research assistant!
"""

"""
🧩 LangGraph Building Blocks
THE ESSENTIAL PIECES
Before we dive in, let's understand what we'll be building with:

📦 Imports
• StateGraph (the container)
• END (marks completion)
• TypedDict (defines data)
⚙️ Nodes
• Python functions
• Take state as input
• Return partial updates
🔗 Edges
• Connect nodes together
• Define execution order
• Can be conditional
📊 State
• Data flowing through
• Shared between nodes
• Updated at each step
🎯 SIMPLE EXAMPLE
Think of it like a recipe:
1. Ingredients (State) = Your data
2. Steps (Nodes) = Functions that transform data
3. Instructions (Edges) = "Do this, then that"
4. Recipe Book (StateGraph) = Puts it all together!

✨ You'll build these step by step in the following tasks!
"""

#!/usr/bin/env python3
"""Task 1: Understanding Imports - Setting up LangGraph basics"""

import os

# ╔════════════════════════════════════════╗
# ║     LangGraph Import Structure         ║
# ╠════════════════════════════════════════╣
# ║                                        ║
# ║  langgraph.graph                       ║
# ║      ├── StateGraph (Class)           ║
# ║      │    └─ Creates workflow graphs  ║
# ║      └── END (Constant)               ║
# ║           └─ Marks graph termination  ║
# ║                                        ║
# ║  typing.TypedDict                      ║
# ║      └── For defining State structure ║
# ║           └─ Type-safe state schema   ║
# ║                                        ║
# ╚════════════════════════════════════════╝

print("📚 Task 1: Understanding Imports\n")

# TODO 1: Import StateGraph and END from langgraph.graph
# Hint: from langgraph.graph import StateGraph, END
from langgraph.graph import StateGraph , END  # Replace with StateGraph, END

# TODO 2: Import TypedDict from typing
# Hint: from typing import TypedDict
from typing import TypedDict  # Replace with typing

# TODO 3: Define State with messages list
# Hint: messages should be type list
class State(TypedDict):
    messages: list  # Replace with list
    next_step: str

# Test that imports work
print("Testing imports...")
try:
    # This will only work when TODOs are completed
    test_graph = StateGraph(State)
    print("✅ StateGraph imported successfully!")
    print(f"✅ State has fields: {list(State.__annotations__.keys())}")
    print(f"✅ END constant is available: {END}")
except:
    print("❌ Complete the TODOs to make imports work!")

print("\n" + "=" * 60)
print("💡 KEY CONCEPTS:")
print("- StateGraph: Creates stateful workflow graphs")
print("- END: Marks the final node in a graph")
print("- TypedDict: Defines the structure of our state")
print("- State: Data that flows through all nodes")
print("=" * 60)

os.makedirs("/root/markers", exist_ok=True)
with open("/root/markers/task1_imports_complete.txt", "w") as f:
    f.write("TASK1_COMPLETE")

print("\n✅ Task 1 completed!")