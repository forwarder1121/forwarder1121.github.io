---
title: "[논문 리뷰] Swin Transformer: Hierarchical Vision Transformer using Shifted Windows22"
excerpt: "Swin2"
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





아키텍쳐는 아래와 같다



![image](https://github.com/user-attachments/assets/feb04b5d-fe3c-4c15-bc72-d12682957e85)





크게 두 부분으로 이루어진 것을 확인할 수 있는데.



CNN은 Image의 feature를 추출하고, RNN은 image/label의 feature와 라벨의 dependency를 추출한다.

그리고 같은 공간에 사상되어서 내적 계산후에 최상위 라벨을 beam search로 찾는다.



## Model



라벨 k는 e_k로 원핫 인코딩 된다.

그리고 이걸 Ui 행렬로 임베딩 시킨다.

RNN은 이걸 받아서 라벨들의 dependency를 모델링한다.



그리고 이 RNN의 결과와 CNN의 결과를 동일 선형공간에 사상시킨다.

그리고 이걸 Ul행렬과 곱한뒤에 softmax를 이용하여 확률값으로 변환한다.



쉽게 설명해서 위 그림의 보라색 부분이 학습이 진행되는 부분이다.



## Inference

저자들은 label들의 sequence를 **prediction-path**로 명명하였다.

![image](https://github.com/user-attachments/assets/11f09b98-eee0-4b2c-b161-d019072a4d87)



여기서 lk를 찾는 방법은 greedy approximation과 beam search가 있다.

여기서 추론의 안정성을 위해 beam search를 사용한다.

(greedy는 무식하게 가장 높은 확률의 라벨을 채택하기 때문에 불안정)



## Training

CNN 파트는 훈련시키지 않고 나머지 layer를 훈련시킴

그리고 훈련 데이터의 라벨 순서는 빈도순으로 내림차순 정렬. 이 덕분에 감지하기 쉬운 object label을 찾고 이것이 다른 object 탐지에 도움을 줄 수 있음(label dependency)



----



# 4. Experiments

다양한 multi-label classification에서 SOTA 달성



---



# 5. Conclusion and Future Work



CNN-RNN은 multi-label image clasification을 위해 제안됨

image/label embedding을 동일 공간으로 사상, label 끼리의 상관성을 고려 가능하고, SOTA 달성



그러나 작은 object는 탐지 어렵다는 단점 존재 -> 추후 연구 필요



내 생각에 CNN을 ViT로 바꾸면 개선되지 않을까.. 생각

2016년 논문이라 이미 진행되었으려나



















































