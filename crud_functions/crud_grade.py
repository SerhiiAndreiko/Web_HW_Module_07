def create_grade(student_id, subject_id, grade):
    new_grade = Grade(student_id=student_id, subject_id=subject_id, grade=grade)
    session.add(new_grade)
    session.commit()
    print(f'Grade for Student ID: {student_id} in Subject ID: {subject_id} created successfully.')

def read_grade(grade_id):
    grade = session.query(Grade).get(grade_id)
    if grade:
        print(f'Grade ID: {grade.id}, Student ID: {grade.student_id}, Subject ID: {grade.subject_id}, Grade: {grade.grade}')
    else:
        print(f'Grade with ID {grade_id} not found.')

def update_grade(grade_id, new_grade):
    grade = session.query(Grade).get(grade_id)
    if grade:
        grade.grade = new_grade
        session.commit()
        print(f'Grade ID: {grade.id} updated successfully.')
    else:
        print(f'Grade with ID {grade_id} not found.')

def delete_grade(grade_id):
    grade = session.query(Grade).get(grade_id)
    if grade:
        session.delete(grade)
        session.commit()
        print(f'Grade ID: {grade.id} deleted successfully.')
    else:
        print(f'Grade with ID {grade_id} not found.')
