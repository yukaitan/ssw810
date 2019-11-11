import os
from prettytable import PrettyTable
import HW09_Yukai_Tan as a
import unittest

class TestRepository(unittest.TestCase):
    def test_student_summary(self):
        path = "/Users/yukai/Desktop/ssw-810/HW9"
        test = a.Repository(path)
        
 
        
        exception = PrettyTable()
        exception.field_names = ["CWID", "Name", "Completed Courses"] 
        exception.add_row(['10103', 'Baldwin, C', "['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']"])
        exception.add_row(['10115', 'Wyatt, X', "['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']"])
        exception.add_row(['10172' , 'Forbes, I' ,"['SSW 555', 'SSW 567']"])
        exception.add_row(["10175","Erickson, D","['SSW 564', 'SSW 567', 'SSW 687']"])
        exception.add_row(["10183", "Chapman, O", "['SSW 689']"])
        exception.add_row(["11399", "Cordova, I", "['SSW 540']"])
        exception.add_row(["11461", "Wright, U", "['SYS 611', 'SYS 750', 'SYS 800']"])
        exception.add_row(["11658", "Kelly, P", "['SSW 540']"])
        exception.add_row(["11714", "Morton, A" , "['SYS 611', 'SYS 645']"])
        exception.add_row(["11788", "Fuller, E", "['SSW 540']"])
        
        self.assertEqual(str(test.student_summary()), str(exception))
        
    
    def test_instructor_summary(self):
        path = "/Users/yukai/Desktop/ssw-810/HW9"
        test = a.Repository(path)
        
        exception = PrettyTable()
        exception.field_names = ['CWID', 'Name', 'Dept','Course','Students'] 
        exception.add_row(["98765", 'Einstein, A' , 'SFEN' , 'SSW 567' , '4'])
        exception.add_row(["98765" , 'Einstein, A' , 'SFEN' , 'SSW 540' , '3'])
        exception.add_row(["98764" , 'Feynman, R' , 'SFEN' , 'SSW 564', '3'])
        exception.add_row(["98764" , 'Feynman, R' , 'SFEN' , 'SSW 687' , '3'])
        exception.add_row(["98764" , 'Feynman, R' , 'SFEN' , 'CS 501' , '1'])
        exception.add_row(["98764" , 'Feynman, R' , 'SFEN' , 'CS 545' , '1'])
        exception.add_row(["98763" , 'Newton, I' , 'SFEN' , 'SSW 555' , '1'])
        exception.add_row(["98763" , 'Newton, I' , 'SFEN' , 'SSW 689' , '1'])
        exception.add_row(["98760" , 'Darwin, C' , 'SYEN' , 'SYS 800' , '1'])
        exception.add_row(["98760" , 'Darwin, C' , 'SYEN' , 'SYS 750' , '1'])
        exception.add_row(["98760" , 'Darwin, C' , 'SYEN' , 'SYS 611' , '2'])
        exception.add_row(["98760" , 'Darwin, C' , 'SYEN' , 'SYS 645' , '1'])
        
        self.assertEqual(str(test.instructor_summary()), str(exception))
      
        
        
        
        
        
        
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)