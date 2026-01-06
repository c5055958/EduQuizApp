from werkzeug.security import generate_password_hash
from db.db import get_db_connection

conn = get_db_connection()

admin_password = generate_password_hash("admin123")

conn.execute("""
INSERT OR IGNORE INTO users (name, email, password, role)
VALUES (?, ?, ?, ?)
""", ("Admin", "admin@example.com", admin_password, "admin"))

conn.commit()
conn.close()

print("Admin created successfully")