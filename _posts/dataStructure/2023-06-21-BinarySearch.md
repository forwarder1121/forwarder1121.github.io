---
published: true
layout: post
excerpt: 이분탐색
tags:
  - 자료구조
date: 2023-06-21 14:53:00 UTC
categories:
  - dataStructure
---
## BinarySearch 

정렬된 정수의 집합에서 특정 원소를 찾는 알고리즘이다.

## 스토리

우리가 업다운 게임을 한다고 생각하면 된다.  
1~100까지의 숫자를 내가 생각하고, 독자가 이를 맞추어야 하는 상황.  
이때 나는 Up,Down의 유무만 알려줄 것이다.  
당신은 어떻게 내가 생각한 숫자를 맞출 것인가?  
그렇다. 당신이 지금 떠올린 방법이 BinarySearch, 즉 이진탐색이다.  

## 의사 코드

```
void binarySearch(int* array, const int x, const int N) {
	//right, left, mid 초기화
	while (원소가 구간내에 있는한) {
		if(x==array[mid])   // mid를 반환
		else if (x > array[mid]) // 구간을 오른쪽으로 분할
		else //구간을 왼쪽으로 분할
	}
}
```

## 실제 코드

```
int binarySearch(int* array, const int x, const int N) {
	int left = 0;
	int right = N - 1;
	
	while (left<=right) {
		int mid = (left + right) / 2;
		if (x == array[mid])	return mid;
		else if (x > array[mid]) {
			left = mid + 1;
		}
		else {
			right = mid - 1;
		}
	}
	return -1;
}
```

## 실행 결과
!(https://github.com/forwarder1121/forwarder1121.github.io/assets/66872094/8b5d9803-8912-402d-9b97-ad47d2c352c3)
