import sqlite3
import random
import string

DB_NAME = "company_hr.db"


class ITAgent:

    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()

    def generate_username(self, name: str):

        username = name.lower().replace(" ", "")
        username += str(random.randint(100, 999))

        return username

    def generate_company_email(self, username: str):

        return f"{username}@company.com"

    def generate_temp_password(self):

        chars = string.ascii_letters + string.digits

        return "".join(random.choice(chars) for _ in range(10))

    def save_employee(self, candidate):

        username = self.generate_username(candidate.name)

        company_email = self.generate_company_email(username)

        password = self.generate_temp_password()

        employee_id = f"EMP{random.randint(1000, 9999)}"

        applications = [
            "Company Email",
            "Slack",
            "HR Portal"
        ]

        if (
            "Engineer" in candidate.position
            or "Developer" in candidate.position
            or "AI" in candidate.position
        ):
            applications.extend([
                "GitHub Enterprise",
                "Jira"
            ])

        self.cursor.execute(
            """
            INSERT INTO employees
            (
                employee_id,
                name,
                personal_email,
                corporate_email,
                username,
                position
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                employee_id,
                candidate.name,
                candidate.email,
                company_email,
                username,
                candidate.position
            )
        )

        self.conn.commit()

        return {
            "employee_id": employee_id,
            "username": username,
            "company_email": company_email,
            "temporary_password": password,
            "applications": applications,
            "status": "Account Created"
        }