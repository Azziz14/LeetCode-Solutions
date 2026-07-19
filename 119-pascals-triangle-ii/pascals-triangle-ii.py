class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        
        # Compute each element based on the previous element's value
        for k in range(1, rowIndex + 1):
            next_element = row[-1] * (rowIndex - k + 1) // k
            row.append(next_element)
            
        return row
