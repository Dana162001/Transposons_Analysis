import unittest
import transposons_count


class TestCase(unittest.TestCase):
    def test_transposons_count(self):

        transposons = [
            [1, 10],
            [5, 15],
            [1, 100],
            [50, 60],
            [10, 15],
        ]

        sequences = [
            [2, 7],
            [3, 6],
            [5, 8],
            [5, 20],
            [10, 20],
            [10, 15],
        ]

        output = transposons_count.seq_in_trans(sequences, transposons)

        excepted_output = [3, 2, 6, 0, 1]

        self.assertEqual(excepted_output, output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
