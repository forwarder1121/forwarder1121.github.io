---
published: true
layout: post
excerpt: 재귀적 이분탐색
tags:
  - 자료구조
categories:
  - dataStructure
---

# 재귀적 BinarySearch

이진탐색의 알고리즘은 그대로 가져오되, 구현방식을 기존의 반복문에서 재귀로 바꿔보자.  

참고) [반복 BinarySearch](https://forwarder1121.github.io/2023/06/21/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-BinarySearch.html)

나는 재귀로 구현할때가 좀더 생각하기 편했는데, 이유는 간단하다.  

> 수학적 귀납법과 같이, Basis(n=초항)만 지정해주고 n=k일떄 맞게 동작하겠지... 라고 **받아드린후** n=k+1일때만 생각해서 구현하면 되기 때문.

수학적귀납법의 구조를 재귀 알고리즘에 그대로 가져오게 되면  

여기서 Basis는 종료조건,  
**n=k는 그냥 믿어라** <- 이 자세가 중요하다. 굳이 단계 하나하나 증명할 필요가 없다!!  
그리고 n=k+1를 맞게 작성해라.  

다시 한번 말하지만, 재귀함수를 굳이 하나하나 들어가서 살펴보고, 생각할 필요가 없고,  
(이 경우에는 n=8일때는 어떻게 되지? n=4는? 2는? 1은? 이런걸 생각하지 않아도 된다)  
이미 재귀에 의해 이전 단계(n=k)는 정상적으로 작동할 것이라 **믿고** 그 바로 다음 단계(n=k+1)만 생각하자.

# Code
```
int binarySearch_recursive(int* array, const int x, int left, int right) {
	// Basis1:x가 array에 존재하지 않을경우
	if (left >= right) return -1;

	// 정렬된 array[left...right]에서 x를 탐색
	int mid = (left + right) / 2;
	// array[mid]와 x를 비교 후 적절히 재귀
	if (array[mid] > x) binarySearch_recursive(array, x, left, mid - 1);
	else if (array[mid] < x) binarySearch_recursive(array, x, mid + 1, right);
	// Basis2:x가 array에 존재하고 array[mid]==x인 경우
	else return mid;
}
```
코드를 보면 Basis(n=초항)인 종료조건이 기술되어 있고, **n=k는 믿음으로 구성** 그리고 n=k+1가 기술되어 있는것을 볼 수 있다.  

실행결과는 이전의 반복이진탐색과 같으므로 생략한다.  

이것의 증명은 다음글에 이어하겠다.
