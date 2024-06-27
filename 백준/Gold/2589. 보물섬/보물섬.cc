#include <iostream>
#include <queue>
using namespace std;

int N,M;
int map[51][51],tempMap[51][51];
int dy[]={-1,0,1,0};
int dx[]={0,1,0,-1};

queue<pair<int,int>> q;

int ret=0;

int main(){

    //input (W : 0, L : 1)
    cin>>N>>M;
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            char temp;
            cin>>temp;
            if(temp=='W') map[i][j]=0;
            else map[i][j]=1;
        }
    }

    

    //bfs(for each L)
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            bool visited[51][51]={false};
            //init temp map
            for(int a=0;a<N;a++){
                for(int b=0;b<M;b++){
                    tempMap[a][b]=map[a][b];
                }
            }
            //if i,j is land
            if(tempMap[i][j]){
                visited[i][j]=true;
                q.push({i,j});
                while(q.size()){
                    pair<int,int> here=q.front(); q.pop();
                    for(int k=0;k<4;k++){
                        int ny=here.first+dy[k];
                        int nx=here.second+dx[k];
                        if(ny<0||ny>=N||nx<0||nx>=M) continue;
                        if(!map[ny][nx]) continue;
                        if(visited[ny][nx]) continue;
                        visited[ny][nx]=true;
                        tempMap[ny][nx]=tempMap[here.first][here.second]+1;
                        q.push({ny,nx});
                        ret=max(ret,tempMap[ny][nx]);
                    }
                }    
            }
            
            
        }
    }

    
    cout<<ret-1<<endl;


    return 0;
}