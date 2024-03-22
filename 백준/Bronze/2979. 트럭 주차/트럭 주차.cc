#include <stdio.h>
#include <string.h>
#include <iostream>
#include <vector>
using namespace std;
string str;

int main(){
    //input
    int taxes[3];
    int total = 0;
    for(int i=0; i<3; i++) cin>>taxes[i];
    int arriveTimes[3];
    int departureTimes[3];
    for(int i=0;i<3;i++) {
        cin>>arriveTimes[i];
        cin>>departureTimes[i];
    }
    
    //get min,max time
    int minTime=arriveTimes[0],maxTime=departureTimes[0];
    for(int i=1; i<3; i++){
        if(minTime>arriveTimes[i]) minTime=arriveTimes[i];
        if(maxTime<departureTimes[i]) maxTime=departureTimes[i]; 
    }

    //check time i 
    for(int i=minTime;i<=maxTime;i++){
        int numOfCars=0;
        for(int car=0;car<3;car++) {
            if(i>=arriveTimes[car]&&i<departureTimes[car]){
                numOfCars++;
            }
        }
        total+=taxes[numOfCars-1]*numOfCars;
    }
    cout<<total;
}