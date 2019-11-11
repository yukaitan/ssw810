
from prettytable import PrettyTable
import HW10_Yukai_Tan as a
import unittest

class TestRepository(unittest.TestCase):
    def test_student_summary(self):
        path = "/Users/yukai/Desktop/ssw-810/HW10"
        test = a.Repository(path)
        
 
        
        exception = PrettyTable()
        exception.field_names = ['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required', 'Remaining Electives'] 
        exception.add_row(['10103', 'Baldwin, C', 'SFEN', "['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']", "['SSW 540', 'SSW 555']","['None']"])
        exception.add_row(['10115', 'Wyatt, X', 'SFEN', "['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']", "['SSW 540', 'SSW 555']", "['None']"])
        exception.add_row(['10172', 'Forbes, I', 'SFEN', "['SSW 555', 'SSW 567']", "['SSW 540', 'SSW 564']", "['CS 501', 'CS 513', 'CS 545']"])
        exception.add_row(["10175", "Erickson, D", 'SFEN', "['SSW 564', 'SSW 567', 'SSW 687']", "['SSW 540', 'SSW 555']", "['CS 501', 'CS 513', 'CS 545']"])
        exception.add_row(["10183", "Chapman, O", 'SFEN', "['SSW 689']", "['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567']", "['CS 501', 'CS 513', 'CS 545']"])
        exception.add_row(["11399", "Cordova, I", 'SYEN', "['SSW 540']", "['SYS 612', 'SYS 671', 'SYS 800']","['None']"])
        exception.add_row(["11461", "Wright, U", 'SYEN', "['SYS 611', 'SYS 750', 'SYS 800']", "['SYS 612', 'SYS 671']", "['SSW 540', 'SSW 565', 'SSW 810']"])
        exception.add_row(["11658", "Kelly, P", 'SYEN', "[]", "['SYS 612', 'SYS 671', 'SYS 800']", "['SSW 540', 'SSW 565', 'SSW 810']"])
        exception.add_row(["11714", "Morton, A", 'SYEN', "['SYS 611', 'SYS 645']", "['SYS 612', 'SYS 671', 'SYS 800']", "['SSW 540', 'SSW 565', 'SSW 810']"])
        exception.add_row(["11788", "Fuller, E", 'SYEN', "['SSW 540']", "['SYS 612', 'SYS 671', 'SYS 800']", "['None']"])
        
        #print(exception)
        
        self.assertEqual(str(test.student_summary()), str(exception))
        
    
    def test_instructor_summary(self):
        path = "/Users/yukai/Desktop/ssw-810/HW10"
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
      
    
    def test_major_summary(self):
        path = "/Users/yukai/Desktop/ssw-810/HW10"
        test = a.Repository(path)
        
        exception = PrettyTable()
        exception.field_names = ['Dept', 'Required', 'Electives']      
        exception.add_row(['SFEN', "['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567']", "['CS 501', 'CS 513', 'CS 545']"])
        exception.add_row(['SYEN', "['SYS 612', 'SYS 671', 'SYS 800']", "['SSW 540', 'SSW 565', 'SSW 810']"])
        print(exception)
        
        self.assertEqual(str(test.major_summary()), str(exception))
       
        
        
        
        
        
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)