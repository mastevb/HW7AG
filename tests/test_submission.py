import unittest
import sqlite3
import os
from sqlite3 import Error 
from gradescope_utils.autograder_utils.decorators import weight, visibility, number, partial_credit

class TestSubmission(unittest.TestCase):
    @weight(0)
    @visibility('visible')
    def test_files_found(self):
        self.assertTrue(os.path.isfile("/autograder/submission/hw3-q1.sql") and 
                        os.path.isfile("/autograder/submission/hw3-q2.sql") and 
                        os.path.isfile("/autograder/submission/hw3-q3.sql") and 
                        os.path.isfile("/autograder/submission/hw3-q4.sql") and 
                        os.path.isfile("/autograder/submission/hw3-q5.sql") and 
                        os.path.isfile("/autograder/submission/hw3-q6.sql") and 
                        os.path.isfile("/autograder/submission/hw3-q7.sql") and 
                        os.path.isfile("/autograder/submission/hw3-d.txt"),
                        "one or more submission files not found, double check they are all named correctly and resubmit")