from django.core.management.base import BaseCommand
from core.models import TopicContent

class Command(BaseCommand):
    help = 'Seeds the database with comprehensive SQL learning sheets'

    def handle(self, *args, **options):
        topics = [
            {
                "topic": "Basics",
                "category": "sql",
                "data": {
                    "title": "SQL Basics",
                    "description": "SQL (Structured Query Language) is the standard language for interacting with Relational Database Management Systems (RDBMS). It is used to create, read, update, and delete data.",
                    "sections": [
                        {
                            "heading": "Core Concepts",
                            "content": "Understanding the foundation of relational databases is crucial.",
                            "points": [
                                "Tables: Data is stored in tables containing rows (records) and columns (attributes).",
                                "Primary Key: A column (or set of columns) that uniquely identifies each row in a table. It cannot contain NULL values.",
                                "Foreign Key: A column that creates a link between two tables, referencing the Primary Key of another table."
                            ]
                        },
                        {
                            "heading": "Common Data Types",
                            "points": [
                                "INT / INTEGER: Whole numbers.",
                                "VARCHAR(n): Variable-length character strings.",
                                "BOOLEAN: True or False values.",
                                "DATE / TIMESTAMP: Used to store dates and exact times."
                            ]
                        }
                    ],
                    "examples": [
                        {
                            "title": "Creating a Basic Table",
                            "code": "CREATE TABLE Users (\n    id INT PRIMARY KEY,\n    username VARCHAR(50) NOT NULL,\n    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n);",
                            "explanation": "This creates a 'Users' table with a unique ID, a required username, and an automatic timestamp."
                        }
                    ]
                }
            },
            {
                "topic": "Queries and Operations",
                "category": "sql",
                "data": {
                    "title": "Queries and Operations",
                    "description": "Data Manipulation Language (DML) statements are used to query and modify data within your tables.",
                    "sections": [
                        {
                            "heading": "The CRUD Operations",
                            "content": "CRUD stands for Create, Read, Update, and Delete.",
                            "points": [
                                "SELECT (Read): Fetches data from the database.",
                                "INSERT (Create): Adds new rows to a table.",
                                "UPDATE (Update): Modifies existing data.",
                                "DELETE (Delete): Removes rows from a table."
                            ]
                        },
                        {
                            "heading": "Filtering and Sorting",
                            "points": [
                                "WHERE: Filters records based on specific conditions.",
                                "ORDER BY: Sorts the result set in ascending (ASC) or descending (DESC) order.",
                                "LIMIT: Restricts the number of rows returned."
                            ]
                        }
                    ],
                    "examples": [
                        {
                            "title": "Filtering with WHERE and ORDER BY",
                            "code": "SELECT username, email \nFROM Users \nWHERE age >= 18 \nORDER BY created_at DESC \nLIMIT 10;",
                            "explanation": "Fetches the 10 newest adult users, showing only their username and email."
                        }
                    ]
                }
            },
            {
                "topic": "SQL Joins",
                "category": "sql",
                "data": {
                    "title": "SQL Joins",
                    "description": "A JOIN clause is used to combine rows from two or more tables, based on a related column between them.",
                    "sections": [
                        {
                            "heading": "Types of Joins",
                            "content": "Choosing the right join dictates which records are kept when the match fails.",
                            "points": [
                                "INNER JOIN: Returns records that have matching values in both tables.",
                                "LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table. Unmatched right side is NULL.",
                                "RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table.",
                                "FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table."
                            ]
                        }
                    ],
                    "examples": [
                        {
                            "title": "Inner Join Example",
                            "code": "SELECT Orders.order_id, Users.username\nFROM Orders\nINNER JOIN Users ON Orders.user_id = Users.id;",
                            "explanation": "Retrieves the order ID along with the username of the person who placed it. Excludes orders without a matching user."
                        }
                    ]
                }
            },
            {
                "topic": "Aggregate Functions",
                "category": "sql",
                "data": {
                    "title": "Aggregate Functions",
                    "description": "Aggregate functions perform a calculation on a set of values and return a single value. They are often used with the GROUP BY clause.",
                    "sections": [
                        {
                            "heading": "Common Functions",
                            "content": "These are used heavily in data analysis and reporting.",
                            "points": [
                                "COUNT(): Returns the number of rows that match a specified criterion.",
                                "SUM(): Returns the total sum of a numeric column.",
                                "AVG(): Returns the average value of a numeric column.",
                                "MAX() / MIN(): Returns the largest/smallest value."
                            ]
                        },
                        {
                            "heading": "Grouping Data",
                            "points": [
                                "GROUP BY: Groups rows that have the same values into summary rows.",
                                "HAVING: Used instead of WHERE to filter records after an aggregate function has been applied."
                            ]
                        }
                    ],
                    "examples": [
                        {
                            "title": "Grouping and Filtering Aggregates",
                            "code": "SELECT department, COUNT(employee_id) as total_employees, AVG(salary) as avg_salary\nFROM Employees\nGROUP BY department\nHAVING COUNT(employee_id) > 5;",
                            "explanation": "Calculates the number of employees and average salary per department, but only shows departments with more than 5 employees."
                        }
                    ]
                }
            }
        ]

        for item in topics:
            TopicContent.objects.update_or_create(
                topic_name=item['topic'],
                category=item['category'],
                defaults={'content_data': item['data']}
            )
        
        self.stdout.write(self.style.SUCCESS("Successfully seeded comprehensive SQL sheets!"))