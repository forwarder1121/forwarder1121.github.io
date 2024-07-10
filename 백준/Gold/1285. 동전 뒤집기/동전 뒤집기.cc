#include <string>
#include <vector>
#include <iostream>
using namespace std;

int ret;
int N;



int countTails(const vector<int> &array){
    int sum=0;
    for(int j=0;j<N;j++){
        int n=0;
        for(int i=0;i<N;i++){
            if(array[i]&(1<<j)) n++;
        }
        sum+=min(n,N-n);
    }
    return sum;
}


void flipArray(vector<int> array,int targetRowIdx){
    
    // base case
    if(targetRowIdx==N) {
        ret=min(ret,countTails(array));
        return;
    }
  
    flipArray(array,targetRowIdx+1);
    // array[targetRowIdx]의 0~(N-1) 비트를 반전
    array[targetRowIdx]^=(1<<N)-1;
    flipArray(array,targetRowIdx+1);
    
}




int main() {

    cin>>N;
    ret=N*N;
    vector<int> array(N,0);
    
    // 초기화
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            char tmp;
            cin>>tmp;
            //tmp가 T면 array[i]의 j번째 비트를 1로 설정
            if(tmp=='T') {
                array[i]|=(1<<j);
            }
        }
    }
    //DFS
    flipArray(array,0);
    cout<<ret;
    return 0;
}

