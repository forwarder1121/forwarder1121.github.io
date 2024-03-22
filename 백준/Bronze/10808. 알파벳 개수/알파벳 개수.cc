#include <stdio.h>
#include <string.h>
#include <iostream>
#include <vector>
using namespace std;
int main(){

    //input
    string str;
    cin>>str;
    vector<int> v(26);
    for(int i=0;i<26;i++){
        char check='a'+i;
        for(int j=0;j<str.length();j++){
            if(str[j]==check) v[i]++;
        }
    }

    for(int i:v){
        cout<<i<<" ";
    }
    

    return 0;
}