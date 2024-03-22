#include <stdio.h>
#include <string.h>
#include <iostream>
#include <vector>
using namespace std;
string str;
int cnt[26];
int main(){
    cin>>str;
    for(char a:str){
        cnt[a-'a']++;
    }
    for(int i:cnt) cout<<i<<" ";
    return 0;
}