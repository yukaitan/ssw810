#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 13:45:49 2019

@author: yukai
"""

from prettytable import PrettyTable
from collections import defaultdict
import datetime
import os

class Repository:
    def __init__(self, dir):
        self.students = {}
        self.instructors = {}
        self.open_and_analyze_files(dir)
        #self.student_summary()
        #self.instructor_summary()
        
        
        
    def open_and_analyze_files(self, dir):
        files = []
        doc_lst = []
        files = os.listdir(dir)
        
        if "instructors.txt" and "students.txt" and "grades.txt" in files:
            student_doc = os.path.join(dir, "students.txt")
            doc_lst.append(student_doc)
            instructor_doc = os.path.join(dir, "instructors.txt")
            doc_lst.append(instructor_doc)
            grade_doc = os.path.join(dir, "grades.txt")
            doc_lst.append(grade_doc)
            
            
            for doc in doc_lst:
                
                try:
                    fp = open(doc, 'r')
                except FileNotFoundError:
                    raise FileNotFoundError(f"Can't open {doc}")
                else:
                    with fp:
                        for line in fp:
                                tem = line.split('\t')
                                if doc == student_doc:
                                    if len(tem) != 3:
                                        print("Error: students.txt file has wrong attribute")
                                    for e in tem:
                                        if e == '':
                                            print("Error: There's a element is none in students.txt")
                                    self.students[tem[0]] = Student(tem[0], tem[1], tem[2]) 
                                elif doc == instructor_doc:
                                    if len(tem) != 3:
                                        print("Error: instructors.txt file has wrong attribute")
                                    for e in tem:
                                        if e == '': 
                                            print("Error: There's a element is none in instructors.txt")
                                    self.instructors[tem[0]] = Instructor(tem[0], tem[1], tem[2])
                                elif doc == grade_doc:
                                    if len(tem) != 4:
                                        print("Error: grades.txt file has wrong attribute")
                                    for e in tem:
                                        if e == '':
                                            print("Error: There's a element is none in grades.txt")
                                    #print(f"tem1 is {tem[1]}, tem2 is {tem[2]}")
                                    self.students[tem[0]].add_student_defaultdic(tem[1], tem[2])
                                    #self.students[tem[0]].add_completed_courses(tem[1])
                                    
                                    self.instructors[tem[3].strip('\n')].add_student_number(tem[1])
        else:
            raise FileNotFoundError("instructors.txt or students.txt or grades.txt not found")
            
        
        
    
    def student_summary(self): 
        
        pretty_student_summary = PrettyTable()
        pretty_student_summary.field_names = ["CWID", "Name", "Completed Courses"] 
        
        for key in self.students:
            tem = [] 
            tem_course = []
            p_cwid = key
            p_name = self.students[key].name
            p_completed_course = self.students[key].student_grade
            for key in p_completed_course:
                tem_course.append(key)
            
            tem_course.sort()
            
            tem = [p_cwid, p_name, tem_course]
        
            pretty_student_summary.add_row(tem)
            
        print(pretty_student_summary)    
        return pretty_student_summary
        
    def instructor_summary(self):
         
        
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

class Student:
    
    
    def __init__(self, cwid, name, major):
        
        self.cwid = cwid
        self.name = name
        self.major = major
        self.student_grade = defaultdict(str)
        
    def add_student_defaultdic(self, key, value):
        self.student_grade[key] = value
        
    
class Instructor:
    
    def __init__(self, cwid, name, dept):
        
        self.cwid = cwid
        self.name = name
        self.dept = dept
        self.student_freq = defaultdict(int)

    def add_student_number(self, course):
            self.student_freq[course] += 1
  

sit = Repository("/Users/yukai/Desktop/ssw-810/HW9")
sit.student_summary()
sit.instructor_summary()

      
