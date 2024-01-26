---
title: "컴퓨터 네트워크 스터디 3주차"
excerpt: "Cookie, Session, JWT"
categories:
  - computerNetwork
---

> 컴퓨터 네트워크 스터디 3주차

# Statefull : Cookie , Session, JWT

## HTTP

HTTP는 **Connectionless, Stateless** 특성을 지닌다.
~less는 ~하지 않는 것이라는 뜻.
즉 **HTTP는 연결과 상태를 유지하지 않는다**

> ### Conncectionless
>
> HTTP는 TCP connection을 유지시키지 않는다.
> 즉, Request를 받고 Response를 보내면 둘은 연결이 끊어진다.
> (TCP connection을 유지하는 Keep-alive는 고려하지 않음)

> ### Stateless
>
> HTTP는 상태정보를 저장하지 않는다.
> 따라서 연결이 끊어지는 순간 모든 상태 정보가 사라진다.

이러한 HTTP의 본질적인 특징 때문에 Cookie와 Session이 필요하다.
만일 Cookie와 Session이 없다면 아래와 같이 통신은 치매 걸린 단말들의 대화가 될 것이다.

A : 안녕! 내 이름은 A야. 사탕 먹을래?  
B : 안녕! A야. 고마워~~ 잘먹을께  
A : 너는 이름이 뭐야?  
B : 누구세요? (정말 모름)

## Cookie

쿠키는 클라이언트에 저장되는 키와 값이 포함된 작은 데이터 파일이다.
이러한 쿠키는 다음과 같이 구성된다.

- 이름 : 쿠키의 이름
- 값 : 쿠키의 값
- 파기시점 : 쿠키의 명줄
- 도메인 : 쿠키가 적용되는 도메인
- 경로 : 쿠키의 도메인에 있는 경로

쿠키의 작동 방식은 아래와 같다.

1. 클라이언트가 서버에 정보를 요청한다.
2. 서버는 쿠키를 포함한 응답을 보낸다.
3. 클라이언트는 쿠키를 로컬 저장소인 쿠키 저장소에 저장한다.
4. 클라이언트는 서버에 재접속을 한다. 이때 쿠키 저장소에 있는 쿠키를 꺼내서 요청을 한다.
5. 서버는 쿠키를 읽어 클라이언트를 식별한다.

## Session

클라이언트에 로컬 저장소를 이용하여 쿠키를 관리하고, 서버에 요청 시 이 쿠키를 포함하여 HTTP request를 한다.
그러나, 민감한 정보가 이에 포함되고 누군가 이를 갈취해간다면 우리의 개인정보는 그대로 털릴 것이다.
이를 위해 세션이라는 개념이 도입되었다.
세션 또한 쿠키의 일종이라 볼 수 있는데, 다만 핵심 정보를 클라이언트 측이 아닌 서버 측이 가지고 있는 것이다.

세션의 작동 방식은 아래와 같다.

1. 클라이언트가 서버에 정보를 요청한다.
2. 서버는 클라이언트의 정보를 서버 측 저장소인 세션 저장소에 기록, 그리고 이 기록의 인덱스(sessionID)를 담은 쿠키를 생성하여 이를 포함해 응답을 보낸다.
3. 클라이언트는 인덱스(sessionID)가 담긴 쿠키를 로컬 저장소인 쿠키 저장소에 저장한다.
4. 클라이언트는 서버에 재접속을 한다. 이때 쿠키 저장소에 있는 쿠키를 꺼내서 요청을 한다.
5. 서버는 쿠키를 읽어 인덱스(sessionID)를 파악하고 세션 저장소를 확인해 클라이언트를 식별한다.

## cookie vs session

쿠키는 중요 정보를 클라이언트에 저장하여 빠르고, 브라우저를 종료해도 정보가 그대로 남아 있다.
그러나 요청을 보낼 때 스니핑 당한다면 개인정보를 털릴 수 있다.
세션은 중요 정보를 서버가 가지고 있으므로 스니핑 당해도 아무런 걱정이 없다.
그러나 서버의 자원을 사용하기 때문에 서버에 요청자가 많을 경우 서버가 부하가 걸린다.
즉, **신속/편의성을 지닌 쿠키 vs 보안성을 지닌 세션**을 알맞게 적용해야 한다.

