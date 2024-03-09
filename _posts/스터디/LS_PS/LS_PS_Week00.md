---
title: "C++ 코딩테스트 Week 00"
excerpt: "재귀함수, 순열, 조합, split, Memory&pointer"
categories:
    - computerNetwork
---

# 재귀 함수(recursion)

재귀함수란 정의 단계에서 자신을 재참조하는 함수이다.

점화식을 바탕으로 Divde and Conquer 할때 사용한다.

재귀 함수는 반드시 기저사례(=종료조건)을 써야한다.

싸이클을 쓰면 안된다.(f(a)와 f(b)가 서로 호출)

그리고 함수 호출에 대한 오버헤드가 발생하므로 반복문으로 가능하면 반복문으로 구현하자.

depth에서 올라올 때, 원복하는 것을 주의하자.

---

# 경우의 수

## 순열(permutation)

### Libraray : next_permutation

C++의 std::next_permutation 함수가 이 기능을 지원해준다.

next_pemutataion은 오름차순 정렬된 배열을 기반으로 순열을 만든다.

따라서 **next_permutation을 하기전에 배열을 오름차순 정렬**을 해주어야 한다.

> https://en.cppreference.com/w/cpp/algorithm/next_permutation

```cpp
#include <iostream>

using namespace std;

int main(){
    int a[]={1,2,3};
    do{
        for(int i:a) cout<<i<<" ";
        cout<<"\n";
    }while(next_permutation(a,a+3));
    return 0;
}
```

단순 array는 begin, end가 지원되지 않음.

```cpp
#include <iostream>

using namespace std;

int main(){
    vector<int> a={2,1,3};
    sort(a.begin(), a.end());
    do{
        for(int i:a) cout<<i<<" ";
        cout<<"\n";
    }while(next_permutation(a.begin(),a.end()));
    return 0;
}
```

---

### DIY : makePermutation

개발자라면 이미 구현된 라이브러리를 알맞게 사용해야 할 뿐 아니라, 직접 그것을 만들 수 있어야한다. 이와 같은 맥락으로 위에서 본 순열을 직접 생성하는 함수를 만들어보자.

<img width="446" alt="image" src="https://github.com/forwarder1121/forwarder1121.github.io/assets/66872094/f69a6e6f-7756-4181-8bd0-0e12424221f9">

강의는 이렇게 재귀함수를 타고 내려가는 걸로 말하던데, **재귀함수는 그냥 재귀적으로 되겠지~ 생각하는게 더 좋다고 생각**한다.

> 일단 돌아가게 만든 코드.
>
> C++ 언어 다 까먹어서 C 언어 베이스로 만들었다.
>
> 변수 리펙토링하고, 코드 스타일도 C++로 바꿔보자.
>
> ```cpp
> #include <iostream>
>
> using namespace std;
> void printArray(int* arr,int size);
> void makePermutation(int* arr,int n,int r,int depth);
> int main(){
>     int array[5]={1,2,3};
>     makePermutation(array,3,3,0);
>     return 0;
> };
>
> void makePermutation(int* arr,int n,int r,int depth){
>     //base condition
>     if(depth==r){
>         printArray(arr,n);
>     }
>     //branch
>     for(int i=depth;i<n;i++){
>         swap(arr[i],arr[depth]);
>         makePermutation(arr,n,r,depth+1);
>         swap(arr[i],arr[depth]);
>     }
> }
>
> void printArray(int* arr,int size){
>     for(int i=0;i<size;i++) {
>         printf("%d",arr[i]);
>     }
>     printf("\n");
> }
> ```

> arr 전역변수화, nPr의 의미에 맞게 r까지만 출력하도록 수정
>
> ```js
> //arr 전역변수화
> //r까지만 출력하도록 수정
> #include <iostream>
>
> int arr[5]={1,2,3,4,5};
> using namespace std;
>
> void printArray(int r);
> void makePermutation(int n,int r,int depth);
>
> int main(){
>     makePermutation(5,3,0);
>     return 0;
> }
>
> //nPr
> //select arr[depth] element
> void makePermutation(int n,int r,int depth){
>     //base condition
>     if(depth==r){
>         printArray(r);
>     }
>     //branch
>     for(int i=depth;i<n;i++){
>         swap(arr[i],arr[depth]);
>         makePermutation(n,r,depth+1);
>         swap(arr[i],arr[depth]);
>     }
> }
>
> void printArray(int r){
>     for(int i=0;i<r;i++) {
>         printf("%d",arr[i]);
>     }
>     printf("\n");
> }
> ```

