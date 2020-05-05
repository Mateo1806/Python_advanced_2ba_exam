# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        # À compléter...
        self.assertEqual(program.fact(0),1)
        self.assertEqual(program.fact(5),120)
        pass
    
    def test_roots(self):
        # À compléter...
        self.assertEqual(program.roots(1,1,1),(-0.1125178063039387, -8.887482193696062))
        self.assertEqual(program.roots(1,0,1),())
        pass
    
    def test_integrate(self):
        # À compléter...
        self.assertEqual(program.integrate('x ** 2 - 1', -1, 1),-1.3333333333)
        self.assertEqual(program.integrate('x ** 2 - 1', -2, 2),1.3333333333)
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
