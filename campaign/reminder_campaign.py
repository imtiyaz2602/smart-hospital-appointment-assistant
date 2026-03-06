import sys
import os
from datetime import datetime, timedelta

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.db import get_connection
from voice.text_to_speech import speak


def run_reminder_campaign():

    conn = get_connection()
    cursor = conn.cursor()

    tomorrow = datetime.now() + timedelta(days=1)
    date_str = tomorrow.strftime("%Y-%m-%d")

    cursor.execute("""
        SELECT patient_name, appointment_time
        FROM appointments
        WHERE appointment_time LIKE ?
    """, (f"{date_str}%",))

    rows = cursor.fetchall()

    if not rows:
        print("No reminders today")
        return

    for patient, time in rows:

        message = f"Hello {patient}. Reminder for your appointment tomorrow at {time}"

        print("Outbound call:", message)

        speak(message)


if __name__ == "__main__":
    run_reminder_campaign()