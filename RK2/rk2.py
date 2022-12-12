import unittest
from rk1_copy import Cond, Orch, CondOrch, A1, A2, A3

class test(unittest.TestCase):
    
    def setUp(self):
        self.streets = [
            Orch(1, 'филармонический'),
            Orch(2, 'народный оркестр'),
            Orch(3, 'хоровой'),
        
            Orch(11, 'духовой оркестр'),
            Orch(22, 'джазисты'),
            Orch(33, 'симфонический'),
        ]
        self.houses = [
            Cond(1, 'Сидоров', 25000, 1),
            Cond(2, 'Петров', 35000, 2),
            Cond(3, 'Иваненко', 45000, 3),
            Cond(4, 'Сорокина', 35000, 3),
            Cond(5, 'Иванин', 25000, 3),
        ]
        self.houses_streets = [
            CondOrch(1,1),
            CondOrch(2,2),
            CondOrch(3,3),
            CondOrch(3,4),
            CondOrch(3,5),
            CondOrch(11,1),
            CondOrch(22,2),
            CondOrch(33,3),
            CondOrch(33,4),
            CondOrch(33,5),
        ]


    def test_A1(self):
        expected_result = [
            ('Петров', 35000, 'народный оркестр'), 
            ('Сидоров', 25000, 'филармонический'), 
            ('Иваненко', 45000, 'хоровой'),
            ('Сорокина', 35000, 'хоровой'), 
            ('Иванин', 25000, 'хоровой')
        ]

        result = A1(self.streets, self.houses)
        self.assertEqual(result, expected_result)
    
    def test_A2(self):
        expected_result = [
            ('хоровой', 105000), 
            ('народный оркестр', 35000), 
            ('филармонический', 25000)
        ]
        result = A2(self.streets, self.houses)
        self.assertEqual(result, expected_result)

    def test_A3(self):
        expected_result = {'народный оркестр': ['Петров'], 'духовой оркестр': ['Сидоров']}
        result = A3(self.streets, self.houses, 'оркестр')
        self.assertEqual(result, expected_result) 

if __name__ == '__main__':
    unittest.main()