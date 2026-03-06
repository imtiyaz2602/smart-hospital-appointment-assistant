import sys
import os

# Allow Python to access project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.appointment_tools import book_appointment


result = book_appointment(
    "Imran Khan",
    1,
    "2026-03-06 10:00"
)

print(result)