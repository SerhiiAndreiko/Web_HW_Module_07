import argparse
from models import *
from crud_functions import *

parser = argparse.ArgumentParser(description='Perform CRUD operations on the database.')

parser.add_argument('operation', choices=['create', 'read', 'update', 'delete'], help='Operation to perform')
parser.add_argument('model', choices=['teacher', 'group', 'student', 'subject', 'grade'], help='Model to operate on')


parser.add_argument('--id', type=int, help='ID of the record')
parser.add_argument('--name', type=str, help='Name for create/update operations')
parser.add_argument('--group_id', type=int, help='Group ID for student creation')
parser.add_argument('--teacher_id', type=int, help='Teacher ID for subject creation')
parser.add_argument('--grade', type=float, help='Grade value for grade creation/update')

args = parser.parse_args()

operation = args.operation
model = args.model

if model == 'teacher':
    if operation == 'create':
        create_teacher(args.name)
    elif operation == 'read':
        read_teacher(args.id)
    elif operation == 'update':
        update_teacher(args.id, args.name)
    elif operation == 'delete':
        delete_teacher(args.id)

elif model == 'group':
    if operation == 'create':
        create_group(args.name)
    elif operation == 'read':
        read_group(args.id)
    elif operation == 'update':
        update_group(args.id, args.name)
    elif operation == 'delete':
        delete_group(args.id)

elif model == 'student':
    if operation == 'create':
        create_student(args.name, args.group_id)
    elif operation == 'read':
        read_student(args.id)
    elif operation == 'update':
        update_student(args.id, args.name)
    elif operation == 'delete':
        delete_student(args.id)

elif model == 'subject':
    if operation == 'create':
        create_subject(args.name, args.teacher_id)
    elif operation == 'read':
        read_subject(args.id)
    elif operation == 'update':
        update_subject(args.id, args.name)
    elif operation == 'delete':
        delete_subject(args.id)

elif model == 'grade':
    if operation == 'create':
        create_grade(args.student_id, args.subject_id, args.grade)
    elif operation == 'read':
        read_grade(args.id)
    elif operation == 'update':
        update_grade(args.id, args.grade)
    elif operation == 'delete':
        delete_grade(args.id)
