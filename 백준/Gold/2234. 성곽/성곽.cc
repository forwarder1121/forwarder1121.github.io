#include <iostream>
using namespace std;
int M,N;

int visited[51][51],map[51][51];
int dx[4]={-1,0,1,0};
int dy[4]={0,-1,0,1};
int roomSize[2501];
int groupNum;
int maxRoomSize;
int crashedMaxRoomSize;

void go(int y,int x,int group){
    
    // visiting process
    visited[y][x]=group;
    roomSize[group]++;

    // bruching & pruning process
    for(int i=0;i<4;i++){
        int nx=x+dx[i];
        int ny=y+dy[i];
        if(nx<0 || nx>=N || ny<0 || ny>=M) continue;
        if(!((map[y][x]>>i)&1)&&!visited[ny][nx]) go(ny,nx,group);
    }
}


int main(){
    //init
    cin>>N>>M;
    for(int i=0;i<M;i++){
        for(int j=0;j<N;j++){
            cin>>map[i][j];
        }
    }

    //dfs
    for(int i=0;i<M;i++){
        for(int j=0;j<N;j++){
            if(!visited[i][j]){
                go(i,j,++groupNum);;
            }
        }
    }

    for(int i=1;roomSize[i];i++) maxRoomSize=max(roomSize[i],maxRoomSize);

    for(int i=0;i<M;i++){
        for(int j=0;j<N;j++){
            if(i+1<M){
                int currentGroup=visited[i][j];
                int nextGroup=visited[i+1][j];
                if(currentGroup!=nextGroup) crashedMaxRoomSize=max(crashedMaxRoomSize,roomSize[currentGroup]+roomSize[nextGroup]);
            }
            if(j+1<N){
                int currentGroup=visited[i][j];
                int nextGroup=visited[i][j+1];
                if(currentGroup!=nextGroup) crashedMaxRoomSize=max(crashedMaxRoomSize,roomSize[currentGroup]+roomSize[nextGroup]);
            }
            
        }
    }

    cout<<groupNum<<endl;
    cout<<maxRoomSize<<endl;
    cout<<crashedMaxRoomSize<<endl;

    return 0;
}
