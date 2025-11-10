import java.util.*;
class Solution {
    public int solution(String begin, String target, String[] words) {
        
        boolean[] visited=new boolean[words.length];
        Deque<String[]> queue=new ArrayDeque<>();
        queue.addLast(new String[]{begin,"0"});
        
        while(!queue.isEmpty()){
            String[] cur=queue.pollFirst();
            String cur_state=cur[0];
            int depth=Integer.parseInt(cur[1]);
            if (cur_state.equals(target)) return depth;
            for(int i=0;i<words.length;i++){
                if(oneDiff(cur_state,words[i])&&!visited[i]){
                    visited[i]=true;
                    queue.addLast(new String[]{words[i],String.valueOf(depth+1)});
                }
            }
        }
        return 0;
    }
    
    private boolean oneDiff(String a,String b){
        int count=0;
        for (int i=0;i<a.length();i++){
            if(a.charAt(i)!=b.charAt(i)){
                count+=1;
            }
        }
        return count==1;
    }
}