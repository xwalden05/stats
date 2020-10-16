import unittest
from descr_stats import mean_stat

class TestMeanStat(unittest.TestCase):
    ### Checks median_stat function.
    def test_mean1(self):
        self.assertEqual(mean_stat([5,3,17]),8.333333333333334)

    def test_mean2(self):
        self.assertEqual(mean_stat([5]),5.0)

    def test_mean3(self):
        self.assertEqual(mean_stat([-1,4,.5,2.5]),1.5)

if __name__ == '__main__':
    unittest.main()
