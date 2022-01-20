### 파이썬 챗봇



파이썬은

| 저장 | 조건 | 반복 |
| ---- | ---- | ---- |



1. 저장

   ```python
   a = 30
   b = '안녕'
   ```

   * `=`은 저장을 해주는 기호이다.
     * 변수에 넣어준다. 입력해준다. 저장해준다. 지정해준다.

   * `==`은 동일하다는 의미이다.

     * ex.

       * ```python
         a==3
         # a는 3이다. 3인가? 맞나?
         ```

2. 조건

   #### boolean 연산자

   | True (진실) | False (거짓) |
   | ----------- | ------------ |
   | 1           | 0            |

   `and / &`는 하나만 F여도 결과값이 `F`이다.

   `or / |`는 하나만 T여도 결과값이 `T`이다.

   

3. 반복

   * enumerate : 인덱스도 함께 뱉어주는

     * ```python
       # i는 인덱스, m은 리스트 안의 값이다!
       for i, m enumerate([리스트]):
       ```

       * 인덱스가 먼저 오고, 그 다음에 리스트 안에 있는 내용이 나온다.