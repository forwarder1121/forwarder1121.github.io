#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;
int N;
int main(){

    //initalize
    cin>>N;
    priority_queue<float> pq;
    for(int i=0;i<N;i++){
        float tmp;
        cin>>tmp;
        if(pq.size()==7){
            if(tmp<pq.top()){
                pq.pop();
                pq.push(tmp);
            }  
        }else{
            pq.push(tmp);
        }
    }
    vector<float> v;
    while(!pq.empty()){
        v.push_back(pq.top());
        pq.pop();
    }
    reverse(v.begin(),v.end());
    //print 7 smallest elements
    for(float ret:v) printf("%.3f\n",ret);

    return 0;
}