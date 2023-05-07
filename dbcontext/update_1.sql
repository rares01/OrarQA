ALTER TABLE Discipline
ADD COLUMN study_year_id INTEGER REFERENCES StudyYear(id),
ADD COLUMN teacher_id INTEGER REFERENCES Teacher(id);

UPDATE Discipline SET study_year_id = 1, teacher_id = 1;