"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """
    Word Finder: finds random words from a dictionary.
    
    >>> wf = WordFinder("words.txt")
    235886 words read
    
    >>> len(wf.words) > 0
    True
    
    >>> wf.words[0] == "A"
    True
    """

    def __init__(self, path):
        """Reads dictionary and reports number of items read."""
        with open(path, 'r') as file:
            self.words = [line.strip() for line in file if line.strip()]
        print(f"{len(self.words)} words read")

    def random(self):
        """Return a random word from the list of words."""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """
    Special Word Finder: excludes blank lines and comments from the dictionary.
    
    Uses 'specialwords.txt' file, which contains both words and comments.
    
    >>> swf = SpecialWordFinder("specialwords.txt")
    4 words read
    
    >>> len(swf.words)
    4
    
    >>> 'kale' in swf.words
    True
    
    >>> 'apple' in swf.words
    True
    
    >>> swf.random() in ['kale', 'parsnips', 'apple', 'mango']
    True
    """
    
    def __init__(self, path):
        """Reads file and ignores comments and blank lines."""
        with open(path, 'r') as file:
            self.words = [line.strip() for line in file if line.strip() and not line.startswith("#")]
        print(f"{len(self.words)} words read")
