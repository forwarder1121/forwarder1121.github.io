#include <iostream>
#include <algorithm>

using namespace std;
int N,l,r,ret;
pair<int,int> cordinates[1000001];

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);




    //initialize
    cin>>N;
    for(int i=0;i<N;i++){
        cin>>cordinates[i].first>>cordinates[i].second;
    }
    //sort the coordinates in ascending order
    sort(cordinates,cordinates+N);

    l=cordinates[0].first;
    r=cordinates[0].second;

    
    for(int i=1;i<N;i++){
        if(cordinates[i].first<=r) r=max(cordinates[i].second,r);
        else{
            ret+=r-l;
            l=cordinates[i].first;
            r=cordinates[i].second;
        }
    }
    ret+=r-l;

    cout<<ret<<endl;

    return 0;
}