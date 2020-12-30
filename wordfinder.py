"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    def __init__(self, path):
        """
        Create a WordFinder from a list of words that exists in path

        path: an actual filepath to a file with a list of words, one word per line
        """
        self.path = path
        self.getWordsFromFile()

       
    def getWordsFromFile(self):
        "Get words from file and save in self.words"
        try:
            file = open(self.path)
            words = []
            for line in file:
                words.append(line)
            self.words = words
            print(f"{len(words)} words read")
        except:
            print("Could not retrieve words from path")

    def random(self):
        "Returns a random word from self.words"
        return choice(self.words).replace("\n","")
