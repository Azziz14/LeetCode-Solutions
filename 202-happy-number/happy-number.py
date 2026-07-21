class Solution:
    def getnext(self,num):
        total = 0
        while num>0:
            digit=num%10
            total+=digit**2
            num=num//10
        return total
    def isHappy(self, n: int) -> bool:
        slow = n 
        fast = n
       
        while True:
            slow = self.getnext(slow)
            fast= self.getnext(self.getnext(fast))
            if slow==fast:
                break 
        return slow==1