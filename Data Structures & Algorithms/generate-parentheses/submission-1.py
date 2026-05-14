class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # ()
        # (()) ()()
        # ((())) (())() ()(()) ()()() (()())

        # base case ()
        # for each case n > 1
            # we can either surround each prevoius result or prepend/append each previous result
        if n == 0:
            return []
        results = []

        def backtrack(curr: str, openn, closed):
            if closed == openn == n:
                results.append(curr)
            if openn < n:
                backtrack(curr + "(", openn + 1, closed)
            if closed < openn:
                backtrack(curr + ")", openn, closed + 1)

        backtrack("", 0, 0)
        return results