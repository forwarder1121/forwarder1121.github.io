#include <iostream>

using namespace std;

int N,ret=100000000;
int map[11][11];
int flowerMap[11][11];
int dy[]={1,0,-1,0};
int dx[]={0,1,0,-1};

void eraseFlower(int y,int x){
    flowerMap[y][x]=0;
    for(int i=0;i<4;i++){
        int ny=y+dy[i];
        int nx=x+dx[i];
        flowerMap[ny][nx]=0;
    }
}

int setFlower(int y,int x){
    flowerMap[y][x]=1;
    int limitCost=map[y][x];
    for(int i=0;i<4;i++){
        int ny=y+dy[i];
        int nx=x+dx[i];
        flowerMap[ny][nx]=1;
        limitCost+=map[ny][nx];
    }
    return limitCost;
}


bool check(int y,int x){
    if(flowerMap[y][x]) return 0;
    for(int i=0;i<4;i++){
        int ny=y+dy[i];
        int nx=x+dx[i];
        if(ny<0||ny>=N||nx<0||nx>=N||flowerMap[ny][nx]) return 0;
    }
    return 1;
}

void plantFlower(int cnt,int cost){
    if(cnt==3){
        ret=min(ret,cost);
        return;
    }
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(check(i,j)){
                plantFlower(cnt+1,cost+setFlower(i,j));
                eraseFlower(i,j);
            }
        }
    }
}

int main(){
    //init
    cin>>N;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cin>>map[i][j];
        }
    }
    plantFlower(0,0);
    cout<<ret;
    


    return 0;
}