import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('teachers.db')
cursor = conn.cursor()

# Create the 'teachers' table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    subject TEXT NOT NULL,
    form_link TEXT NOT NULL
)
''')

# Insert sample teachers (replace links with real ones)
sample_teachers = [
    ('Dr. Sarah Johnson', 'Mathematics', 'https://docs.google.com/forms/d/e/1FAIpQLSdp9W0BRXi-rIx3ZQJZDDz7gDU1Ee2RpCqogVKMl7IVG3X15w/viewform?usp=header'),
    ('Prof. Michael Chen', 'Computer Science', 'https://docs.google.com/forms/d/e/1FAIpQLSdjx26MzkhMNsECW2lRjrTYrYriou4HPp_mPqAzZ2sBIZfk6A/viewform?usp=header'),
    ('Ms. Emily Rodriguez', 'English Literature', 'https://docs.google.com/forms/d/e/1FAIpQLSeUJnQ4n-xf23yjiwt5X2E64DlE_I8Ey7RTh4q02guZeRnefg/viewform?usp=header'),
    ('Dr. James Wilson', 'Physics', 'https://docs.google.com/forms/d/e/1FAIpQLSejlrk1sRHYb0zF-Nd_wC1crWh43wdppL4PIxrRjga_rYP7wA/viewform?usp=header')
]

# Insert sample data only if table is empty
cursor.execute("SELECT COUNT(*) FROM teachers")
count = cursor.fetchone()[0]

if count == 0:
    cursor.executemany('''
        INSERT INTO teachers (name, subject, form_link)
        VALUES (?, ?, ?)
    ''', sample_teachers)
    print("✅ Sample teachers added to database.")
else:
    print("ℹ️ Database already has teachers, skipping insertion.")

# Commit and close
conn.commit()
conn.close()
print("✅ Database initialized successfully.")
