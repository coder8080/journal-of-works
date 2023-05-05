import sqlalchemy
from flask import Flask, render_template
from sqlalchemy.orm import Session
from data.db_session import *
from data.users import User
from data.jobs import Jobs
from data.department import Department

db_name = input()

global_init(db_name)
session = create_session()


first_department = session.query(Department).get(1)
user_ids = set([*first_department.members.split(', '), first_department.chief])
for user_id in user_ids:
    sum_worked = 0
    # берём все задачи, где пользователь - тимлид
    for job in session.query(Jobs).all():
        print([el.strip() for
               el in job.collaborators.split(',')])
        if (job.team_leader == user_id or str(user_id) in [el.strip() for
                                                           el in job.collaborators.split(',')])\
                and job.is_finished:
            sum_worked += job.work_size
    # if sum_worked > 25:
    user = session.query(User).get(user_id)
    print(user.surname, user.name, sum_worked)
