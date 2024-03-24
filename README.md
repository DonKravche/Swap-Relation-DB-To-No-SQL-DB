# Database Manager

This Python script provides functionality for managing a MongoDB database. It includes methods for adding data, retrieving existing relations between students and advisors, deleting rows, searching documents, updating documents, and listing advisors/students with associated counts.

## Requirements
- Python 3.x
- `pymongo` library
- MongoDB

## Setup
1. Install Python 3.x from [python.org](https://www.python.org/downloads/)
2. Install `pymongo` library using pip:
    ```
    pip install pymongo
    ```
3. Install MongoDB following the instructions on the [official website](https://www.mongodb.com/try/download/community)

## Usage
1. Make sure MongoDB is running on your local machine.
2. Import the `DatabaseManager` class from the script.
3. Create an instance of `DatabaseManager`.
4. Use the provided methods to interact with the MongoDB database.

## Example

```python
from database_manager import DatabaseManager

# Create an instance of DatabaseManager
db_manager = DatabaseManager()

# Add data
db_manager.add_data("students", student_id=1, name="John", surname="Doe", age=25)
db_manager.add_data("advisors", advisor_id=1, name="Jane", surname="Smith", age=30)

# Retrieve existing relations
relations = db_manager.get_existing_relations()
print("Existing Relations:", relations)

# Delete a row
db_manager.delete_row("students", row_id=1)

# Search documents
students = db_manager.search("students", name="John")
print("Search Results for Students:", students)

# Update documents
db_manager.update("advisors", advisor_id=1, name="Jane", surname="Doe", age=35)

# List advisors with associated student counts
advisors_with_counts = db_manager.list_advisors_with_students_count(order_by='ASC')
print("Advisors with Student Counts:", advisors_with_counts)

# List students with associated advisor counts
students_with_counts = db_manager.list_students_with_advisors_count(order_by='DESC')
print("Students with Advisor Counts:", students_with_counts)
```

## Notes
- Ensure that MongoDB is properly configured and running before using this script.
- Make sure to handle exceptions appropriately, especially when dealing with database connections and operations.
- This script assumes a local MongoDB instance running on the default port (27017). Modify the connection parameters accordingly if your MongoDB instance is hosted elsewhere or using a different port.
- This readme assumes basic familiarity with Python and MongoDB.

**Note:** The provided script has been documented for usage, but ensure to thoroughly test it, especially if there are doubts about its functionality.
