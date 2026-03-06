import json
import os

MEMORY_FILE = "memory/conversation.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)


def add_message(role, content):
    memory = load_memory()

    memory.append({
        "role": role,
        "content": content
    })

    save_memory(memory)


def get_recent_memory(limit=5):
    memory = load_memory()
    return memory[-limit:]