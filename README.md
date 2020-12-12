# BookPlanner (BookMark) 📚
>+ <b>SW사관학교 정글에서의 첫 프로젝트. (Web)
>+ 함께 공유하는 북마크와 나만 볼 수 있는 북마크를 하나로 관리할 수 있도록 하는 툴</b>

--------------------------------------------------------------------------------
## 0. 계획세우기

### 와이어프레임
<img src="https://user-images.githubusercontent.com/26760693/101716973-c0b3e600-3ae1-11eb-9074-9179ee12ae57.png"  width="150" height="225">  <img src="https://user-images.githubusercontent.com/26760693/101716974-c1e51300-3ae1-11eb-8ebe-6451cb7f9668.png"  width="150" height="225">  <img src="https://user-images.githubusercontent.com/26760693/101716976-c1e51300-3ae1-11eb-9613-4b227be056c8.png"  width="150" height="225">  <img src="https://user-images.githubusercontent.com/26760693/101716977-c27da980-3ae1-11eb-85b5-7bd3b3c1ed88.png"  width="150" height="225">  <img src="https://user-images.githubusercontent.com/26760693/101716979-c3164000-3ae1-11eb-9fd2-8143d4a59266.png"  width="150" height="225">  

### 파일관리 (GIT)
1. Git을 통해 Organization group을 생성
2. 이곳을 master branch로 설정
3. 각자의 개인 repository에 fork.
4. 개인 개발
5. 개인 branch(main) 에서 upstream(master)으로 pull request 
6. upstream에서 개인 branch(main)으로 merge하여 프로젝트를 진행

### DB table 설계
* [DB 구상](https://github.com/BookPlanner/BookPlanner/blob/main/resources/db%20table%20%EA%B5%AC%EC%83%81)

## 1. TODO

### 서버
* aws 연동
* app.py url설정 
* 컨텐츠 생성(C)
* 컨텐츠 불러오기(R)
* 컨텐츠 수정(U)
* 컨텐츠 삭제(D)
* 로그인 구현 (쿠키/세션)
* 회원가입 (쿠키/세션)
* DB-server 연결

### 클라이언트
* 홈 ui
* 로그인/회원가입 ui
* 메인 ui
* 모달 ui
* jinja 템플릿엔진이 무엇인지, 왜 사용하는지
* 서버사이드렌더링이 무엇인지, 왜 사용하는지

## 2. ISSUE
- ['Check'](https://github.com/BookPlanner/BookPlanner/blob/main/resources/Want) List  
  
| 분류 | 내용 | 상태 |
|---|:---:|---:|
| 클라이언트,서버 | sorting 기능 추가 | ✔ |
| 서버 | 수정 기능 추가 | ❌ |
| DB | dummy data 생성 | ✔ |
| 클라이언트 | Popovers, tooltips 등 이용하여 책이미지 넣기 | ❌ |
| 클라이언트 | 추가 및 수정 modal 이후, refresh | ✔ |
| 서버 | 가입 시, 비밀번호 암호 수준 올리기 | ✔ |
| 서버  | jinja2 이용하여 content 생성 | ✔ |
| 클라이언트 | 중요도에 따른 Tag 넣기(Bulma)  | ✔ |
| 서버 | CRUD 처리 할수있는 템플릿 생성 | ✔ |
| 서버 | 로그인/로그아웃(쿠키와 세션) | ✔ |
| | |

## 3. 실행화면
![ezgif com-gif-maker](https://user-images.githubusercontent.com/61036124/101969290-f6360c00-3c66-11eb-9c6e-a039e62317ee.gif)
