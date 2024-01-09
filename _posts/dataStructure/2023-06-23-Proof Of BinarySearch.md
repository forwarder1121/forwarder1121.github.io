---
published: true
layout: post
excerpt: 이진탐색의 정확성 증명
tags:
  - 자료구조
date: 2023-06-23T00:00:00.000Z
categories:
  - dataStructure
---
# BinarySeach의 증명

어떤 문제를 해결하기 위해 알고리즘을 구성하는 것은 중요하다.   
그러나 그에 못지 않게 알고리즘이 과연 정확하게 동작하는지 정확성에 대한 문제 또한 중요하다.   
특히 컴퓨터를 전공하는 학생이라면 알고리즘의 타당성, 정확성에 항상 의문을 가지며 접근해야 할 것이다.

## 코드
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

## 증명

Invarient : array[i]=x 라면 left<=i<=right 이다.  

증명하고자 하는 명제  

P(n) = array[i]=x 라면 i를 return 한다. (크기가 n인 배열에 대하여)

base) P(1) => array[0]=x라면 mid=0이므로 0을 return 한다. 다시말해 P(1)은 참

Step) P(n)이 성립한다고 가정하자.
	  P(n+1)에 대해 생각하자.

	i) array[mid]==x 이면 mid를 return한다. 즉 P(n+1)도 참.  
    ii) array[mid]<x  이면 구간을 왼쪽 절반에 대해 다시 탐색한다.
   					 array[mid+1, mid+2, ... n-1] 에 x가 존재할 것이다.
       				 이때 P(n)이 참이라 하였으므로 반드시 성공할 것이다. 즉 P(n+1)도 참
    iii) array[mid]>x  이면 구간을 오른쪽 절반에 대해 다시 탐색. ii)의 경우와 마찬가지로 P(n+1)도 참
   곧, P(n)이 성립하면 P(n+1)도 성립하므로 P(n)은 모든 자연수 n에 대하여 성립   
  
  
## 시간 복잡도
  
  입력 N에 대해 1회 반복을 할때마다 2분할로 나누며 탐색한다.   
  이는 최악의 경우 N이 1이 될때까지(logN번) 반복할 것이다.  
  따라서 BinarySearch의 시간복잡도는 O(logN)이다.  
  
  CS에서의 log는 보통 밑이 2인 로그를 나타냄을 참고하자.
  