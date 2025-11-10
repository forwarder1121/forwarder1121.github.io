import java.util.*;
class Solution {
    public int solution(int[][] maps) {
        final int N=maps.length;
        final int M=maps[0].length;
        
        boolean[][] visited=new boolean[N][M];
        int[][] dist=new int[N][M];
        
        int[] dx={-1,1,0,0};
        int[] dy={0,0,-1,1};
        
        Deque<int[]> queue=new ArrayDeque<>();
        queue.addLast(new int[]{0,0});
        visited[0][0]=true;
        dist[0][0]=1;
        
        while(!queue.isEmpty()){
            int []cur=queue.pollFirst();
            int cx=cur[0];
            int cy=cur[1];
            if (cx==N-1&&cy==M-1){
                return dist[cx][cy];
            }
            for (int i=0;i<4;i++){
                int nx=cx+dx[i];
                int ny=cy+dy[i];
                if (nx>=0&&nx<N&&ny>=0&&ny<M) {
                    if (maps[nx][ny]==1&&!visited[nx][ny]){
                        visited[nx][ny]=true;
                        dist[nx][ny]=dist[cx][cy]+1;
                        queue.addLast(new int[] {nx,ny});
                    }
                }
            }   
        }
        return -1;
    }
}