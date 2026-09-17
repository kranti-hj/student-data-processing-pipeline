# Student Data Processing Pipeline

##  Project Overview

The **Student Data Processing Pipeline** is a Python-based data processing project that generates random student data, processes raw CSV data, handles missing and invalid values, transforms the data, and produces a structured output file.

The project demonstrates a basic end-to-end data processing pipeline using Python.

##  Pipeline Flow

```text
Random Data Generator
        ↓
Raw CSV Data
        ↓
Data Cleaning
        ↓
Data Transformation
        ↓
Processed CSV Data
        ↓
Logging
```

##  Objectives

* Generate random student data.
* Read raw data from a CSV file.
* Handle missing values.
* Handle invalid data types.
* Convert values into appropriate data types.
* Handle invalid and out-of-range values.
* Calculate student grades.
* Determine Pass/Fail status.
* Check attendance eligibility.
* Save structured processed data.
* Maintain logs of pipeline operations.
* Use a configuration file for project settings.

##  Project Structure

```text
student_data_processing_pipeline/
│
├── data/
│   ├── raw_students.csv
│   └── processed_students.csv
│
├── logs/
│   └── pipeline.log
│
├── config/
│   └── config.json
│
├── src/
│   ├── __init__.py
│   ├── data_generator.py
│   ├── data_cleaner.py
│   ├── transformer.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

##  Technologies Used

* Python
* CSV
* JSON
* Random
* Logging
* File Handling

## Features

### 1. Random Data Generation

The system automatically generates random student records containing:

* Student ID
* Name
* Age
* Course
* Marks
* Attendance

Some missing and invalid values are intentionally generated to test the data-cleaning process.

### 2. Missing Value Handling

Missing age values are replaced with a default age.

Missing attendance values are replaced with the configured default attendance value.

### 3. Type Conversion

The pipeline converts:

* Age → Integer
* Marks → Float
* Attendance → Float

Invalid values are handled safely instead of stopping the program.

### 4. Data Validation

The pipeline checks marks and attendance values.

Values below 0 are converted to 0.

Values above 100 are limited to 100.

### 5. Data Transformation

The pipeline generates:

* Percentage
* Grade
* Result
* Attendance Status

### 6. Logging

Important operations and warnings are recorded in:

```text
logs/pipeline.log
```

### 7. Configuration Management

Project settings are stored in:

```text
config/config.json
```

This makes it possible to change settings without modifying the main Python code.

##  Installation

### Step 1: Install Python

Install Python 3.x on your computer.

Check the installation:

```bash
python --version
```

### Step 2: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 3: Enter the Project Folder

```bash
cd student_data_processing_pipeline
```

### Step 4: Run the Pipeline

```bash
python src/main.py
```

## 📊 Output

After running the program, the following files are generated:

### Raw Data

```text
data/raw_students.csv
```

### Processed Data

```text
data/processed_students.csv
```

### Log File

```text
logs/pipeline.log
```

 Example Transformation

### Raw Data

| Student |     Age | Marks | Attendance |
| ------- | ------: | ----: | ---------: |
| Rahul   |      21 |    85 |         92 |
| Priya   | Missing |    78 |         88 |
| Amit    | unknown |   abc |         75 |

### Processed Data

| Student | Age | Marks | Grade | Result |
| ------- | --: | ----: | ----- | ------ |
| Rahul   |  21 |    85 | A     | Pass   |
| Priya   |  20 |    78 | B     | Pass   |
| Amit    |  20 |     0 | F     | Fail   |

Learning Outcomes

This project demonstrates:

* Python file handling
* CSV processing
* JSON configuration
* Functions and modules
* Exception handling
* Data cleaning
* Data transformation
* Random data generation
* Logging
* Basic data pipeline design
* Git and GitHub workflow

Author

Kranti Hajare

CSE – Data Science Student

License

This project is created for educational and academic purposes.
