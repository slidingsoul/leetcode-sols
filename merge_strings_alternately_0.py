class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        counter = len(word1)

        if len(word2) < len(word1):
            counter = len(word2)

        res = ""

        for i in range(counter):
            res += word1[i]
            res += word2[i]

        if len(word2) < len(word1):
            res += word1[i+1:]
        elif len(word1) < len(word2):
            res += word2[i+1:]

        return res