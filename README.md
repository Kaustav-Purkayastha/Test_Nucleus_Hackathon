# TEST_NUCLEUS HACKATHON PROJECT

### An Automation Tool for Data Quality Validation:

Welcome to the TestNucleus hackathon project! This tool is designed to automate data quality validation through various tests. Follow the steps below to set up and run the project on your system.

## Prerequisites:

1. **Python**: Ensure you have Python 3.x installed on your system.
2. **Virtual Environment**: It is recommended to use a virtual environment to manage dependencies.

## Setup Instructions:

### 1. Clone the Repository

Clone the Git repository to your local system:

```bash
git clone <repository-url>
```

Navigate into the project directory:

```bash
cd <repository-directory>
```

### 2. Set Up the Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
```
```bash
venv\Scripts\activate
```

### 3. Install Dependencies
Install the required libraries using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database
Run the `setup_database.py` script to set up the initial database schema:

```bash
python setup_database.py
```

### 5. Insert Sample Data
To insert sample data into the database, run the `sample_data.py` script:

```bash
python sample_data.py
```

### 6. Execute Tests
Run the `main.py` script to execute the data quality tests and view the results:

```bash
python main.py
```

### 7. View Data in Tables
To view the data in the test_nucleus database, use the `adhoc_data_view.py` script:

```bash
python adhoc_data_view.py
```

### 8. Modify Database Schema
If you need to make changes to the core database schema, update the files located in the sql folder.


## Project Structure:
* `src/`: Contains the main source code files.
* `main.py`: Entry point for executing tests.
* `setup_database.py`: Script to set up the database schema.
* `sample_data.py`: Script to insert sample data.
* `adhoc_data_view.py`: Script to view data in tables.
* `test_dispatcher.py`: Contains the logic for executing tests.
* `database.py`: Handles database interactions.
* `utils.py`: Contains utility functions for data validation.
* `sql/`: Contains SQL scripts for database schema and data manipulations.
* `requirements.txt`: Lists the project dependencies.

## Contributing:

Feel free to contribute to this project by submitting issues or pull requests. Please follow the project's [coding standards and guidelines](CONTRIBUTING.md).

## License:

This project is licensed under the [MIT License](LICENSE).

For any questions or support, please contact [kaustavpurk2@gmail.com](mailto:kaustavpurk2@gmail.com).
