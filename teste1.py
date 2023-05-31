import unittest
from io import StringIO
from unittest.mock import patch

from questao1 import BubbleSortStrategy, SelectionSortStrategy, MergeSortStrategy, Sorter
from questao2 import WordCounter, WordCountObserver

class SortStrategyTest(unittest.TestCase):
    def BubbleSortStrategy(self):
        data = [7, 2, 5, 1, 8, 3]
        sorter = Sorter(BubbleSortStrategy())
        sorted_data = sorter.sort_data(data)
        self.assertEqual(sorted_data, [1, 2, 3, 5, 7, 8])

    def SelectionSortStrategy(self):
        data = [7, 2, 5, 1, 8, 3]
        sorter = Sorter(SelectionSortStrategy())
        sorted_data = sorter.sort_data(data)
        self.assertEqual(sorted_data, [1, 2, 3, 5, 7, 8])

    def MergeSortStrategy(self):
        data = [7, 2, 5, 1, 8, 3]
        sorter = Sorter(MergeSortStrategy())
        sorted_data = sorter.sort_data(data)
        self.assertEqual(sorted_data, [1, 2, 3, 5, 7, 8])

    def test_empty_list(self):
        data = []
        sorter = Sorter(BubbleSortStrategy())
        sorted_data = sorter.sort_data(data)
        self.assertEqual(sorted_data, [])

class WordCounterTest(unittest.TestCase):
    def test_word_count(self):
        phrase = "Olá mundo! Esta é uma frase de teste."
        expected_total_count = 8

        word_counter = WordCounter()
        word_count_observer = WordCountObserver()
        word_counter.attach(word_count_observer)

        with patch('sys.stdout', new=StringIO()) as fake_output:
            word_counter.notify(phrase)
            actual_total_count = word_count_observer.total_count

        self.assertEqual(actual_total_count, expected_total_count)

    def test_even_count_words(self):
        phrase = "Esta frase possui palavras de tamanhos variados."
        expected_even_count = 5

        word_counter = WordCounter()
        word_count_observer = WordCountObserver()
        word_counter.attach(word_count_observer)

        with patch('sys.stdout', new=StringIO()) as fake_output:
            word_counter.notify(phrase)
            actual_even_count = word_count_observer.even_count

        self.assertEqual(actual_even_count, expected_even_count)

    def test_uppercase_count_words(self):
        phrase = "Amanhã irei ao cinema com minha família."
        expected_uppercase_count = 1

        word_counter = WordCounter()
        word_count_observer = WordCountObserver()
        word_counter.attach(word_count_observer)

        with patch('sys.stdout', new=StringIO()) as fake_output:
            word_counter.notify(phrase)
            actual_uppercase_count = word_count_observer.uppercase_count

        self.assertEqual(actual_uppercase_count, expected_uppercase_count)

    def test_empty_phrase(self):
        phrase = ""
        expected_total_count = 0
        expected_even_count = 0
        expected_uppercase_count = 0

        word_counter = WordCounter()
        word_count_observer = WordCountObserver()
        word_counter.attach(word_count_observer)

        with patch('sys.stdout', new=StringIO()) as fake_output:
            word_counter.notify(phrase)
            actual_total_count = word_count_observer.total_count
            actual_even_count = word_count_observer.even_count
            actual_uppercase_count = word_count_observer.uppercase_count

        self.assertEqual(actual_total_count, expected_total_count)
        self.assertEqual(actual_even_count, expected_even_count)
        self.assertEqual(actual_uppercase_count, expected_uppercase_count)


if __name__ == '__main__':
    unittest.main()
