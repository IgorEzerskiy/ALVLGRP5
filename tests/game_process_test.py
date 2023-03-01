from unittest import TestCase
from unittest.mock import patch, mock_open

from words import config
from words.custom_exceptions import WordCompleted
from words.data_reader import CSVGetter
from words.game_process import GameProcess


DATA = "header\nword1\nword2\nword3\n"


def get_random(*args):
    return "abc"


# class FakeReader:
#     @staticmethod
#     def get_random_word():
#         return "random"


class GameProcessTestCase(TestCase):
    """
    run TC -> setup -> test_game_process_init -> tearDown -> setUp -> ...
    """

    def setUp(self) -> None:
        self.game_process = GameProcess(CSVGetter(config.WORDS_FILE))

    def tearDown(self) -> None:
        pass

    @patch('words.data_reader.CSVGetter.get_random_word', new=get_random)
    @patch('builtins.open', mock_open(read_data=DATA))
    def test_game_process_init(self):
        game_process = GameProcess(CSVGetter('fakefile'))
        self.assertEqual(game_process.word, "random")

    def test_hidden_word_shows_asterisks_only(self):
        self.assertEqual(self.game_process.hidden_word, "*" * 6)

    def test_hidden_word_shows_asterisks_and_letters(self):
        self.game_process.used_letters = ['a', 'o']
        self.assertEqual(self.game_process.hidden_word, "*a**o*")

    def test_validate_letter_raise_word_completed_on_all_letters_guessed(self):
        self.game_process.used_letters = ['r', 'a', 'n', 'o', 'm']
        with self.assertRaises(WordCompleted):
            self.game_process.validate_letter('d')

    def test_validate_letter_non_alpha(self):
        self.game_process.validate_letter(1)
        self.assertEqual(self.game_process.hidden_word, "*" * 6)
        self.assertFalse(self.game_process.used_letters)
