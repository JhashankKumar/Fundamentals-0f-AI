"""
Task 1: Import Required Libraries
Learn what libraries we need for AI API calls.
"""
from openai import OpenAI
import os

"""
Task 2: Initialize the OpenAI Client
Learn how to connect to OpenAI's servers.
"""
# The OpenAI client needs two things:
# 1. API Key - Your authentication (like a password)
# 2. Base URL - Where to send requests (like an address)

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE")
)

"""
Task 3: Making Your First API Call
Understand EVERY part of the chat completion call.
"""

# ==========================================
#
# To make an API call, you MUST provide:
# 1. model - Which AI model to use (required)
# 2. messages - Your conversation with the AI (required)
#
# The messages parameter is a list of dictionaries, each with:
# - role: Who is speaking ("user", "assistant", or "system")
# - content: What they are saying
# ==========================================

response = client.chat.completions.create(
    model="openai/gpt-4.1-mini", 
    messages=[
        {
            "role": "user",
            "content": "Hello AI, please introduce yourself" 
        }
    ]
)


# ==========================================
# REAL RESPONSE OBJECT STRUCTURE
# This is an ACTUAL response from OpenAI:
# ==========================================
"""
ChatCompletion(
    id='gen-1758773976-Ek9OxTgdgkP4Mo3ub6qf',
    choices=[
        Choice(
            finish_reason='stop',
            index=0,
            message=ChatCompletionMessage(
                content="Hello! I'm ChatGPT, an AI language model created by OpenAI. I'm here to help with a wide range of tasks such as answering questions, providing explanations, generating creative content, assisting with writing, and much more. How can I assist you today?",
                role='assistant'
            )
        )
    ],
    created=1758773976,
    model='openai/gpt-4.1-mini',
    object='chat.completion',
    usage=CompletionUsage(
        completion_tokens=55,
        prompt_tokens=13,
        total_tokens=68
    )
)
"""

"""
Task 4: Extracting the AI's Response
Learn the EXACT path to get the AI's answer from the response object.
"""

# ==========================================
# THE MAGIC PATH TO THE AI'S ANSWER
# ==========================================
#
# After making an API call, the AI's text is ALWAYS at:
# response.choices[0].message.content
#
# Let's understand each part:
# ┌─────────┐     response: The complete response object from OpenAI
# │response │
# └────┬────┘
#      │
#      ▼
# ┌─────────┐     .choices: List of possible responses (usually just one)
# │.choices │
# └────┬────┘
#      │
#      ▼
# ┌─────────┐     [0]: Get the first (and typically only) choice
# │  [0]    │
# └────┬────┘
#      │
#      ▼
# ┌─────────┐     .message: The message object containing the response
# │.message │
# └────┬────┘
#      │
#      ▼
# ┌─────────┐     .content: The actual text string from the AI!
# │.content │
# └─────────┘
# ==========================================

ai_text = response.choices[0].message.content 

"""
Task 5: Understanding Tokens and Business Costs
Learn how tokens work and calculate real business costs for AI usage.
"""

# ==========================================
# WHAT ARE TOKENS?
# ==========================================
#
# Think of tokens as "pieces of words" that AI uses:
# - Simple words = 1 token (e.g., "cat", "run")
# - Complex words = multiple tokens (e.g., "unbelievable" = 3 tokens)
# - Rough estimate: 1 token ≈ 4 characters or 0.75 words
#
# The response.usage object tells you EXACTLY how many tokens you used:
# ┌────────────────────────────────────┐
# │ response.usage                      │
# │  ├── prompt_tokens      (input)    │ ← What you asked
# │  ├── completion_tokens  (output)   │ ← What AI answered
# │  └── total_tokens       (sum)      │ ← What you pay for
# └────────────────────────────────────┘
# ==========================================

input_tokens = response.usage.prompt_tokens     
output_tokens = response.usage.completion_tokens   
total_tokens = response.usage.total_tokens  


# ==========================================
# CALCULATING REAL BUSINESS COSTS
# ==========================================
#
# GPT-4.1-mini Official Pricing:
# ┌─────────────────────────────────────┐
# │ Input:  $0.80 per 1M tokens         │
# │         = $0.0008 per 1K tokens     │
# │                                      │
# │ Output: $3.20 per 1M tokens         │
# │         = $0.0032 per 1K tokens     │
# └─────────────────────────────────────┘
#
# Notice: Output costs 4x more than input!
# This is why keeping AI responses concise matters for your budget.
# ==========================================

# GPT-4.1-mini pricing (per 1,000 tokens) - already set for you!
input_price_per_1k = 0.0008   # That's $0.80 per million tokens
output_price_per_1k = 0.0032  # That's $3.20 per million tokens

# Calculate actual costs for this API call
input_cost = (input_tokens / 1000) * input_price_per_1k
output_cost = (output_tokens / 1000) * output_price_per_1k
total_cost = input_cost + output_cost