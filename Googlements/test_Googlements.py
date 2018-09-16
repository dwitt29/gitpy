#!/usr/bin/python

import unittest

from Googlements import Googlement

class testLegal(unittest.TestCase):

    def setUp(self):
        pass

    def test_Legal_True_001(self):
        t=Googlement('001')
        self.assertTrue(t.Legal)

    def test_Legal_True_103(self):
        t=Googlement('103')
        self.assertTrue(t.Legal)

    def test_Legal_False_400(self):
        t=Googlement('400')
        self.assertFalse(t.Legal)

    def test_Legal_False_000(self):
        t=Googlement('000')
        self.assertFalse(t.Legal)

    def test_Legal_True_0003(self):
        t=Googlement('0003')
        self.assertTrue(t.Legal)

    def test_Legal_True_20(self):
        t=Googlement('20')
        self.assertTrue(t.Legal)

    def test_Legal_True_1234(self):
        t=Googlement('1234')
        self.assertTrue(t.Legal)

    def test_Legal_False_40(self):
        t=Googlement('40')
        self.assertFalse(t.Legal)

    def test_Legal_False_1235(self):
        t=Googlement('1235')
        self.assertFalse(t.Legal)

    def test_getL_True_1235(self):
        l=1235
        t=Googlement(l)
        self.assertEqual(t.getL(),len(str(l)))
   
    def test_Decay_True_0001(self):
        t=Googlement('0001')
        self.assertEqual(t.Decay(),'1000')

    def test_Decay_True_0414(self):
        t=Googlement('0414')
        self.assertEqual(t.Decay(),'1002')
        
    def test_Decay_True_1002(self):
        t=Googlement('1002')
        self.assertEqual(t.Decay(),'1100')
        
    def test_Decay_True_1100(self):
        t=Googlement('1100')
        self.assertEqual(t.Decay(),'2000')
        
    def test_Decay_True_2000(self):
        t=Googlement('2000')
        self.assertEqual(t.Decay(),'0100')
        
    def test_Decay_True_0100(self):
        t=Googlement('0100')
        self.assertEqual(t.Decay(),'1000')
        
    def test_Decay_True_1000(self):
        t=Googlement('1000')
        self.assertEqual(t.Decay(),'1000')
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
