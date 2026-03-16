import java.util.*;
class Solution {
    static final int SIZE=51;
    static final int SCALE=2;
    static final int MAX=SIZE*SCALE+1;
    static final int[] dx={-1,1,0,0};
    static final int[] dy={0,0,-1,1};
        
    public int solution(int[][] rectangles, int characterX, int characterY, int itemX, int itemY) {
        boolean[][] graph=new boolean[MAX][MAX];
        
        for(int[] r: rectangles){
            int x1=r[0]*SCALE;
            int y1=r[1]*SCALE;
            int x2=r[2]*SCALE;
            int y2=r[3]*SCALE;
            for(int x=x1;x<x2+1;x++){
                for(int y=y1;y<y2+1;y++){
                    graph[x][y]=true;
                }
            }
        }
        for(int[] r: rectangles){
            int x1=r[0]*SCALE;
            int y1=r[1]*SCALE;
            int x2=r[2]*SCALE;
            int y2=r[3]*SCALE;
            for(int x=x1+1;x<x2;x++){
                for(int y=y1+1;y<y2;y++){;
                    graph[x][y]=false;
                }
            }
        }
        
        int sx=characterX*SCALE;
        int sy=characterY*SCALE;
        int tx=itemX*SCALE;
        int ty=itemY*SCALE;
        
        // BFS
        int[][] dist=new int[MAX][MAX];
        for(int x=0;x<MAX;x++){
            for(int y=0;y<MAX;y++){
                dist[x][y]=-1;
            }
        }
        
        Deque<int[]> queue=new ArrayDeque<>();
        queue.addLast(new int[]{sx,sy});
        dist[sx][sy]=0;
        
        while(!queue.isEmpty()){
            int[] cur=queue.pollFirst();
            int cx=cur[0],cy=cur[1];
            if (cx==tx&&cy==ty){
                return dist[cx][cy]/2;
            }
            for(int i=0;i<4;i++){
                int nx=cx+dx[i];
                int ny=cy+dy[i];
                if ((0<=nx)&&(nx<MAX)&&(0<=ny)&&(ny<MAX)){
                    if ((graph[nx][ny]==true)&&(dist[nx][ny]==-1)){
                        dist[nx][ny]=dist[cx][cy]+1;
                        queue.addLast(new int[] {nx,ny});
                    }
                }
            }
            
        }
        return -1;
    }
}