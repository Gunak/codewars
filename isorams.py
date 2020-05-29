from collections import Counter

# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram.
# Ignore letter case.

def is_isogram(string):
    s = string.lower()
    count = Counter(s)
    for c in count:
        if count[c] > 1:
            return False
    return True


if __name__ == "__main__":
    print(is_isogram("Dermatoglyphics" ))
    print(is_isogram("aba" ))
    print(is_isogram("moOse" ))
