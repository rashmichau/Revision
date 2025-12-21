# print("hello world")

# class add:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def addition(self):
#         print(self.a+self.b)

#     def frac(self,other):

    
# c=add(6,8)
# c.addition()
# d=(a/b)+(c/d)
# a=int(input("enter any digit :"))
# b=int(input("enter any digit:"))
# lst=[a if a>b else b]
# print(lst)

# a="rashmi"
# b=a[3::-1]
# print(b)

"""
Simple CLI Chatbot using Hugging Face Transformers
-------------------------------------------------
This script loads Microsoft’s DialoGPT-medium conversational model and lets you
chat with it from the terminal. Perfect for local experimentation or as a
starting point for more advanced LLM-based bots.



Requirements (install once):
    pip install transformers torch sentencepiece accelerate

Usage:
    python chatbot_dialoGPT.py

The first execution will download the ~350‑500 MB model weights to your Hugging
Face cache (~/.cache/huggingface/). After that, the bot starts instantly.

Type "quit" or "exit" to end the conversation.
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def load_model(model_name: str = "microsoft/DialoGPT-medium"):
    """Load tokenizer & model; share via global variables to avoid reload."""
    print("Loading model (", model_name, ")")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return tokenizer, model


def chat_loop(tokenizer, model):
    print("\n🤖 Chatbot ready! Type 'quit' to exit.\n")
    chat_history_ids = None
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in {"quit", "exit"}:
            print("Goodbye!")
            break

        # Encode user input plus end‑of‑sentence token
        new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")

        # Append conversation history (if any) with the new user input
        bot_input_ids = new_input_ids if chat_history_ids is None else torch.cat([chat_history_ids, new_input_ids], dim=-1)

        # Generate bot response
        chat_history_ids = model.generate(
            bot_input_ids,
            max_length=1000,
            pad_token_id=tokenizer.eos_token_id,
            no_repeat_ngram_size=3,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.75,
        )

        # Decode only the new tokens
        response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    tok, mod = load_model()
    chat_loop(tok, mod)
