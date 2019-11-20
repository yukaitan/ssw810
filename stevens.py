from flask import Flask, render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def hello():
    return "Stevens Repository"


@app.route('/student_courses')
def student_courses():
    DB_FILE = '/Users/TC/iCloudDrive/Desktop/ssw810/hw11/hw11_startup.db'

    db = sqlite3.connect(DB_FILE)
    query = '''SELECT i.CWID, i.Name, i.Dept, g.Course, count(g.Student_CWID) as Student from HW11_instructors i
    left join HW11_grades g on i.CWID = g.Instructor_CWID group by g.Course;'''

    results = db.execute(query)

    data = [{'CWID': CWID, 'name': Name, 'Dept': dept,'Courses': Course, 'Students': Students } for CWID, Name, dept, Course, Students in results]
    
    db.close()

    return render_template('student_course.html', title = 'Stevens Repository', table_title = 'Number of students by course and instructor',students = data)

app.run(debug=True)

