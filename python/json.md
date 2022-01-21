### JSON

#### JSON 파일이란?

 * JavaScript Object Notation의 약자로 JavaScript 언어의 자료형을 텍스트로 표현한 포맷
 *  키-값 쌍으로 이루어짐
 * 서로 다른 시스템간에 데이터를 교환하기에 좋고, 언어가 다르더라도 데이터를 교환하는데 용이하다는 장점

#### JSON 파일 다루기

``` python
import json
```

``` python
name_json = open('path', endcoding='UTF8')
name = json.load(name_json)
```

#### EXAMPLE

``` python
impoert json

# data/movie.json
movie_json = open('data/movie.json', encoding='UTF8')
movie = json.load(movie_json)
```



