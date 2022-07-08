# client.html 개념정리

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
