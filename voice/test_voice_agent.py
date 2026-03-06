import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from voice.microphone_input import record_audio
from voice.speech_to_text import transcribe_audio
from agent.voice_agent import agent_response
from voice.text_to_speech import speak


if __name__ == "__main__":

    print("Starting Voice AI Agent...")

    # record microphone
    audio_file = record_audio()

    start_time = time.time()

    # speech to text
    text = transcribe_audio(audio_file)

    print("User said:", text)

    # AI reasoning
    response = agent_response(text)

    print("AI:", response)

    # speak response
    speak(response)

    end_time = time.time()

    latency = end_time - start_time

    print(f"Response latency: {latency:.2f} seconds")