그렇다면, 쿠키처럼 서버에 부담도 가지 않으면서 세션처럼 보안성도 갖춘 존나 섹시한 개념은 존재하지 않는 것일까?
존재한다. 그게 바로 JWT이다.

## JWT

JWT는 Json Web Token의 약어이다.
Json 객체에 인증에 필요한 정보를 담은 뒤, 서버가 가진 비밀키로 서명한 토큰이다.
즉, JWT는 **암호화한 쿠키**라고 생각하면 된다.
JWT는 Header, Payload, Signature로 구성되어 있다.

- Header
  - 암호화 알고리즘, 토큰 타입
- Payload
  - 토큰의 내용
- Signature
  - Header, Payload를 헤더에서 선언한 암호화 방식으로 암호화 된 것

따라서 JWT는 토큰을 사용해 사용자 상태를 서버가 저장하지 않아도 되며, 서버만이 복호화 할 수 있는 비밀키를 가지고 있기에 보안성에도 문제가 없는 방식이다.
그러나, 한번 발급해 서버의 손을 떠난 토큰은 변경할 수 없다는 것과 토큰의 크기가 커지면 트래픽에 영향이 미칠 수 있다는 단점을 지니고 있다.

---

# SOP, CORS

## Same-Origin Policy

SOP란 Same-Origin Policy의 약어다.
이는 같은 출처에 대해서만 접근을 허용하는 정책이다.
브라우저가 사용자를 악의적인 코드로부터 보호하기 위해서 만들어졌다.
이떄 출처란 protocol, host, port를 의미한다.

> 즉, SOP 란 동일 protocol, host, port를 가진 사이트에서만 리소스를 공유할 수 있다는 정책

그러나 현재의 웹 사이트는 여러 API들이 각각 다른 출처로 리소스를 요청해야 한다.
따라서 API를 실행하려하면 에러가 발생하는데, 이는 SOP가 오히려 방해되는 정책이 된다.

그러기에 CORS, Cross-Origin Resource Sharing이란 개념이 필요하게 되었다.

## Cross-Origin Resource Sharing

API들이 제3자인 다른 출처로부터 리소스를 받는 것을 허용하는 정책이다.
SOP가 기본값, 그리고 백엔드에서 각 API에 필요로 하는 출처에 CORS 정보를 기입하면 된다.
[MDN Document : CORS](https://developer.mozilla.org/ko/docs/Web/HTTP/CORS)

---

# REST

> REST란 REpresentational State Transfer의 약어로,
> 서버에서 클라이언트로 특정 시점의 자원의 대표를 전송하는 것이다.

우리가 내일 온도를 구하고자 한다 서버에 요청한다 하면,
서버는 JSON 형식으로 '내가 위치한 내일의 날씨'를 줄 것이다. 즉, 내가 요청한 **내일 온도**가 아닌 그 중 represenational한 '내가 위치한 곳의 내일의 날씨'를 주는 것이다.
또한 이는 현 시간(state) 기준이고, 이는 서버에 요청하는 시간에 따라 계속 달라질 수 있다.

> REST의 구체적인 개념은 HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)을 명시하고, HTTP Method(POST, GET, PUT, DELETE)를 통해 해당 자원에 대한 CRUD Operation을 적용하는 것을 의미한다.

REST의 구성 요소

- 자원 : URI
  - 모든 자원에 고유한 ID가 존재, 이 자원은 서버에 존재
  - 클라이언트는 URI를 이용해 자원을 지정, 서버에게 해당 자원의 상태에 대한 접근을 요청
- 행위 : HTTTP Method
  - GET, POST, PUT, DELETE와 같은 http 메소드 사용
- 표현 :
  - 클라이언트가 자원의 상태에 대해 접근을 요청하면 서버는 JSON,XML,TEXT등 알맞은 표현으로 나타내어 전송

## RESTful API

REST를 기반한 API를 뜻한다.
특정한 양식에 따라 API를 이용할 수 있는데,

1. URI는 정보의 자원을 표현해야 한다.
2. 자원에 대한 행위는 HTTP Method(GET, PUT, POST, DELETE)로 표현한다.

## REST 제약 조건

1. Client-Server
   - 클라이언트는 서버의 리소스 URI만 알고 있으면 되고, 서버 내부의 동작과정을 몰라도 된다.
2. Stateless
   - 클라이언트가 보내는 각 요청에는 그 요청에 필요한 모든 정보가 포함되어야 한다.
