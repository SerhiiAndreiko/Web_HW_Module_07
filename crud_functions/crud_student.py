def create_student(student_name, group_id):
    student = Student(student_name=student_name, group_id=group_id)
    session.add(student)
    session.commit()
    print(f'Student {student_name} created successfully.')

def read_student(student_id):
    student = session.query(Student).get(student_id)
    if student:
        print(f'Student ID: {student.id}, Name: {student.student_name}, Group ID: {student.group_id}')
    else:
        print(f'Student with ID {student_id} not found.')

def update_student(student_id, new_name):
    student = session.query(Student).get(student_id)
    if student:
        student.student_name = new_name
        session.commit()
        print(f'Student ID: {student.id} updated successfully.')
    else:
        print(f'Student with ID {student_id} not found.')

def delete_student(student_id):
    student = session.query(Student).get(student_id)
    if student:
        session.delete(student)
        session.commit()
        print(f'Student ID: {student.id} deleted successfully.')
    else:
        print(f'Student with ID {student_id} not found.')
