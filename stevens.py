from flask import Flask, render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def titles():
    return "Stevens Repository"


@app.route('/instroctor')
def student_courses():
    dbpath = r"C:\Users\18646\Desktop\ssw810\810_startup.db"

    try:
        db = sqlite3.connect(dbpath)
    except sqlite3.OperationalError:
        return f"Error: Unable to open database at {dbpath}"
    else:


        query = """select CWID, Name, Dept, Course, count(StudentCWID) from instructors join grades on CWID = InstructorCWID group by Course, instructors.CWID"""

        data = [{'CWID': CWID, 'name': Name, 'Dept': Dept,'Courses': Course, 'Students': Students } for CWID, Name, Dept, Course, Students in db.execute(query)]
    
        db.close()

    return render_template('student_course.html', 
                            title = 'Stevens Repository', 
                            table_title = 'Number of students by course and instructor',
                            students = data)

app.run(debug=True)

