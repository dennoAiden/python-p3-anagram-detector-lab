class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        # Helper function to check if two words are anagrams
        def is_anagram(w1, w2):
            return sorted(w1) == sorted(w2)
        
        # Filter the list to find words that are anagrams of the initialized word
        return [w for w in words if is_anagram(self.word, w)]
