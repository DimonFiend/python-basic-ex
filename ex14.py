'''
    Ex 14 - Write a program that will check if two strings are palindromes.
            A palindrome is a word that spells the same forward and backward.
            Palindrome: a word, phrase, or sequence that reads the same backward as
            forward, examples for valid palindromes: madam, nurses run.

            For example:
                first_str = "racecar"
                second_str = "Java"
                Function output should be: True (for first_str)
                                           False (for second_str)
'''
def is_palindrome(word: str) -> bool:
    str_length : int = len(word)
    for i in range(str_length // 2):
        if word[i] != word[str_length - i - 1]:
            return False
    return True

if __name__ == "__main__":
    first_str : str = "racecar"
    second_str : str = "Java"
    print(is_palindrome(first_str))
    print(is_palindrome(second_str))

