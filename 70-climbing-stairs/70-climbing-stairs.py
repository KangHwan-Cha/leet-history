class Solution:
    def climbStairs(self, n: int) -> int:
        # 상수 보다 작은 경우는 예외 처리
        prev = 0
        curr = 1
        Temp = 0
        for _ in range(1, n+1):
            Temp = prev + curr
            prev, curr = curr, Temp
        
        return Temp