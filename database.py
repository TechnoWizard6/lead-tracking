import os
import mysql.connector


def get_db():

    connection = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )

    return connection


def get_lead_by_token(db, token):

    cursor = db.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM leads
        WHERE lead_token=%s
        LIMIT 1
        """,
        (token,)
    )

    lead = cursor.fetchone()

    cursor.close()

    return lead


def log_activity(
    db,
    lead_token,
    event,
    activity,
    ip_address
):

    cursor = db.cursor()

    cursor.execute(
        """
        INSERT INTO activity_logs
        (
            lead_token,
            event,
            activity,
            ip_address
        )

        VALUES
        (
            %s,
            %s,
            %s,
            %s
        )
        """,
        (
            lead_token,
            event,
            activity,
            ip_address
        )
    )

    db.commit()

    cursor.close()
