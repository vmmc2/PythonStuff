class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        # Treating the corner cases
        if numRows == 0: 
            return answer
        # Treating the general cases...
        for i in range(1, numRows + 1):
            answer.append([1 for i in range(0, i)])
        for i in range(1, len(answer) - 1):
            for j in range (0, len(answer[i]) - 1):
                answer[i + 1][j + 1] = answer[i][j] + answer[i][j + 1]
        print(answer)
        return answer
