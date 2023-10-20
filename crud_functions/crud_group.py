def create_group(group_name):
    group = Group(group_name=group_name)
    session.add(group)
    session.commit()
    print(f'Group {group_name} created successfully.')

def read_group(group_id):
    group = session.query(Group).get(group_id)
    if group:
        print(f'Group ID: {group.id}, Name: {group.group_name}')
    else:
        print(f'Group with ID {group_id} not found.')

def update_group(group_id, new_name):
    group = session.query(Group).get(group_id)
    if group:
        group.group_name = new_name
        session.commit()
        print(f'Group ID: {group.id} updated successfully.')
    else:
        print(f'Group with ID {group_id} not found.')

def delete_group(group_id):
    group = session.query(Group).get(group_id)
    if group:
        session.delete(group)
        session.commit()
        print(f'Group ID: {group.id} deleted successfully.')
    else:
        print(f'Group with ID {group_id} not found.')
