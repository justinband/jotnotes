CREATE DATABASE JotNotes;
\connect jotnotes

CREATE TABLE Notes (
    id SERIAL PRIMARY KEY,
    note TEXT
);