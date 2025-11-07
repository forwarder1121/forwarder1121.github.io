class Solution {
    public int solution(int n, int[][] computers) {
       final int N=n;
        boolean[] visited=new boolean[N];
        int count=0;
        
        for(int i=0;i<N;i++){
            if(!visited[i]){
                dfs(i,computers,visited,N);
                count++;
            }
        }
        return count;
    }
    private void dfs(int u,int[][] computers,boolean[] visited,int N){
        visited[u]=true;
        for(int v=0;v<N;v++){
            if(computers[u][v]==1&&!visited[v]){
                dfs(v,computers,visited,N);
            }
        }
    }
}