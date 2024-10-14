#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int n,l,r,x,ret;
vector<int> v;
int main(){

    //initialize
    cin>>n;
    l=0,r=n-1;
    for(int i=0; i<n; i++) {
        int tmp;
        cin>>tmp;
        v.push_back(tmp);
    }
    cin>>x;
    sort(v.begin(), v.end());

    //find the count of pairs that sum up to x
    while(l<r){
        int sum=v[l]+v[r];
        if(sum>x) r--;
        else if(sum<x) l++;
        else{
            ret++;
            r--;
            l++;
        }
    }

    cout<<ret<<endl;
    return 0;
}