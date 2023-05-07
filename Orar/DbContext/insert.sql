INSERT INTO Discipline (name)
VALUES ('SD');
-- Insert a row with id=2 and name='Mathematics'
INSERT INTO Discipline (name)
VALUES ('IP');
-- Insert a row with id=3 and name='Physics'
INSERT INTO Discipline (name)
VALUES ('TW');
-- Insert a row with id=4 and name='Chemistry'
INSERT INTO Discipline (name)
VALUES ('BD');


INSERT INTO TimeSlot (start_hour, end_hour)
VALUES (8, 10);
INSERT INTO TimeSlot (start_hour, end_hour)
VALUES (10, 12);
INSERT INTO TimeSlot (start_hour, end_hour)
VALUES (12, 14);
INSERT INTO TimeSlot (start_hour, end_hour)
VALUES (14, 16);
INSERT INTO TimeSlot (start_hour, end_hour)
VALUES (16, 18);
INSERT INTO TimeSlot (start_hour, end_hour)
VALUES (18, 20);



INSERT INTO StudyYear (number)
VALUES (1);
INSERT INTO StudyYear (number)
VALUES (2);
INSERT INTO StudyYear (number)
VALUES (3);



INSERT INTO Teacher (first_name, last_name)
VALUES ('Jane', 'Smith');
INSERT INTO Teacher (first_name, last_name)
VALUES ('John', 'Doe');


INSERT INTO Weekday (day)
VALUES ('Monday');
INSERT INTO Weekday (day)
VALUES ('Tuesday');
INSERT INTO Weekday (day)
VALUES ('Wednesday');
INSERT INTO Weekday (day)
VALUES ('Thursday');
INSERT INTO Weekday (day)
VALUES ('Friday');


INSERT INTO RoomType (name)
VALUES ('Course');
INSERT INTO RoomType (name)
VALUES ('Laboratory');
INSERT INTO RoomType (name)
VALUES ('Seminary');


INSERT INTO Room (name, room_type_id)
VALUES ('A101', 1);
INSERT INTO Room (name, room_type_id)
VALUES ('B203', 2);

INSERT INTO StudentGroup (number)
VALUES (101);
INSERT INTO StudentGroup (number)
VALUES (102);

INSERT INTO SemiYear (name)
VALUES ('A');
INSERT INTO SemiYear (name)
VALUES ('B');
INSERT INTO SemiYear (name)
VALUES ('E');


