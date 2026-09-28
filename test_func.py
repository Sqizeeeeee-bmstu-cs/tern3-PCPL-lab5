from unittest.mock import patch

from functions import f1, f2, f3, gen_random
from myclass import Unique


def test_unique_removes_duplicates():
    assert list(Unique([1, 2, 1, 3, 2])) == [1, 2, 3]

def test_unique_empty():
    assert list(Unique([])) == []


def test_unique_case_sensitive_by_default():
    assert list(Unique(['a', 'A', 'a'])) == ['a', 'A']


def test_unique_ignore_case():
    assert list(Unique(['a', 'A', 'b', 'B'], ignore_case=True)) == ['a', 'b']


def test_unique_ignore_case_keeps_numbers():
    assert list(Unique([1, 'a', 'A', 1], ignore_case=True)) == [1, 'a']

# -----------------------------------------------------------------------------------------

def test_f1_unique_and_sorted():
    data = [{'job-name': 'Python'}, {'job-name': 'python'},
            {'job-name': 'Аналитик'}, {'job-name': 'Java'}]
    assert f1(data) == ['Java', 'Python', 'Аналитик']


def test_f1_empty():
    assert f1([]) == []


def test_f2_filters_by_prefix():
    data = ['Программист', 'программист Python', 'Аналитик', 'Старший программист']
    assert f2(data) == ['Программист', 'программист Python']


def test_f2_no_matches():
    assert f2(['Аналитик']) == []


def test_f3_appends_suffix():
    assert f3(['Программист']) == ['Программист с опытом Python']


def test_f3_empty():
    assert f3([]) == []


def test_gen_random_count_and_range():
    nums = list(gen_random(50, 1, 5))
    assert len(nums) == 50
    assert all(1 <= n <= 5 for n in nums)


def test_gen_random_zero():
    assert list(gen_random(0, 1, 10)) == []


def test_gen_random_with_mock():
    with patch('functions.random.randint', side_effect=[7, 8, 9]) as mock_randint:
        assert list(gen_random(3, 1, 10)) == [7, 8, 9]
    assert mock_randint.call_count == 3
    mock_randint.assert_called_with(1, 10)
