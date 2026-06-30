CREATE TABLE leads
(
    id INT AUTO_INCREMENT PRIMARY KEY,

    lead_token VARCHAR(100) UNIQUE,

    name VARCHAR(100),

    phone VARCHAR(30),

    page_name VARCHAR(255),

    page_url TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE activity_logs
(
    id INT AUTO_INCREMENT PRIMARY KEY,

    lead_token VARCHAR(100),

    event VARCHAR(100),

    activity TEXT,

    ip_address VARCHAR(50),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
