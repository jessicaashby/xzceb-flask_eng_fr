import unittest

from translator import englishToFrench
from translator import frenchToEnglish

def test_none_frenchToEnglish(self):
    self.assertEqual(' ', frenchToEnglish(' '))

def test_none_englishToFrench(self):
    self.assertEqual(' ', englishToFrench(' '))

def test_bonjour_frenchToEnglish(self):
    self.assertEqual('bonjour', frenchToEnglish('hello'))

def test_hello_englishToFrench(self):
    self.assertEqual('hello', englishToFrench('bonjour'))

if __name__ == '__main__':
    unittest.main()

