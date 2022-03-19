from flask import render_template, redirect, url_for
from app import app, db
from forms import StudentForm, SubjectForm
from models import Subjects, Students


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form = StudentForm()
    form.subject.choices = [(subject.id, subject.name) for subject in Subjects.query.order_by(Subjects.name).all()]
    students = Students.query.order_by(Students.name).all()  # Получаю всех студентов из БД
    if form.validate_on_submit():
        student = Students(
            name=form.name.data,
            birth_date=form.birth_date.data,
            mark=form.mark.data,
            subject_id=form.subject.data,
            status=form.status.data
        )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('add_student'))
    return render_template('add_student.html', form=form, items=students)


@app.route('/add_subject', methods=['GET', 'POST'])
def add_subject():
    form = SubjectForm()
    subjects = Subjects.query.order_by(Subjects.name).all()  # Получаю все предметы из БД
    if form.validate_on_submit():
        subject = Subjects(
            name=form.name.data
        )
        db.session.add(subject)
        db.session.commit()
    return render_template('add_subject.html', form=form, items=subjects)


@app.route('/delete-ыгио/<int:id>')
def delete_subject(id):
    subject = Subjects.query.get_or_404(id)
    try:
        db.session.delete(subject)
        db.session.commit()
        return redirect(url_for('add_subject'))
    except:
        return 'Нет такого айди'


@app.route('/update-student/<int:id>', methods=['GET', 'POST'])
def update_student(id):
    students = Students.query.get_or_404(id)
    form = StudentForm()
    form.subject.choices = [(subject.id, subject.name) for subject in Subjects.query.order_by(Subjects.name).all()]
    if form.validate_on_submit():
        students.name = form.name.data
        students.birth_date = form.birth_date.data
        students.mark = form.mark.data
        students.subject_id = form.subject.data
        students.status = form.status.data
        try:
            db.session.commit()
        except:
            return 'произошла проблема с отправкой данных'
        return redirect(url_for('add_student'))
    else:
        return render_template('update_student.html', form=form, student=students)

@app.route('/delete/<int:id>')
def delete_students(id):
    student = Students.query.get_or_404(id)
    try:
        db.session.delete(student)
        db.session.commit()
        return redirect(url_for('add_student'))
    except:
        return 'Нет такого айди'

@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404
