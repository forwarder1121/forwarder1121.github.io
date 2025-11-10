class Solution {
    public int solution(int n, int[][] computers) {
        boolean[] visited=new boolean[n];
        int answer = 0;
        for(int i=0;i<n;i++){
            if(!visited[i]){
                dfs(n,computers,visited,i);
                answer++;
            }
        }
        return answer;
    }
    
    private void dfs(int N, int[][] computers, boolean[] visited,int u){
        visited[u]=true;
        for (int v=0;v<N;v++){
            if (computers[u][v]==1&&!visited[v]){
                dfs(N,computers,visited,v);
            }
        }
    }
}