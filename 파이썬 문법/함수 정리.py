1.print 함수
    정의 : 값을 출력하는 함수
    사용방법 : print 뒤에 ()를 붙이고 ()안에 변수 이름이나 "", '' 안에 문자나 숫자를 써서 출력한다.

2.int() str() float() 함수
    정의 : int : 정수를 나타내는 함수 str : 문자를 나타내는 함수 float : 유리수를 나타내는 함수
    사용방법 : int + (), str + (), float + ()

3.인덱싱이란?
    어떤 문자나 숫자가 몇번째 칸에 있는지 새주는 함수

4. 슬라이싱
    정의 : 문자열이나 숫자를 거꾸로 뒤집는다.
    사용방법 : 변수이름[x:y:z] x부터 y까지 z씩 증가(단 x, y, z는 모두 숫자)

5.replace() 함수
    정의 : 문자열을 다루는 함수
    사용방법 : 변수이름.replace("x", "y") x를 y로 바꾼다.

6.split() 함수
    정의 : 지정한 값으로부터 띄어주는 함수
    사용방법 : (변수이름).split("띄어쓰기 기준")

7. %formatting 이란
    print 칸 안에 변수의 값을 넣어주기 위해 필요한 아이

8.format() 함수
    정의 : print 칸안에 변수의 값을 넣어주는 아이
    사용방법 : () 안에 들어갈 데이터를 format 함수 안에 넣기

9.f-string
    정의 : print"" 칸 안에 변수의 값을 넣어주는 애
    사용방법 : print( f"{변수이름}")

10.strip() rstrip() lstrip() 함수
    정의 : 공백을 제거해주는 함수
    사용방법 : 변수이름.strip

11.upper(), lower() 함수
    정의 : upper : 대문자로 변환 해주는 함수, lower : 소문자로 변환해주는 함수
    사용방법 : 변수이름.upper(), 변수이름.lower()

12.endswith(), startswith() 함수
    정의 : endswith : 끝나는 문자가 맞는지 확인해주는 함수, startswith : 시작하는 문자가 맞는지 확인해주는 함수
    사용방법 : 변수이름.endswith("끝나는 문자가 맞는지 확인할 문자"), 변수이름.startswith("시작하는 문자가 맞는지 확인할 문자")

13.리스트와 변수 차이
변수 : 저장 공간
리스트 : 여러개의 변수를 저장하는 공간

16.join 함수
    정의 : 리스트 내 항목을 합칠 때 사용
    사용방법 : 항목들 사이에 ""안에 들어간걸 추가한다.

17. \n, \t 제어문자
    정의 : \n : 줄바꿈 제어 문자      \t : 들여쓰기 제어 문자

18. 리스트를 오름차순/리스트를 내림차순
    오름차순 : 이름.sort()
    내림차순 : 이름.sort(reverse = True)


19.튜플을 리스트로 전환하는 방법
    list(튜플이름)

20. 리스트를 튜플로 전환하는 방법
    tuple(리스트 이름)

21. 튜플 언팩킹 이란
    정의 : 튜플의 묶여있는것을 푸는 것
    사용방법 : (이름)

22. 딕셔너리의 활용
    1. 딕셔너리 리스트 추가하는 방법 : 딕셔너리 안에 [이름이나 수]를 넣는다
    2. 딕셔너리의 키 만 출력하는 방법 : 딕셔너리 이름.keys()
    3. 딕셔너리의 값 만 출력하는 방법 : 딕셔너리 이름.vals()
    4. 두 개의 딕셔너리를 합치는 방법 : 딕셔너리 1 이름.update(딕셔너리 2 이름)
    5. [키] 튜플과 [값]튜플을 딕셔너리로 변환하는 방법 : dict(zip(키 이름, 값 이름 ))

23. if 활용
    정의:참, 혹은 거짓에 따라 반응하는 것
    사용방법 :if 논리 :
               참[코드]
            else:
               거짓[코드]


24. int
    정의 : 숫자변환함수
    사용방법 : 정수로 전환할 때 쓰인다

25. 배수구하는 방법
for 변수 in range(시작값, 끝값, 단위값):
    print(변수)

26. 홀수/ 짝수 구하는 방법
수%2==1  => 홀수
수%2==0  => 짝수