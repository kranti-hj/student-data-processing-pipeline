import csv
import logging


def safe_integer(value, default_value):
    """Convert a value to integer safely."""

    try:
        return int(value)
    except (ValueError, TypeError):
        return default_value


def safe_float(value, default_value):
    """Convert a value to float safely."""

    try:
        return float(value)
    except (ValueError, TypeError):
        return default_value


def clean_student_data(input_file, default_age, default_attendance):
    """Read and clean raw student data."""

    cleaned_data = []

    with open(input_file, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            # Handle missing/invalid age
            original_age = row["age"]

            if original_age == "":
                logging.warning(
                    "Missing age for student %s. Using default age.",
                    row["student_id"]
                )

            age = safe_integer(original_age, default_age)

            # Handle marks
            original_marks = row["marks"]

            marks = safe_float(original_marks, 0)

            if original_marks != "" and marks == 0:
                logging.warning(
                    "Invalid marks for student %s. Using 0.",
                    row["student_id"]
                )

            # Keep marks within valid range
            if marks < 0:
                marks = 0

            if marks > 100:
                marks = 100

            # Handle attendance
            original_attendance = row["attendance"]

            if original_attendance == "":
                logging.warning(
                    "Missing attendance for student %s. Using default.",
                    row["student_id"]
                )

            attendance = safe_float(
                original_attendance,
                default_attendance
            )

            # Keep attendance within valid range
            if attendance < 0:
                attendance = 0

            if attendance > 100:
                attendance = 100

            cleaned_row = {
                "student_id": row["student_id"],
                "name": row["name"].strip(),
                "age": age,
                "course": row["course"].strip().upper(),
                "marks": marks,
                "attendance": attendance
            }

            cleaned_data.append(cleaned_row)

    logging.info(
        "Data cleaning completed. Records processed: %s",
        len(cleaned_data)
    )

    return cleaned_data