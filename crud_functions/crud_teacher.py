from models_for_crud import Teacher 

def create_teacher(name):
    teacher = Teacher(teacher_name=name)
    session.add(teacher)
    session.commit()
    print(f'Teacher {name} created successfully.')

def read_teacher(teacher_id):
    teacher = session.query(teacher).get(teacher_id)
    if teacher:
        print(f'Teacher ID: {teacher.id}, Name: {teacher.teacher_name}')
    else:
        print(f'Teacher with ID {teacher_id} not found.')

def update_teacher(teacher_id, new_name):
    teacher = session.query(Teacher).get(teacher_id)
    if teacher:
        teacher.teacher_name = new_name
        session.commit()
        print(f'Teacher ID: {teacher.id} updated successfully.')
    else:
        print(f'Teacher with ID {teacher_id} not found.')

def delete_teacher(teacher_id):
    teacher = session.query(Teacher).get(teacher_id)
    if teacher:
        session.delete(teacher)
        session.commit()
        print(f'Teacher ID: {teacher.id} deleted successfully.')
    else:
        print(f'Teacher with ID {teacher_id} not found.')
