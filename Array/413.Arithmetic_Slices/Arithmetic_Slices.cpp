class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        if(nums.size() < 3) return 0;
        
        int n = nums[1] - nums[0], cnt = 2, total = 0;
        
        for(int i = 2; i < nums.size(); i++)
        {
            if(nums[i] - nums[i - 1] == n) cnt++;
            
            else
            {
                if(cnt >= 3)
                {
                    cnt -= 2;
                    total += ((cnt * cnt + cnt) / 2);
                }
                
                n = nums[i] - nums[i - 1];
                cnt = 2;
            }
        }
        
        if(cnt > 2)
        {
            cnt -= 2;
            total += ((cnt * cnt + cnt) / 2);
        }
        
        return total;
    }
};