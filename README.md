# 📚 Book Reviews Web PJT

<br>

__✔ 작성 정보__

제        작 : 김지원

날        짜 : 2022-09-02

환        경 : Windows 10 Pro

개발도구 : Visual Studio Code, Google Chrome

사용 프레임워크 : BootStrap,  Django 3.2+

<br>

✔ **프로젝트 목표**

책에 대한 정보들을 등록할 수 있으며, 등록 한 정보들은 수정 및 삭제가 가능한 페이지

- 반응형 웹 페이지로 구현할 것
- BootStrap을 사용해 Front-end 꾸미기

<br>

---

<br>

## 🔹 폴더 구조

```
📂 books
   ㄴ 📂 migrations
   ㄴ 📂 templates
      ㄴ 📂 books
        ㄴ 📂 detail
        ㄴ 📂 edit
        ㄴ 📂 new
           ㄴ _title.html
           ㄴ ...
        ㄴ index.html
        ㄴ ...
   ㄴ urls.py
   ㄴ ...
📂 mypjt
   ㄴ settings.py
   ㄴ ...
```

<br>

유지보수를 쉽게 하기 위해 html page 내에 받고, 나타낼 book의 data field는 모두 하위 폴더, 파일을 만들어 `include` 하는 방식을 사용하였다.

## 🔹 구현 결과

🖥 **<u>구현 결과</u>**

<br>

<u>**Main Page**</u>

반응형 웹을 구현하여 화면이 992px 이상인 경우에는 4개씩, 그것보다 작을 때는 2개씩 화면에 나타나도록 했다.

첫 화면에는 책 표지와 제목, 평점과 카테고리를 확인할 수 있다. 책의 이름을 클릭하면 해당 책의 Detail page로 이동하게 된다.

NEW BOOK을 누르면 새로운 책 정보를 등록 할 수 있다.

![image](https://user-images.githubusercontent.com/109324634/198100686-a2a46a9a-14dc-468f-b59d-a4bfc9d85896.png)

![image](https://user-images.githubusercontent.com/109324634/198100864-f9178146-f39f-4ee2-958c-9e9be4b58749.png)

<br>

**<u>New Page</u>**

새로운 책을 등록할 때 접근하는 페이지이다. 반응형 웹을 구현하여 입력칸의 길이가 같은 비율을 유지하도록 하였다.

![image](https://user-images.githubusercontent.com/109324634/198101270-8444f42e-5b1e-4123-95df-8b04e1315fe4.png)

![image](https://user-images.githubusercontent.com/109324634/198101503-e5f00222-5961-4f00-8b42-82d3d441f3cc.png)

![image](https://user-images.githubusercontent.com/109324634/198102214-07e14293-f89c-4665-96ea-831f9343186a.png)

사용자는 위와 같이 정보를 입력할 수 있다. genre의 경우 `select` tag를 사용했으며, 사용자는 미리 정해져있는 genre중에서 선택을 할 수 있다.

Submit을 누르면 저장이 되고, back을 누르면 main page로 돌아간다.

Submit으로 책의 정보를 저장하면 바로 해당 책의 Detail page로 이동하게 된다.

<br>

**<u>Detail Page</u>**

detail page 또한 반응형 웹을 구현했다.  화면이 992px 이상인 경우에는 책 표지와 정보가 나란히 나타나고, 992px보다 작은 경우에는 책 표지 먼저, 밑에 정보가 나타난다. 

detail page에서 edit을 누르면 수정을 할 수 있고, delete를 누르면 책 정보가 삭제된다.

![image](https://user-images.githubusercontent.com/109324634/198102599-5b67e891-2da6-4855-921c-8673813ef41d.png)

![image](https://user-images.githubusercontent.com/109324634/198103055-0fcc13c9-9c0f-414f-be83-6e7b250a0417.png)

<br>

**<u>Edit Page</u>**

원래 저장되어 있었던 값들이 default로 보여지며, reset을 누르면 원래 저장되어 있는 값을 불러온다. 수정하고 싶은 값을 수정하고 submit을 누르면 update가 완료된다.

![image](https://user-images.githubusercontent.com/109324634/198104077-ce75fb2d-6c59-4637-ba09-846d032e99ac.png)

<br>

---

## 🔹 회고

- BootStrap과 Django를 사용해 쉽게 반응형 웹 페이지를 구현할 수 있었다.
- Front-end의 유지보수를 쉽게 하기 위해서 data별로 하위 폴더/파일을 세분화 해서 나눈 방식이 좋았다. 앞으로 개발할 때 이 방법을 잊지않고 사용해야겠다.
- model의 data를 view.py에서 일일히 저장하지 말고, model form을 사용하는 방식으로 수정해 볼 것이다.
- 후에 직접 내용을 등록하는 것이 아닌, API를 사용해서 자동으로 정보를 나타내는 것으로 발전 시키고 싶다.
