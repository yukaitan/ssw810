
from prettytable import PrettyTable
import HW11_Yukai_Tan as a
import unittest
import sqlite3

class TestRepository(unittest.TestCase):
    def test_student_summary(self):
        path = r"C:\Users\18646\Desktop\ssw810"
        test = a.Repository(path)
        
 
        
        exception = PrettyTable()
        exception.field_names = ['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required', 'Remaining Electives'] 
        exception.add_row(['10103', 'Jobs, S', 'SFEN', "['CS 501', 'SSW 810']", "['SSW 540', 'SSW 555']","['None']"])
        exception.add_row(['10115', 'Bezos, J', 'SFEN', "['SSW 810']", "['SSW 540', 'SSW 555']", "['CS 501', 'CS 546']"])
        exception.add_row(['10183', 'Musk, E', 'SFEN', "['SSW 555', 'SSW 810']", "['SSW 540']", "['CS 501', 'CS 546']"])
        exception.add_row(["11714", "Gates, B", 'CS', "['CS 546', 'CS 570', 'SSW 810']", "[]", "['None']"])
        exception.add_row(["11717", "Kernighan, B", 'CS', "[]", "['CS 546', 'CS 570']", "['SSW 565', 'SSW 810']"])
       
        
        #print(exception)
        
        self.assertEqual(str(test.student_summary()), str(exception))
        
    
    def test_instructor_summary(self):
        path = r"C:\Users\18646\Desktop\ssw810"
        test = a.Repository(path)
        
        exception = PrettyTable()
        exception.field_names = ['CWID', 'Name', 'Dept','Course','Students'] 
        exception.add_row(["98764" , 'Cohen, R' , 'SFEN' , 'CS 546' , '1'])
        exception.add_row(["98763" , 'Rowland, J' , 'SFEN' , 'SSW 810' , '4'])
        exception.add_row(["98763" , 'Rowland, J' , 'SFEN' , 'SSW 555', '1'])
        exception.add_row(["98762" , 'Hawking, S' , 'CS' , 'CS 501' , '1'])
        exception.add_row(["98762" , 'Hawking, S' , 'CS' , 'CS 546' , '1'])
        exception.add_row(["98762" , 'Hawking, S' , 'CS' , 'CS 570' , '1'])
        
        
        self.assertEqual(str(test.instructor_summary()), str(exception))
      
    
    def test_major_summary(self):
        path = r"C:\Users\18646\Desktop\ssw810"
        test = a.Repository(path)
        
        exception = PrettyTable()
        exception.field_names = ['Dept', 'Required', 'Electives']      
        exception.add_row(['SFEN', "['SSW 540', 'SSW 555', 'SSW 810']", "['CS 501', 'CS 546']"])
        exception.add_row(['CS', "['CS 546', 'CS 570']", "['SSW 565', 'SSW 810']"])
        #print(exception)
        
        self.assertEqual(str(test.major_summary()), str(exception))

    def test_instructor_table_db(self):
        
        path = r"C:\Users\18646\Desktop\ssw810"
        test = a.Repository(path)
        
        exception = PrettyTable()
        exception.field_names = ['CWID', 'Name', 'Dept','Course','Students'] 
        exception.add_row(["98762" , 'Hawking, S' , 'CS' , 'CS 501' , '1'])
        exception.add_row(["98762" , 'Hawking, S' , 'CS' , 'CS 546' , '2'])
        exception.add_row(["98762" , 'Hawking, S' , 'CS' , 'CS 570' , '1'])
        exception.add_row(["98763" , 'Rowland, J' , 'SFEN' , 'SSW 555' , '1'])
        exception.add_row(["98763" , 'Rowland, J' , 'SFEN' , 'SSW 810' , '4'])
        
        
        self.assertEqual(str(test.instructor_table_db(r"C:\Users\18646\Desktop\ssw810\810_startup.db")), str(exception))
       
        
        
        
        
        
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)