CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    subject TEXT NOT NULL,
    form_link TEXT NOT NULL
);

-- Example initial data
INSERT INTO teachers (name, subject, form_link)
VALUES
('Dr. Sarah Johnson', 'Mathematics', 'https://docs.google.com/forms/d/e/.../viewform'),
('Prof. Michael Chen', 'Computer Science', 'https://docs.google.com/forms/d/e/.../viewform');
