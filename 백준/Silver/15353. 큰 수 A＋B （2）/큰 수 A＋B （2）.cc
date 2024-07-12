#include <iostream>
#include <stack>
using namespace std;

int n;
int ret;
int main(){

    cin>>n;
    stack<int> stk;
    for(int i=0;i<n;i++){
        char tmp;
        cin>>tmp;
        if(tmp=='('){
            stk.push(i);
        }
        else{
            int front=stk.top();
            stk.pop();
            if(stk.empty()){
                ret=max(ret,i-front+1);
                stk.push(front);
            }
        }
    }
    cout<<ret<<endl;
    return 0;
}