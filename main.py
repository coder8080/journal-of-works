from flask import Flask, render_template
from sqlalchemy.orm import Session
from data import db_session
from data.users import User
from data.jobs import Job

db_session.global_init('db/database.db')
session = db_session.create_session()

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def index():
    works = []
    for work in session.query(Job).all():
        leader_id = work.team_leader
        leader = session.query(User).filter(User.id == leader_id).first()
        leader_name = leader.name + ' ' + leader.surname
        new_work = work
        new_work.leader_name = leader_name
        works.append(new_work)
    params = {'works': works}
    return render_template('index.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
