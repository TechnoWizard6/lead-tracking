import mysql.connector
import os


def get_db():
        return mysql.connector.connect(
                    host=os.environ.get("MYSQLHOST"),
                    port=int(os.environ.get("MYSQLPORT", 3306)),
                    user=os.environ.get("MYSQLUSER"),
                    password=os.environ.get("MYSQLPASSWORD"),
                    database=os.environ.get("MYSQLDATABASE")
        )


def create_tables(db):
        cursor = db.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                                    lead_token VARCHAR(100) UNIQUE,
                                                name VARCHAR(100),
                                                            phone VARCHAR(30),
                                                                        page_name VARCHAR(255),
                                                                                    page_url TEXT,
                                                                                                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                                                                                                        )
                                                                                                            """)

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS activity_logs (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                                    lead_token VARCHAR(100),
                                                event VARCHAR(100),
                                                            activity TEXT,
                                                                        ip_address VARCHAR(50),
                                                                                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                                                                                            )
                                                                                                """)

    cursor.execute("""
            INSERT IGNORE INTO leads
                        (lead_token, name, phone, page_name, page_url)
                                VALUES
                                            (
                                                            'abc123',
                                                                            'Hii',
                                                                                            'whatsapp:+917057273525',
                                                                                                            'YOO Villas for Hii',
                                                                                                                            'https://6a3d17e4f455624e2c44955a--relaxed-buttercream-4fb006.netlify.app'
                                                                                                                                        )
                                                                                                                                            """)

    db.commit()
    cursor.close()


def get_lead_by_token(db, lead_token):
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM leads WHERE lead_token = %s",
            (lead_token,)
        )
        lead = cursor.fetchone()
        cursor.close()
        return lead


def log_activity(db, lead_token, event, activity, ip_address):
        cursor = db.cursor()
        cursor.execute(
            """
            INSERT INTO activity_logs (lead_token, event, activity, ip_address)
            VALUES (%s, %s, %s, %s)
            """,
            (lead_token, event, activity, ip_address)
        )
        db.commit()
        cursor.close()


# Run table creation on import
try:
        _db = get_db()
        create_tables(_db)
        _db.close()
except Exception as e:
        print(f"Warning: Could not run create_tables on startup: {e}")
