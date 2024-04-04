#include <iostream>
#include <vector>

using namespace std;

vector<pair<int,int>> chicken,house;
vector<vector<int>>chickenList;
int N,M;
int map[52][52];
int result=1000000000;
void combination(int start,vector<int> v){
    if(v.size()==M){
        chickenList.push_back(v);
        return;
    }
    for(int i=start+1;i<chicken.size();i++){
        v.push_back(i);
        combination(i,v);
        v.pop_back();
    }
}

int main(){
    //input
    
    cin>>N>>M;
    
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cin>>map[i][j];
        }
    }

    //find Chicken, house
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(map[i][j]==1) house.push_back({i,j});
            if(map[i][j]==2) chicken.push_back({i,j});
        }
    }
    //combination --> stored in chickenList
    vector<int> v;
    combination(-1,v);

    //bfs(shortest route)
    for(vector<int> cList : chickenList){
        int ret=0;
        for(pair<int,int> home:house){
            int _min=100000000;
            for(int ch:cList){
                int distance=abs(home.first-chicken[ch].first)+abs(home.second-chicken[ch].second);
                _min=min(_min,distance);
            }
            ret+=_min;
        }
        result=min(result,ret);
    }

    cout<<result<<"\n";




    return 0;
}