---
categories:
  - WebBase
---

# 노마드코더 KokoaClone 후기

## Result

아래 링크를 클릭하면 2주 동안 내가 만든 코코아 클론 사이트를 확인 할 수 있다.

[코코아 클론 링크](https://forwarder1121.github.io/kokoa-clone/)

(media-query로 설정해서 핸드폰으로 보거나, 그에 준하는 사이즈의 창으로 보아야 한다.)

![image](https://github.com/forwarder1121/kokoa-clone/assets/66872094/928e45c1-bf73-4196-a5db-90b272b572d8)

## Overview

노마드코더의 웹기초(html, css, js)의 10주차 스터디 중, 오늘부로 2주간의 거친 첫 번째 코스 코코아 클론 만들기를 완주했다.

군대가기 전에 이미 학교에서 html,css,js에 대한 건 많이 알고 있다고 생각했고 외부 프로젝트도 하면서 react도 다루어봤었어서 쉽겠지.. 돈만날리는건 아니겠지 생각했는데, 꽤 의미있는 학습을 했다.

학교에서는 이론을 배우고, 실무적인건 따로 배워야 한다고 어렴풋이 알고 있었는데, 딱 노마드코더가 그 **실무적인** 것에 적합한 강의를 제공해 주지 않나... 생각한다. 물론 강의료가 비싸긴 하다.

이번 KokoaClone 코스에서는 html과 css로만 작업했는데, 디자인의 영역이라 생각했던 css에 대해 좀 더 알게 되었다.

특히 animation이 이렇게나 섹시한 기능을 보여줄 수 있는 몰랐다. 그리고 BEM방식의 naming 방식도.

## What I learned

website는 단순한 text file에 불과하며, 브라우저가 해석할 수 있는 text(html,css,js)를 구성하여 브라우저를 띄우면 이 text를 브라우저가 해석하여 우리가 보는 웹사이트로 구성된다.

html(뼈대) : 브라우저에게 website의 content가 어떻게 구성되어 있는지 설명할 때 사용

css(근육) : 브라우저에게 content가 어떻게 보여야하는지 알려줌

js(뇌) : 브라우저에게 어떻게 동작해야 하는지를 알려줌

### HTML

#### Self-closing tag

html 태그는 열었으면 닫음이 있는게 원칙. 그러나 일부는 그 의미상 닫는 태그가 불필요한 것도 있는데, 이를 self-closing tag라 칭함.

사용법은 아래와 같음

```html
<img src="file_directory" />
```

#### head tag

html 문서의 상단 부분에 위치한 head 태그 안의 구문들은 우리 눈에 보이지 않는 태그들로 브라우저를 설명해준다.

#### wrong input

html의 tag나 attribute에 잘못된 값을 집어넣어도 에러가 발생하지 않지만, 브라우저가 이해를 하지 못해서 논리적으로 오류가 발생한다.

#### Semantic tag

코드의 가독성을 위해 태그 자체가 의미를 가지도록 semantic tag를 이용하자.

### CSS

#### cascading style sheet

말 그대로 css는 위에서 아래로 읽으면서 덮어쓰기가 된다.

#### grab html tag

css가 html tag를 꾸미기 위해서는 일단 html태그를 지칭할 수 있어야(grab)한다.

이때 고유 식별자인 id, 혹은 class를 이용하자.

#### display attribute : block vs inline

- block : 요소 옆에 다른 요소가 올 수 없다. div가 display : block 속성을 지니는 대표적 요소

- in-line : 같은 줄에 다른 요소가 올 수 있다. span, a, img등이 그 대표적 요소

  ​ 다만 높이, 너비를 가지지 못해서 갖게 하고 싶으면 display : block 을 지정을 따로 해주어야 한다.

  ​ 높이, 너비를 가지지 못하여 margin,padding이 좌우에는 적용되지만 위 아래를 적용되지 않음

#### spacing : margin vs padding

- margin : outside of border of box element
- padding : inside of border of box element

#### collapsing margin

자식 경계가 부모 경계와 같은 때 일어나는 현상. (배꼽이 배보다 커지는 현상)

이 현상을 이해하는 것보단, 그냥 적당히 display : flex을 이용하는 것이 생산적이라 니꼬 쌤이라 말함.

#### display : inline-block

block요소와 in-line요소의 특징을 모두 가질 수 있게 하는 속성.

즉, 크기와 높이를 가지면서, 옆에 다른 요소를 배치할 수 있음.

그러나, responsive-website를 지원하지 않아서 display : flex 를 이용한다.

#### display : flex

자식들이 어떻게 정렬될지를 결정하는 속성

2개의 축을 가진다.

main-axis, cross axis.

main-axis내의 정렬은 justify-content 속성을 이용,

cross-axis내의 정렬은 align-content 속성을 이용하면 된다.

다만 이 둘 축의 방향은 절대적인게 아니라 flex-direction : column이라 하면 가로세로가 반전된다.

#### postion : fix

말 그래도 스크롤해도 고정된 위치에 있도록 하는 속성

relative인 부모를 찾아 그 부모를 기준삼아 이동한다.

#### pseudo-selector

html의 상태를 보고 선택할 수 있게 하는 선택자.

focus-within : focused된 자식을 가진 부모 element

- :hover
- :active
- :focus
- :visited
- :focus-within

등이 있음. 그리고 부모 자식간의 관계로 선택할 수 있는 선택자도 있지만 이미 알고 있으므로 생략.

#### color

color는 #을 붙이고 16진수로 표현하거나, rgb 혹은 알파값을 가진 rgba 객체를 이용하면 됨

웹사이트의 색깔 추출은 확장 프로그램등을 이용.

#### transition

변화 : 어떤 상태에서 다른 상태로 가는 변화로, 애니매이션을 구현할 때 이용.

state가 없는 선택자에 붙여야 개발이 수월

#### transformation

변형 : box-element를 변화시키지 않고, 단순히 화면에서 변형해서 보여준다.

다른 요소에 영향을 미치지 않음

#### animation

@keyframe을 이용해서 세밀하게 조절하던가, 아니면 단순히 transition+transformation만 이용하던가.

#### media-query

오직 css만을 사용해서 사용자의 스크린 사이즈, 가로 세로 모드등을 알 수 있는 방법

#### .gitignore

notice git file that what we want to ignore in file-version controll

#### index.html

대부분의 웹서버는 deault로 index.html을 찾도록 되어 있다.

#### 단축키

vs code에서 !만 누르면 html format이 생성된다.

link:css하면 css파일을 쉽게 추가할 수 있다.

.nav>ul>li\*4>a 하면 개쩜

#### icon

아이콘은 직접 만들어도 되지만 웬만해서는 다른 사이트, font-aswesome에 가서 가져오자.

여기서 가져온 i 태그는 글자랑 똑같이 취급되어서 font-size 혹은 color 속성으로 조정해 줄 수 있다.

#### 자식 컨테이너 하나를 중심, 다른 하나를 끝에 놓는 법

1. 부모 요소 justify-content:center
2. 자식이 n개이면 자식 width : 100/n %
3. 자식:nth-child(중앙인덱스){display : flex; justify-content:center}
4. 자식:last-child{display:flexs; justify-content:flex-ends; align-items:center;}

#### reset.css

작업할 때 브라우저의 기본스타일을 없에고 작업하는게 건강에 좋음.

reset.css파일을 제공해주는 웹사이트가 있으니 이용할 것.

#### css file directory

css 파일관리는 보통 component의 스타일을 관리하는 파일, screen의 스타일을 관리하는 파일, 그리고 이 모든 것을 import하고 기본 설정들을 기입하는 style.css파일로 관리

#### form : action, method(post,get)

action : 어떤 페이지로 data를 보낼 것인가. 페이지가 이동한다.

method : get방식과 post방식 중 request방식 채택

#### box-sizing:box

css는 padding이 주어지면 width를 보존하기 위해서 오른쪽으로 box를 이동시킨다. (화면이 짤리게 되는 주범)

이런 행위를 하지 말라는 말

> padding을 주어도 box-size를 늘리지 말라!

#### making circle : border-radius

사각형을 원으로 만들기 위해서는 정사각형 변의 길이의 50%를 border-radius로 주면 된다.

#### ruler extension

클론 코딩할때 픽셀을 잴 수 있는 확장 프로그램을 사용해라.

width, height, margin, padding의 수치 측정에 이용

#### component

반복되는 것을 component화 하고, css의 component 폴더에서 style 관리하면 재사용성이 높아진다.

#### BEM naming

block, element, modifier로 분류해서 네이밍하는 방식. 존나 좋으니까 꼭 써라

#### multi-class

하나의 태그가 2개 이상의 class를 가질 수 있다. (id와 다르게)

그래서 modifier class를 이용해도 되고, 이를 이용해 다양한 속성을 부여할 수 있다.

#### CSS : Variable

놀랍게도 css에서도 변수를 이용할 수 있다.

이게 존나 신세계다. variable.css에서 관리하며 var()을 이용해 속성을 줄 수 있다.

#### select by parents

작업 규모가 커지면 tag로만 선택해서 속성을 부여해서 바꾸면, 원치 않은 tag들도 변경되게 된다. 따라서 parent combinator-selector를 이용해서 태그를 세밀하게 선택하자. 혹은 이준클래스를 가지게 할 수도 있다.

#### inline can't have margin

상술한 바와 같이 span같은 놈은 inline 속성을 지니고 있어 크기를 가지지 못하고, 따라서 위아래의 margin/padding들을 가지지 못한다.

이를 해결하려면 display:block해서 가로세로를 가질 수 있게 해야한다.

#### Do not use UPPERCASE in html

대문자는 디자인적 요소이기 때문에 html에서 대문자만 이루어진 글을 쓰고 싶으면, html에서는 그냥 소문자로 쓰고 css에서 text-transform : uppercase 하면 된다.

#### opacity

투명도를 지정하는 속성. 색상의 톤을 맞출 때 도움이 된다.

#### z-index

요소의 높낮이를 나타내는 속성, 배경색을 주고 다른 요소를 가려버릴 수 있다. (로딩화면 등에 이용)

#### border-top-left-radius

처럼 속성을 4사분면기준으로 따로 따로 설정할 수 있다.

#### flex : order

flex container's children elements have each order used in position order in parent.

이걸 직접 변경해주거나, 단순히 역순으로 배치하는 것이 목적이라면

flex-direction:row-reverse로 해줄 수도 있음.

> 요소의 순서를 바꾸는 것은 웬만해서는 html문서 순서를 건드리기 보다는 css에서 modifier을 이용하자.
>
> 이때 modifier에서는 위와 같은 방법 이용

#### loading-screen

여기서는 css만으로 로딩화면을 흉내내기 위해서

postion : flex두고

opactiy가 1에서 0으로 변하는 애니매이션을 추가했음.

참고로 클릭도 받지 못하게 visibiliy:hidder; 이용. distplay:hidden이면 클릭은 받는 상태.

그러나 두 경우 모두 단지 브라우저에서만 안보이는 것이고, html형태로 살아있음

#### will-change

브라우저에게 특정 태그가 바뀔테니 GPU를 이용해서 그 태그나 그 태그의 애니매이션을 정확히 계산하라 하는 것. 가끔씩 애니매이션이 이상하게 보일 때 적용하면 된다.

#### animation : fade in

아래서부터 차례로 등장하는 것

```css
@keyframes fadeIn {
  from {
    transform: translateY(10px);
    opacity: 0;
  }
  to {
    transform: none;
    opacity: 1;
  }
}

.tag {
  animation: fadeIn 1s linear;
}
```

이런 형식으로 이용하면 된다.

#### animation tip

focus-within을 이용하면 내부에 어떤 element가 focused되어 있을시의 animation 처리를 수월하게 할 수 있다.

크기를 키워도 되고,, whatever you what
