import unittest

def binary_equals(hay: list[int], needle: int) -> int:
    LEN = len(hay)
    l = -1
    r = LEN
    while 1 < r-l:
        mid = l + (r-l)//2
        val = hay[mid]
        if val <= needle:
            l = mid
        else:
            r = mid

    return -1 if l == -1 or hay[l] != needle else l


def binary_upper_bounds(hay: list[int], needle: int) -> int:
    LEN = len(hay)
    l = -1
    r = LEN
    while 1 < r-l:
        mid = l + (r-l)//2
        val = hay[mid]
        if val <= needle:
            l = mid
        else:
            r = mid

    return -1 if r == LEN else r

def binary_lower_bounds(hay: list[int], needle: int) -> int:
    LEN = len(hay)
    l = -1
    r = LEN
    while r-l > 1:
        mid = l + (r-l)//2
        val = hay[mid]
        if val <= needle:
            l = mid
        else:
            r = mid

    return l

def binary_closest(hay: list[int], needle: int) -> int:
    LEN = len(hay)
    l = -1
    r = LEN
    while r-l > 1:
        mid = l + (r-l)//2
        val = hay[mid]
        if val <= needle:
            l = mid
        else:
            r = mid
    # hay[l] <= needle
    # hay[r] > needle
    # compare l and r and needle
    if l == -1:
        res = r
    elif r == LEN:
        res = l
    elif needle-hay[l] < hay[r]-needle:
        res = l
    else:
        res = r

    return res


class TestAddFunction(unittest.TestCase):
    def test_binary_equals(self):
        self.assertEqual(binary_equals([1,2,3,4], 1),  0)
        self.assertEqual(binary_equals([1,2,3,4], 2),  1)
        self.assertEqual(binary_equals([1,2,3,4], 3),  2)
        self.assertEqual(binary_equals([1,2,3,4], 4),  3)
        self.assertEqual(binary_equals([1,2,3,4], 5), -1)
        self.assertEqual(binary_equals([1,2,3,4], 0), -1)
        

    def test_binary_upper_bounds(self):
        self.assertEqual(binary_upper_bounds([1,2,4,5],  3),  2)
        self.assertEqual(binary_upper_bounds([1,2,4,5],  5), -1)
        self.assertEqual(binary_upper_bounds([1,2,4,5],  0),  0)
        self.assertEqual(binary_upper_bounds([1,2,4,5], -1),  0)
        self.assertEqual(binary_upper_bounds([1,2,4,5],  4),  3)

    def test_binary_lower_bounds(self):
        self.assertEqual(binary_lower_bounds([1,2,4,5], 3),  1)
        self.assertEqual(binary_lower_bounds([1,2,4,5], 2),  1)
        self.assertEqual(binary_lower_bounds([1,2,4,5], 1),  0)
        self.assertEqual(binary_lower_bounds([1,2,4,5], 0), -1)
        self.assertEqual(binary_lower_bounds([1,2,4,5], 6),  3)
        self.assertEqual(binary_lower_bounds([1,2,4,5], 5),  3)
        self.assertEqual(binary_lower_bounds([1,2,4,5], 4),  2)

    def test_binary_closest_up(self):
        self.assertEqual(binary_closest([1,2,5,6],  0), 0)
        self.assertEqual(binary_closest([1,2,5,6], -1), 0)
        self.assertEqual(binary_closest([1,2,5,6],  1), 0)
        self.assertEqual(binary_closest([1,2,5,6],  2), 1)
        self.assertEqual(binary_closest([1,2,5,6],  3), 1)
        self.assertEqual(binary_closest([1,2,5,6],  4), 2)
        self.assertEqual(binary_closest([1,2,5,6],  5), 2)
        self.assertEqual(binary_closest([1,2,5,6],  6), 3)
        self.assertEqual(binary_closest([1,2,5,6],  7), 3)
        self.assertEqual(binary_closest([1,2,5,6],  8), 3)


def main() -> None:
    unittest.main()

if __name__ == '__main__':
    main()