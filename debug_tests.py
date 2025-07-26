import unittest
import debug #name of file being tested

class TestAbsFunction(unittest.TestCase):
    def test_1(self):
        s = debug.Solution()
        self.assertEqual(s.dailyTemperatures([30,38,30,36,35,40,28]), [1, 4, 1, 2, 1, 0, 0])
    def test_2(self):
        s = debug.Solution()
        self.assertEqual(s.dailyTemperatures([73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0])
    def test_3(self):
        s = debug.Solution()
        self.assertEqual(s.dailyTemperatures([30,40,50,60]), [1,1,1,0])
    # def test_4(self):
    #     s = debug.Solution()
    #     self.assertEqual(s.dailyTemperatures(), )
    # def test_5(self):
    #     s = debug.Solution()
    #     self.assertEqual(s.dailyTemperatures(), )
    # def test_6(self):
    #     s = debug.Solution()
    #     self.assertEqual(s.dailyTemperatures(), )
    # def test_7(self):
    #     s = debug.Solution()
    #     self.assertEqual(s.dailyTemperatures(), )
        
        

if __name__ == "__main__":
    unittest.main(verbosity=2)
