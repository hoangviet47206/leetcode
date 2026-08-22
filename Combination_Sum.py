class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        tmp = []
        def backtrack(start, path, total):
            if total == target:
                tmp.append(path[:])
                return
            if total > target:
                return
            for j in range(start, len(candidates)):
                path.append(candidates[j])
                backtrack(j, path, total + candidates[j])
                path.pop()
        backtrack(0, [], 0)
        return tmp
                    
def main():
    sol = Solution()
    result = sol.combinationSum(candidates = [2,3,6,7], target = 7)
    print(result)
if __name__ == "__main__":
    main()
            