3. Cache
   - 요청이 캐시가 가능한지 여부를 명시해야 한다.
4. Uniform Interface
   - 일관된 인터페이스를 구축해 사용성을 높인다. (JSON 사용)

---

# URI, URL, URN

Uniform Resoucre Identifier, 하나의 리소스를 가르키는 문자열이다.
이 URI가 리소스의 주소를 가리키면 URLocation, 이름을 가리키면 URName이다.
![URI, URI, URN](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fcf569Z%2FbtqSIZO6Ewm%2FFjknijdnfAehSy6B8IXMlk%2Fimg.jpg)
URI는 한동안 URL만을 사용했는데, 문제점이 있었다.
서버가 리소스의 위치를 변경하면 URL은 그 리소스를 더 이상 접근할 수 없게 되었기 때문.
따라서 URN이라는 개념이 도입되었다. 이름으로 리소스를 식별하니 위치가 변경되더라도 리소스를 추적하여 가져올 수 있다.
그러나, 현재는 URL이 표준으로 사용되고 있으며 나중에 URN으로의 표준화가 진행될 듯 싶다.

---

# XSS : Cross Site Scripting

웹 해킹 공격중의 일종이다. CSS로 줄어 부르는게 맞지만, Cascading-Style-Sheet가 이미 있어 XSS라 부른다.

XSS는 공격자가 상대방의 브라우저에 스크립트가 실행되도록 하는 공격이다.
공격자가 site 사이를 cross하여 scripte코드를 실행하는 것이라 XSS라 부른다.

## Reflected XSS

1. 공격자가 XSS 공격 스크립트가 포함된 URI를 사용자에 노출시킨다.
2. 사용자가 해당 URL을 클릭하여 취약한 웹 사이트의 서버에서 해당 스크립트를 포함한 request를 전송하고, 웹 서버는 해당 스크립트를 포함한 response를 전송한다.

## Stored XSS

1. 공격자는 XSS 공격에 취약한 웹 사이트를 탐색, 스크립트를 포함한 게스글을 웹 사이트에 업로드 한다.
2. 사용자는 게시글을 확인하고 URL에 대한 요청을 서버에 전송한다.
3. 웹 서버에서 스크립트를 포함한 Response를 전송하며 공격이 수행된다.

이러한 XSS를 통해 공격자는 사용자의 쿠키 정보, 세션 ID를 획득할 수 있다.
또한 악성 프로그램을 다운받는 사이트로 리다이렉트할 수도 있다.

## Prevention

XSS의 공격에 사용되는 <.> 등의 특수문자를 필터링하여 XSS의 공격을 예방할 수 있다.

---

# SQL Injection

