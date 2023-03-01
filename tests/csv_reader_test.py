from unittest import TestCase
from unittest.mock import patch, mock_open

from words.data_reader import CSVGetter
from words import config

DATA = "header\nword1\nword2\nword3\n"


class CSVGetterTestCase(TestCase):
    """
    0. test init
    1. get_random_word return a word
    """
    def test_csv_getter_init(self):
        getter = CSVGetter(config.WORDS_FILE)
        self.assertEqual(getter.file_path, config.WORDS_FILE)

    def test_get_random_word_return_word(self):
        getter = CSVGetter(config.WORDS_FILE)
        word = getter.get_random_word()
        # isinstance(word, str) == True
        # print(word)
        self.assertIsInstance(word, str)

    @patch('builtins.open', mock_open(read_data=DATA))
    def test_get_random_word_mocked(self):
        getter = CSVGetter("nofile")
        word = getter.get_random_word()
        print(word)
        self.assertIn(word, DATA.split('\n'))
