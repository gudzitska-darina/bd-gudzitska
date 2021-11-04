import sql_repo


def generate_subjects(num, connection):
    sql_repo.generate_subjects(num, connection)
    print("[INFO] Data for 'subjects' generate successful")


def generate_students(num, connection):
    sql_repo.generate_students(num, connection)
    print("[INFO] Data for 'students' generate successful")


def generate_groups(num, connection):
    sql_repo.generate_groups(num, connection)
    print("[INFO] Data for 'groups' generate successful")


def add_student(data, connection):
    sql_repo.add_student(data, connection)
    print("[INFO] Add to 'students' successful")


def add_group(data, connection):
    sql_repo.add_group(data, connection)
    print("[INFO] Add to 'groups' successful")


def add_subject(data, connection):
    sql_repo.add_subject(data, connection)
    print("[INFO] Add to 'subjects' successful")


def update_group(data, connection):
    sql_repo.update_group(data, connection)
    print("[INFO] Update group successful")


def update_subject(data, connection):
    sql_repo.update_subject(data, connection)
    print("[INFO] Update subject successful")


def update_student(data, connection):
    sql_repo.update_student(data, connection)
    print("[INFO] Update students successful")


def delete_group(data, connection):
    sql_repo.delete_group(data, connection)
    print("[INFO] Delete from 'groups' successful")


def delete_subject(data, connection):
    sql_repo.delete_subject(data, connection)
    print("[INFO] Delete from 'subjects' successful")


def delete_student(data, connection):
    sql_repo.delete_student(data, connection)
    print("[INFO] Delete from 'students' successful")


def search_in_groups(data, connection):
    sql_repo.search_in_groups(data, connection)


def search_in_subjects(data, connection):
    sql_repo.search_in_subjects(data, connection)


def search_in_students(data, connection):
    sql_repo.search_in_students(data, connection)

