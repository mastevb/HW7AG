import unittest
import re
import pyodbc
import json
from decimal import *
from gradescope_utils.autograder_utils.decorators import weight, visibility, \
    number, partial_credit


class Helper:
    @staticmethod
    def load_problem(sub_file, ans_file):
        sub = open(sub_file).read()
        rows = self.connection.query("'''" + sub + "'''")

        ans = open(ans_file, 'r').read()
        ans = json.loads(ans)

        return rows, ans

    @staticmethod
    def load_ans(ans_file):
        ans = open(ans_file, 'r').read()
        ans = json.loads(ans)

        return ans

    @staticmethod
    def ordered(obj):
        if isinstance(obj, dict):
            return sorted(Helper.ordered(v) for k, v in obj.items())
        if isinstance(obj, list):
            return sorted(Helper.ordered(x) for x in obj)
        else:
            return obj

    @staticmethod
    def compare(rows, ans):
        # solution
        sol = ans["results"]
        sol_count = ans['metrics']['resultCount']
        # student
        stud = rows['results']
        stud_count = rows['metrics']['resultCount']
        comp = False
        if len(sol) == len(stud):
            comp = Helper.ordered(sol) == Helper.ordered(stud)
        if not comp:
            print("incorrect output")
        else:
            print("Test Passed")

    @staticmethod
    def has_subquery(file):
        sub = open(file, 'r').read()
        sub = re.split('select', sub, flags=re.IGNORECASE)
        return len(sub) > 2


class TestOutput(unittest.TestCase):
    def setUp(self):
        self.sub_path = "/autograder/source/submission/"
        self.sol_path = "/autograder/source/solutions/"
        self.answers_path = '/autograder/source/answers/'

        # set up connection to AsterixDB
        self.conn = AsterixConnection()

    @weight(0)
    # @visibility('after_due_date')
    @number("1")
    def test_q1(self):
        sub_path = self.sub_path + 'q1.sqlp'
        ans_path = self.answers_path + 'q1.json'
        rows, ans = Helper.load_problem(sub_path, ans_path)
        Helper.compare(rows, ans)

    @weight(0)
    # @visibility('after_due_date')
    @number("2")
    def test_q2(self):
        sub_path = self.sub_path + 'q2.sqlp'
        ans_path = self.answers_path + 'q2.json'
        rows, ans = Helper.load_problem(sub_path, ans_path)
        Helper.compare(rows, ans)

    @weight(0)
    # @visibility('after_due_date')
    @number("3")
    def test_q3(self):
        sub_path = self.sub_path + 'q3.sqlp'
        ans_path = self.answers_path + 'q3.json'
        rows, ans = Helper.load_problem(sub_path, ans_path)
        Helper.compare(rows, ans)

    @weight(0)
    # @visibility('after_due_date')
    @number("4")
    def test_q4(self):
        sub_path = self.sub_path + 'q4.sqlp'
        ans_path = self.answers_path + 'q4.json'
        rows, ans = Helper.load_problem(sub_path, ans_path)
        Helper.compare(rows, ans)

    @weight(0)
    # @visibility('after_due_date')
    @number("5")
    def test_q1(self):
        sub_path = self.sub_path + 'q5.sqlp'
        ans_path = self.answers_path + 'q5.json'
        rows, ans = Helper.load_problem(sub_path, ans_path)
        Helper.compare(rows, ans)

    @weight(0)
    # @visibility('after_due_date')
    @number("6")
    def test_q6(self):
        sub_path = self.sub_path + 'q6.sqlp'
        ans_path = self.answers_path + 'q6.json'
        rows, ans = Helper.load_problem(sub_path, ans_path)
        Helper.compare(rows, ans)

    @weight(0)
    # @visibility('after_due_date')
    @number("7")
    def test_q7(self):
        sub_path = self.sub_path + 'q7.sqlp'
        ans_path = self.answers_path + 'q7.json'
        rows, ans = Helper.load_problem(sub_path, ans_path)
        Helper.compare(rows, ans)

    @weight(0)
    # @visibility('after_due_date')
    @number("8")
    def test_q8(self):
        sub_path = self.sub_path + 'q8.sqlp'
        ans_path = self.answers_path + 'q8.json'
        rows, ans = Helper.load_problem(sub_path, ans_path)
        Helper.compare(rows, ans)

    @weight(0)
    # @visibility('after_due_date')
    @number("9")
    def test_q9(self):
        sub_path = self.sub_path + 'q9.sqlp'
        ans_path = self.answers_path + 'q9.json'
        rows, ans = Helper.load_problem(sub_path, ans_path)
        Helper.compare(rows, ans)

    @weight(0)
    # @visibility('after_due_date')
    @number("10")
    def test_q10(self):
        sub_path = self.sub_path + 'q10.sqlp'
        ans_path = self.answers_path + 'q10.json'
        rows, ans = Helper.load_problem(sub_path, ans_path)
        Helper.compare(rows, ans)

    @weight(0)
    # @visibility('after_due_date')
    @number("11")
    def test_q11(self):
        sub_path = self.sub_path + 'q11.sqlp'
        ans_path = self.answers_path + 'q11.json'
        rows, ans = Helper.load_problem(sub_path, ans_path)
        Helper.compare(rows, ans)

    @weight(0)
    # @visibility('after_due_date')
    @number("12")
    def test_q12(self):
        sub_path = self.sub_path + 'q12.sqlp'
        ans_path = self.answers_path + 'q12.json'
        rows, ans = Helper.load_problem(sub_path, ans_path)
        Helper.compare(rows, ans)