공격자가 악성 SQL 코드를 삽입하여 DB에 무단 접근하는 공격을 말한다.
![SQL Injection](https://i.namu.wiki/i/tCkLrmNGPDijaLHxc66Sn83vbOM4jQn8e_3-L7U6Gs5Sv-MdhQUzhSDNMGakjmfEPQqAiuLNpEjPHoPncyI0PHFrsC_iuf1WNdmw7Lwg2UADTS_55qg2ZwQSB7UAjGNACmtWmNhW-p5aWD-M-G8PHA.webp)

## Prevention

클라이언트 측의 입력을 받을 때 프론트 단에서 폼 입력값을 한 번 검증하고, 백엔드 단에서도 입력값을 검증해야 한다.
또한 SQL 쿼리를 사용자에게 직접 보이지 않게 하는 것도 중요하다.
실제로는 관련 라이브러리를 사용해 SQL Injection을 방직한다.

---

# CSRF

Cross Site Request Forgery의 약어로 사이트를 간 요청을 위조하는 공격이다.
사용자가 자신의 의지와 무관하게 공격자가 의도한 행위를 요청하게 한다.
![CSRF](https://velog.velcdn.com/images%2Fgwanuuoo%2Fpost%2F7f926efe-4b52-49d9-8dfd-78b26c0c1bb1%2FScreen%20Shot%202021-06-27%20at%202.15.28%20PM.png)

1. 사용자가 CSRF에 취약한 서버에 접속
2. 서버의 sessionID가 사용자 브라우저의 쿠키 저장소에 저장
3. 공격자는 사용자가 악성 스크립트 페이지를 누르도록 유도
4. 사용자가 악성 페이지를 접근하면 웹 브라우저에 의해 쿠키에 저장된 sessionID와 함께 서버에 요청.
5. 서버는 악성 페이지로부터의 요청이 sessionID를 가지고 있으므로 이것이 인증 사용자라고 잘못 판단하게됨.
6. 악성 페이지에서 의도하지 않는 행동을 요청하게 한다.

XSS 공격은 악성코드가 클라이언트에서 실행되는데, CSRF는 서버에서 악성코드가 실행된다고 볼 수 있다.

## prevention

1. referer 체크 ( 요청의 출처를 표시 )
2. CSRF 토큰 사용
3. 요청시 추가 인증 요구(CAPCHA)

---

# Web Cashe

캐시(Cashe)란 자주 사용하는 데이터나 값을 미리 복사해 놓는 하드웨어이다.
![Cashe](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FZdW35%2FbtqCbTDmFj5%2FAKbAUKiWseStnfD1Cd7gqk%2Fimg.png)

반복적으로 동일한 결과를 돌려주거나, 데이터를 접근하는데 시간이 오래 걸리는 경우 사용하는데 웹에서도 비슷하게 구현한 것을 Web Cashe라고 한다.

웹 캐시의 작동방식을 살펴보자

1. 캐시는 네트워크로부터 도착한 요청을 읽는다.
2. 캐시는 요청에 대한 응답을 가지고 있는지 검사하고 없다면 사본을 받아와 캐시에 저장
3. 캐시는 자신이 가지고 있는 것이 신선한지 검사한다.
4. 캐시는 새로운 응답 메세지를 만들고 클라이언트에게 보낸다.

---

# Proxy Server

Proxy는 대리라는 뜻으로, 프록시 서버는 대리 서버라는 뜻이다.
클라이언트와 서버 사이에 위치하여 트랜잭션을 수행하는 중개인이다.

프록시 서버 사용 목적

1. 익명성으로 보안 유지
2. 캐시를 통해 속도 향상
3. IP 우회
4. 원하지 않은 사이트 차단

프록시 서버의 위치에 따라 Forward Proxy, Reverse Proxy로 나뉜다.

## Froward Proxy

![Forward Proxy](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FecDpEm%2Fbtq84ORRy4O%2FbUzIb7gFw5kMV9GgrELRK0%2Fimg.png)

일반적인 프록시 서버이다.
클라이언트가 프록시 서버에 요청한 내용을 프록시 서버에서 캐시로 저장해 두면 추후 데이터 요청 시 이를 이용해 전송 시간을 절약할 수 있다. 또한 학교와 같은 경우, 유해 사이트를 차단하는 기능을 추가할 수 있다.

## Reverse Proxy

![Reverse Proxy](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FclnpTH%2Fbtq85EohI89%2FLMK7hdOm9SI9v5fd2O187K%2Fimg.png)

리버스 프록시 서버의 사용 목적

1. 로드 밸렁싱 : 서버에 트래픽 분산
2. 보안 강화 : 외부 요청을 필터링
3. 캐싱 : 응답 시간 개선
4. 웹 서버 최적화 : 웹 서버의 설정, 성능 최적화

# L7 Load Balancer

L7 로드 밸런서는 OSI 7계층의 헤더까지 읽어서 트래픽을 여러 서버에 분산하는 역할을 한다.
또한 헬스 체크를 통해 정기적으로 서버가 살아 있는지 확인하고, 살아 있는 서버에 트래픽을 전달한다.

# Connection timeout, Read timeout

timeout이란 **프로그램이 특정한 시간 애에 성공적으로 수행되지 않아 진행이 자동적으로 중단되는 것**이다.
Connection 과정에서, Read 과정에서 각각 타임아웃이 발생할 경우를 말한다.

![Timeout](https://velog.velcdn.com/images/no-int/post/3028e456-4169-483b-936d-faf08dca97f7/image.png)

> Connection timeout은 TCP 3 way handshake 과정에서 발생
> Read timeout은 연결 후 요청을 주고 받는 과정에서 발생

---

> 참고 자료
> [얄팍한 코딩사전 : Session, JW](https://youtu.be/1QiOXWEbqYQ?si=2D8rRxqhDZcNtrrf) >[얄팍한 코딩사전 : CORS](https://youtu.be/bW31xiNB8Nc?si=xFNm0HuYxQjlBcU6) >[Vellog : CORS](https://hudi.blog/sop-and-cors/) >[Tistory : REST](https://im-developer.tistory.com/168)
