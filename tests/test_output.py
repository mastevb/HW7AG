import unittest
import re
import pyodbc 
import json
from decimal import *
from gradescope_utils.autograder_utils.decorators import weight, visibility, number, partial_credit

class Helper():
    @staticmethod
    def load_problem(sub_file, ans_file, c):
        sub = open(sub_file).read()
        rows = c.execute(sub)
        rows = rows.fetchall()

        ans = open(ans_file, 'r').read()
        ans = json.loads(ans)

        return rows, ans

    @staticmethod
    def load_ans(ans_file):
        ans = open(ans_file, 'r').read()
        ans = json.loads(ans)

        return ans

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

        # set up connection to Azure 
        server = 'cse414-server.database.windows.net'
        database = 'cse414-20au'
        username = 'cse414'
        password = 'EufBf49b3R2DQXy'
        driver= '{ODBC Driver 17 for SQL Server}'
        self.conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        self.c = self.conn.cursor()


    def tearDown(self):
        self.conn.close()

    @weight(0)
    #@visibility('after_due_date')
    @number("1")
    def test_q1(self):
        sub_path = self.sub_path + 'hw3-q1.sql'
        ans_path = self.answers_path + 'hw3-q1.json'
        rows, ans = Helper.load_problem(sub_path, ans_path, self.c)

        self.assertIsNotNone(rows)
        self.assertEqual(ans['length'], len(rows))

        # sub = []
        # for row in rows: 
        #     self.assertEqual(3, len(row))
        #     sub.append([x for x in row])
        # sub = sorted(sub, key=lambda x: x[0])
        
        # self.assertEqual(ans['data'], sub)
        sub = []
        for row in rows:
            sub.append([x for x in row])
        
        sub_list = list(sub)
        ans_list = list(ans['data'])
        self.assertEqual(ans_list, sub_list, "incorrect output")
        print("Test Passed")

    @weight(0)
    #@visibility('after_due_date')
    @number("2")
    def test_q2(self):
        sub_path = self.sub_path + 'hw3-q2.sql'
        ans_path = self.answers_path + 'hw3-q2.json'
        rows, ans = Helper.load_problem(sub_path, ans_path, self.c)

        self.assertIsNotNone(rows)
        self.assertEqual(ans['length'], len(rows))

        sub_list = list([x[0] for x in rows])
        ans_list = list(ans['data'])
        self.assertEqual(ans_list, sub_list, "incorrect output")
        print("Test Passed")

    @weight(0)
    #@visibility('after_due_date')
    @number("3")
    def test_q3(self):
        sub_path = self.sub_path + 'hw3-q3.sql'
        ans_path = self.answers_path + 'hw3-q3.json'
        rows, ans = Helper.load_problem(sub_path, ans_path, self.c)

        ans_null_path = self.answers_path + 'hw3-q3-null.json'
        ans_null = Helper.load_ans(ans_null_path)
        
        ans_rounded_path = self.answers_path + 'hw3-q3-rounded.json'
        ans_rounded = Helper.load_ans(ans_rounded_path)

        ans_rounded_null_path = self.answers_path + 'hw3-q3-rounded-null.json'
        ans_rounded_null = Helper.load_ans(ans_rounded_null_path)

        self.assertIsNotNone(rows)
        self.assertEqual(ans['length'], len(rows))

        # sub = []
        # for row in rows:
        #     self.assertEqual(len(row), 2, "incorrect number of columns")
        #     place, pct = row 
        #     if pct == None: 
        #         pct = 0 
        #     sub.append([place, round(pct)])
        # sub = sorted(sub, key=lambda x: x[0])
        # ans = sorted([[x[0], round(x[1])] for x in ans['data']], key=lambda x: x[0])
        sub = []
        for row in rows:
            self.assertEqual(len(row), 2, "incorrect number of columns")
            if row[1] == None:
                sub.append([row[0], row[1]])
            else:
                sub.append([row[0], float(row[1])])

        sub_list = list([[x[0], x[1]] for x in sub])
        ans_list = list(ans['data'])
        ans_rounded_list = list(ans_rounded['data'])
        ans_null_list = list(ans_null['data'])
        ans_rounded_null_list = list(ans_rounded_null['data'])

        print("submission: ", sub_list)
        print("answer    : ", ans_list)
        print("answerrndd: ", ans_rounded_list)

        check = ans_list == sub_list or ans_null_list == sub_list or ans_rounded_list == sub_list or ans_rounded_null_list == sub_list

        self.assertTrue(check, "incorrect output")
        print("Test Passed")

        #self.assertEqual(ans, sub)
        # if ans == sub:
        #     set_score(15)
        # else:
        #     sub = [x[0] for x in sub]
        #     ans = [x[0] for x in ans]
        #     if sub == ans:
        #         set_score(13.5)
        #     else:
        #         set_score(0)

    
    @weight(0)
    #@visibility('after_due_date')
    @number("4")
    def test_q4(self):
        sub_path = self.sub_path + 'hw3-q4.sql'
        ans_path = self.answers_path + 'hw3-q4.json'
        rows, ans = Helper.load_problem(sub_path, ans_path, self.c)


        self.assertIsNotNone(rows)
        self.assertEqual(ans['length'], len(rows))

        sub_list = list([x[0] for x in rows])
        ans_list = list(ans['data'])
        self.assertEqual(ans_list, sub_list, "incorrect output")
        print("Test Passed")

    
    @weight(0)
    #@visibility('after_due_date')
    @number("5")
    def test_q5(self):
        sub_path = self.sub_path + 'hw3-q5.sql'
        ans_path = self.answers_path + 'hw3-q5.json'
        rows, ans = Helper.load_problem(sub_path, ans_path, self.c)

        ans_alt_path = self.answers_path + 'hw3-q5-alt.json'
        ans_alt = Helper.load_ans(ans_alt_path)

        self.assertIsNotNone(rows)
        checkLength = len(rows) == ans['length'] or len(rows) == ans_alt['length']
        self.assertTrue(checkLength, "incorrect output length")

        sub_list = list([x[0] for x in rows])
        ans_list = list(ans['data'])
        ans_alt_list = list(ans_alt['data'])
        checkOutput = ans_list == sub_list or ans_alt_list == sub_list
        self.assertTrue(checkOutput, "incorrect output")
        print("Test Passed")

    
    @weight(0)
    #@visibility('after_due_date')
    @number("6")
    def test_q6(self):
        sub_path = self.sub_path + 'hw3-q6.sql'
        ans_path = self.answers_path + 'hw3-q6.json'
        rows, ans = Helper.load_problem(sub_path, ans_path, self.c)

        self.assertIsNotNone(rows)
        self.assertEqual(ans['length'], len(rows))

        sub_list = list([x[0] for x in rows])
        ans_list = list(ans['data'])
        self.assertEqual(ans_list, sub_list, "incorrect output")
        self.assertTrue(Helper.has_subquery(sub_path), "subquery should be present")
        print("Test Passed")
        # if ans_list == sub_list: 
        #     if Helper.has_subquery(sub_path):
        #         set_score(7)
        #     else: 
        #         set_score(3)


    @weight(0)
    #@visibility('after_due_date')
    @number("7")
    def test_q7(self):
        sub_path = self.sub_path + 'hw3-q7.sql'
        ans_path = self.answers_path + 'hw3-q7.json'
        rows, ans = Helper.load_problem(sub_path, ans_path, self.c)

        self.assertIsNotNone(rows)
        self.assertEqual(ans['length'], len(rows))

        sub_list = list([x[0] for x in rows])
        ans_list = list(ans['data'])
        self.assertEqual(ans_list, sub_list, "incorrect output")
        self.assertFalse(Helper.has_subquery(sub_path), "subquery should not be present")
        print("Test Passed")
        # if ans_list == sub_list: 
        #     if not Helper.has_subquery(sub_path):
        #         set_score(8)
        #     else: 
        #         set_score(4)