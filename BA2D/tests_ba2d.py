# I used this for debugging but it wasn't necessary in the end, and is not complete
# I'm including it because why not
import ba2d
import unittest

class TestBa2d(unittest.TestCase):
    a = "AAA"
    b = "ACG"
    c = "TTT"
    list_a = [a, b]
    result_A = [[1.0, 0.5, 0.5], [0.0, 0.5, 0.0], [0.0, 0.0, 0.5], [0.0, 0.0, 0.0]]
    list_b = [a, c]
    result_B = [[0.5, 0.5, 0.5], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.5, 0.5, 0.5]]
    x = [a for a in ba2d.kmer_generator(b, 2)]

    def test_motif_matrix(self):
        self.assertEqual(ba2d.motif_matrix(self.list_a), self.result_A,
                "error building motif matrix of 'AAA' and 'ACG'")
        self.assertEqual(ba2d.motif_matrix(self.list_b), self.result_B,
                "error building motif matrix of 'AAA' and 'TTT'")

    def test_kmer_generator(self):
        self.assertEqual(self.x, ["AC", "CG"], "error with kmer_generator of 'ACG'")

    def test_profile_most(self):
        x_profile_most = ba2d.profile_most(self.result_A, "TTTACG", 3)
        self.assertEqual(self.x_profile_most[0], "ACG",
                "error with profile_most")

    def test_score(self):
        self.assertEqual(1, 2)

    def test_greedy_motif_search(self):
        self.assertEqual(1, 2)

    def test_rosalind_exemple(self):
        with open("rosalind_ba2d.txt", "r") as f:
            (k, t) = map(int, f.readline().strip().split())
            seqs_list = [l for l in f.read().strip().split() if l != ""]
            assert len(seqs_list) == t
            result = ba2d.greedy_motif_search(seqs_list, k, t)
            self.assertEqual(self.result, ["CAG", "CAG", "CAA", "CAA", "CAA"], "error with example")




if __name__ == "__main__":
    unittest.main()
