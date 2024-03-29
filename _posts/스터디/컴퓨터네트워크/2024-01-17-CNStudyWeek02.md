---
categories:
  - computerNetwork
---

# 컴퓨터 네트워크 스터디 2주차

이번주는 OSI 7계층, 혹은 TCP/IP 프로토콜의 최상단인 애플리케이션 계층에서의 동작을 규정하는 프로토콜에 대해 학습하였다.

크게 HTTP, HTTPS, DNS에 대해 알아보았다.

​

## HTTP

​

### What is HTTP?

HTTP를 모르는 사람은 없을 것이다. 근데, 과연 정확히 안다고는 말할 수 있을까?

HTTP는 우리가 인터넷 상에서 원하는 정보를 서버에서 가져와서 보기 위한 프로토콜이다.

HTTP는 Hypertext Transfer protocol의 약어다.

text는 말그대로 글자인데, 그렇다면 Hypertext는 존나 좋은 글자?

가 아니라 Hypertext는 글자인데 링크가 있어서 다른 문서로 이동할 수 있는, 고급진 말로 non-linear한 text를 칭한다.

정리하자면

> HTTP는 Hypertext Transfer protocol :: 링크를 포함한 텍스트 파일을 전송하는 데 필요한 규약

이라 할 수 있다.

참고로, 인터넷으로 이미지나 영상도 볼 수 있는데 왜 굳이 hyperImg.. hypervideo.. 가 아니라 하필 text인 이유는 초기 HTTP는 진짜 오직 text, 글자만 볼 수 있었기 때문이다.

그리고 세월이 흐름에 따라 지금과 같이 여러 매체 또한 주고 받을 수 있게 된 것.

​

### HTTP : Request, Response model

구글에 '개발자로 취업하는 법'이라는 검색을 했다고 하자.

그렇다면 관련 검색 결과들이 수두룩하게 보일 것이다.

그 수두룩한 검색 결과를 직접 컴퓨터에 저장해 놓고 쓰는 시간 빌게이츠는 없을 것이다.

다 서버에 있는 정보들을 가져오는 것이다.

> 이렇게 검색이나 클릭 등의 동작을 통해서 서버에 데이터를 요청하는 것을 Request,
>
> 그럼 서버는 요청에 응답을 하면서 데이터를 주는데 이를 Response 라고 한다.

구체적으로 Request, Response가 어떻게 이루어지길래 서버가 가지고 있는 데이터를 가져올 수 있는 걸까?

교수님께 질문하기 위해서 '이거 좀 알려주셈'라고 말하는 사람은 없을 것이다.

특히 메일로 질문드리는 경우라면 사회적 규범에 맞게 정해진 양식을 지키며 작성할 텐데, 컴퓨터도 이와 같이 규범(프로토콜)에 맞춘 양식을 따라야 한다.

우리 컴퓨터와 서버가 메세지를 주고 받음에 있어서 정해진 양식인 HTTP 메세지 포멧에 대해 알아보자.

사실 포멧은 HTTP/1.1가 HTTP2로 넘어 오게 되면서 약간 달라졌는데, 현재 HTTP/1.1이 가장 대중적인 관계로 HTTP/1.1 기준의 포멧으로 알아보자.

