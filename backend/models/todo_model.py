from config.db import get_db_connection


class TodoModel:

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM todos")
        todos = cursor.fetchall()

        for todo in todos:
            if todo["due_date"]:
                todo["due_date"] = todo["due_date"].strftime("%Y-%m-%d")

        cursor.close()
        conn.close()
        return todos

    @staticmethod
    def create(title, priority, due_date):
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO todos (title, priority, is_completed, due_date)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (title, priority, 0, due_date))

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def update_status(todo_id, is_completed):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE todos SET is_completed = %s WHERE id = %s",
            (is_completed, todo_id)
        )

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def update(todo_id, title, priority, due_date):
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            UPDATE todos
            SET title = %s, priority = %s, due_date = %s
            WHERE id = %s
        """
        cursor.execute(query, (title, priority, due_date, todo_id))

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete(todo_id):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM todos WHERE id = %s", (todo_id,))
        conn.commit()

        cursor.close()
        conn.close()
