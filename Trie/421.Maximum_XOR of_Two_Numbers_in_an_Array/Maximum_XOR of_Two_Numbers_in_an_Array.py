class Trie:
    def __init__(self, *words):
        self.root = dict()
        for word in words:
            self.add(word)

    def add(self, word):
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, dict())
            
    def find_max_xor(self,num) -> int:
        curr_bit = []
        word = (bin(num)[2:]).zfill(31)
        current_dict = self.root
        for letter in word:

            if letter == '0': c = '1'
            else: c = '0'
            if c not in current_dict:
                current_dict = current_dict[letter]
                curr_bit.append(0)
            else:
                current_dict = current_dict[c] 
                curr_bit.append(1)
        ans = 0
        for i in curr_bit:
            ans <<= 1
            ans += i
        return ans


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        total_tmp = []
        for num in nums:
            tmp = []
            for i in (bin(num)[2:].zfill(31)): 
                tmp.append(i)
            total_tmp.append(tmp)
        bt = Trie(total_tmp[0])
        for i in total_tmp[1:]: bt.add(i)

        mx = 0
        for num in nums:
            num = bt.find_max_xor(num)
            mx = max(num, mx)
        return mx
        
    
        