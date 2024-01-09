---
categories:
  - React
---
# The Basic of React



## Why React?

React는 JS의 라이브러리이다.

interactive한 web을 더 쉽게 제작하기 위해 만들어졌다.

그렇다면 어떻게 더 쉽게 제작한다는 걸까?

간단한 코드를 통해서 알아보자.



HTML에 있는 태그에 이벤트 리스너를 달아서 간단한 이벤트를 처리하도록 하는 코드를 두 방법으로 작성해서 비교하자.

```js
<!DOCTYPE html>

<html>
    <body>
        <span>Total Clicks: 0</span>
        <button id="btn">Click me</button>
    </body>
    <script> 
        let counter = 0;
        const button=document.getElementById("btn");
        const span=document.querySelector("span");
        function handleClick(){
            counter++;
            span.innerHTML=`Total clicks: ${counter}`; 
        }
        button.addEventListener("click",handleClick);
    </script>
</html>
```

순수한 JS인 Vanilia JS로 작성한 코드이다. 

별로 길지도 않고 가독성도 나쁘지 않다... 고 생각하는가?

버튼 이벤트를 달기 위해서

1. HTML에 button을 만들고
2. JS에서 그걸 가져오고
3. event listener를 등록하고
4. 연산을 통해 다시 HTML파일을 갱신하는 것

이 모든 과정을 웹사이트에 필요한 수백, 수천가지의 이벤트들을 처리하기 위해 반복하는 것은 매우 소모적인 작업이다.

따라서 Facebook은 이 문제를 해결하기 위해서 React JS라는 존나 섹시한 놈을 만들었다. ~~페북만들때 어지간히 귀찮았나 보다~~



그렇다면 React JS로 만든 코드를 살펴보자.

```react
<!DOCTYPE html>

<html>
    <body id="root">

    </body>
    <script src="https://unpkg.com/react@17.0.2/umd/react.production.min.js"></script>
    <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
    <script src=https://unpkg.com/@babel/standalone/babel.min.js></script>
    <script type="text/babel">
              import { jsx as _jsx } from "react/jsx-runtime";
              import { jsxs as _jsxs } from "react/jsx-runtime";
              const root = document.getElementById("root");
              function Title() {
                return /*#__PURE__*/_jsx("h3", {
                  id: "title",
                  onMouseEnter: () => console.log("mouse enter"),
                  children: "Hello I'm a Title"
                });
              }
              const Button = () => /*#__PURE__*/_jsx("button", {
                style: {
                  backgroundColor: "tomato"
                },
                onClick: () => console.log("click"),
                children: "Click me"
              });
              const Container = () => /*#__PURE__*/_jsxs("div", {
                children: [/*#__PURE__*/_jsx(Title, {}), /*#__PURE__*/_jsx(Button, {})]
              });
              ReactDOM.render( /*#__PURE__*/_jsx(Container, {}), root);
    </script>
</html>


```

조금 복잡하다고 생각할 수는 있지만, 막성 필요없는 주석 부분 다 때어내고 보면 쉽다.

핵심은 HTML 태그에 HTML요소들을 배치하는 것이 아니라 React JS안에서 HTML태그들을 만들고, 속성들을 집어 넣어서 결과만을 HTML에 게시하는 것.  특히 이때 속성으로 event listener를 설정할 수 있어서 정~말 편하게 이벤트들을 처리 할 수 있게 된다.

이것은 매우 많은 이벤트들을 처리해야 하는 interactive한 website제작에 있어 React JS가 지니는 장점을 보여주기에 충분하다.



## React의 동작 방식

React JS와 React DOM이라는 것이 동작하며 React 작동하는데, React JS는 로직을 처리하는 엔진 같은 역할을 수행하고, React DOM은 그렇게 로직을 거친 결과인 react element를 HTML에 배치하는 역할을 한다.

ex) ReactDOM.render(target,place) : target을 place에 배치(lendering)한다.

이들을 include하기 위한 코드는 아래와 같다.

```js
 <script src="https://unpkg.com/react@17.0.2/umd/react.production.min.js"></script>
 <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
```



## JSX

JSX는 JS의 확장문법이다. JS에 추가적인 문법들을 포함시킨거라 보면 되는데, 위에 React JS로 쓴 코드를 보면, 편하긴 한데 어디까지나 JS 코드라는 것은 명확해 보인다. 그런데, 만일 JS안에서 아예 HTML과 유사한 문법을 사용해버리면 더 편하지 않을까? 

그래서 나온게 JSX이다. HTML과 유사해서 가독성이 더 좋다.

```react
<!DOCTYPE html>

<html>
    <body id="root">

    </body>
    <script src="https://unpkg.com/react@17.0.2/umd/react.production.min.js"></script>
    <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
    <script src=https://unpkg.com/@babel/standalone/babel.min.js></script>
    <script type="text/babel">
        const root=document.getElementById("root");
        function Title(){
            return(
                <h3 id="title" onMouseEnter={()=>console.log("mouse enter")}>
                Hello I'm a Title
                </h3>
            )
        }
            
        const Button=()=>(
            <button style={{backgroundColor:"tomato",}} onClick={()=>console.log("click")}>
            Click me
        </button>)
      
        const Container=()=>(
            <div>
                <Title/>
                <Button/>
            </div>
        )
       
        ReactDOM.render(<Container/>,root);
    </script>
</html>


```

마치 HTML의 생성자들을 만들고 Container에서 다시 이들의 생성자들을 호출하는 모습이 객체지향화된 HTML같아 보인다.



JSX의 문법에 대해 짧게만 알아보자.

1. component의 첫글자는 대문자로 써야 한다. 그렇지 않으면 일반적인 HTML태그로 인식한다.

   ```react
   const Button=()=>(
               <button style={{backgroundColor:"tomato",}} onClick={()=>console.log("click")}>
               Click me
           </button>)
    //이렇게 버튼을 내가 먼들고 이를 이용하려면
   <Button/> // 요렇게 써야지
   <button/> // 요렇게 쓰면 진짜 그 HTML의 버튼으로 인식된다.
   ```

2. 화살표 함수

   화살표 함수란 그냥 함수를 좀더 쉬운 방법으로 표현한건데, 사실 JSX코드에도 그냥 함수와 화살표 함수 두가지 방식으로 썼었다.

   ```react
   //일반적인 함수
   const Button(){ 
   	return(<button> Click me </button>)
   }
   //화살표 함수
   const Button=()=>(<button> Click me </button>)
   ```

   두개는 완전히 동일한 기능을 수행하지만, 조금이라도 타자를 적게 치기 위해 화살표 함수를 만들었다.

   

이렇게 편한 JSX는 아직 웹브로우저에서 지원하지 않으므로,  Babel이라는 일종의 컴파일러를 설치해야 한다.

```js
<script src=https://unpkg.com/@babel/standalone/babel.min.js></script>
```

그러면 Babel은 JSX문법으로 작성한 React 코드를 번역해서 React JS엔진에 가져다 주고, 그 결과를 React DOM이 HTML에 배치하여 사용자에게 보여준다.



# 정리

1. interactive한 website는 무수히 많은 이벤트들을 등록해야 한다.
2. 그건 존나 귀찮기 때문에 react가 탄생했고, jsx라는 것도 등장하면서 쉽고 빠른 개발이 가능해짐
3. Meta 매수하러 가야겠다.