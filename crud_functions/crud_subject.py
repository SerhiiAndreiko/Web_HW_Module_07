def create_subject(subject_name, teacher_id):
    subject = Subject(subject_name=subject_name, teacher_id=teacher_id)
    session.add(subject)
    session.commit()
    print(f'Subject {subject_name} created successfully.')

def read_subject(subject_id):
    subject = session.query(Subject).get(subject_id)
    if subject:
        print(f'Subject ID: {subject.id}, Name: {subject.subject_name}, Teacher ID: {subject.teacher_id}')
    else:
        print(f'Subject with ID {subject_id} not found.')

def update_subject(subject_id, new_name):
    subject = session.query(Subject).get(subject_id)
    if subject:
        subject.subject_name = new_name
        session.commit()
        print(f'Subject ID: {subject.id} updated successfully.')
    else:
        print(f'Subject with ID {subject_id} not found.')

def delete_subject(subject_id):
    subject = session.query(Subject).get(subject_id)
    if subject:
        session.delete(subject)
        session.commit()
        print(f'Subject ID: {subject.id} deleted successfully.')
    else:
        print(f'Subject with ID {subject_id} not found.')