![HTTP message format](https://blog.kakaocdn.net/dn/zNWLu/btqX1oiQvLm/GgDhtcghfN75p9qqXFJbv0/img.png)

​

#### Request message

Request message, 즉 요청 메세지는 서버에게 '나 이거 좀 보여줘'라고 말하는 것과 같다.

이 요청의 포멧을 보면 아래와 같이 이루어져 있다.

1. Request Line

   - 메소드 : 부탁의 목적. 흔히 알고 있는 GET 혹은 POST 방식으로 데이터를 가져오고 싶은 요청인지, 혹은 삭제하고 싶은 요청 등
   - request url : 부탁의 대상. 예를 들어 http://www.naver.com이라 한다면 네이버 사이트를 가져오고 싶다는 요청일 것
   - http version : 부탁의 언어. 지금 나는 http/1.1 버전의 웹 브라우저를 사용하고 있으니 1.1만 알아들을 수 있음, 서버 너도 대답할 때 1.1 포멧에 맞추어 얘기해 달라는 것

2. Header

   - request header : 지금 나의 상태를 서버에게 얘기해주는 헤더. 교수님께 질문드릴 때 학부생 레벨의 설명을 원한다던지, 아니면 대학원생 레벨 아니면 감자.. 의 나의 수준에 맞게, 내 수준에서 알아 들을 수 있는 언어를 사용해달라는(웹 브라우저가 받을 수 있는 파일을 나타냄) **Accept 헤더** 가 있다. 또한 요청이 어느 url에서 타고 온 건지를 나타내는 **Referer 헤더**, 웹 브라우저나 OS 등의 사용자 환경을 나타내는 **User-Agent 헤더** 등이 포함되어 있다.
   - general header : HTTP 메세지를 제어하는 헤더. 예를 들어 이 메세지를 로컬 컴퓨터에 저장해 두고 필요할 때 꺼내 쓰라는 의미의 케시 여부를 결정하는 **Cache-Control** 헤더, TCP 연결을 끊지 말라는 의미의 **Connection/Keep-Alive 헤더** 등이 포함된다.
   - Entity header : 실질적인 요청의 메세지는 Message body안에 들어간다. 예를 들어 파일을 업로드 한다고 하면, 파일의 내용이 Message body안에 들어가게 되는데 이 내용에 대한 메타데이터.
   - 기타 header : Cookie에 이용되는 세션 ID 등.. 이 포함

3. Blank Line

   - 말 그대로 빈 줄, 구분선이다.

4. Body

   - 실제적으로 전송하고자 하는 내용. 파일 업로드가 요청이라면 파일이 포함되고, 이미지 업로드라면 이미지가 여기에 포함된다.

     요청에 따라 body가 필요없는 경우도 있으니 Body는 Request Message의 필수 요소가 아니다.

​

#### Response message

Response message는 위의 request message 포멧에서 request line이 status line으로 바뀐 것과 Header안의 requset header가 response header로 바뀐 것이 끝이다.

그럼 Status Line, response header 에 대해 알아보자.

1. Status Line
   - HTTP version : HTTP 버전을 나타낸다. 웹 브라우저한테 해독할 때 해당 버전의 프로토콜을 쓰라는 것
   - status code : 선착순 티켓팅을 실패하면 404 error가 뜬다. 그 404가 status code
   - reason place : status code에 대한 이유가 들어있는 곳. 위 예시의 404 status code의 reason은 "Not Found". 즉 당신이 찾으려는 티켓을 못찾겠다는 말.
2. Header
   - response header : 서버 상의 리소스를 식별하기 위한 정보를 지닌 **ETag 헤더**, 리다이렉션 위치를 포함하는 **Location 헤더** 등이 포함되어 있다.
   - 이하는 Request message의 포멧과 같다.

​

### Difference between GET & POST

우선, get : 가져오다 post : 게시하다 라는 뜻 때문에 혼동이 될 수 있는데,

**GET, POST 둘 다 서버에 요청을 보내는 Request Method**이다.

다만 GET은 통상적으로 정보를 가져올 때 많이 쓰이고, POST는 정보를 게시할 때 많이 쓰여서 그리 명명된 것.

​

#### GET 방식

만약 "How to study CN?"이라는 검색어를 구글에 입력한다면 url에 이 검색어가 추가되면서 검색결과를 보여준다.

> 요청을 전송할 떄 이 url + 검색어를 포함해 전송하고, 이 방식이 GET 방식이다.

서버는 이 요청에 대한 답으로 검색결과를 보여준다.

그런데 만약 주민등록번호를 입력하고, url + 주민등록번호 문자열이 서버로 넘겨지게 된다면? 중간에 누군가 가로채게 된다면? 그래서 내가 사칭피해를 당하게 된다면??

그래서 GET방식은 민감한 데이터를 다룰 때는 사용하지 않는다.

다만 자동완성 기능과 같이 브라우저에 남는 기록, 캐시, 북마크 추가와 같은 사용자가 편리하다는 장점도 있기 때문에 민감하지 않은 검색과 같은 영역에서는 사용한다.

​

#### POST 방식

> 요청을 보낼 떄 정보가 GET 방식처럼 url에 포함되는 것이 아니라 HTTP message의 body에 정보를 포함시켜서 보낸다.

따라서 POST방식은 안전하다. 주민등록번호와 같은 민감한 정보를 다룰 수 있다.

고 생각하는가??

HTTP message를 중간에 가로채서 header만 추출하면 주민번호가 있는 body가 그대로 들어나게 된다.

따라서 POST방식은 그 자체로 안전한 방식이라 볼 수 없다.

GET방식은 그냥 바로 url에 주민번호가 찍혀서 보안이 허술하다 못해 없는 수준이라 비교적 POST가 안전하다고들 생각하는 것.

실제로는 POST방식에 암호화를 적용시켜서 사용한다.

​

### Difference between PUT & PATCH

​

#### PUT 방식

put : 가져다 놓는다. 만일 (A:10,B:10)가 있을 때 A:5를 put하면 (A:5)로 변함

​

#### PATCH 방식

patch : 패치한다. 만일 (A:10,B:10)가 있을 때 A:5를 put하면 (A:5, B:10)로 변함

한마디로 put은 아예 전부 업데이트, patch는 일부를 업데이트 한다는 것.

​

### HTTP Status Code

일단 404 error는 초딩 시절 마인크래프트 APK 무료 다운 받기 드롭 박스에서 많이 봤다. 404는 복돌이 신고 당해서 해당 리소스가 존재하지 않다는 것.

그 외에 100번대부터 500번대까지의 상태 코드가 있는데, 백의 자리는 클래스를 나타내고 십과 일의 자리는 코드 분류번호다.

백의 단위가 같으면 클래스가 같은 것

![HTTP status code](https://www.fis.kr/upload/image_attach/2022/10/72.jpg)

​

### HTTP's stateless

HTTP의 무상태이란 서버가 위에 나타낸 http status code가 담고 잇는 요청에 대한 상태를 가지고 보관하고 있지 않은 것을 말한다.

단순 소개 화면 같은 경우에는 이처럼 무상태로 설계하면 응답 서버도 쉽게 바꿀 수 있기 때문에 이점이 있지만, 인터넷 쇼핑몰과 같은 경우 로그인, 장바구니와 같이 상태 정보를 한대의 서버가 지속적으로 관리해야하는 경우에는 무상태성이 적합하지 않을 것.

​

### HTTP Keep-Alive

주제에서 벗어난 얘기를 잠깐 해보자.

지금 강남역에 헌팅을 하러 서있다. 당신은 인싸라서 아무나한테 잘 말걸고 다닌다. 따라서 아무나 붙잡고 얘기를 한다. 이게 UDP 방식이다.

상대가 기겁하며 안들리는척 갈 길 가더라도 나는 개 상남자라서 혼잣말을 계속한다. (데이터 유실) 하지만 아무나 붙잡아서 얘기만 해도 되기 때문에 빠르다.(UDP의 빠른 데이터 전송)

반면, 당신의 친구는 전략을 달리 썼다. 이 친구는 악수를 매우 좋아하는 친구여서 헌팅할 때마다 악수를 먼저 한다.

1. 마음에 드는 이성이 보이면 가서 악수를 청한다.
2. 상대는 도망치거나, 악수를 받는다.
3. 친구가 본격적으로 말을 건다.

이것이 TCP이고, 위의 3단계는 TCP의 3 Way-Handshake이다. 일단 악수를 받았다면 도망치지 않을 것이므로 데이터 유실은 없을 것이다.

그런데 이 친구는 존나 멍청해서 한마디 할때마다 악수를 청한다.

악수 -> 안녕하세요 어디가는 길이세요? -> 악수 -> 아 저도 거기가고 있었는데 -> 악수 -> 뭐지 이놈은

상식적으로 처음 만났을 때 악수하고, 헤어질 때 악수하는게 깔끔하고 시간 소모도 없을 것이다.

> 이처럼 대화의 장, 즉 TCP Connection이 되었으면 계속 3 Way Handshaping을 하지 않는 것이 Keep-Alive이다.

충격적인 사실은 2000년대 전의 HTTP/0.9~1.0때에는 진짜 저 친구처럼 악수를 계속했다는 것이다. (Keep-Alive가 적용되지 않았었음)

​

### HTTP PipeLine

클라이언트와 서버는 관 2개를 연결해 있다고 생각하자. 하나는 클라이언트가 서버로 보내는 것을 저장하는 관, 나머지는 그 반대.

덕분에 원래대로면 하나를 보내고 응답을 기다리고... 불필요한 시간이 소비되었을 텐데, 관이 있기 때문에 일단 내가 보낼 것을 전부 보내면 된다.

> 즉, Pipline은 요청에 대한 응답을 기다리지 않고, 다음 요청을 바로 송신하는 기능이다.

그러나 이 파이프라인 기능은 TCP에서는 요청을 보내고 기다려야하는 것이 필수적이였기 때문에 먼저 보냈다고 해도 응답을 또 기대려야 했다.

만일 1,2,3 요청을 보냈는데 1요청만 1시간째 하고 있다 하면 2,3은 놀고 있게 된다. 이게 HOL 블로킹(Head of Lock Blocking)이고, 따라서 파이프라인은 성과를 크게 올리지 못했다.

​

### HTTP/1.1 HTTP/2 HTTP/3

1. HTTP/1.1
   1. Keep-Alive
   2. Pipeline : HOL blocking 문제
2. HTTP/2

   1. Multiflexing : Pipline의 HOL blocking 문제 해결. (TCP 커넥션 유지하는 스트림 채널 이용)
   2. HPACK : 메시지 헤더 압축 (자주 쓰이는 것 치환)
   3. Server Push : 필요한 것을 요청이 오기 전에 먼저 보냄 (똑똑 교수님 들어가도... / 강의 자료는 여기있고, 지난 족보는 여기있고, 장학금과 A+도 주겠네!)

3. HTTP/3
   1. UDP : 일단 보냄. (단점인 신뢰성은 개발자가 알아서 구현)
   2. TLS1.3 사용 : 좀 더 빠른 인증방법 채택하서 빠르다.

​

## HTTPS

​

### What is HTTPS?

url에 어느 순간 보면 http:// 가 https:// 로 바뀐 것을 볼 수 있는데

> HTTPS는 HTTP 통신이 SSL방식으로 암호화되어 있다는 뜻이다.

​

### Difference between SSL & TLS

사실 두 개는 같다. 암호화 기술인 SSL이 해킹공격에 대한 취약성을 보완하며 발전해 나가는 과정에서 TLS가 탄생한 것.

SSL의 역사는

SSL 2.0 -> SSL 3.0 -> TLS 1.0 -> TLS 1.1 -> TLS 1.2 -> TLS 1.3 이다. 여기서도 볼 수 있듯이 SSL과 TLS은 본질적으로 같다.

참고로 SSL 1.0은 나오자마자 취약성이 발견되서 상장 폐지 엔딩을 해버렸다.

​

### 암호화 방식

​

#### 대칭키 암호화 방식

클라이언트와 서버는 같은(대칭) 키를 가지고 있다.

이 키를 이용해서 클라이언트는 요청을 암호화해서 request하고, 서버는 이 키를 이용해서 request message를 복호화한다.

그런데, 처음에 이 '같은 키'라는 건 어떻게 서로 교환할까?

초기에 키를 보내는 과정이 필연적으로 발생하게 되는데, 이때 누군가 가로채버린다면 답이 없다.

​

#### 비대칭키(공개키) 암호화방식

클라이언트와 서버는 다른(비대칭) 키를 가지고 있다.

공개키와 비밀키라는 개념이 등장하는데, 공개키와 비밀키는 쌍으로 존재하고 한쪽 키로 암호화한 것은 다른 키로만 복호화 할 수 있다. 수학적으로 증명되었다고 한다.

1. 서버는 공개키와 비밀키를 만든다.
1. 공개키를 전부에게 뿌린다. (비밀키는 서버 나만이 가지고 있는 비밀 ><)
1. 클라이언트는 요청을 공개키로 암호화해서 전송한다.
1. 서버는 이 암호화를 풀 수 있는 유일한 비밀키를 가지고 있으므로, 이를 복호화한다.

이는 대칭키가 가지고 있는 초기에 키를 보내는 과정에서의 취약성을 지니지 않으므로, 안전하다. 하지만 초기 수학적으로 공개키와 비밀키 쌍을 추출하는데 많은 시간이 걸리는 것이 단점이다. 따라서 실제로는 두 방식의 장점을 적절히 섞은 방식을 사용하고 있다.

​

### 전자 서명

고등학교 시절, 그러면 안되지만 술을 산다고 생각해보자.

편의점에 들어가서 '저 성인인데 술 좀 주세요'라고 하면 술을 줄까?

당신이 아무리 알바생한테 성인이라고 말을 해도 알바생은 민증을 요구할 것이다.

민증이 뭐길래?

민증은 인증기관인 정부에서 이 사람이 성인이라는 정보를 담은 일종의 '서명'이다.

> 다시 말해, 전자 서명은 신뢰를 받는 인증기관에서 서버 A가 진짜 서버 A라고 보증서는 것을 말한다.
>
> (실제로는 보증이 아니라 해시값 비교를 통해 A임을 수학적으로 증명한다.)

​

### HTTPS의 암호화 과정 (SSL Handshake)

TCP Handshake은 TCP 영역에서 대화를 하기 위해 악수하는 것, SSL Handshake은 보안을 구축하기 위해 악수하는 것이라 생각하면 된다.

이때, 상술한 대칭키와 비대칭키의 장점만을 합친 하이브리드 암호화 방식을 택한다.

이는 대칭키를 바로 사용하는 것이 아닌, 대칭키 재료를 비대칭키로 전달한다는 방식을 취한다.

// 암호화 방식 결정

1. 클라이언트는 서버에게 Client Hello(사용 가능한 암호화,해시 방식 포함)를 보낸다.
2. 서버는 클라이언트에게 Server Hello(암호화, 해시 방식 결정)을 보낸다.

// 서로임을 디지털 서명을 통해 증명(서버, 클라이언트 순으로 증명)

1. 서버는 클라이언트에게 Certificate(디지털 서명)를 보낸다.
2. 서버는 클라이언트에게 Certificate Request(클라이언트 인증 요청)을 보낸다.
3. 클라이언트는 서버를 검증한다.
4. 클라이언트는 서버에게 Certificate(디지털 서명)를 보낸다.
5. 서버는 클라이언트를 검증한다.

// 대칭키 재료 전달

1. 클라이언트는 대칭키 재료를 비대칭키 방식으로 공개키를 이용해 암호화하여 서버에 보낸다.(Client Key Exchange)
2. 서버는 이를 비밀키를 사용해 복호화해서 대칭키 재료를 찾는다.
3. 클라이언트와 서버는 이로써 대칭키 재료를 공유하고, 이로부터 같은 대칭키를 갖는다.

// 최종 확인

1. 클라이언트는 서버에게 Change Cipher Spec(통신 방법 결정)을 보낸다.
2. 클라이언트는 서버에게 Finished를 보낸다.
3. 서버는 클라이언트에게 Change Ciperher Spec(통신 방법 승인)을 보낸다.
4. 서버는 클라이언트에게 Finished를 보낸다.

이후로는 서로를 신뢰하고 정보를 주고 받는다.

​

## DNS

​

### What is DNS?

DNS는 Domain Name System의 약어로, 사람이 외우기 힘든 IP주소를 문자열에 대응시키는 프로토콜이다.

예를 들어 "www.google.com"이란 문자열이 172.217.175.4라는 숫자에 대응한다.

브라우저는 우리가 문자열을 주소에 입력하면 DNS 서버에 대응하는 숫자인 IP주소를 알려달라고 요청하고, 응답받아서 알맞은 주소로 이동시킨다.

​

### How DNS works?

문자열과 IP주소를 대응시키는 과정을 **이름 결정**이라 한다.

DNS clinet, Cashe-server, Authoriative-server가 협력해서 이름을 결정한다.

1. DNS 클라이언트인 우리의 웹 브라우저가 문자열을 들고 와서 캐시 서버에 전송한다.
2. 캐시 서버는 받은 문자열을 권위 서버에 보낸다.
3. 권위 서버는 전체 주소에서 top-level 도메인부터 nth-level 도메인까지 내려가며 캐시 서버와 재귀적으로 통신하고, 알맞은 존파일을 가지고 있는 하위 서버의 위치를 알려준다.
4. 최종적으로 캐시서버는 알맞은 IP주소를 받는다.
5. 캐시서버는 DNS 클라이언트인 우리의 웹 브라우저에게 IP 주소를 알린다.

​

​

### DNS Query : 재귀, 반복

이 부분은 구글링 해도 모르겠어서 ChatGPT의 도움을 받았다.

> DNS(도메인 네임 시스템)에서 재귀 쿼리와 반복 쿼리는 두 가지 다른 유형의 DNS 쿼리 프로세스를 나타냅니다.
>
> 1. **재귀 쿼리 (Recursive Query):**
>    - 클라이언트가 DNS 서버에게 전체 도메인 이름 해결을 요청합니다.
>    - DNS 서버는 클라이언트의 요청을 처리하기 위해 필요한 모든 단계를 진행하며 다른 DNS 서버들과의 상호 작용이 필요한 경우 이를 처리합니다.
>    - 최종적으로 DNS 서버가 클라이언트에게 완전한 응답을 제공합니다.
> 2. **반복 쿼리 (Iterative Query):**
>    - 클라이언트가 DNS 서버에게 도메인 이름 해결을 요청합니다.
>    - DNS 서버는 클라이언트에게 해당 도메인에 대한 최초 정보를 제공하거나 다른 DNS 서버의 주소를 알려줍니다.
>    - 클라이언트는 이후 필요한 단계를 진행하기 위해 추가적인 쿼리를 다른 DNS 서버로 보내며, 이 과정이 반복됩니다.
>    - 최종적으로 클라이언트가 필요한 정보를 얻을 때까지 이러한 과정을 반복합니다.
>
> 즉, 재귀 쿼리는 클라이언트가 모든 과정을 서버에게 요청하고 완전한 응답을 받는 반면, 반복 쿼리는 클라이언트가 단계적으로 정보를 얻어가며 해결을 진행하는 방식입니다.

쉽게 말해 '서버 너가 다 해줘'는 재귀, 클라이언트인 내가 다 하는 것은 반복 쿼리이다.

내가 DNS 동작 방식에서 말한 방식은 클라이언트인 캐쉬 서버가 다 하는 반복방식!! 이다.

​

### Why DNS use UDP?

DNS는 신뢰성을 잃는 대신 빠른 이름 결정을 위한 UDP를 택했다.

사용자 사용성을 위해서 UDP를 택한 것이고, DNS 내부의 존 전송에서는 TCP 방식을 쓰긴 한다.

​

### What is DNS record?

권위 서버는 루트 서버가 가장 최상단, 그리고 여러 하위 서버들이 트리 형태로 구성되어 있고, 각 서버들은 자신이 관리하는 도메인 범위(Zone)에 관련된 정보를 존파일이라는 DB에 DNS 레코드 형태로 저장한다. 도메인 이름에 대응하는 IP주소들을 가지고 있고 클라이언트한테 '쟤한테 가서 물어봐'라는 반복 쿼리에 응답한다.

​
