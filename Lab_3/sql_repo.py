import random

from student import  Student
from base import Session, engine, Base
from subject import Subject
from group import  Group


Base.metadata.create_all(engine)
session = Session()


def add_student(data):
    str1 = str(data).split(' ')
    if not isinstance(str1[2], int):
        if session.get(Group, int(str1[2])) is None:
            print("Not correct data!")
            return
    new_student = Student(str1[0], str1[1], str1[2])
    session.add(new_student)
    session.commit()
    session.close()
    print("[INFO] Add to 'students' successful")


def add_group(data):
    mass = data.split(' ')
    if isinstance(mass[2], int):
        print("Not correct data!")
        return
    new_group = Group(mass[0], mass[1], int(mass[2]))
    session.add(new_group)
    session.commit()
    session.close()
    print("[INFO] Add to 'groups' successful")


def add_subject(data):
    mass = data.split(' ')
    if isinstance(mass[1], int):
        print("Not correct data!")
        return
    new_subject = Subject(mass[0], mass[1])
    session.add(new_subject)
    session.commit()
    session.close()
    print("[INFO] Add to 'subjects' successful")


def update_group(data):
    mass = data.split(' ')
    if session.get(Group, int(mass[0])) is None:
        print("Not correct id!")
        return

    group = session.get(Group, int(mass[0]))
    if mass[1] == "name":
        group.name = mass[2]
    elif mass[1] == "faculty":
        group.faculty = mass[2]
    elif mass[1] == "student_number":
        group.student_number = mass[2]
    else:
        print("No such column")
        return
    session.commit()
    session.close()
    print("[INFO] Update group successful")


def update_subject(data):
    mass = data.split(' ')
    if session.get(Subject, int(mass[0])) is None:
        print("Not correct id!")
        return

    subject = session.get(Subject, int(mass[0]))
    if mass[1] == "name":
        subject.name = mass[2]
    elif mass[1] == "credits":
        subject.credits = mass[2]
    else:
        print("No such column")
        return
    session.commit()
    session.close()
    print("[INFO] Update subject successful")


def update_student(data):
    mass = data.split(' ')
    if session.get(Student, int(mass[0])) is None:
        print("Not correct id!")
        return

    student = session.get(Student, int(mass[0]))
    if mass[1] == "firstname":
        student.firstname = mass[2]
    elif mass[1] == "lastname":
        student.lastname = mass[2]
    elif mass[1] == "group":
        if session.get(Group, int(mass[2])) is None:
            student.group = mass[2]
    else:
        print("No such column")
        return
    session.commit()
    session.close()
    print("[INFO] Update students successful")


def delete_group(data):
    if session.get(Group, int(data)) is None:
        print("Not correct id!")
        return
    session.delete(Group, int(data))
    session.commit()
    session.close()
    print("[INFO] Delete from 'groups' successful")


def delete_subject(data):
    if session.get(Subject, int(data)) is None:
        print("Not correct id!")
        return
    session.delete(Subject, int(data))
    session.commit()
    session.close()
    print("[INFO] Delete from 'subjects' successful")


def delete_student(data):
    if session.get(Student, int(data)) is None:
        print("Not correct id!")
        session.delete(Student, int(data))
        session.commit()
        session.close()
    print("[INFO] Delete from 'students' successful")


def create_index1_group(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE INDEX idx1_group_st_num ON groups USING hash (student_number); 
            SELECT * FROM groups WHERE student_number < 100"""
        )
        c = cursor.fetchall()
    for i in c:
        print("|", i[0], "|", i[1], "|", i[2], "|\n")


def create_index2_group(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE INDEX idx2_group_st_num ON groups USING hash (name); 
            SELECT * FROM groups WHERE student_number > 200 AND name LIKE 'C__'
            ORDER BY name ASC"""
        )
        c = cursor.fetchall()
    for i in c:
        print("|", i[0], "|", i[1], "|", i[2], "|\n")


def create_index1_student(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE INDEX idx1_stud ON students USING hash (lastname); 
            SELECT * FROM students WHERE lastname = '89'
            """
        )
        c = cursor.fetchall()
    for i in c:
        print("|", i[0], "|", i[1], "|", i[2], "|", i[3], "|\n")


def create_index2_student(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE INDEX idx2_stud ON students USING hash (group_id); 
            SELECT * FROM students WHERE group_id BETWEEN 5 AND 10  
            AND lastname = '6789'
            ORDER BY firstname ASC"""
        )
        c = cursor.fetchall()
    for i in c:
        print("|", i[0], "|", i[1], "|", i[2], "|", i[3], "|\n")


def create_ch_tab(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE subjects_audits (
           id INT GENERATED ALWAYS AS IDENTITY,
           subject_id INT NOT NULL,
           name VARCHAR(30) NOT NULL,
           changed_on TIMESTAMP(6) NOT NULL
            )"""
        )


def create_trigger1(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TRIGGER subject_update_trigger
            BEFORE UPDATE
            ON subjects 
            FOR EACH ROW
            EXECUTE PROCEDURE log_name_changes()
            """
        )


def create_trigger1_fun(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE OR REPLACE FUNCTION log_name_changes()
              RETURNS TRIGGER 
              LANGUAGE PLPGSQL
              AS
            $$
            BEGIN
                IF NEW.name <> OLD.name THEN
                     INSERT INTO subjects_audits(subject_id,name,changed_on)
                     VALUES(OLD.id,OLD.name,now());
                END IF;
            
                RETURN NEW;
            END;
            $$"""
        )


def test_trigger1(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """UPDATE subjects SET name = 'qqq', credits = 13 WHERE id = 374741"""
        )
    print("[INFO] Update (trigger) 'subjects' successful")


def create_trigger2(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TRIGGER subject_delete_trigger
            AFTER INSERT
            ON subjects 
            FOR EACH ROW
            EXECUTE PROCEDURE log_named_changes()
            """
        )


def create_trigger2_fun(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE OR REPLACE FUNCTION log_named_changes()
              RETURNS TRIGGER 
              LANGUAGE PLPGSQL
              AS
            $$
            BEGIN
                IF NEW.name <> OLD.name THEN
                     INSERT INTO subjects_audits(subject_id,name,changed_on)
                     VALUES(OLD.id,OLD.name,now());
                END IF;

                RETURN NEW;
            END;
            $$"""
        )


def test_trigger2(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO subjects (name, credits) VALUES('zzz', 13)"""
        )
    print("[INFO] INSERT (trigger) 'subjects' successful")