CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT, admin BOOLEAN NOT NULL);

CREATE TABLE courses (id SERIAL PRIMARY KEY, name TEXT UNIQUE, course_creator INTEGER REFERENCES users);

CREATE TABLE students_in_course (course_id INTEGER REFERENCES courses ON DELETE CASCADE, user_id INTEGER REFERENCES users ON DELETE CASCADE);

CREATE TABLE tasks (id SERIAL PRIMARY KEY, text_question TEXT, course_id INTEGER REFERENCES courses ON DELETE CASCADE, multiple_choice BOOLEAN);

CREATE TABLE answers (id SERIAL PRIMARY KEY, task_id INTEGER REFERENCES tasks ON DELETE CASCADE, student_id INTEGER REFERENCES users ON DELETE CASCADE, sent_at TIMESTAMP, content TEXT, course_id INTEGER REFERENCES courses ON DELETE CASCADE);

CREATE TABLE course_text (id SERIAL PRIMARY KEY, topic TEXT, course_id INTEGER REFERENCES courses ON DELETE CASCADE, content TEXT);

CREATE TABLE choices (id SERIAL PRIMARY KEY, choice_text TEXT, task_id INTEGER REFERENCES tasks ON DELETE CASCADE);

CREATE TABLE choice_student_answers (choice_id INTEGER REFERENCES choices ON DELETE CASCADE, task_id INTEGER REFERENCES tasks ON DELETE CASCADE, student_id INTEGER REFERENCES users ON DELETE CASCADE);

CREATE TABLE choice_correct_answers (choice_id INTEGER REFERENCES choices ON DELETE CASCADE, task_id INTEGER REFERENCES tasks ON DELETE CASCADE)
