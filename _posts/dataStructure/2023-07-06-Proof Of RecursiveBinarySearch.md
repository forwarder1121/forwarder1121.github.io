---
published: true
layout: post
excerpt: 재귀적 이분탐색의 증명
tags:
  - 자료구조
categories:
  - dataStructure
---
# 재귀적 BInarySearch의 증명

개발자라면 알고리즘의 정확성을 때론 직접 증명할 수 있어야한다.  
그럼으로써 알고리즘의 응용단계에서 왜 그런 알고리즘이 정확히 동작하는지를 판단할 수 있게 된다.

# Code
```
int binarySearch_recursive(int* array, const int x, int left, int right) {
	//Basis1:x가 array에 존재하지 않을경우
	if (left >= right) return -1;

	//정렬된 array[left...right]에서 x를 탐색
	int mid = (left + right) / 2;
	//array[mid]와 x를 비교 후 적절히 재귀
	if (array[mid] > x) binarySearch_recursive(array, x, left, mid - 1);
	else if (array[mid] < x) binarySearch_recursive(array, x, mid + 1, right);
	//Basis2:x가 array에 존재하고 array[mid]==x인 경우
	else return mid;
}
```

# Proof

> BinarySearch_recursive()는 x가 array안에 있을 경우 그 index값을 성공적으로 반환한다.

Invariant : array[i]<array[j]이면 i<j이다.(array는 정렬돼있다)  
			array[k]==x이면 left<=k<=right이다.

수학적 귀납법을 통해 증명하자.  
> 배열의 크기를 n이라 하자.  
Base) n=1일 경우, 위 코드에 의해 함수는 성공한다.  
Step) n=k일 경우 BinarySearch_recursive()가 성공한다고 가정하자.  
Induction) n=k+1일 경우를 생각하자.  
			i) array[mid]>x 인 경우  
            	x는 array[left,,,(mid-1)]에 존재한다.(invariant에 의해) 이때 코드는 binarySearch_recursive(array, x, left, mid - 1)를 재귀로 호출, 이는 Step에 의해 array[left...(mid-1)]를 성공적으로 탐색하므로 성공.  
            ii) array[mid]<x인 경우
            	x는 array[(mid+1)...right]에 존재한다. 이때도 마찬가지로 Step의 가정에 의해 성공하므로 성공.  
            iii) array[mid]==x인 경우
            	위 코드는 mid를 반환한다.
               
# Time Complexity

BinarySearch는 각 단계마다 탐색범위를 2등분하므로, 최악의 경우에 T(N)=logN인 시간복잡도를 가진다.
