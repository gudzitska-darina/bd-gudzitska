import random


def generate_subjects(num, connection):
    i = 0
    with connection.cursor() as cursor:
        while i <= num:
            cursor.execute(
                """INSERT INTO subjects (name, credits) values(
                    substr('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',((random()*(36-1)+1)::integer),15),
                    trunc(random()*60)::int)"""
            )
            i += 1


def generate_groups(num, connection):
    i = 0
    with connection.cursor() as cursor:
        while i <= num:
            cursor.execute(
                """Insert INTO groups (name, faculty) values(
                chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || trunc(random()*30)::int,
                chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int),
                trunc(random()*980)::int)
                )"""
            )
            i += 1


def generate_students(num, connection):
    i = 0
    min = __getfirstid(connection)
    max = __getcount(connection)
    with connection.cursor() as cursor:
        while i <= num:
            cursor.execute(
                """Insert INTO students (firstname, lastname, group_id) values(
                substr('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',((random()*(36-1)+1)::integer),15),
                substr('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',((random()*(36-1)+1)::integer),10),
                %s)""" % random.randint(min, max)
            )
            i += 1


def __getfirstid(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT id FROM groups
            ORDER BY id ASC
            LIMIT 1"""
        )
        c = cursor.fetchall()
        for i in c:
            min = i[0]
    return min

def __getcount(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT COUNT(*) FROM groups"""
        )
        c = cursor.fetchall()
        for i in c:
            max = i[0]
    return max


def getgroupbyid(id, connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT name FROM groups WHERE id = %s """ % id
        )
        c = cursor.fetchall()
        for i in c:
            getid = i[0]
    return getid


def getsubbyid(id, connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT name FROM subjects WHERE id = %s """ % id
        )
        c = cursor.fetchall()
        for i in c:
            getid = i[0]
    return getid


def getstudbyid(id, connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT firstname FROM students WHERE id = %s """ % id
        )
        c = cursor.fetchall()
        for i in c:
            getid = i[0]
    return getid


def add_student(data, connection):
    str1 = str(data).split(' ')
    if not (isinstance(str1[2], int)):
        if getgroupbyid(int(str1[2]), connection) is None:
            print("Not correct data!")
            return
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO students (firstname, lastname, group_id) VALUES(%s, %s, %s)""",
            (str1[0], str1[1], str1[2])
        )
    print("[INFO] Add to 'students' successful")


def add_group(data, connection):
    mass = data.split(' ')
    if (isinstance(mass[2], int)):
        print("Not correct data!")
        return
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO groups (name, faculty) VALUES(%s, %s)""",
            (mass[0], mass[1], int(mass[2]))
        )
    print("[INFO] Add to 'groups' successful")


def add_subject(data, connection):
    mass = data.split(' ')
    if (isinstance(mass[1], int)):
        print("Not correct data!")
        return
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO subjects (name, credits) VALUES(%s, %s)""",
            (mass[0], mass[1])
        )
    print("[INFO] Add to 'subjects' successful")


def update_group(data, connection):
    mass = data.split(' ')
    check = getgroupbyid(int(mass[0]), connection)
    with connection.cursor() as cursor:
        if check is None:
            print("Not correct id!")
            return
        cursor.execute(
            """UPDATE groups SET name = %s, faculty = %s WHERE id = %s""",
            (mass[1], mass[2], int(mass[0]))
        )
    print("[INFO] Update group successful")


def update_subject(data, connection):
    mass = data.split(' ')
    if getsubbyid(int(mass[0]), connection) is None:
        print("Not correct id!")
        return
    with connection.cursor() as cursor:
        cursor.execute(
            """UPDATE subjects SET name = %s, credits = %s WHERE id = %s""",
            (mass[1], int(mass[2]), int(mass[0]))
        )

    print("[INFO] Update subject successful")


def update_student(data, connection):
    mass = data.split(' ')
    if getstudbyid(int(mass[0]), connection) is None:
        print("Not correct id!")
        return
    if getgroupbyid(mass[3], connection) is None:
        print("Not correct group_id!")
        return
    with connection.cursor() as cursor:
        cursor.execute(
            """UPDATE students SET firstname = %s, lastname = %s group_id = %s WHERE id = %s""",
            (mass[1], mass[2], int(mass[3]), int(mass[0]))
        )
    print("[INFO] Update students successful")


def delete_group(data, connection):
    if getgroupbyid(int(data), connection) is None:
        print("Not correct id!")
        return
    with connection.cursor() as cursor:
        cursor.execute(
            """DELETE FROM groups WHERE id = %s """ % int(data)
        )
    print("[INFO] Delete from 'groups' successful")


def delete_subject(data, connection):
    if getsubbyid(int(data), connection) is None:
        print("Not correct id!")
        return
    with connection.cursor() as cursor:
        cursor.execute(
            """DELETE FROM subjects WHERE id = %s """ % int(data)
        )
    print("[INFO] Delete from 'subjects' successful")


def delete_student(data, connection):
    if getstudbyid(int(data), connection) is None:
        print("Not correct id!")
        return
    with connection.cursor() as cursor:
        cursor.execute(
            """DELETE FROM students WHERE id = %s """ % int(data)
        )
    print("[INFO] Delete from 'students' successful")


def search_in_groups(data, connection):
    data = data.split(' ')
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT * FROM groups WHERE name = '%s' AND faculty = '%s' AND student_number = %s"""
            % (data[0], data[1], int(data[2]))
        )
        c = cursor.fetchall()
        return c


def search_in_subjects(data, connection):
    data = data.split(' ')
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT * FROM subjects WHERE name = '%s' AND credits = %s"""
            % (data[0], int(data[1]))
        )
        c = cursor.fetchall()
        return c


def search_in_students(data, connection):
    data = data.split(' ')
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT * FROM students WHERE firstname = '%s' AND lastname = '%s' AND group_id = %s"""
            % (data[0], data[1], int(data[2]))
        )
        c = cursor.fetchall()
        return c
