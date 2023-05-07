CREATE TABLE Discipline (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);
CREATE TABLE TimeSlot (
  id SERIAL PRIMARY KEY,
  start_hour INTEGER,
  end_hour INTEGER
);
CREATE TABLE StudyYear (
  id SERIAL PRIMARY KEY,
  number INTEGER
);

CREATE TABLE Teacher (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255)
);
CREATE TABLE Weekday (
  id SERIAL PRIMARY KEY,
  day VARCHAR(255)
);

CREATE TABLE RoomType (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE Room (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  room_type_id INTEGER REFERENCES RoomType(id)
);

CREATE TABLE StudentGroup (
  id SERIAL PRIMARY KEY,
  number INTEGER
);

CREATE TABLE Scheduler (
  id SERIAL PRIMARY KEY
);

CREATE TABLE SemiYear (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE SchedulerEntry (
  id SERIAL PRIMARY KEY,
  weekday_id INTEGER REFERENCES Weekday(id),
  time_slot_id INTEGER REFERENCES TimeSlot(id),
  teacher_id INTEGER REFERENCES Teacher(id),
  discipline_id INTEGER REFERENCES Discipline(id),
  study_year_id INTEGER REFERENCES StudyYear(id),
  semi_year_id INTEGER REFERENCES SemiYear(id),
  student_group_id INTEGER REFERENCES StudentGroup(id),
  scheduler_id INTEGER REFERENCES Scheduler(id)
);

CREATE TABLE Student (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  study_year_id INTEGER REFERENCES StudyYear(id),
  semi_year_id INTEGER REFERENCES SemiYear(id),
  student_group_id INTEGER REFERENCES StudentGroup(id)
);




