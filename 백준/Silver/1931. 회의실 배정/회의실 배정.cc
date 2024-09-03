#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N,ret;
vector<pair<int,int>> list;
int main(){

    //initialize
    cin>>N;
    for(int i=0;i<N;i++){
        pair<int,int> p;
        cin>>p.second>>p.first;
        list.push_back(p);
    }

    //sort by end-of-pair
    sort(list.begin(),list.end());

    //check logic
    int from,to;
    to=list[0].first;
    from=list[0].second;
    ret++;
    list.pop_back();
    
    for(int i=1;i<N;i++){
        if(list[i].second<to) continue;
        from=list[i].second;
        to=list[i].first;
        ret++;
    }

    //print result
    cout<<ret<<'\n';

    return 0;
}