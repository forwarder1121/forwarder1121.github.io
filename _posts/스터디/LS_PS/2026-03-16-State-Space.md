---
title: "State-Space Perspective on Algorithmic Problem Solving"
excerpt: "알고리즘 문제를 state space와 탐색 전략으로 통합적으로 이해하는 관점"
categories:
    - algorithm
tags:
    - state-space
    - algorithm-design
    - dfs
    - dp
    - greedy
    - problem-modeling
---

# State-Space Perspective on Algorithmic Problem Solving

많은 알고리즘 교재에서는 DFS, BFS, Dynamic Programming, Greedy 등을 서로 다른 알고리즘 패러다임으로 설명합니다.

하지만 실제 문제를 풀다 보면 이러한 기법들은 완전히 독립적인 방법이라기보다 **하나의 공통된 구조 위에서 선택되는 전략**처럼 느껴질 때가 많습니다.

저는 코딩 테스트를 준비하며 다양한 문제를 풀던 과정에서 다음과 같은 관점으로 알고리즘을 정리하게 되었습니다.

> **모든 알고리즘 문제는 state space와 transition으로 이루어진 탐색 문제로 표현할 수 있다.**

이 글에서는 이러한 관점을 기반으로 서로 다른 알고리즘 기법들을 **하나의 구조 안에서 통합적으로 이해하는 프레임워크**를 소개합니다.

---

# 1. Problem as a State Space

알고리즘 문제는 다음과 같은 구조로 모델링할 수 있습니다.

```

(S, A, T, C, G)

```

- **S** : 가능한 모든 상태 (State set)
- **A** : 가능한 선택 (Action set)
- **T** : 상태 전이 함수 (Transition)
- **C** : 비용 함수 (Cost)
- **G** : 목표 상태 (Goal condition)

즉 문제 해결은 다음과 같은 과정입니다.

```

initial_state → ... → goal_state

```

이 구조는 자연스럽게 **state space graph**를 형성합니다.

```

node = state
edge = transition

```

따라서 많은 알고리즘 문제는 본질적으로 **state graph 위에서의 탐색 문제**로 해석할 수 있습니다.

---

# 2. State as Minimal Information

State는 단순히 어떤 데이터를 저장하는 구조가 아니라

> **문제를 해결하기 위해 필요한 최소한의 정보 집합**

입니다.

예를 들어 N-Queens 문제를 생각해보면 상태를 다음과 같이 표현할 수 있습니다.

### 비효율적인 상태 표현

```

board 전체

```

### 효율적인 상태 표현

```

row
used_columns
used_diagonals

```

이처럼 상태를 어떻게 정의하느냐에 따라 **state space의 크기와 탐색 난이도**가 크게 달라집니다.

따라서 알고리즘 설계에서 가장 중요한 단계는

```

state modeling

```

즉 **문제를 해결하는 데 필요한 최소 정보 구조를 정의하는 것**입니다.

---

# 3. Transition and State Graph

상태는 선택(action)을 통해 다음 상태로 전이됩니다.

```

(state, action) → next_state

```

이 구조는 자연스럽게 그래프를 형성합니다.

```

nodes = states
edges = transitions

```

따라서 많은 알고리즘 문제는 다음과 같이 이해할 수 있습니다.

```

state graph 탐색 문제

```

---

# 4. Algorithms as Exploration Strategies

이 관점에서 알고리즘 기법들은 다음과 같이 해석할 수 있습니다.

| Algorithm    | Interpretation               |
| ------------ | ---------------------------- |
| DFS          | state graph depth-first 탐색 |
| BFS          | level-order 탐색             |
| Dijkstra     | cost 기반 탐색               |
| A\*          | heuristic 기반 탐색          |
| DP           | memoized DFS                 |
| Backtracking | constraint 기반 DFS          |

즉 알고리즘은 본질적으로

```

state space exploration strategy

```

라고 볼 수 있습니다.

---

# 5. Greedy as State-Space Compression

Greedy 알고리즘은 DFS나 BFS처럼 state space를 탐색하지 않습니다.

대신 매 단계에서 하나의 선택만을 수행하여 **state space를 강하게 축소**합니다.

즉

```

branch exploration

```

을 하지 않고

```

local optimal choice

```

만을 수행합니다.

이러한 선택이 항상 최적해로 이어지기 위해서는 다음과 같은 증명이 필요합니다.

- Exchange Argument
- Cut Property

따라서 Greedy는

```

state space compression 전략

```

으로 해석할 수 있습니다.

---

# 6. DFS와 DP의 구조적 관계

다음과 같은 DFS 구조를 생각해보겠습니다.

```python
def P(state):

    if base_condition:
        return evaluate(state)

    best = worst

    for choice in choices:
        best = max(best, P(next_state))

    return best
```

이 구조는 **state space를 탐색하는 기본 DFS 템플릿**입니다.

여기에 메모이제이션을 추가하면

```python
from functools import lru_cache

@lru_cache(None)
def P(state):
    ...
```

동일한 구조가 그대로 **Dynamic Programming**이 됩니다.

즉

```
DP = DFS + memoization
```

으로 이해할 수 있습니다.

---

# 7. Problem Solving Process

이 관점에서 알고리즘 문제 해결 과정은 다음과 같이 정리할 수 있습니다.

```
1. 가능한 행동(Action) 정의
2. 행동을 결정하기 위해 필요한 정보(State) 도출
3. State Space 형성
4. 적절한 탐색 전략 선택
```

즉 알고리즘 문제 해결 능력은 결국

> **state space를 정의하는 문제 모델링 능력**

이라고 볼 수 있습니다.

---

# 8. Insight

많은 알고리즘 교재에서는 DFS, BFS, DP, Greedy 등을 **각각 별개의 기법**처럼 설명합니다.

하지만 state-space 관점에서 보면 이들은

```
state space를 탐색하는 서로 다른 전략
```

으로 통합적으로 이해할 수 있습니다.

그리고 다음과 같은 DFS 템플릿에서

```
memoization
```

이라는 **단 한 줄의 차이**로 DP가 만들어지는 구조는 이러한 관점이 실제 구현에서도 자연스럽게 나타난다는 것을 보여주는 예시라고 생각합니다.

---

# Conclusion

이 글에서는 다양한 알고리즘 기법을 **state space 탐색 전략**으로 통합적으로 해석하는 관점을 소개했습니다.

이 프레임워크는 서로 다른 알고리즘 패러다임을 하나의 구조로 이해할 수 있게 하며, 알고리즘 문제 해결의 핵심이 **문제를 state space로 어떻게 정의하는가**에 있음을 보여줍니다.

```

```
