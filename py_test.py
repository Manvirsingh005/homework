import pytest


def count_vowel_consonant_pairs(text):
    """
    Counts the number of occurrences where a vowel is
    immediately followed by a consonant in the input string.

    Args:
        text (str): The input string to analyze.

    Returns:
        int: Count of vowel-consonant pairs.
    """
    vowels = "aeiouAEIOU"
    count = 0

    for i in range(len(text) - 1):
        if text[i] in vowels and text[i + 1].isalpha() and text[i + 1] not in vowels:
            count += 1

    return count


# Parameterized test
test_data = [("hello", 1), ("", 0), ("12345", 0), ("PyThOn", 1), ("a!e@i#o$u%", 0),]


@pytest.mark.parametrize("input_string, expected_output", test_data)
def test_count_vowel_consonant_pairs(input_string, expected_output):
    assert count_vowel_consonant_pairs(input_string) == expected_output


'''@pytest.fixture()'''

