CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT, admin BOOLEAN);

CREATE TABLE courses (id SERIAL PRIMARY KEY, name TEXT UNIQUE);

CREATE TABLE course (id SERIAL PRIMARY KEY, course_id INTEGER REFERENCES courses, user_id INTEGER REFERENCES users);
