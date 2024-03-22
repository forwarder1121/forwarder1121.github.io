#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
int cnt[26];
int N;
string str;
int main(){
    
    cin>>N;
    for(int i=0;i<N;i++){
        cin>>str;
        cnt[str[0]-'a']++;
    }
    bool find=false;
    for(int i=0;i<26;i++){
        if(cnt[i]>=5) {
            cout<<(char)('a'+i);
            find=true;
        }
    }
    if(!find) cout<<"PREDAJA";

    return 0;
}
