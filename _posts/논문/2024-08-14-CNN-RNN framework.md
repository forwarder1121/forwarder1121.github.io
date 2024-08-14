---
title: "[논문 리뷰] CNN-RNN: A Unified Framework for Multi-label Image Classification"
Learning by Masked Prediction of Hidden Units"
excerpt: "HuBERT"
categories:
    - Paper

---

논문의 전문은 [여기](https://arxiv.org/pdf/1604.04573)에서 확인할 수 있다.



참고로 이 논문은 2016년에 발표되어 다소 옛날 기술을 많이 소개하긴 한다.



---



# Abstract

CNN은 single-label image classification에서 성공적으로 이용됨

(single/muliple-label image classification : 이미지에서 라벨링을 하나/여러개로 수행)

여기서 더 나아가 이 저자들은 multiple-label image classification에서 중요한 특징인 "label끼리의 상관성을 이용" 하기 위하여 RNN을 섞은 CNN-RNN framework를 소개함



> **label끼리의 상관성이란?**
>
> 하늘을 찍은 사진을 예로 들면, "Sky"라는 라벨과 "Blue"라는 라벨은 같이 나올 확률이 높음. 하지만 "Snake"은 땅에 있는 오브젝트이니 이런 라벨과 같이 등장하지 않을 것.



---



# 1. Introduction



현실 이미지 task는 단 하나의 라벨을 지니지 않고, 여러개의 라벨을 지니는 multi-label classification임.

기존 연구는 그냥 single-label을 여러번 돌려서 레이블 여러개를 뽑아내었는데, 이는

**라벨끼리의 상관성을 고려하지 않는다** 



![image](https://github.com/user-attachments/assets/ed8ff118-bd90-487d-89a7-be06008521e3) 



생각해보면 Airplane과 Sky는 같이 많이 나올것이다.

그러나 water와 car는 같이 나오지 않을 것.



이러한 라벨끼리의 의존성을 이 논문에서는 **label dependency**라 함



기존 연구들은 이 특성을 반영하기 위해 엄청난 computation cost를 필요로 해서, 이 저자들은 CNN-RNN framework를 만듦



![image](https://github.com/user-attachments/assets/cfe5a866-5122-462d-91c8-0358a7bc95f6)



CNN-RNN framework는 이미지와 라벨 embedding을 동일 저차원 공간에 사상시킴

여기서 이미지 embedding은 그냥 VGG NET 사용했음(훈련 X), 그리고 RNN 사용하여서 라벨 embedding을 뽑음으로써 **label dependency**를 반영할 수 있도록 함



결론적으로 이 CNN-RNN framework는 여러 mulit-label dataset에서 SOTA 달성했는데, 저자들은 아래와 같이 그 이유를 서술함

1. 라벨들끼리의 상관성을 RNN으로 고려 가능하게함
2. RNN이 작은 object 탐지에 필요한 attention mechanism을 제공함



---



# 2. Related Work



Multi-label classification에 수행되었던 관련 연구들...

1. 그냥 CNN 돌려서 top-k 추출 -> label dependency 무시됨
2. image/label embedding을 동일 공간에 사상 -> 라벨 의미 중복성 반영되나, 라벨끼리의 상관성은 반영 불가
3. label classifiers를 stacking -> 라벨 상관성 고려가능하나, 연산량이 너무큼



CNN-RNN framework는 이러한 걸 해결함



---



# 3. Method