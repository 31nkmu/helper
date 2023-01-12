from peewee import *
from playhouse.migrate import *
from typing import List

db = PostgresqlDatabase(
    database='test',
    user='hello',
    password='1',
    host='localhost',
    port=5432
)


class Student(Model):
    name = CharField(max_length=50)

    class Meta:
        database = db


class Teacher(Model):
    name = CharField(max_length=30)

    class Meta:
        database = db


class StudentTeacher(Model):
    student = ForeignKeyField(Student, related_name='students', to_field='id', on_delete='cascade')
    teacher = ForeignKeyField(Teacher, related_name='teacher', to_field='id', on_delete='cascade')

    class Meta:
        database = db
        db_table = 'student_teacher'


db.connect()


# Teacher.create_table()
# Student.create_table()
# StudentTeacher.create_table()


# INSERT
class Insert:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def _get_list_dict(self) -> List[dict]:
        res = []
        for item in range(len(list(self.kwargs.values())[0])):
            dict_ = {}
            for k in self.kwargs.keys():
                dict_[k] = self.kwargs[k][item]
            res.append(dict_)
        return res

    def write_data(self, db_name):
        with db.atomic():
            for i in self._get_list_dict():
                db_name.insert_many(i).execute()


# students = Insert(name=['John', 'Sam', 'Bil', 'Amina', 'Din'])
# teachers = Insert(name=['Naruto', 'Pain', 'Nagato', 'Madara'])
# s_t = Insert(student=[1, 2, 3, 4, 4, 1, 2, 5],
#              teacher=[1, 3, 2, 3, 1, 2, 2, 3])
# students.write_data(Student)
# teachers.write_data(Teacher)
# s_t.write_data(StudentTeacher)


# SELECT
query = (StudentTeacher
         .select(Teacher.name.alias('teacher'), Student.name.alias('student'))
         .join(Teacher, on=(StudentTeacher.teacher == Teacher.id))
         .join(Student, on=(StudentTeacher.student == Student.id)))

with db.atomic():
    for data in query.namedtuples():
        pass
# print(data.teacher, data.student)


# ALTER
migrator = PostgresqlMigrator(db)
# migrate(
#     migrator.add_column('students', 'column', CharField(max_length=30, null=True)),
#     migrator.rename_table('student', 'students'),
#     migrator.rename_table('teacher', 'teachers'),
#     migrator.drop_column('student', 'column')
# )


# UPDATE
res = (Teacher
       .update(name='Noma')
       .where(Teacher.id == 1)
       .execute())


# DELETE
# teacher = Teacher().get(Teacher.id == 2)
# teacher.delete_instance()

Teacher.delete().execute()
Student.delete().execute()
StudentTeacher.delete().execute()


db.close()