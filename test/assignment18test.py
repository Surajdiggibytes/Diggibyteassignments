import unittest
from  Src.assignment18 import util18

class MyTestCase(unittest.TestCase):
    def test_something(self):
        n = int(input("For test case:"))
        emails = []
        output=['abc10@gmail.com', 'abc12@gmail.com', 'abc44@gmail.com']
        # abc12@gmail.com abc10@gmail.com abc44@gmail.com
        for i in range(n):
            email = input().strip()
            if util18.fun(email):
                emails.append(email)
        out =sorted(emails)
        return out


        self.assertEqual(out, output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
