# LeetCode_792_Number_of_Matching _Subsequences

Given a string `s` and an array of strings `words`, return *the number of* `words[i]` *that is a subsequence of* `s`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, `"ace"` is a subsequence of `"abcde"`.

**Example 1:**

```
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

```

**Example 2:**

```
Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
```

**Constraints:**

- `1 <= s.length <= 5 * 104`
- `1 <= words.length <= 5000`
- `1 <= words[i].length <= 50`
- `s` and `words[i]` consist of only lowercase English letters.

## Solution:

我們第一步先將word開頭都丟入一結構儲存

![Untitled](LeetCode_792_Number_of_Matching%20_Subsequences%2043ed72087fc44a90a41e9d160dc77863/Untitled.png)

之後跑s的每個字元並將結構中對應的word刪掉開頭並放入新的位置中

如果無法再把word刪除開頭就ans += 1

直到跑完s得出答案

## Code:

Python

```python
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        mp = defaultdict(list); ans = 0
        for word in words: mp[word[0]].append(word)
        for word in s:
            tmp = copy.copy(mp[word])
            mp[word].clear()
            for curr_elemt in tmp:
                if len(curr_elemt) == 1: ans += 1
                else: mp[curr_elemt[1]].append(curr_elemt[1:])
        return ans
```