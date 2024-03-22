#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
string str;
int main(){
    

    getline(cin,str);
    for(int i=0;i<str.length();i++){
        int tmp;
        //small letter
        if(str[i]>='a' && str[i]<='z'){
            tmp=str[i]+13;
            if(tmp>'z') tmp-=26;
            str[i]=tmp;
        }
        //big letter
        else if(str[i]>='A' && str[i]<='Z'){
            tmp=str[i]+13;
            if(tmp>'Z') tmp-=26;
            str[i]=tmp;
        }
    }
    cout<<str<<endl;
    return 0;
}
