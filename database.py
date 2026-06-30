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
    (
        lead_token,
        name,
        phone,
        page_name,
        page_url
    )
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
