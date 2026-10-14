class Solution {
    public int[] rearrangeArray(int[] nums) {
        int[] result = new int[nums.length];
        int pos =0;
        int neg =1;
        for (int x:nums){
            if (x > 0){
                result[pos]=x;
                pos +=2;
            }
            else{
                result[neg]=x;
                neg += 2;
            }
        }
        return result;
    }
}