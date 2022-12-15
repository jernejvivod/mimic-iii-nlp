import unittest

from mimic_iii_explorer_client.utils.utils import limit_ids


class TestUtils(unittest.TestCase):
    def test_limit_ids(self):
        ids = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

        res1 = limit_ids(ids, 0.5)
        self.assertEqual(len(res1), 5)
        self.assertTrue(set(res1).issubset(set(ids)))

        res2 = limit_ids(ids, 0.75)
        self.assertEqual(len(res2), 8)
        self.assertTrue(set(res2).issubset(set(ids)))

        self.assertRaises(ValueError, limit_ids, ids, -1)
        self.assertRaises(ValueError, limit_ids, ids, -1.1)
        self.assertRaises(ValueError, limit_ids, ids, 11)
        self.assertRaises(ValueError, limit_ids, ids, 1.1)


if __name__ == '__main__':
    unittest.main()