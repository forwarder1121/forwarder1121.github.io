#include <iostream>
#include <string>
#include <algorithm>
using namespace std;


int main(){

    string A,B,ret;
    cin>>A>>B;
    int sum=0;
    while(A.size()||B.size()||sum){
        if(A.size()){
            sum+=A.back()-'0';
            A.pop_back();
        }
        if(B.size()){
            sum+=B.back()-'0';
            B.pop_back();
        }
        ret+=sum%10+'0';
        sum/=10;
    }

    reverse(ret.begin(),ret.end());
    cout<<ret<<endl;
    return 0;
}