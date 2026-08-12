class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        left = 0
        answer = 0
        for i in range(len(fruits)):
            fruit = fruits[i]
            if fruit in basket:
                basket[fruit]+=1
            else:
                basket[fruit]=1
            while len(basket)>2:
                old_fruit=fruits[left]
                basket[old_fruit]-=1
                if basket[old_fruit]==0:
                    del basket[old_fruit]
                left+=1
            current_length=i-left+1
            if current_length>answer:
                answer=current_length
        return answer