# π Book Reviews Web PJT

<br>

__β μμ± μ λ³΄__

μ         μ : κΉμ§μ

λ         μ§ : 2022-09-02

ν        κ²½ : Windows 10 Pro

κ°λ°λκ΅¬ : Visual Studio Code, Google Chrome

μ¬μ© νλ μμν¬ : BootStrap,  Django 3.2+

<br>

β **νλ‘μ νΈ λͺ©ν**

μ±μ λν μ λ³΄λ€μ λ±λ‘ν  μ μμΌλ©°, λ±λ‘ ν μ λ³΄λ€μ μμ  λ° μ­μ κ° κ°λ₯ν νμ΄μ§

- λ°μν μΉ νμ΄μ§λ‘ κ΅¬νν  κ²
- BootStrapμ μ¬μ©ν΄ Front-end κΎΈλ―ΈκΈ°

<br>

---

<br>

## πΉ ν΄λ κ΅¬μ‘°

```
π books
   γ΄ π migrations
   γ΄ π templates
      γ΄ π books
        γ΄ π detail
        γ΄ π edit
        γ΄ π new
           γ΄ _title.html
           γ΄ ...
        γ΄ index.html
        γ΄ ...
   γ΄ urls.py
   γ΄ ...
π mypjt
   γ΄ settings.py
   γ΄ ...
```

<br>

μ μ§λ³΄μλ₯Ό μ½κ² νκΈ° μν΄ html page λ΄μ λ°κ³ , λνλΌ bookμ data fieldλ λͺ¨λ νμ ν΄λ, νμΌμ λ§λ€μ΄ `include` νλ λ°©μμ μ¬μ©νμλ€.

## πΉ κ΅¬ν κ²°κ³Ό

π₯ **<u>κ΅¬ν κ²°κ³Ό</u>**

<br>

<u>**Main Page**</u>

λ°μν μΉμ κ΅¬ννμ¬ νλ©΄μ΄ 992px μ΄μμΈ κ²½μ°μλ 4κ°μ©, κ·Έκ²λ³΄λ€ μμ λλ 2κ°μ© νλ©΄μ λνλλλ‘ νλ€.

μ²« νλ©΄μλ μ± νμ§μ μ λͺ©, νμ κ³Ό μΉ΄νκ³ λ¦¬λ₯Ό νμΈν  μ μλ€. μ±μ μ΄λ¦μ ν΄λ¦­νλ©΄ ν΄λΉ μ±μ Detail pageλ‘ μ΄λνκ² λλ€.

NEW BOOKμ λλ₯΄λ©΄ μλ‘μ΄ μ± μ λ³΄λ₯Ό λ±λ‘ ν  μ μλ€.

![image](https://user-images.githubusercontent.com/109324634/198100686-a2a46a9a-14dc-468f-b59d-a4bfc9d85896.png)

![image](https://user-images.githubusercontent.com/109324634/198100864-f9178146-f39f-4ee2-958c-9e9be4b58749.png)

<br>

**<u>New Page</u>**

μλ‘μ΄ μ±μ λ±λ‘ν  λ μ κ·Όνλ νμ΄μ§μ΄λ€. λ°μν μΉμ κ΅¬ννμ¬ μλ ₯μΉΈμ κΈΈμ΄κ° κ°μ λΉμ¨μ μ μ§νλλ‘ νμλ€.

![image](https://user-images.githubusercontent.com/109324634/198101270-8444f42e-5b1e-4123-95df-8b04e1315fe4.png)

![image](https://user-images.githubusercontent.com/109324634/198101503-e5f00222-5961-4f00-8b42-82d3d441f3cc.png)

![image](https://user-images.githubusercontent.com/109324634/198102214-07e14293-f89c-4665-96ea-831f9343186a.png)

μ¬μ©μλ μμ κ°μ΄ μ λ³΄λ₯Ό μλ ₯ν  μ μλ€. genreμ κ²½μ° `select` tagλ₯Ό μ¬μ©νμΌλ©°, μ¬μ©μλ λ―Έλ¦¬ μ ν΄μ Έμλ genreμ€μμ μ νμ ν  μ μλ€.

Submitμ λλ₯΄λ©΄ μ μ₯μ΄ λκ³ , backμ λλ₯΄λ©΄ main pageλ‘ λμκ°λ€.

SubmitμΌλ‘ μ±μ μ λ³΄λ₯Ό μ μ₯νλ©΄ λ°λ‘ ν΄λΉ μ±μ Detail pageλ‘ μ΄λνκ² λλ€.

<br>

**<u>Detail Page</u>**

detail page λν λ°μν μΉμ κ΅¬ννλ€.  νλ©΄μ΄ 992px μ΄μμΈ κ²½μ°μλ μ± νμ§μ μ λ³΄κ° λλν λνλκ³ , 992pxλ³΄λ€ μμ κ²½μ°μλ μ± νμ§ λ¨Όμ , λ°μ μ λ³΄κ° λνλλ€. 

detail pageμμ editμ λλ₯΄λ©΄ μμ μ ν  μ μκ³ , deleteλ₯Ό λλ₯΄λ©΄ μ± μ λ³΄κ° μ­μ λλ€.

![image](https://user-images.githubusercontent.com/109324634/198102599-5b67e891-2da6-4855-921c-8673813ef41d.png)

![image](https://user-images.githubusercontent.com/109324634/198103055-0fcc13c9-9c0f-414f-be83-6e7b250a0417.png)

<br>

**<u>Edit Page</u>**

μλ μ μ₯λμ΄ μμλ κ°λ€μ΄ defaultλ‘ λ³΄μ¬μ§λ©°, resetμ λλ₯΄λ©΄ μλ μ μ₯λμ΄ μλ κ°μ λΆλ¬μ¨λ€. μμ νκ³  μΆμ κ°μ μμ νκ³  submitμ λλ₯΄λ©΄ updateκ° μλ£λλ€.

![image](https://user-images.githubusercontent.com/109324634/198104077-ce75fb2d-6c59-4637-ba09-846d032e99ac.png)

<br>

---

## πΉ νκ³ 

- BootStrapκ³Ό Djangoλ₯Ό μ¬μ©ν΄ μ½κ² λ°μν μΉ νμ΄μ§λ₯Ό κ΅¬νν  μ μμλ€.
- Front-endμ μ μ§λ³΄μλ₯Ό μ½κ² νκΈ° μν΄μ dataλ³λ‘ νμ ν΄λ/νμΌμ μΈλΆν ν΄μ λλ λ°©μμ΄ μ’μλ€. μμΌλ‘ κ°λ°ν  λ μ΄ λ°©λ²μ μμ§μκ³  μ¬μ©ν΄μΌκ² λ€.
- modelμ dataλ₯Ό view.pyμμ μΌμΌν μ μ₯νμ§ λ§κ³ , model formμ μ¬μ©νλ λ°©μμΌλ‘ μμ ν΄ λ³Ό κ²μ΄λ€.
- νμ μ§μ  λ΄μ©μ λ±λ‘νλ κ²μ΄ μλ, APIλ₯Ό μ¬μ©ν΄μ μλμΌλ‘ μ λ³΄λ₯Ό λνλ΄λ κ²μΌλ‘ λ°μ  μν€κ³  μΆλ€.
