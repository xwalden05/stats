import unittest
from descr_stats import mean_stat
from descr_stats import median_stat

class TestMeanStat(unittest.TestCase):
    ### Checks median_stat function.
    def test_mean1(self):
        self.assertEqual(mean_stat([5,3,17]),8.333333333333334)

    def test_mean2(self):
        self.assertEqual(mean_stat([5]),5.0)

    def test_mean3(self):
        self.assertEqual(mean_stat([-1,4,.5,2.5]),1.5)

class TestMedianStat(unittest.TestCase):
    ### Checks median_stat function.
    def test_median1(self):
        self.assertEqual(median_stat([5,3,17]),5)

    def test_median2(self):
        self.assertEqual(median_stat([-7]),-7)

    def test_median3(self):
        self.assertEqual(median_stat([2, 1, 11, 8, 5, 2]),3.5)

    def test_median4(self):
        self.assertEqual(median_stat([-1, 4, .5, 2.5]),1.5)


if __name__ == '__main__':
    unittest.main()
