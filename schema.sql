CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT, admin BOOLEAN NOT NULL);

CREATE TABLE courses (id SERIAL PRIMARY KEY, name TEXT UNIQUE);

CREATE TABLE students_in_course (course_id INTEGER REFERENCES courses, user_id INTEGER REFERENCES users);

CREATE TABLE tasks (id SERIAL PRIMARY KEY, text_question TEXT, course_id INTEGER REFERENCES courses);

CREATE TABLE answers (id SERIAL PRIMARY KEY, task_id INTEGER REFERENCES tasks, task_topic TEXT, student_id INTEGER REFERENCES users, sent_at TIMESTAMP, content TEXT);

CREATE TABLE course_text (id SERIAL PRIMARY KEY, topic TEXT, course_id INTEGER REFERENCES courses, content TEXT)
