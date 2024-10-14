#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;
long long N,K,ret;
vector<pair<int,int>> jewels;
vector<int> bags;
int main(){

    //intialize
    cin>>N>>K;
    for(int i=0;i<N;i++){
        int weight, value;
        cin>>weight>>value;
        jewels.push_back({weight, value});
    }

    for(int i=0;i<K;i++){
        int bagsize;
        cin>>bagsize;
        bags.push_back(bagsize);
    }

    sort(jewels.begin(),jewels.end());    
    sort(bags.begin(),bags.end());
    
    //greedy algorithm
    priority_queue<int> pq;
    int jewelIndex=0;
    for(int bagIndex=0;bagIndex<K;bagIndex++){
        while(jewels[jewelIndex].first<=bags[bagIndex]&&jewelIndex<N){
            pq.push(jewels[jewelIndex].second);
            jewelIndex++;
        }
        if(!pq.empty()){
            ret+=pq.top();
            pq.pop();
        }
    }

    //print results
    cout<<ret;

    return 0;
}