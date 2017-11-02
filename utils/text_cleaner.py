
class TextCleaner():
    def __init__(self):
        self.additional = [
            '!','[',']','{', '}','-', '(',')',"'",'"','!','%','$','#',':',';','.',',','\n','?','/','@','`','~'
        ]

    def clean_for_dictionary(self, document):
        """ Cleans text in order to create a dictionary of words.

        Args:
            document - text, could be sentence or document to be cleaned.

        Returns:
            modified string with symbols missing. replaced with spaces, but we will split
            and strip the words anyway so this is fine.
        """
        modified = document
        for a in self.additional:
            modified = " ".join(modified.split(a))
        return self._clean(modified)

    def clean_for_eval(self, document):
        """ Cleans text for evaluation.

        Args:
            document - text, could be sentence or document to be cleaned.

        Returns:
            modified string with symbols missing. replaced with spaces, but we will split
            and strip the words anyway so this is fine.
        """
        modified = document
        for a in self.additional:
            modified = modified.replace(a, ' ' + a + ' ')
        return self._clean(modified)

    def _clean(self, document):
        """ Lowers and strips words.

            Args:
                document - to be cleaned.

            Returns:
                modified string lowered
        """
        # lower and strip words (e.g. '  HellO ' => 'hello')
        modified = [w.lower().strip() for w in document.split()]
        # parse out empty strings
        modified = [w for w in modified if len(w) > 0]
        # return a string
        return " ".join(modified)