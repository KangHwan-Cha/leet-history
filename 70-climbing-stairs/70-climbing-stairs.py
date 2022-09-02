class Solution:
    def climbStairs(self, n: int) -> int:
        # 상수 보다 작은 경우는 예외 처리
        if n <= 2:
            return n
        
        steps = [0] * (n+1)
        steps[0] = 0
        steps[1] = 1
        steps[2] = 2
        num = 3
        while True:
            steps[num] = steps[num-2] + steps[num-1]
            num += 1
            if num > n: break
        
        return steps[num-1]