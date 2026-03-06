from db import get_connection

def seed_doctors():
    conn = get_connection()
    cursor = conn.cursor()

    doctors = [
        ("Dr Sharma", "Cardiologist"),
        ("Dr Priya", "Dermatologist"),
        ("Dr Kumar", "General Physician"),
        ("Dr Mehta", "Neurologist")
    ]

    cursor.executemany(
        "INSERT INTO doctors (name, specialization) VALUES (?, ?)",
        doctors
    )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed_doctors()
    print("Doctors added")