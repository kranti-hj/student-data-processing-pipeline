import csv
import json
import logging
import os

from data_generator import generate_student_data
from data_cleaner import clean_student_data
from transformer import transform_student_data


def load_config(config_file):
    """Load configuration from JSON file."""

    with open(config_file, "r", encoding="utf-8") as file:
        return json.load(file)


def setup_logging(log_file):
    """Configure logging."""

    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def save_processed_data(output_file, data):
    """Save processed data into CSV."""

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    if not data:
        logging.warning("No data available to save.")
        return

    fieldnames = data[0].keys()

    with open(
        output_file,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(data)

    logging.info(
        "Processed data saved to %s",
        output_file
    )


def main():

    config = load_config("config/config.json")

    setup_logging(config["log_file"])

    logging.info("========== PIPELINE STARTED ==========")

    print("\nStudent Data Processing Pipeline")
    print("--------------------------------")

    # Step 1: Generate raw data
    print("1. Generating random raw data...")

    generate_student_data(
        config["input_file"],
        config["number_of_records"]
    )

    # Step 2: Clean data
    print("2. Cleaning data...")

    cleaned_data = clean_student_data(
        config["input_file"],
        config["default_age"],
        config["default_attendance"]
    )

    # Step 3: Transform data
    print("3. Transforming data...")

    transformed_data = transform_student_data(
        cleaned_data
    )

    # Step 4: Save output
    print("4. Saving processed data...")

    save_processed_data(
        config["output_file"],
        transformed_data
    )

    logging.info("========== PIPELINE COMPLETED ==========")

    print("\nPipeline completed successfully!")
    print("Raw data     :", config["input_file"])
    print("Processed data:", config["output_file"])
    print("Log file     :", config["log_file"])


if __name__ == "__main__":
    main()