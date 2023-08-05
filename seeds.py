from datetime import datetime, date, timedelta
from random import randint
import sqlite3
from faker import Faker
from pprint import pprint

disciplines = [
    'Вища математика',
    'Геометрія',
    'Програмування',
    'Лінійна алгебра',
    'Теорія ймовірності',
    'Кіт Шредінгера',
    'Англійська',
    'Трудова невчання',
    'Історія України',
    'Креслення'
]

groups = [
    'КММ',
    'ТП-2',
    'ОКР',
    'КХМ',
    'АІ'
]

NUMBER_TEACHERS = 10
NUMBER_STUDENTS = 50
fake_data = Faker()
connect = sqlite3.connect('general_table')
cur = connect.cursor()


def seed_teachers():
    teachers = [fake_data.name() for _ in range(NUMBER_TEACHERS)]
    sql = "INSERT INTO teachers(fullname) VALUES(?);"
    cur.executemany(sql, zip(teachers, ))


def seed_students():
    students = [fake_data.name() for _ in range(NUMBER_STUDENTS)]
    sql = "INSERT INTO students(fullname, group_id) VALUES(?, ?);"
    cur.executemany(sql, zip(students, iter(randint(1, len(groups)) for _ in range(len(students)))))


def seed_disciplines():
    sql = "INSERT INTO disciplines(name, teacher_id) VALUES(?, ?);"
    cur.executemany(sql, zip(disciplines, iter(randint(1, NUMBER_TEACHERS) for _ in range(len(disciplines)))))


def seed_groups():
    sql = "INSERT INTO groups(name) VALUES(?);"
    cur.executemany(sql, zip(groups, ))


def seed_grades():
    start_date = datetime.strptime('2022-09-01', '%Y-%m-%d')
    end_date = datetime.strptime('2023-05-30', '%Y-%m-%d')
    sql = "INSERT INTO grades(discipline_id, student_id, grade, date_of) VALUES(?, ?, ?, ?);"

    def date_list_get(start: date, end: date):
        result = []
        current_date = start
        while current_date <= end:
            if current_date.isoweekday() < 6:
                result.append(current_date)
            current_date += timedelta(1)
        return result

    list_dates = date_list_get(start_date, end_date)

    grades = []
    for day in list_dates:
        random_discipline = randint(1, len(disciplines))
        random_students = [randint(1, NUMBER_STUDENTS) for _ in range(5)]
        for student in random_students:
            grades.append((random_discipline, student, randint(1, 12), day))

    cur.executemany(sql, grades)


def execute_query_from_file(filename):
    with open(filename, "r") as file:
        query = file.read()
        cur.execute(query)
        query_result = cur.fetchall()
        return query_result


if __name__ == '__main__':
    try:
        seed_teachers()
        seed_disciplines()
        seed_groups()
        seed_students()
        seed_grades()
        query_res = execute_query_from_file('query_4.sql')
        pprint(query_res)
        connect.commit()
    except sqlite3.Error as err:
        pprint(err)
    finally:
        connect.close()
