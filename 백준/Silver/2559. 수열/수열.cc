#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int N,K;

int main(){
    //input
    cin>>N>>K;
    int arr[N+1];
    for(int i=1;i<=N;i++){
        cin>>arr[i];
    }
    //make presum
    vector<int> psum(N+1);
    for(int i=1;i<=N;i++){
        psum[i]=psum[i-1]+arr[i];
    }
    
    int max=-100*N;

    for(int i=1;i+K-1<=N;i++){
        //tmp_sum : sum of arr[i]~arr[i+K-1]
        int tmp_sum=psum[i+K-1]-psum[i-1];
        if(tmp_sum>max) max=tmp_sum;
    }
    cout<<max<<endl;
    return 0;
}
