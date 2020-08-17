import unittest
import string
import randomchar


class Letter(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(randomchar.letter(-1), "")

    def test_one(self):
        self.assertIn(randomchar.letter(1), string.ascii_letters)

    def test_all(self):
        size = len(string.ascii_letters)
        random_letters = randomchar.letter(size)
        for letter in random_letters:
            self.assertIn(letter, string.ascii_letters)


class LowerCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(randomchar.lower_case(-1), "")

    def test_one(self):
        self.assertIn(randomchar.lower_case(1), string.ascii_lowercase)

    def test_all(self):
        size = len(string.ascii_lowercase)
        random_letters = randomchar.lower_case(size)
        for letter in random_letters:
            self.assertIn(letter, string.ascii_lowercase)


class Digits(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(randomchar.digit(-1), "")

    def test_one(self):
        self.assertIn(randomchar.digit(1), string.digits)

    def test_all(self):
        size = len(string.ascii_lowercase)
        random_digits = randomchar.digit(size)
        for digit in random_digits:
            self.assertIn(digit, string.digits)


class Password(unittest.TestCase):
    chars = string.ascii_letters + string.digits + string.punctuation
    size = len(chars)

    def test_empty(self):
        self.assertEqual(randomchar.password(-1), "")

    def test_one(self):
        self.assertIn(randomchar.password(1), self.chars)

    def test_all(self):
        password = randomchar.password(self.size)
        self.assertEqual(len(password), self.size)
        for char in password:
            self.assertIn(char, self.chars)


if __name__ == "__main__":
    print("randomChar v0.1.0-beta")
