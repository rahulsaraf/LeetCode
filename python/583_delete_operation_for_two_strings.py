"""

Given two words word1 and word2, find the minimum number of steps required to 
make word1 and word2 the same, where in each step you can delete one character
in either string.

@author: Lisong Guo <lisong.guo@me.com>
@date:   Nov 08, 2018

"""


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        rows = len(word1) + 1
        cols = len(word2) + 1

        dp = [[0 for j in range(cols)] for i in range(rows)]

        for irow in range(rows):
            dp[irow][0] = irow
        for icol in range(cols):
            dp[0][icol] = icol

        for irow in range(0, rows-1):
            for icol in range(0, cols-1):
                if word1[irow] == word2[icol]:
                    dp[irow+1][icol+1] = dp[irow][icol]
                else:
                    delete_1 = dp[irow][icol+1]
                    delete_2 = dp[irow+1][icol]

                    dp[irow+1][icol+1] = \
                        min(delete_1, delete_2) + 1
        print(dp)
        
        return dp[rows-1][cols-1]

    
    def minDistance_hashtable(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        from collections import defaultdict
        dtable = defaultdict()

        def backtrace(word1, word2):
            key = (word1, word2)

            if len(word1) == 0:
                dtable[key] = len(word2)
            if len(word2) == 0:
                dtable[key] = len(word1)

            if key in dtable:
                return dtable[key]

            if word1[0] == word2[0]:
                dtable[key] = backtrace(word1[1:], word2[1:])
                return dtable[key]
            else:
                delete_1 = backtrace(word1[1:], word2)
                delete_2 = backtrace(word1, word2[1:])
                dtable[key] = min(delete_1, delete_2) + 1 
                return dtable[key]

        return backtrace(word1, word2)


    def minDistance_lcs(self, word1, word2):
        """
            The idea here is to calculate the longest common substring between
             the two strings, then the minimal deletion distance would be:
             len(word1) + len(word2) - 2 * lcs(word1, word2)
        :type word1: str
        :type word2: str
        :rtype: int
        """
        from collections import defaultdict
        dp = defaultdict(int)

        def lcs(word1, word2):
            s1 = len(word1)
            s2 = len(word2)
            if s1 == 0 or s2 == 0:
                return 0

            key = (s1, s2)
            if key in dp:
                return dp[key]

            if word1[0] == word2[0]:
                dp[key] = 1 + lcs(word1[1:], word2[1:])
            else:
                delete_1 = lcs(word1[1:], word2)
                delete_2 = lcs(word1, word2[1:])
                dp[key] = max(delete_1, delete_2)
                
            return dp[key]
        
        return len(word1) + len(word2) - 2*lcs(word1, word2)


def verify(case_name, test_input, test_target, test_func):
    """
       utility function for unit testing
    """
    actual_output = test_func(*test_input)
    print(case_name, test_input, ' target:', test_target,
          ' output:', actual_output)
    assert(test_target == actual_output)


if __name__ == "__main__":

    solution = Solution()

    word1 = "sea"
    word2 = "eat"
    test_case_1_input = (word1, word2)
    test_case_1_target = 2  # sea -> ea    eat -> ea
    #verify('test case 1:',
    #       test_case_1_input, test_case_1_target, solution.minDistance_hashtable)

    verify('test case 1:',
           test_case_1_input, test_case_1_target, solution.minDistance_lcs)



