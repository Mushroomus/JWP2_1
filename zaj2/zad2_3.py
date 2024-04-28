from sqlalchemy import create_engine, Column, Integer, String, text, Float, select
from sqlalchemy.orm import declarative_base, Session


engine = create_engine('sqlite+pysqlite:///:memory:', echo=True, future=True)
Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    grade = Column(Float)


Base.metadata.create_all(engine)


def add_student(session, name, age, grade):
    new_student = Student(name=name, age=age, grade=grade)
    session.add(new_student)
    session.commit()


def update_student_by_id(session, student_id, new_name=None, new_age=None, new_grade=None):
    student = session.execute(select(Student).filter(Student.id == student_id)).scalar_one()
    if new_name:
        student.name = new_name
    if new_age:
        student.age = new_age
    if new_grade:
        student.grade = new_grade
    session.commit()


def delete_student_by_id(session, student_id):
    student = session.execute(select(Student).filter(Student.id == student_id)).scalar_one()
    session.delete(student)
    session.commit()


def show_student_by_id(session, student_id):
    student = session.execute(select(Student).filter(Student.id == student_id)).scalar_one()
    print(f'Student ID: {student.id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}')


def show_all_students(session):
    students = session.execute(text("SELECT * FROM students")).all()
    for student in students:
        print(f'{student.id}, {student.name}, {student.age}, {student.grade}')


with Session(engine) as session:
    add_student(session, "Jan Kowalski", 30, 4.0)
    add_student(session,"Anna Nowak", 25, 3.5)
    add_student(session,"Marek Wiśniewski", 28, 3.8)


with Session(engine) as session:
    show_all_students(session)

    add_student(session, "Igor Ezir", 30, 4.0)
    update_student_by_id(session, 1, new_name="Jan Update", new_age=26, new_grade=4.2)
    delete_student_by_id(session, 2)
    student = show_student_by_id(session, 1)
    show_all_students(session)