class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.locations = defaultdict(list)

        for index, word in enumerate(wordsDict):
            self.locations[word].append(index)

    def shortest(self, word1: str, word2: str) -> int:
        index_word1 = self.locations[word1]
        index_word2 = self.locations[word2]
        result = float("inf")

        for x in index_word1:
            for y in index_word2:
                result = min(result, abs(y - x))
        return result
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
