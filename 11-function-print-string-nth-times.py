class Solution:
    def printGFG(self, n):
        if n == 0:
            return
        print('GFG', end=' ')

        self.printGFG(n - 1)

if __name__ == "__main__":
    n = 5
    Solution().printGFG(20)