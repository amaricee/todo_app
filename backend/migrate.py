from config.db import get_db_connection

def migrate():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
        title TEXT NOT NULL,
        priority ENUM('1','2','3') NOT NULL,
        is_completed TINYINT(1) DEFAULT 0,
        due_date DATE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("Succes!")

if __name__ == "__main__":
    migrate()
