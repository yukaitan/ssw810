#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 13:45:49 2019

@author: yukai
"""

from prettytable import PrettyTable
from collections import defaultdict
import os
import sqlite3

class Repository:
    """store every information for each school"""
    def __init__(self, dir):
        """initial"""
        self.students = {}
        self.instructors = {}
        self.majors = {}
        self.open_and_analyze_files(dir)
        #self.student_summary()
        #self.instructor_summary()
        
        
        
    def open_and_analyze_files(self, dir):
        """open and ananlyze a path"""
        files = []
        doc_lst = []
        try:
            files = os.listdir(dir)
        except FileNotFoundError:
            raise FileNotFoundError(f"Can't find the path of  {dir}")
        else:
            if "instructors.txt" and "students.txt" and "grades.txt" and 'majors.txt'in files:
                student_doc = os.path.join(dir, "students.txt")
                #student_doc = r"C:\Users\18646\Desktop\ssw810\students.txt"
                doc_lst.append(student_doc)
                instructor_doc = os.path.join(dir, "instructors.txt")
                #instructor_doc = r"C:\Users\18646\Desktop\ssw810\instructors.txt"
                doc_lst.append(instructor_doc)
                grade_doc = os.path.join(dir, "grades.txt")
                #grade_doc = r"C:\Users\18646\Desktop\ssw810\grades.txt"
                doc_lst.append(grade_doc)
                major_doc = os.path.join(dir, "majors.txt")
                #major_doc = r"C:\Users\18646\Desktop\ssw810\majors.txt"
                doc_lst.append(major_doc)
                
                
                for doc in doc_lst:
                    
                    try:
                        fp = open(doc, 'r')
                    except FileNotFoundError:
                        raise FileNotFoundError(f"Can't open {doc}")
                    else:
                        with fp:
                            for line in fp:
                                
                                    
                                    tem = line.replace('|','`').replace(';','`').replace('\t','`').split('`')
                                    if doc == student_doc:
                                        if len(tem) != 3:
                                            print("Error: students.txt file has wrong attribute")
                                        for e in tem:
                                            if e == '':
                                                print("Error: There's a element is none in students.txt")
                                        if tem[0] == 'CWID':
                                            continue
                                        else:
                                            self.students[tem[0]] = Student(tem[0], tem[1], tem[2]) 
                                    elif doc == instructor_doc:
                                        if len(tem) != 3:
                                            print("Error: instructors.txt file has wrong attribute")
                                        for e in tem:
                                            if e == '': 
                                                print("Error: There's a element is none in instructors.txt")
                                        if tem[0] == 'CWID':
                                            continue
                                        else:
                                            self.instructors[tem[0]] = Instructor(tem[0], tem[1], tem[2])
                                    elif doc == grade_doc:
                                        if len(tem) != 4:
                                            print("Error: grades.txt file has wrong attribute")
                                        for e in tem:
                                            if e == '':
                                                print("Error: There's a element is none in grades.txt")
                                        #print(f"tem1 is {tem[1]}, tem2 is {tem[2]}")
                                        if tem[0] == 'StudentCWID':
                                            continue
                                        else:
                                            
                                            try:
                                                self.students[tem[0]].add_student_defaultdic(tem[1], tem[2])
                                            except KeyError:
                                                raise KeyError(f"Student ID: {tem[0]} exist in grades.txt, but not exist in student.txt")

                                        #self.students[tem[0]].add_completed_courses(tem[1])
                                        
                                            try:
                                                self.instructors[tem[3].strip('\n')].add_student_number(tem[1])
                                            except KeyError:
                                                instructor_error = tem[3].strip('\n')
                                                raise KeyError(f"Instructor ID: {instructor_error} exist in grades.txt, but not exist in instructor.txt")
                                    elif doc == major_doc:
                                        if len(tem) != 3:
                                            print("Error: majors.txt file has wrong attribute")
                                        for e in tem:
                                            if e == '':
                                                print("Error: There's a element is none in majors.txt")
                                        #a = self.majors
                                        if tem[0] == 'Major':
                                            continue
                                        elif tem[0] == 'unknow':
                                            raise KeyError("E")
                                        elif tem[0] in self.majors:
                                            if tem[1] == 'R':
                                                
                                                self.majors[tem[0]].add_R(tem[2].strip('\n'))
                                            else:
                                                self.majors[tem[0]].add_E(tem[2].strip('\n'))
                                        else:
                                                
                                            self.majors[tem[0]] = Majors()
                                            if tem[1] == 'R':
                                                
                                                self.majors[tem[0]].add_R(tem[2].strip('\n'))
                                            else:
                                                self.majors[tem[0]].add_E(tem[2].strip('\n'))
                                            
                                        
            else:
                raise FileNotFoundError("instructors.txt or students.txt or grades.txt or majors.txt not found")
                
        
    
    def student_summary(self): 
        """get and return and print out student pretty table"""
        pretty_student_summary = PrettyTable()
        pretty_student_summary.field_names = ["CWID", "Name","Major", "Completed Courses", "Remaining Required", "Remaining Electives"] 
        
        for key in self.students:
            tem = [] 
            tem_course = []
            p_cwid = key
            p_name = self.students[key].name
            p_major = self.students[key].major.strip('\n')
            p_completed_course = self.students[key].student_grade
            R = []
            E = []
            for key in p_completed_course:
                grade = p_completed_course[key]
                if grade == 'D' or grade == 'F':
                    continue
                else:
                    tem_course.append(key)
            
            tem_course.sort()
            for i in self.majors:
                if i == p_major:
                    
                    R = self.majors[i].R
                    E = self.majors[i].E
            
            retD1 = list(set(R).difference(set(tem_course)))
            count = 0
            for course in E:
                if course in tem_course:
                    count = count + 1
            if count == 0:
                retD2 = list(set(E).difference(set(tem_course)))
            else:
                 retD2 = ['None']
                
      
                    
            retD1.sort()
            retD2.sort()
            
            tem = [p_cwid, p_name, p_major, tem_course, retD1, retD2]
        
            pretty_student_summary.add_row(tem)
            
        print(pretty_student_summary)    
        return pretty_student_summary
        
    def instructor_summary(self):
        """get and return and print out instructor pretty table"""
        
        pretty_instructor_summary = PrettyTable()
        
                          
        pretty_instructor_summary.field_names = ["CWID", "Name", "Dept", "Course", "Students"]                      
        
        
        
        for key in self.instructors:
            i_course_freq = self.instructors[key].student_freq
            for i in i_course_freq:
                i_course = i
                i_course_persons = i_course_freq[i]
                i_cwid = key
                i_name = self.instructors[key].name
                i_dept = self.instructors[key].dept.strip('\n')
                a = [i_cwid, i_name, i_dept, i_course, i_course_persons]
                pretty_instructor_summary.add_row(a)

        print(pretty_instructor_summary)
        return pretty_instructor_summary
    
    def major_summary(self):
        """get and return and print out major pretty table"""
        pretty_major_summary = PrettyTable()
        pretty_major_summary.field_names = ["Dept", "Required", "Electives"]     

        
        for key in self.majors:
            Dep_name = key
            R = self.majors[key].R
            E = self.majors[key].E
            R.sort()
            E.sort()
            pretty_major_summary.add_row([Dep_name,R,E])
            
        print(pretty_major_summary)
        return pretty_major_summary
    
    def instructor_table_db(self, db_path):

        db = sqlite3.connect(db_path)
        pretty_instructor_summary2 = PrettyTable()
        pretty_instructor_summary2.field_names = ["CWID", "Name", "Dept", "Course", "Students"]


        query = "select CWID, Name, Dept, Course, count(StudentCWID) from instructors join grades on CWID = InstructorCWID group by Course"
        for row in db.execute(query):

            pretty_instructor_summary2.add_row(list(row))

        print(pretty_instructor_summary2)
        return pretty_instructor_summary2


class Student:
    """store student inforamtion"""
    
    def __init__(self, cwid, name, major):
        
        self.cwid = cwid
        self.name = name
        self.major = major
        self.student_grade = defaultdict(str)
        
    def add_student_defaultdic(self, key, value):
        """add student default dictionary"""
        self.student_grade[key] = value
        
    
class Instructor:
    """store instructor inforamtion"""
    def __init__(self, cwid, name, dept):
        
        self.cwid = cwid
        self.name = name
        self.dept = dept
        self.student_freq = defaultdict(int)

    def add_student_number(self, course):
        """add instructor default dictionary"""
        self.student_freq[course] += 1
            
class Majors:
    
    """store majors information"""
    def __init__(self):
        
        self.E = []
        self.R = []
        
        #self.major_required = defaultdict(str)
        #self.required = required
    def add_E(self, course):
        """add electives course to a list"""
        self.E.append(course)
    
    def add_R(self, course):
        """add required course to a list"""
        self.R.append(course)

  

sit = Repository(r"C:\Users\18646\Desktop\ssw810")
sit.student_summary()
sit.instructor_summary()
sit.major_summary()
sit.instructor_table_db(r"C:\Users\18646\Desktop\ssw810\810_startup.db")
      
