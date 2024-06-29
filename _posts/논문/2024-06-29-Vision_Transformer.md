---
categories:
    - Paper
---

# [ 논문 리뷰 ] AN IMAGE IS WORTH 16X16 WORDS: TRANSFORMERS FOR IMAGE RECOGNITION AT SCALE

---

## Abstract

NLP에서 Transformer 아키텍쳐는 표준이 되었지만, CV에서는 그 사용이 제한되어 왔다.

다시 말해 CV에서는 CNN을 기반으로 사용하며 제한적으로 Transformer를 사용해왔다.

이 논문에서는 CNN 의존적인 기존의 방식에서 탈피하여 Transformer를 직접 CV에 사용하는 방식을 선보인다. 그리고 대규모의 데이터로 pre-trained 한 뒤 이를 전이 학습시킬 경우 CNN보다 training cost가 적을 뿐 아니라 압도적인 정확도를 보인다.

> NLP에서 큰 효과를 거둔 Transformer architecture를 CV에도 적용함으로써 압도적인 성능을 거둘 수 있었다.

---

## Introduction

![transformer ANN ...](https://i.namu.wiki/i/tKMUf8ewTCZJETaAQWZplCPznZKid0xQvj8kjvOGDNyXgZ3o0aZigo8-enWBDmi_QJDDys3bTaBTecixDaPHA9zvJ5yJo7HqAFhOoijoiz0q0cHzhrNRXjoUUFFPWC_hUpw8gnaNA7VaRgo3Ld7gPURmcC0_WPwei-a2yyiWppQ.webp)

Self-Attention을 기반으로 하는 Transformer는 NLP에서 가장 standard한 모델이 되었다. 이는 많은 말 뭉치로 pre-train 한 뒤, 전이학습하는 방식이다. Transformer의 계산 효율성과 확장가능성으로 인해 100B이 넘는 paramter를 가지는 모델까지 훈련시킬 수 있었다. 따라서 자연히 이러한 Transformer를 CV에 도입하려는 시도들이 있어 왔지만, 이론적으로는 완벽하였지만 specialized attention pattern 때문에 ResNet 아키텍쳐 모델을 뛰어 넘을 수 없었다.

구글팀은 이미지를 거의 수정하지 않고 Transformer에 집어 넣기 위해 이미지를 patch로 나누고, 이에 선형 임베딩을 가한뒤에 Transformer에 넣는 방식을 채택하였다. 이러한 patch는 NLP에서의 토큰과 같은 방식으로 처리된다.

여기서 다시 이 논문의 제목을 보자

> AN IMAGE IS WORTH 16X16 WORDS // 이미지 == 자연어, 다시 말해 이미지를 자연어와 동일하게 다룬다는 이야기

구글팀은 ResNet 데이터셋을 가지고 학습을 진행시켰고, 이는 ResNet보다 약간 낮은 정확도를 보였다. 이는 Transformer가 CNN에만 있는 inductive biases가 부족하기 때문이다. 따라서 충분하지 않은 데이터 셋을 가지고 학습을 진행할 경우 일반화가 되지 않는 문제점을 보인다. 그러나 충분한 양의 데이터셋을 이용하여 학습을 진행할 경우 inductive biases를 뛰어 넘는 성능을 얻을 수 있다. 실제로 구글팀이 상당히 큰 크기인 ImageNet-21K, JFT-300M 데이터셋으로 pre-traine 한 Transformer 모델이 SOTA(state of the art)의 성능을 거두었다.

---

## Related Work

기계 번역을 수행하기 위해 개발된 Transformer는 NLP에서 SORA의 성능을 거두었다. 이는 대규모 말뭉치를 학습하여 finetunning하는 방식으로 이루어지는데, BERT와 GPT가 그 대표적인 예이다.

이 Transformer의 self-attention을 이미지에 적용하기 위해서 가장 쉬운 방법은 각 픽셀마다 self-attention을 나머지 모든 픽셀에 적용하는 것인데, 이는 O(n^2)이므로 현실적이지 않다. 따라서 self-attetention을 인접 픽셀들에만 적용, 근사 사용, 가변 block으로 나눠어 적용, 개별 축에 대해 적용하는 방식들이 연구되어 왔지만 이들을 실제 HW 구현하기에는 많은 엔지니어링이 필요하다는 단점이 존재한다.

이 논문에서 다루는 모델을 ViT(Vision Transformer)라 하는데, 이 ViT와 가장 유사한 모델은 이미지를 2x2 패치로 나눈 후에 self-attention을 적용한다. ViT는 이와 유사하지만 SOTA CNN 모델을 뛰어넘는 성능을 가질뿐 아니라, 더 높은 해상도를 처리할 수 있는 모델이다.

그 외에도 CNN과 self-attention을 같이 쓰기 위한 노력들이 있었다.

ViT는 대규모 데이터셋을 사용함으로써 SOTA의 성능을 거두었다.

---

## Method

![image-20240629220626901](/Users/forwarder1121/Library/Application Support/typora-user-images/image-20240629220626901.png)

ViT는 확장가능한 NLP transformer의 아키텍쳐와 그 효율적인 구현을 위해 기존 Transformer의 구조를 최대한 그대로 사용하였다. 위 사진을 보면 Transformer의 Encoder 부분을 그대로 가져온 것을 볼 수 있다. 이는 Transformer의 Encoder를 사용하는 LLM인 BERT와 유사하다.

![img](https://miro.medium.com/v2/resize:fit:700/1*Qww2aaIdqrWVeNmo3AS0ZQ.png)
