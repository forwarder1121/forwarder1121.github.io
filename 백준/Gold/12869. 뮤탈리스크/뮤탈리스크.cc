#include <iostream>
#include <vector>
#include <queue>
using namespace std;
const int MAX=1000000;
int visited[64][64][64];
int N;
int attack[6][3]={
    {9, 3, 1}, 
	{9, 1, 3}, 
	{3, 1, 9}, 
	{3, 9, 1}, 
	{1, 3, 9}, 
	{1, 9, 3},
};

typedef struct scvHeart{
    int a,b,c;
} scv;
int a[3];
queue<scvHeart> q;
int solve(int a,int b,int c){
    visited[a][b][c]=1;
    q.push({a,b,c});
    while(q.size()){
        scv here=q.front(); q.pop();
        if(visited[0][0][0]) break;
        for(int i=0;i<6;i++){
            scv next;
            next.a=max(0,here.a-attack[i][0]);
            next.b=max(0,here.b-attack[i][1]);
            next.c=max(0,here.c-attack[i][2]);
            if(visited[next.a][next.b][next.c]) continue;
            visited[next.a][next.b][next.c]=visited[here.a][here.b][here.c]+1;
            q.push(next);
        }
    }
    return visited[0][0][0]-1;
}

int main(){
    //init
    cin>>N;
    for(int i=0;i<N;i++) cin>>a[i];

    //bfs
    cout<<solve(a[0],a[1],a[2])<<endl;


    return 0;
}