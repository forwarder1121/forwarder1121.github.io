#include <stdio.h>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    //input
    vector<int> v(9);
    for(int i=0;i<9;i++) {
       cin>>v[i];
    }
    sort(v.begin(),v.end());
    
    do{
        int sum=0;
        for(int i=0;i<7;i++) sum+=v[i];
        if(sum==100) break;
    }while(next_permutation(v.begin(),v.end()));
    for(int i=0;i<7;i++) cout<<v[i]<<" ";
}