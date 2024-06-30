---
categories:
    - Paper
---

# [ 논문 리뷰 ] AN IMAGE IS WORTH 16X16 WORDS: TRANSFORMERS FOR IMAGE RECOGNITION AT SCALE

---

# 0. Abstract

NLP에서 Transformer 아키텍쳐는 표준이 되었지만, CV에서는 그 사용이 제한되어 왔다.

다시 말해 CV에서는 CNN을 기반으로 사용하며 제한적으로 Transformer를 사용해왔다.

이 논문에서는 CNN 의존적인 기존의 방식에서 탈피하여 Transformer를 직접 CV에 사용하는 방식을 선보인다. 그리고 대규모의 데이터로 pre-trained 한 뒤 이를 전이 학습시킬 경우 CNN보다 training cost가 적을 뿐 아니라 압도적인 정확도를 보인다.

> NLP에서 큰 효과를 거둔 Transformer architecture를 CV에도 적용함으로써 압도적인 성능을 거둘 수 있었다.

---

# 1. Introduction

![transformer ANN ...](https://i.namu.wiki/i/tKMUf8ewTCZJETaAQWZplCPznZKid0xQvj8kjvOGDNyXgZ3o0aZigo8-enWBDmi_QJDDys3bTaBTecixDaPHA9zvJ5yJo7HqAFhOoijoiz0q0cHzhrNRXjoUUFFPWC_hUpw8gnaNA7VaRgo3Ld7gPURmcC0_WPwei-a2yyiWppQ.webp)

Self-Attention을 기반으로 하는 Transformer는 NLP에서 가장 standard한 모델이 되었다. 이는 많은 말 뭉치로 pre-train 한 뒤, 전이학습하는 방식이다. Transformer의 계산 효율성과 확장가능성으로 인해 100B이 넘는 paramter를 가지는 모델까지 훈련시킬 수 있었다. 따라서 자연히 이러한 Transformer를 CV에 도입하려는 시도들이 있어 왔지만, 이론적으로는 완벽하였지만 specialized attention pattern 때문에 ResNet 아키텍쳐 모델을 뛰어 넘을 수 없었다.

구글팀은 이미지를 거의 수정하지 않고 Transformer에 집어 넣기 위해 이미지를 patch로 나누고, 이에 선형 임베딩을 가한뒤에 Transformer에 넣는 방식을 채택하였다. 이러한 patch는 NLP에서의 토큰과 같은 방식으로 처리된다.

여기서 다시 이 논문의 제목을 보자

> AN IMAGE IS WORTH 16X16 WORDS // 이미지 == 자연어, 다시 말해 이미지를 자연어와 동일하게 다룬다는 이야기

구글팀은 ResNet 데이터셋을 가지고 학습을 진행시켰고, 이는 ResNet보다 약간 낮은 정확도를 보였다. 이는 Transformer가 CNN에만 있는 inductive biases가 부족하기 때문이다. 따라서 충분하지 않은 데이터 셋을 가지고 학습을 진행할 경우 일반화가 되지 않는 문제점을 보인다. 그러나 충분한 양의 데이터셋을 이용하여 학습을 진행할 경우 inductive biases를 뛰어 넘는 성능을 얻을 수 있다. 실제로 구글팀이 상당히 큰 크기인 ImageNet-21K, JFT-300M 데이터셋으로 pre-traine 한 Transformer 모델이 SOTA(state of the art)의 성능을 거두었다.

---

# 2. Related Work

기계 번역을 수행하기 위해 개발된 Transformer는 NLP에서 SORA의 성능을 거두었다. 이는 대규모 말뭉치를 학습하여 finetunning하는 방식으로 이루어지는데, BERT와 GPT가 그 대표적인 예이다.

이 Transformer의 self-attention을 이미지에 적용하기 위해서 가장 쉬운 방법은 각 픽셀마다 self-attention을 나머지 모든 픽셀에 적용하는 것인데, 이는 O(n^2)이므로 현실적이지 않다. 따라서 self-attetention을 인접 픽셀들에만 적용, 근사 사용, 가변 block으로 나눠어 적용, 개별 축에 대해 적용하는 방식들이 연구되어 왔지만 이들을 실제 HW 구현하기에는 많은 엔지니어링이 필요하다는 단점이 존재한다.

이 논문에서 다루는 모델을 ViT(Vision Transformer)라 하는데, 이 ViT와 가장 유사한 모델은 이미지를 2x2 패치로 나눈 후에 self-attention을 적용한다. ViT는 이와 유사하지만 SOTA CNN 모델을 뛰어넘는 성능을 가질뿐 아니라, 더 높은 해상도를 처리할 수 있는 모델이다.

그 외에도 CNN과 self-attention을 같이 쓰기 위한 노력들이 있었다.

ViT는 대규모 데이터셋을 사용함으로써 SOTA의 성능을 거두었다.

---

# 3. Method

![drawing](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/vit_architecture.jpg)

ViT는 확장가능한 NLP transformer의 아키텍쳐와 그 효율적인 구현을 위해 기존 Transformer의 구조를 최대한 그대로 사용하였다. 위 사진을 보면 Transformer의 Encoder 부분을 그대로 가져온 것을 볼 수 있다. 이는 Transformer의 Encoder를 사용하는 LLM인 BERT와 유사하다. 아래와 사진과 비교해보도록 하자.

![img](https://miro.medium.com/v2/resize:fit:700/1*Qww2aaIdqrWVeNmo3AS0ZQ.png)



## 3.1 Vision Transformer(ViT)



Transformer는 1차원 sequence를 입력으로 받기 때문에, 2차원인 이미지를 다루기 위해서 이미지를 1차원으로 변환시켜야 한다.

x를 x_p로 재구성하는 수식은 아래에 나타나있다.



$$
x \in \mathbb{R}^{H \times W \times C}
$$

$$
x_p \in \mathbb{R}^{N \times (P^2 \cdot C)}
$$

- H, W : 원본 이미지의 해상도
- C : 채널 수
- P, P : 각 이미지 패치의 해상도
-  N : 생성된 패치의 수, Transformer 의 입력 시퀀스 길이









$$
z_0 = [x_{\text{class}}; x_1^p E; x_2^p E; \cdots; x_N^p E] + E_{\text{pos}}
$$





Transformer는 모든 레이어에서의 입력이 D차원 벡터로 통일함으로 이를 위해 위에서 변환한 x_p 행렬을 다시 Embedding 행렬인 E와 행렬곱하여 D차원 sequence로 만든다.

그리고 BERT에서의 분류를 위한 [class] 토큰과 유사하게 ViT도 학습 가능한 임베딩을 sequence 앞에 추가한다. 이 토큰의 은닉 상태는 이미지 표현으로 사용되며 MLP 분류 헤드가 이를 이용하여 이미지 분류에 사용한다. 그리고 Positional Embedding인 E_pos 행렬을 더한다.



그리고 이렇게 구성된 Embedding vecter의 sequence인 ViT의 입력으로 사용되며 Multiheaded Self-Attention(MSA) layer와 Multi-Layer Perceptron(MLP) layer를 번걸아가며 적용되며 중간에 계속 Layer Normalization(LN)과 residual connection이 이루어진다.

최종 출력결과인 [class] 토큰의 은닉상태를 비선형 활성화 함수를 사용하는 MLP layer가 처리한다.



아래 수식을 ViT의 아키텍쳐 그림과 비교하며 따라가보면 이해가 된다.

![img](https://velog.velcdn.com/images/kbm970709/post/5ea4ad10-f67b-465a-a562-09d81361e1b8/image.png)

![image](https://github.com/forwarder1121/forwarder1121.github.io/assets/66872094/53372a35-c8b1-4287-a219-2f84ae22d9bc)





**Inductive bias & Hybrid Architecture**

CNN의 locality, two-dimensional neighborhood structure, translation equivariance 특성은 self-attention을 주된 매커니즘으로 사용하는 Transformer에는 제한적으로 나타난다. 따라서 ViT에 CNN의 inductive bias를 주입하기 위하여 CNN의 feature map을 식(3)의 x_p로 사용하는 hybrid 아키텍쳐가 소개된다.



## 3.2 Fine-Tuning and Higher Resolution

ViT는 NLP의 Transformer와 동일하게 대규모 데이터셋에 대해 pre-train을 수행하고 downstream task에 fine-tuning을 진행한다. fine-tuning 시에는 pre-training 때의 prediction head(MLP)를 제거하고 D x K feedforward layer를 연결한다. 여기서 D는 위와 마찬가지로 Transformer내의 입출력 벡터의 차원, K는 downstream class 수이다.

pre-traning때보다 fine-tuning때 고해상도 이미지를 입력으로 주는게 도움이 되며, 이때 고해상도 이미지는 patch-size가 동일하기 때문에 더 긴 sequence를 가지게 될 것이다. ViT는 임의 길이의 sequence를 처리할 수 있기 때문에 HW가 허락한다면 얼마든지 처리할 수 있으며, position embedding을 보간법을 통해 크기를 적절히 설정하여 더함으로써 고해상도 이미지에서도 inductive bias를 잃지 않게 하면 된다.



---



# 4. Experiments



구글 팀은 ResNet, ViT, hybrid 모델을 비교하는 실험을 진행하였다. 다양한 크기의 데이터 셋에서 pre-training을 진행하고, 여러 벤치마크 task에 대해 그 성능을 비교하였다. 결과적으로 ViT가 적은 pre-training cost를 가지고 대부분의 task에서 SOTA의 성능을 거두었다. self-supervision 또한 가능한 ViT에 대해 소개하며 ViT의 미래지향성에 대해 논한다.



## 4.1 Setup



**Datasets**

ViT는 ImageNet-1k, ImageNet-21K, JFT와 같은 데이터셋으로 pre-training 된 후 다양한 downstream task(ReaL labels, CIFAR-10/100, Oxford-IIIT Pets, Oxford Flowers-102, VTAB)에 fine-tuning 되었다.



**Model Variants**

3개의 크기를 가진 ViT로 실험을 진행하였으며 BERT의 "Base","Large"를 그대로 가져온 뒤, "Huge"라는 것은 ViT에서 추가된 model size이다.

![img](https://velog.velcdn.com/images/kbm970709/post/08ba0eef-05af-4816-9c36-ea31673c1da7/image.png)



이러한 ViT와 대조군 2개를 설정하였는데,

CNN 기반의 ResNet(BiT)와 CNN의 feature map을 input으로 받는 hybrid model이 그 대조군들이다.



**Training & Fine-tuning**

모든 모델을 weigh decay 0.1로 둔 Adam을 사용하여 pre-training을 진행하였다. 그후 fine-tuning은 momentum 기반의 SGD를 사용하였다.



**Metrics**

downstream 데이터셋에서 few-shot, fine-tuning accuracy를 사용한다.

few-shot accuracy : Training dataset에 없는 클래스를 맞추는 정확도

fine-tuning accuracy : fine-tuning 이후의 정확도





## 4.2 Comparison to state of the art
