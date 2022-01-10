class Solution:
    def get_num(self, bn: str) -> int:
        return int(bn, 2)
        
    def to_binary(self, num: int) -> str:
        return bin(num)[2:]
    
    
    def addBinary(self, a: str, b: str) -> str:
        return self.to_binary(self.get_num(a) + self.get_num(b))