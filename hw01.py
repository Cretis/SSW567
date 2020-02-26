"""
THis module is homework 01
"""
import unittest
import math

def classify_triangle(line_a, line_b, line_c):
    """
    this function return the type of triangle
    :param line_a:
    :param line_b:
    :param line_c:
    :return: none
    """
    k = sorted([line_a, line_b, line_c])
    if not k[0] + k[1] > k[2]:
        typ = 'not a triangle'
    elif line_a == line_b == line_c:
        typ = 'equilateral'
    elif line_a == line_b or line_a == line_c or line_b == line_c:
        if math.sqrt(k[0] ** 2 + k[1] ** 2) == k[2]:
            typ = 'isosceles right angle'
        else:
            typ = 'isosceles'
    elif math.sqrt(k[0] ** 2 + k[1] ** 2) == k[2]:
        typ = 'right'
    else:
        typ = 'scalene'

    return typ


class TestTriangles(unittest.TestCase):
    """
    this class is unittest class
    """
    def testset1(self):
        """
        Test valid input
        :return: none
        """
        self.assertEqual(classify_triangle(1, 1, 1), 'equilateral', 'should be equilateral triangle')
        self.assertEqual(classify_triangle(3, 4, 5), 'right', 'should be right triangle')
        self.assertEqual(classify_triangle(3, 3, 2), 'isosceles', 'should be isosceles triangle')
        self.assertEqual(classify_triangle(4, 5, 6), 'scalene', 'should be scalene triangle')
        self.assertEqual(classify_triangle(math.sqrt(2), math.sqrt(2), 2), 'isosceles right angle',
                         'should be isosceles right angle')

    def testset2(self):
        """
        Test invalid input
        :return: none
        """
        self.assertEqual(classify_triangle(0, 0, 0), 'not a triangle', 'should not be a triangle')
        self.assertEqual(classify_triangle(1, 1, 5), 'not a triangle', 'should not be a triangle')
        self.assertEqual(classify_triangle(1, 2, 9), 'not a triangle', 'should not be a triangle')


if __name__ == '__main__':
    classify_triangle(1, 1, 1)
    classify_triangle(3, 4, 5)
    unittest.main()
