#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N,a,b,lastFinish;
vector<pair<int,int>> v;
int main(){

    cin>>N;
    for(int i=0;i<N;i++){
        cin>>a>>b;
        v.push_back({a,b});
    }
    sort(v.begin(),v.end());

    for(pair<int,int> item : v){
        int arrive=item.first;
        int taking=item.second;
        lastFinish=max(lastFinish,arrive)+taking;
    }

    cout<<lastFinish;

    return 0;
}