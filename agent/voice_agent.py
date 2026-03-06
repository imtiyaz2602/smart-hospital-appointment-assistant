import os
import json
import sys
import re
from dotenv import load_dotenv
from google import genai

# allow imports from project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.appointment_tools import (
    book_appointment,
    cancel_appointment,
    reschedule_appointment
)

from memory.conversation_memory import add_message, get_recent_memory

# load environment variables
load_dotenv()

# initialize Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# ---------------------------
# Language Detection
# ---------------------------
def detect_language(text):

    text = text.lower()

    hindi_words = ["namaste", "kal", "doctor", "appointment", "mujhe"]
    tamil_words = ["vanakkam", "nalai", "maruthuv", "doctor"]

    if any(word in text for word in hindi_words):
        return "Hindi"

    if any(word in text for word in tamil_words):
        return "Tamil"

    return "English"


# ---------------------------
# AI Agent
# ---------------------------
def agent_response(user_message):

    # save user message to memory
    add_message("user", user_message)

    # detect language
    language = detect_language(user_message)

    # get conversation history
    history = get_recent_memory()

    history_text = ""
    for msg in history:
        history_text += f"{msg['role']}: {msg['content']}\n"

    prompt = f"""
You are a hospital appointment assistant.

User language: {language}

Conversation history:
{history_text}

User request: {user_message}

Decide the action.

Actions:
1. book
2. cancel
3. reschedule
4. general

Respond ONLY in JSON format like:

{{
"action": "book",
"patient_name": "name",
"doctor_id": 1,
"time": "YYYY-MM-DD HH:MM"
}}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        ai_text = response.text.strip()

        print("AI RAW RESPONSE:", ai_text)

    except Exception as e:
        return f"AI error: {e}"

    # ---------------------------
    # Extract JSON safely
    # ---------------------------

    match = re.search(r"\{.*?\}", ai_text, re.DOTALL)

    if not match:
        return "AI response parsing failed"

    json_text = match.group()

    try:
        data = json.loads(json_text)
    except Exception:
        return "AI response parsing failed"

    action = data.get("action")

    # ---------------------------
    # Tool execution
    # ---------------------------

    if action == "book":

        patient = data.get("patient_name")
        doctor_id = data.get("doctor_id")
        time = data.get("time")

        result = book_appointment(patient, doctor_id, time)

    elif action == "cancel":

        patient = data.get("patient_name")

        result = cancel_appointment(patient)

    elif action == "reschedule":

        patient = data.get("patient_name")
        time = data.get("time")

        result = reschedule_appointment(patient, time)

    else:

        result = "I can help with booking, cancelling, or rescheduling appointments."

    # save AI response to memory
    add_message("assistant", result)

    return result