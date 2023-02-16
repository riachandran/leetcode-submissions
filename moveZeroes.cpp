class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int read = 0, write = 0;

        for (int i=0; i<nums.size(); i++){
            if (nums[read] == 0){
                read++;
            }
            else{
                int temp = nums[write];
                nums[write] = nums[read];
                nums[read] = temp;
                write++;
                read++;
            }
        }
    }
};
