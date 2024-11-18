from uni_test import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        clas = Runner('Andrey')
        for i in range(10):
            clas.walk()
            i += 1
        self.assertEqual(clas.distance, 50)

    def test_run(self):
        clas = Runner('Andrey')
        for i in range(10):
            clas.run()
            i += 1
        self.assertEqual(clas.distance, 100)

    def test_challenge(self):
        clas = Runner('Andrey')
        clas_2 = Runner('Dmitry')
        for i in range(10):
            clas.run()
            clas.walk()
            clas_2.run()
            clas_2.walk()
        self.assertNotEqual(clas.distance, clas_2.distance)


if __name__ == '__main__':
    unittest.main()
