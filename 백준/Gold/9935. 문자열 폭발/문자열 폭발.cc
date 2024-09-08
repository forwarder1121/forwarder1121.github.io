#include <iostream>
#include <stack>
#include <string>
#include <algorithm>
using namespace std;
string str,target,ret;
int j;
int main(){

    stack<char> s;
    cin>>str>>target;

    for(int i=0;i<str.length();i++){
        s.push(str[i]);
        if(s.size()>=target.size()){
            bool flag=true;
            for(j=0;j<target.length();j++){
                if(s.top()!=target[target.size()-j-1]){
                    flag=false;
                    break;
                }
                ret+=s.top();
                s.pop();
            }
            if(!flag){
               for(int k=ret.size()-1;k>=0;k--){
                    s.push(ret[k]);
               }
            } 
            ret.clear();
        }
    }
    
    //print result
    if(s.empty()){
        cout<<"FRULA";
        return 0;
    }

    while(!s.empty()){
        ret+=s.top();
        s.pop();
    }
    reverse(ret.begin(),ret.end());
    cout<<ret;

    return 0;
}