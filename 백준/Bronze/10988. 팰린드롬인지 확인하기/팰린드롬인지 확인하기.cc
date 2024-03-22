#include <stdio.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
string str1, str2;

int main(){

    cin>>str1;
    str2=str1;
    reverse(str1.begin(), str1.end());
    
    cout<<(str1==str2)<<endl;
    return 0;
}
