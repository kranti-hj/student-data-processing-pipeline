import csv
import random
import os
import logging


NAMES = [
    "Rahul", "Priya", "Amit", "Sneha", "Raj",
    "Neha", "Rohan", "Anjali", "Kiran", "Pooja"
]

COURSES = [
    "CSE", "ISE", "ECE", "EEE", "ME"
]


def generate_student_data(output_file, number_of_records):
    """Generate random and intentionally messy student data."""

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "student_id",
            "name",
            "age",
            "course",
            "marks",
            "attendance"
        ])

        for student_id in range(1001, 1001 + number_of_records):

            name = random.choice(NAMES)
            course = random.choice(COURSES)

            age = random.randint(18, 25)
            marks = random.randint(20, 100)
            attendance = random.randint(40, 100)

            # Randomly create missing values
            if random.random() < 0.10:
                age = ""

            if random.random() < 0.10:
                attendance = ""

            # Randomly create invalid marks
            if random.random() < 0.08:
                marks = "abc"

            # Randomly create invalid age
            if random.random() < 0.05:
                age = "unknown"

            writer.writerow([
                student_id,
                name,
                age,
                course,
                marks,
                attendance
            ])

    logging.info(
        "Random raw data generated: %s records",
        number_of_records
    )


if __name__ == "__main__":
    generate_student_data("data/raw_students.csv", 30)