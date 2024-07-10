#include <iostream>
using namespace std;
int ret;
int R,C;
int visited;
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};
char**map;
void go(char** map,int x,int y,int depth){
    ret=max(ret,depth);
    visited|=(1<<(map[x][y]-'A'));
    for(int i=0;i<4;i++){
        int nx=x+dx[i];
        int ny=y+dy[i];
        if(nx>=0&&nx<R&&ny>=0&&ny<C){
            if(visited&(1<<(map[nx][ny]-'A'))) continue;
            //visiting process
            go(map,nx,ny,depth+1);
            //restore
            visited^=(1<<(map[nx][ny]-'A'));
        }
    }
}

int main(){

    //init
    cin>>R>>C;
    map=new char*[R];
    for(int i=0;i<R;i++){
        map[i]=new char[C];
    }
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cin >> map[i][j];
        }
    }

    go(map,0,0,1);
   
    cout<<ret<<endl;
    
    return 0;
}
