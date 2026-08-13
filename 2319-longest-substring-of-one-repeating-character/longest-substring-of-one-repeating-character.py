from typing import List

class Node:
    def __init__(self, size=1, max_len=1, pref_len=1, suff_len=1, pref_char='', suff_char=''):
        self.size = size
        self.max_len = max_len
        self.pref_len = pref_len
        self.suff_len = suff_len
        self.pref_char = pref_char
        self.suff_char = suff_char

class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.s = s
        self.tree = [Node() for _ in range(4 * self.n)]
        self._build(1, 0, self.n - 1)

    def _merge(self, left: Node, right: Node) -> Node:
        res = Node()
        res.size = left.size + right.size
        res.pref_char = left.pref_char
        res.suff_char = right.suff_char
        
        # Update prefix
        res.pref_len = left.pref_len
        if left.pref_len == left.size and left.pref_char == right.pref_char:
            res.pref_len += right.pref_len
            
        # Update suffix
        res.suff_len = right.suff_len
        if right.suff_len == right.size and right.suff_char == left.suff_char:
            res.suff_len += left.suff_len
            
        # Update max length
        res.max_len = max(left.max_len, right.max_len)
        if left.suff_char == right.pref_char:
            res.max_len = max(res.max_len, left.suff_len + right.pref_len)
            
        return res

    def _build(self, node: int, start: int, end: int):
        if start == end:
            char = self.s[start]
            self.tree[node] = Node(1, 1, 1, 1, char, char)
            return
            
        mid = (start + end) // 2
        self._build(2 * node, start, mid)
        self._build(2 * node + 1, mid + 1, end)
        self.tree[node] = self._merge(self.tree[2 * node], self.tree[2 * node + 1])

    def update(self, node: int, start: int, end: int, idx: int, char: str):
        if start == end:
            self.tree[node] = Node(1, 1, 1, 1, char, char)
            return
            
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, char)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, char)
            
        self.tree[node] = self._merge(self.tree[2 * node], self.tree[2 * node + 1])
        
    def get_max(self) -> int:
        return self.tree[1].max_len

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        seg_tree = SegmentTree(s)
        ans = []
        n = len(s)
        
        for i in range(len(queryIndices)):
            idx = queryIndices[i]
            char = queryCharacters[i]
            seg_tree.update(1, 0, n - 1, idx, char)
            ans.append(seg_tree.get_max())
            
        return ans