# Smart Hospital Appointment Assistant

## Overview

Smart Hospital Appointment Assistant is an AI-powered voice-based system that helps patients manage hospital appointments through natural conversation.

The assistant allows users to **book, cancel, and reschedule appointments**, detect scheduling conflicts, and receive reminders before their scheduled visits.

The system converts voice input into text using speech recognition, processes requests using an AI reasoning agent, and interacts with a scheduling system to manage appointments efficiently.

The architecture integrates **speech recognition, AI reasoning, appointment tools, memory management, and reminder services** to automate hospital appointment workflows.

This project demonstrates a **modular real-time voice AI pipeline** designed for conversational healthcare applications.

---

## Features

* Voice conversation interface
* AI-driven appointment booking
* Appointment cancellation
* Appointment rescheduling
* Conflict detection for double bookings
* Multilingual detection (English / Hindi / Tamil)
* Conversation memory
* Reminder scheduler for upcoming appointments
* Outbound reminder campaign
* Latency measurement
* FastAPI backend API

---

## System Architecture

The system processes voice requests through multiple stages:

Voice Input
↓
Speech-to-Text (Whisper)
↓
AI Agent (LLM reasoning)
↓
Tool Execution (Appointment Tools)
↓
SQLite Database
↓
Reminder Scheduler / Campaign System
↓
Text-to-Speech
↓
Voice Response

---

## Architecture Diagram

![Architecture](diagrams/architecture.png)

---

## Project Structure

smart-hospital-appointment-assistant

agent/
  voice_agent.py

backend/
  server.py

campaign/
  reminder_campaign.py

scheduler/
  reminder_service.py

database/
  db.py
  init_db.py

memory/
  conversation_memory.py

tools/
  appointment_tools.py

voice/
  microphone_input.py
  speech_to_text.py
  text_to_speech.py
  test_voice_agent.py

run_reminder.py
requirements.txt
README.md

---

## Installation

Install the required dependencies:

pip install -r requirements.txt

---

## Run Voice Agent

Start the voice AI agent:

python voice/test_voice_agent.py

Example voice command:

Book cardiologist tomorrow at 10 for Imran

---

## Run API Server

Start the backend API server:

uvicorn backend.server:app --reload

Open the API documentation in your browser:

http://127.0.0.1:8000/docs

---

## Reminder System

The project includes two reminder mechanisms.

### 1. Reminder Scheduler

Automatically checks upcoming appointments and sends reminders.

Run:

python run_reminder.py

The scheduler scans the database and notifies patients about upcoming appointments.

---

### 2. Outbound Reminder Campaign

Simulates outbound reminder calls to patients who have appointments scheduled for the next day.

Run:

python campaign/reminder_campaign.py

---

## Example Voice Commands

Book appointment:
Book cardiologist tomorrow at 10 for Imran

Cancel appointment:
Cancel my appointment tomorrow

Reschedule appointment:
Reschedule my appointment to 3 PM

---

## Technologies Used

* Python
* FastAPI
* Whisper (Speech Recognition)
* Groq / LLM Agent
* SQLite
* Text-to-Speech (pyttsx3)
* LangDetect

---

## Latency Measurement

The system measures latency across different stages:

* Speech-to-Text
* AI reasoning
* Text-to-Speech

Example output:

Latency Breakdown
STT: 4.2 seconds
Agent: 0.3 seconds
TTS: 2.5 seconds
Total: ~7 seconds

---

## Assignment Coverage

This implementation covers the major requirements of the assignment:

* Voice conversation agent
* Appointment lifecycle management
* Conflict detection
* Multilingual interaction
* Contextual memory
* Reminder scheduler
* Outbound reminder campaigns
* Latency measurement

---

## Author

**Mohammad Imtiyaz Khan**
