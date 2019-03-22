import testly

from algoritms.Math import fibonachi


class Tests(testly.TestCase):

    def dataProvider_test_fibonachi(self):
        # use tuple
        yield 0, 0
        yield 1, 1
        yield 2, 1
        yield 3, 2
        yield 4, 3
        yield 5, 5
        yield 6, 8
        yield 7, 13
        yield 8, 21
        yield 9, 34
        yield 10, 55
        yield 11, 89
        yield 12, 144
        yield 13, 233
        yield 14, 377
        yield 15, 610
        yield 16, 987
        yield 17, 1597
        yield 18, 2584
        yield 19, 4181
        yield 20, 6765

    def test_fibonachi(self, in_, out):
        self.assertEqual(fibonachi(in_), out)

if __name__ == '__main__':
    testly.main(verbosity=2)