class Solution {
    public int solution(int[] numbers, int target) {
        int answer = dfs(numbers,target,0,0);
        return answer;
    }
    
    private int dfs(int[] numbers,int target,int depth,int cur_num){
        int count=0;
        // base-condition
        if (depth==numbers.length){
            return target==cur_num?1:0;
        }
        // apply
        count+=dfs(numbers,target,depth+1,cur_num+numbers[depth]);
        count+=dfs(numbers,target,depth+1,cur_num-numbers[depth]);
        return count;
    }
}