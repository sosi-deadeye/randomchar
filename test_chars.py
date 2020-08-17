import unittest
import string
import randomChar


class Letter(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(randomChar.letter(-1), "")

    def test_one(self):
        self.assertIn(randomChar.letter(1), string.ascii_letters)

    def test_all(self):
        size = len(string.ascii_letters)
        random_letters = randomChar.letter(size)
        for letter in random_letters:
            self.assertIn(letter, string.ascii_letters)


class LowerCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(randomChar.lower_case(-1), "")

    def test_one(self):
        self.assertIn(randomChar.lower_case(1), string.ascii_lowercase)

    def test_all(self):
        size = len(string.ascii_lowercase)
        random_letters = randomChar.lower_case(size)
        for letter in random_letters:
            self.assertIn(letter, string.ascii_lowercase)


class Digits(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(randomChar.digit(-1), "")

    def test_one(self):
        self.assertIn(randomChar.digit(1), string.digits)

    def test_all(self):
        size = len(string.ascii_lowercase)
        random_digits = randomChar.digit(size)
        for digit in random_digits:
            self.assertIn(digit, string.digits)


class Password(unittest.TestCase):
    chars = string.ascii_letters + string.digits + string.punctuation
    size = len(chars)

    def test_empty(self):
        self.assertEqual(randomChar.password(-1), "")

    def test_one(self):
        self.assertIn(randomChar.password(1), self.chars)

    def test_all(self):
        password = randomChar.password(self.size)
        self.assertEqual(len(password), self.size)
        for char in password:
            self.assertIn(char, self.chars)


if __name__ == "__main__":
    print("randomChar v0.1.0-beta")
