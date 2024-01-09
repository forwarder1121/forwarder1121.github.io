---
layout: post
excerpt: 정렬 알고리즘의 일부인 선택정렬
tags:
  - 자료구조
date: 2023-06-21T14:53:00.000Z
published: true
categories:
  - dataStructure
---




# Selection Sort

입력 : N>=1개의 서로 다른 정수의 배열 a
출력 : 오름차순으로 구성된 배열

## 전략
각 i단계마다, 
a[i]부터 a[n-1]까지 탐색을 한 뒤, 가장 작은 수를 a[j]와 바꾼다.

### 스토리
반의 모든 아이들을 임의대로 한줄로 서게 한 뒤,
1회차에 1번째~끝 아이를 보고 1번째로 작은 키의 아이를 1번째 아이와 바꾸고,
2회차에 2번째~끝 아이를 보고 2번째로 작은 키의 아이를 2번째 아이와 바꾸고,
3번째에 3번쨰~끝 아이를 보고 3번째로 작은 키의 아이를 3번째 아이와 바꾸고,
...

**i번째에 i번째~끝아이를 보고 i번째로 작은 키의 아이를 i번쨰 아이와 바꾸
고**,

..
이 작업을 마지막 반 아이들의 수만큼 해주면 키의 오름차순으로 반아이들이 정렬된다는 논리이다.

### 슈도코드

```
for(int i=0; i<n; i++){
	a[i]부터 a[n-1]까지 중 가장 작은 수를 a[minIndex];
	a[i]와 a[minIndex]를 교환;
}
```

### 발전된 슈도코드

```
for(int i=0; i<n; i++){
	//a[i]부터 a[n-1]까지 중 가장 작은 수를 a[minIndex];
	minIndex=i;
	for(int j=i; j<n; j++){
		만일 a[minIndex]>a[j]라면 minIndex=j;
	}
	//a[i]와 a[minIndex]를 교환;
	swap(a[i],a[minIndex]);
}
```

### 실제 코드
```
void selectionSort(int n, int* array) {
	for (int i = 0; i < n; i++) {
		int minIndex=i;
		for (int j = i; j < n; j++) {
			if (array[j] < array[minIndex])
				minIndex = j;
		}
		swap(array[i], array[minIndex]);
	}
}
```


### 실제 테스트코드
```
#include <iostream>
#include <typeinfo>
using namespace std;
void selectionSort(int n, int* array);

int main() {
	int size;
	cout << "입력할 배열의 총 크기를 입력하세요 : ";
	cin >> size;
	
	int* array = new int[size];
	for (int i = 0; i < size; i++) {
		cout << "array[" << i << "] = ";
		cin >> array[i];
	}

	cout << "입력된 배열은 다음과 같습니다." << endl;
	for (int i = 0;  i < size; i++) {
		cout << "array[" << i << "] = " << array[i] << endl;
	}

	selectionSort(size, array);

	cout << "정렬된 배열은 다음과 같습니다." << endl;
	for (int i = 0; i < size; i++) {
		cout << "array[" << i << "] = " << array[i] << endl;
	}
	
	delete[] array;
	
	return 0;
}

void selectionSort(int n, int* array) {
	for (int i = 0; i < n; i++) {
		int minIndex=i;
		for (int j = i; j < n; j++) {
			if (array[j] < array[minIndex])
				minIndex = j;
		}
		swap(array[i], array[minIndex]);
	}
}
```

### 실행 결과
![202306201](https://github.com/forwarder1121/forwarder1121.github.io/assets/66872094/a18cd573-8bb6-46cf-973c-a06aa2f29950)

### 정확성 증명
seletionSort내부의 i번쨰 for문에서 
array[0]~array[i-1]는 오름차순으로 정렬되어 있다.
이는 i가 증가하여 n-1가 될 떄까지 불변하므로 정확한 알고리즘이다.

### 참고 문헌
[선택 정렬(위키)](https://ko.wikipedia.org/wiki/%EC%84%A0%ED%83%9D_%EC%A0%95%EB%A0%AC)

[선택 정렬 예제(백준)](https://www.acmicpc.net/problem/23882)
