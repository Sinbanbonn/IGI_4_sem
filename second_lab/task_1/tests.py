import unittest
from our_functions import *

class TestCountSentences(unittest.TestCase):

    def test_1_sent(self):
        text = "I was walking around."
        self.assertEqual(sent_count(text), 1)

    def test_3_sent(self):
        text = "I was walking around. I was walking around. I was walking around?"
        self.assertEqual(sent_count(text), 3)

    def test_6_sent(self):
        text = "I was walking around... I was walking around. I was walking around? I was walking around? I was walking around. I was walking around?"
        self.assertEqual(sent_count(text), 6)

    def test_1_sent_non(self):
        text = "I was walking around?"
        self.assertEqual(non_dec_sent(text), 1)

    def test_3_sent_non(self):
        text = "I was walking around! I was walking around! I was walking around?"
        self.assertEqual(non_dec_sent(text), 3)

    def test_6_sent_non(self):
        text = "I was walking around! I was walking around! I was walking around? I was walking around? I was walking around! I was walking around?"
        self.assertEqual(non_dec_sent(text), 6)


    def test_1_word(self):
        text = "I was walking around?"
        self.assertEqual(word_search(text), 4)

    def test_3_word(self):
        text = "I was walking around! I was walking around! I was walking around?"
        self.assertEqual(word_search(text), 12)

    def test_6_word(self):
        text = "I was walking around! I was walking around! I was walking around? I was walking around? I was walking around! I was walking around?"
        self.assertEqual(word_search(text), 24)

