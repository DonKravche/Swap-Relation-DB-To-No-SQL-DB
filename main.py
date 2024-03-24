import sqlite3
import json
from pymongo import MongoClient


class DatabaseManager:
    def __init__(self):
        self.client = MongoClient("localhost", 27017)  # Connect to MongoDB
        self.database = self.client["Database"]  # Select "Database" database

    def add_data(self, table_name, **kwargs):
        """Add data to a specified table in MongoDB."""
        self.database[table_name].insert_one(kwargs)

    def get_existing_relations(self):
        """Retrieve existing relations between students and advisors."""
        result = self.database["student_advisor"].find()
        return [(i['student_id'], i['advisor_id'],) for i in result]

    def delete_row(self, table_name, row_id):
        """Delete a row from the specified table based on the provided row_id."""
        if table_name == "advisor":
            self.database[table_name].delete_one({"advisor_id": row_id})
        else:
            self.database[table_name].delete_one({"student_id": row_id})

    def search(self, table_name, **kwargs):
        """Search documents in the specified collection based on provided criteria."""
        query = {}
        for key in kwargs:
            if key in ["student_id", "advisor_id", "name", "surname", "age"]:
                query[key] = kwargs[key]
        result = self.database[table_name].find(query)
        return list(result) if result else []

    def update(self, table_name, **kwargs):
        """Update documents in the specified collection based on provided criteria."""
        id_fields = {'students': 'student_id', 'advisors': 'advisor_id'}
        id_field = id_fields.get(table_name)
        update_query = {key: kwargs[key] for key in kwargs if key in ["name", "surname", "age"]}
        if id_field and update_query:
            filter_query = {id_field: kwargs.get('id')}
            result = self.database[table_name].update_one(filter_query, update_query)
            return result.modified_count
        return 0

    def list_advisors_with_students_count(self, order_by='ASC', **kwargs):
        """List advisors with the count of associated students."""
        advisors = self.database["advisors"].find(**kwargs)
        advisor_student_counts = []
        for advisor in advisors:
            student_count = self.database["student_advisor"].count_documents({"advisor_id": advisor["advisor_id"]})
            advisor_student_counts.append({"advisor_id": advisor["advisor_id"], "name": advisor["name"],
                                           "surname": advisor["surname"], "student_count": student_count})
        advisor_student_counts.sort(key=lambda x: x["student_count"], reverse=(order_by.upper() == "DESC"))
        return advisor_student_counts

    def list_students_with_advisors_count(self, order_by='ASC', **kwargs):
        """List students with the count of associated advisors."""
        students = self.database["students"].find(**kwargs)
        student_advisor_counts = []
        for student in students:
            advisor_count = self.database["student_advisor"].count_documents({"student_id": student["student_id"]})
            student_advisor_counts.append({"student_id": student["student_id"], "name": student["name"],
                                           "surname": student["surname"], "advisor_count": advisor_count})
        student_advisor_counts.sort(key=lambda x: x["advisor_count"], reverse=(order_by.upper() == "DESC"))
        return student_advisor_counts
