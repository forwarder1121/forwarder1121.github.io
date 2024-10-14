#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
int N,ret;
vector<pair<int,int>> v;
int main(){

    //initialize
    cin>>N;
    for(int i=0;i<N;i++){
        int deadline,reward;
        cin>>deadline>>reward;
        v.push_back({deadline,reward});
    }

    sort(v.begin(),v.end());

    priority_queue<int,vector<int>,greater<int>> pq;
    for(pair<int,int> problem:v){
        int deadline,reward;
        deadline=problem.first;
        reward=problem.second;
        // 일단 풀 수 있다고 가정
        ret+=reward;
        pq.push(reward);

        // 만약 못 푼 문제였다면 가장 가치가 없는 일 제거
        if(pq.size()>deadline){
            ret-=pq.top();
            pq.pop();
        }
    }

    //print result
    cout<<ret<<endl;

    return 0;
}