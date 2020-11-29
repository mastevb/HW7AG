import unittest
import sqlite3
import os
from sqlite3 import Error 
from gradescope_utils.autograder_utils.decorators import weight, visibility, number, partial_credit

class TestSubmission(unittest.TestCase):
    @weight(0)
    @visibility('visible')
    def test_files_found(self):
        self.assertTrue(os.path.isfile("/autograder/submission/q1.sqlp") and
                        os.path.isfile("/autograder/submission/q2.sqlp") and
                        os.path.isfile("/autograder/submission/q3.sqlp") and
                        os.path.isfile("/autograder/submission/q4.sqlp") and
                        os.path.isfile("/autograder/submission/q5.sqlp") and
                        os.path.isfile("/autograder/submission/q6.sqlp") and
                        os.path.isfile("/autograder/submission/q7.sqlp") and
                        os.path.isfile("/autograder/submission/q8.sqlp") and
                        os.path.isfile("/autograder/submission/q9.sqlp") and
                        os.path.isfile("/autograder/submission/q10.sqlp") and
                        os.path.isfile("/autograder/submission/q11.sqlp") and
                        os.path.isfile("/autograder/submission/q12.sqlp"),
                        "one or more submission files not found, double check they are all named correctly and resubmit")