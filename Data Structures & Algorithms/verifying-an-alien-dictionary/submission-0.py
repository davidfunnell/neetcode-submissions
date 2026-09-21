class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {letter:i for i, letter in enumerate(order)}

        for x in range(len(words) - 1):
            word1 = words[x]
            word2 = words[x+1]

            for y in range(len(word1)):
                if y == len(word2):
                    return False
                if word1[y] != word2[y]:
                    if order_dict[word1[y]] > order_dict[word2[y]]:
                        return False
                    break

        return True