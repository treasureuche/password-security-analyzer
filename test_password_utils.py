
import unittest
from password_utils import check_password_strength


class TestPasswordStrength(unittest.TestCase):

    def test_weak_password(self):
        score, strength = check_password_strength("hello")
        self.assertEqual(score, 1)
        self.assertEqual(strength, "WEAK")

    def test_common_password(self):
        score, strength = check_password_strength("password123")
        self.assertEqual(score, 2)
        self.assertEqual(strength, "WEAK")

    def test_medium_password(self):
        score, strength = check_password_strength("Hello123")
        self.assertEqual(score, 3)
        self.assertEqual(strength, "MEDIUM")

    def test_strong_password(self):
        score, strength = check_password_strength("Cedar!River82#Moon")
        self.assertEqual(score, 5)
        self.assertEqual(strength, "STRONG")


if __name__ == "__main__":
    unittest.main()
