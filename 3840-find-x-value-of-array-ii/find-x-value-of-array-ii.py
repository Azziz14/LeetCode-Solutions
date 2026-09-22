class SegmentTreeNode:
    def __init__(self, k):
        self.count = [0] * k
        self.prod = 1  # Total product in this node modulo k

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = [SegmentTreeNode(k) for _ in range(4 * n)]
        
        def combine(left_node, right_node, k):
            res = SegmentTreeNode(k)
            res.prod = (left_node.prod * right_node.prod) % k
            
            # Left node counts remain as they are
            for i in range(k):
                res.count[i] = left_node.count[i]
            
            # Combine left node's total product with right node's counts
            for i in range(k):
                if right_node.count[i] > 0:
                    new_rem = (left_node.prod * i) % k
                    res.count[new_rem] += right_node.count[i]
            
            return res

        def build(node, start, end):
            if start == end:
                rem = nums[start] % k
                tree[node].count = [0] * k
                tree[node].count[rem] = 1
                tree[node].prod = rem
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = combine(tree[2 * node], tree[2 * node + 1], k)

        def update(node, start, end, idx, val):
            if start == end:
                nums[idx] = val
                rem = val % k
                tree[node].count = [0] * k
                tree[node].count[rem] = 1
                tree[node].prod = rem
                return
            mid = (start + end) // 2
            if start <= idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
            tree[node] = combine(tree[2 * node], tree[2 * node + 1], k)

        def query(node, start, end, l, r):
            if r < start or end < l:
                dummy = SegmentTreeNode(k)
                dummy.prod = 1
                return dummy
            if l <= start and end <= r:
                return tree[node]
            mid = (start + end) // 2
            p1 = query(2 * node, start, mid, l, r)
            p2 = query(2 * node + 1, mid + 1, end, l, r)
            return combine(p1, p2, k)

        build(1, 0, n - 1)
        result = []

        for idx_i, val_i, start_i, x_i in queries:
            update(1, 0, n - 1, idx_i, val_i)
            res_node = query(1, 0, n - 1, start_i, n - 1)
            result.append(res_node.count[x_i])

        return result