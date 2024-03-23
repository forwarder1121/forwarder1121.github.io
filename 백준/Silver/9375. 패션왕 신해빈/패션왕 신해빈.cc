#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <map>
#include <string>
using namespace std;
int numOfTestCases,n;
string cloth,type;

int main(){
    cin>>numOfTestCases;
    for(int k = 0; k < numOfTestCases;k++){
        map<string,int> clothes;
        int numOfCombinations=1;
        cin>>n;
        for(int i = 0; i < n;i++){
            cin>>cloth>>type;
            clothes[type]++;
        }
       
        //calculate
        for(auto it=clothes.begin();it!=clothes.end();it++){
            numOfCombinations*=(it->second+1);
        }
        numOfCombinations-=1;

        cout<<numOfCombinations<<endl;
    }

}