# client.html에서 새로 알게된 개념 정리

## client_style.css
client_( ).css 파일이 세 개이므로 모두 모아놓은 하나의 파일
html에서 css를 연결할 때 하나로 불러옴
```html
<link rel="sylesheet" href="./css/client_style.css">
```

</br>

## Bootstrap : 반응형 웹사이트
### Bootstrap : Grid
```html
<div class="col-12">
  <p>박스 1</p>
</div>
<div class="col-6">
  <p>박스 2</p>
</div>
```
col-12 / col-6</br>
페이지를 12등분 나눠서 col-12는 페이지 전체를 차지,</br>
col-6은 페이지의 6등분(반)을 차지함

### Bootstrap_CSS 사용
1. https://getbootstrap.com/ 접속
2. BootStrap > introduction > CSS 링크 복사
```html
<link rel="stylesheet" href="[bootstrap css 링크]">
```

`=> 나머지 Bootstrap 설명은 블로그에!`

## keyframes & animation [CSS]
### @keyframes
: CSS 애니메이션에서 구간을 정하고 각 구간별로 어떤 스타일을 적용시킬지 정하는 문법

`@keyframes 사용 시 필요한 3가지`
1. animaion-name : @keyframes 가 적용될 사용자가 지정하는 이름
2. 스테이지 : from-to 로 0~100%의 구간
3. CSS 스타일 : 각 스테이지(구간)에 적용시킬 스타일

```css
/*fadeIn : 화면 들어갈 때*/
@keyframes fadeIn{
    from {opacity: 0;}
    to {opacity: 1;}
}

/*fadeOut : 화면 나올 때*/
@keyframes fadeOut{
    from {opacity: 1;}
    to {opacity: 0;}
}
```

### animation
: 애니메이션에 이름을 지정하거나 지속시간, 속도 조절 등을 지정할 수 있는 속성을 가지고 있음

`animation 속성`
- animation-name : @keyframes 이름 (fadeIn, fadeOut 과 같은)
- animation-duratuion : 타임 프레인의 길이, 키프레임이 동작하는 시간 설정
- animation-timing-function : 애니메이션 속도 조절
- animation-delay : 애니메이션을 시작하기 전 지연시간 설정
- animation-iteration-count : 반복 횟수
- animation-direction : 반복 방향 (정방향/역방향/번갈아가며 반복)
- animation-fill-mode : 애니메이션 시작 / 끝 상태 제어 (none/forwords/backwords/both)

```js
function start(){
  main.style.animation = "fadeOut 1s";
  qna.style.animation = "fadeIn 1s";
  
  main.style.display="none";
  main.style.display="block";
}
```
이렇게 하면 애니메이션 적용이 제대로 되지 않는다!</br>
display가 animation의 1s를 기다려주지 않고 실행되기 때문!</br>
</br>
이때 필요한 함수가 바로 `setTimeout()` 이다

### setTimeout()
: 코드를 바로 실행하지 않고 일정시간 기다린 후 실행시키는 함수

- 첫번째 인자 : 실행할 코드를 담고 있는 함수
- 두번째 인자 : 지연시간(ms)

```js
function start(){
  main.style.animation = "fadeOut 1s";
  setTimeout(()=>{
    qna.style.animation = "fadeIn 1s";
    setTimeout(()=>{
        main.style.display="none";
        main.style.display="block";
    },450);
  },450);
}
```
