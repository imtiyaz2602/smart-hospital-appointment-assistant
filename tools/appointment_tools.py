import sqlite3
from datetime import datetime, timedelta
from database.db import get_connection


def book_appointment(patient_name, doctor_id, appointment_time):

    conn = get_connection()
    cursor = conn.cursor()

    appointment_time = datetime.strptime(appointment_time, "%Y-%m-%d %H:%M")

    # prevent past booking
    if appointment_time < datetime.now():
        return "Cannot book appointment in the past."

    cursor.execute("""
        SELECT * FROM appointments
        WHERE doctor_id=? AND appointment_time=?
    """, (doctor_id, appointment_time))

    existing = cursor.fetchone()

    if existing:
        # suggest next slot
        new_time = appointment_time + timedelta(hours=1)
        return f"Slot already booked. Next available slot: {new_time}"

    cursor.execute("""
        INSERT INTO appointments (patient_name, doctor_id, appointment_time)
        VALUES (?, ?, ?)
    """, (patient_name, doctor_id, appointment_time))

    conn.commit()
    conn.close()

    return "Appointment booked successfully"


def cancel_appointment(patient_name):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM appointments
        WHERE patient_name=?
    """, (patient_name,))

    if cursor.rowcount == 0:
        return "No appointment found."

    conn.commit()
    conn.close()

    return "Appointment cancelled successfully"


def reschedule_appointment(patient_name, new_time):

    conn = get_connection()
    cursor = conn.cursor()

    new_time = datetime.strptime(new_time, "%Y-%m-%d %H:%M")

    cursor.execute("""
        UPDATE appointments
        SET appointment_time=?
        WHERE patient_name=?
    """, (new_time, patient_name))

    if cursor.rowcount == 0:
        return "No appointment found to reschedule."

    conn.commit()
    conn.close()

    return "Appointment rescheduled successfully"