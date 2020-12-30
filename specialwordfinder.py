from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """
    A subclass of Wordfinder that accouts for files that have extra lines and python comments
    """
    def __init__(self, path):
        """Creates a SpecialWordFinder class
        
        words: list
            list of words that does not include empty lines and python comments
        """
        super().__init__(path)
        self.words = [word for word in self.words if not word == "\n" and not word.startswith("#")]
