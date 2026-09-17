import logging


def calculate_grade(marks):
    """Calculate grade based on marks."""

    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def calculate_result(marks):
    """Calculate pass or fail."""

    if marks >= 40:
        return "Pass"

    return "Fail"


def attendance_status(attendance):
    """Check attendance requirement."""

    if attendance >= 75:
        return "Eligible"

    return "Shortage"


def transform_student_data(cleaned_data):
    """Transform cleaned student data."""

    transformed_data = []

    for student in cleaned_data:

        marks = student["marks"]
        attendance = student["attendance"]

        student["percentage"] = round(marks, 2)
        student["grade"] = calculate_grade(marks)
        student["result"] = calculate_result(marks)
        student["attendance_status"] = attendance_status(attendance)

        transformed_data.append(student)

    logging.info(
        "Data transformation completed. Records transformed: %s",
        len(transformed_data)
    )

    return transformed_data