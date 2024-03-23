#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>

using namespace std;
string pattern,str;
int N;

int main(){
    cin>>N;
    cin>>pattern;
    for(int i=0;i<N;i++){
        bool flag = true;
        cin>>str;
        //filter by length
        if(pattern.length()-1>str.length()){
            cout<<"NE"<<endl;
            continue;
        }
        //forward
        for(int j=0;j<str.length();j++){
            if(pattern[j]=='*') break;
            if(str[j]!=pattern[j]) flag = false;
        }
        
        reverse(str.begin(), str.end());
        reverse(pattern.begin(), pattern.end());
        //backward
        for(int j=0;j<str.length();j++){
            if(pattern[j]=='*') break;
            if(str[j]!=pattern[j]) flag = false;
        }

        cout<<(flag?"DA":"NE")<<endl;
        reverse(pattern.begin(), pattern.end());
    }
    return 0;
}
