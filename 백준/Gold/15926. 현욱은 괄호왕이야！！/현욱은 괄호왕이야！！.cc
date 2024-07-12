#include <iostream>
#include <stack>
using namespace std;

int n;
int ret;
int main(){

    cin>>n;
    stack<int> stk;
    stk.push(-1);
    for(int i=0;i<n;i++){
        char tmp;
        cin>>tmp;
        if(tmp=='('){
            stk.push(i);
        }
        if(tmp==')'){
            stk.pop();
            if(!stk.empty()){
                ret=max(ret,i-stk.top());
            }else{
                stk.push(i);  // If there's no '(' before ')', push current index to stack.
            }
        }
    }
    cout<<ret<<endl;
    return 0;
}