> **vector container** 이용
>
> 참고 : https://cplusplus.com/reference/vector/vector/
>
> ```js
> #include <iostream>
>
> int arr[5]={1,2,3,4,5};
> using namespace std;
> vector<int> v;
>
> void printV(vector<int> &v){
>     for(int i=0;i<v.size();i++){
>         cout<<v[i]<<" ";
>     }
>     cout<<"\n";
> }
>
> void makePermutation(int n,int r,int depth){
>     //base case
>     if(r==depth){
>         printV(v);
>         return;
>     }
>     for(int i=depth;i<n;i++){
>         swap(v[i],v[depth]);
>         makePermutation(n,r,depth+1);
>         swap(v[i],v[depth]);
>     }
>     return;
> }
>
> int main(){
>     for(int i=1;i<=3;i++) v.push_back(i);
>     makePermutation(3,3,0);
>     return 0;
> }
>
> ```

branch 이후 다시 올라갈 때 `복원`해주는 것을 잊지 말자.

![image](https://github.com/forwarder1121/forwarder1121.github.io/assets/66872094/ace4adc3-d1d8-4d70-ae71-bfd9276bb041)

---

## 조합(combination)

순서를 고려하지 않고 뽑는 경우를 말한다.

### 재귀함수

```js
#include <iostream>
using namespace std;

int n=5, r=3;
void printVector(vector<int> v){
   for(int i:v) cout<<i<<" ";
   cout<<"\n";
}

//nCr
void combination(int start,vector<int> b){
    if(b.size()==r){
        printVector(b);
        return;
    }
    for(int i=start+1;i<n;i++){
        b.push_back(i);
        combination(i,b);
        b.pop_back();
    }
}

int main(){
    vector<int> b;
    combination(-1,b);
    return 0;
}
```

### 중첩반복문

---

# Split

```cpp
#include <iostream>
using namespace std;
vector<string> split(string input,string delimiter){
    vector<string> ret;
    long long pos=0;
    string token="";
    while((pos=input.find(delimiter))!=string::npos){
        token=input.substr(0,pos);
        ret.push_back(token);
        input.erase(0,pos+delimiter.length());
    }
    ret.push_back(input);
    return ret;
}

int main(){
    string s="this is for test",d=" ";
    vector<string> result=split(s,d);
    for(string a:result) cout<<a<<"\n";

    return 0;
}
```

---

# Memory, Pointer

---

# Comment

순열, 조합 알고리즘의 코드는 암기할것

```cpp
#include <iostream>

int arr[5]={1,2,3,4,5};
using namespace std;
vector<int> v;

void printV(vector<int> &v){
    for(int i=0;i<v.size();i++){
        cout<<v[i]<<" ";
    }
    cout<<"\n";
}

void makePermutation(int n,int r,int depth){
    //base case
    if(r==depth){
        printV(v);
        return;
    }
    for(int i=depth;i<n;i++){
        swap(v[i],v[depth]);
        makePermutation(n,r,depth+1);
        swap(v[i],v[depth]);
    }
    return;
}

int main(){
    for(int i=1;i<=3;i++) v.push_back(i);
    makePermutation(3,3,0);
    return 0;
}

```

```cpp
#include <iostream>
using namespace std;

int n=5, r=3;
void printVector(vector<int> v){
   for(int i:v) cout<<i<<" ";
   cout<<"\n";
}

//nCr
void combination(int start,vector<int> b){
    if(b.size()==r){
        printVector(b);
        return;
    }
    for(int i=start+1;i<n;i++){
        b.push_back(i);
        combination(i,b);
        b.pop_back();
    }
}

int main(){
    vector<int> b;
    combination(-1,b);
    return 0;
}
```

```cpp
#include <iostream>
using namespace std;
vector<string> split(string input,string delimiter){
    vector<string> ret;
    long long pos=0;
    string token="";
    while((pos=input.find(delimiter))!=string::npos){
        token=input.substr(0,pos);
        ret.push_back(token);
        input.erase(0,pos+delimiter.length());
    }
    ret.push_back(input);
    return ret;
}

int main(){
    string s="this is for test",d=" ";
    vector<string> result=split(s,d);
    for(string a:result) cout<<a<<"\n";

    return 0;
}
```
