#include <iostream>

using namespace std;
int map[6][6];
int R,C,K;
int cnt;
int visited[6][6];
int dy[]={1,0,-1,0};
int dx[]={0,-1,0,1};
void go(int y,int x){
    if(visited[y][x]>K) return;
    if(y==0&&x==C-1) {
        if(visited[0][C-1]==K) cnt++;
        return;
    }
    
    for(int i=0;i<4;i++){
        int ny=y+dy[i];
        int nx=x+dx[i];
        if(ny<0||ny>=R||nx<0||nx>=C) continue;
        if(visited[ny][nx]) continue;
        if(map[ny][nx]) continue;
        visited[ny][nx]=visited[y][x]+1;
        go(ny,nx);
        visited[ny][nx]=0;
    }
    

}

int main(){

    //init
    cin>>R>>C>>K;
    for(int i=0;i<R;i++){
        for(int j=0;j<C;j++){
            char tmp;
            cin>>tmp;
            map[i][j]=(tmp=='T'?1:0);
        }
    }
    //dfs
    visited[R-1][0]=1;
    go(R-1,0);

    cout<<cnt<<endl;

    return 0;
}