## 20210113 실습 리뷰

1. compreLab2.py

   - 수정 전

   ```python
   def mydict(**p):
       d = {}
       if p:
           d = {'my' + str(i): p[i] for i in p}
       return d
   print(mydict(a=1, b=2, c=3))
   print(mydict())
   print(mydict(교육='멀티캠퍼스', 현재='파이썬'))
   ```

   - 수정 후

     : `if p:` 구절은 가변 아규먼트의 전달이 1개 이상임을 보장해준다. 하지만 이 구절이 없다 해도, 가변 아규먼트가 없으면 그냥 빈 딕셔너리를 리턴한다. 따라서 생략 가능하다.

   ```python
   def mydict(**p):
       d = {'my' + str(i): p[i] for i in p}
       return d
   print(mydict(a=1, b=2, c=3))
   print(mydict())
   print(mydict(교육='멀티캠퍼스', 현재='파이썬'))
   ```

   

2. compreLab4.py

   - 수정 전

   ```python
   import random
   n = []
   for i in range(10):
       n.append(random.randint(0, 100))
   print(n)
   d = {i + 1: 'pass' if n[i] >= 60 else 'nopass' for i in range(10)}
   print(d)
   ```

   - 수정 후

     : for 반복문을 쓰지 않고 list comprehension을 이용하여 리스트를 생성하는 간단한 방법을 채용

   ```python
   import random
   n = [random.randint(0, 100) for i in range(10)]
   print(n)
   d = {i + 1: 'pass' if n[i] >= 60 else 'nopass' for i in range(10)}
   print(d)
   ```

   

3. strLab2.py

   - 수정 전

   ```python
   s6 = '891022-2473837'
   print('남자' if s6[7] == 1 or s6[7] == 3 else '여자')
   ```

   - 수정 후

     : s6는 숫자로 이루어진 문자열 데이터이므로 `==`기호 뒤에 따옴표를 붙여 `'1'`과 같이 표기해주어야 한다.
  
     참고로, `if s6[7] == '1' or '3'`과 같은 구문은 지원하지 않는다. `'3'` 자체로는 값을 가지고 있는 데이터여서 항상 TRUE 값을 반환한다. 따라서 if 구문은 무조건 수행된다.
   
   ```python
   s6 = '891022-2473837'
print('남자' if s6[7] == '1' or s6[7] == '3' else '여자')
   ```
   
   