"""
🧠 WHAT ARE EMBEDDINGS?
Think of embeddings as a "GPS for meaning":

Text gets converted into numbers (coordinates)
Similar meanings get similar coordinates
Computer can now measure "distance" between meanings
Example - Your search "forgot my password" becomes:
→ [0.2, 0.8, 0.3, ...] (384 numbers)

🎓 HOW DO MODELS LEARN MEANING?
Models learn like children learning language:

See "reset password", "forgot password", "change password"
Learn these all relate to password problems
Assign them similar number patterns
✨ Real Magic - Different words, same meaning:
"forgot my password" ≈ "account recovery"
"vacation days" ≈ "PTO" ≈ "annual leave"
"work from home" ≈ "remote work" ≈ "WFH"
💡 KEY INSIGHT:

Embeddings finally let computers understand that: "I can't log in" and "authentication failed" are talking about the SAME PROBLEM - even with ZERO common words!

This is what makes semantic search so powerful!
"""

#!/usr/bin/env python3
"""
🧠 Task 1: Embeddings - Teaching Computers to Understand Meaning
"""

import os
from sentence_transformers import SentenceTransformer, util

def main():
    # TODO 1: Initialize model that converts text → meaningful numbers
    model = SentenceTransformer("all-MiniLM-L6-v2", local_files_only=True)

    # Scenario: User searching documentation
    query = "forgot my password"

    docs = [
        "Password recovery: Use the 'Reset Password' link on login page",
        "Vacation policy: Request time off 2 weeks in advance",
        "Account security: Enable two-factor authentication",
        "Login help: Contact IT if you cannot access your account"
    ]

    # TODO 2: Convert query and docs to embeddings
    query_emb = model.encode(query)
    doc_embs = model.encode(docs)

    # TODO 3: Find semantic matches
    scores = util.cos_sim(query_emb, doc_embs)[0]

    print(f"Query: '{query}'\n")
    print("Results (score > 0.3 = relevant):")
    for doc, score in zip(docs, scores):
        marker = "✅" if score > 0.3 else "  "
        print(f"{marker} [{score:.2f}] {doc}")

    print("\n💡 Notice: Found 'Password recovery' and 'Login help'")
    print("   Even though query didn't contain those exact words!")

    os.makedirs("/root/markers", exist_ok=True)
    open("/root/markers/task1_embeddings_complete.txt", "w").write("DONE")

if __name__ == "__main__":
    main()