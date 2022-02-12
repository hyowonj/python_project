'''
# 숫자열
# 숫자 (정수 int, 실수 float)
a = int(input())
b = int(input())
c = int(input())
print((a + b + c) / 3)
'''

'''
# 문자열
# 문자열의 연산
# 덧셈: 문자열 붙이기
# 곱셈: 문자열 반복
# 인덱싱: a[n], n은 0부터

# 슬라이싱: a[n:m:o], n: 시작, m: 끝, o = 오프셋
# 슬라이싱의 예:
a = 'Life is too short.'
print(a[:])
print(a[0:4])
print(a[12:17]
print(a[::-1])

# 포맷팅 (format): 형식 문자열
print("I am %d years old" % 6)
print("정수 = %d, 실수 = %f, 8진수 = %o, 16진수 = %x, 문자열 = %s"
     % (1, 1.0, 8, 16, "hello"))

# 주민등록번호
num = "881120-1068234"
year = num[:2]
month = num[2:4]
day = num[4:6]
gender = num[7]

if gender in ('1', '2'):
    year = '19' + year
else:
    year = '20' + year

if gender in ('1', '3'):
    gender = '남자'
else:
    gender = '여자'
print('%s년 %s월 %s일 %s' % (year, month, day, gender))
'''


'''
# 리스트
# list(), []
# 덧셈: 리스트 내용 붙이기 [] + []
# 곱셈: 리스트의 내용 반복
# 값 추가: append, insert
# 값 제거: del, pop, remove
# 정렬: sort, sorted
# 확장: extend == 리스트 덧셈
# 갯수 세기: len, count

a = [1, '2', '4', 1.0, [1, 2]]
a.remove(1)
del a[0]
a.pop()
print(a)

a = [1, 2, 3, 4, 5]
a.insert(2, 'hello')
print(a)

a = [1, 2, 3, 4, 5, 5, 5]
print(len(a), a.count(5))

# 역순 정렬:
a = [1, 2, 3, 4, 5]
# a.sort(reverse=True)
b = sorted(a, reverse=True)
print(b)
'''


'''
# 튜플 (값을 변경할 수 없는 리스트)
t1 = () # 비어 있는 튜플
t1 = (1,) # 값이 하나인 튜플
t3 = (1, 2) # 값이 두 개 이상 있는 튜플
t3 = 1, 2 # 값이 두 개 이상이면 괄호 생략 가능
# 인덱싱, 슬라이싱, 덧셈, 곱셈 가능

t = 1, 2
print(id(t))
t = t + (3, 4)
print(id(t)) 
'''


'''
# 딕셔너리 
# key 와 value 로 이루어진 타입
# key = immutable, value = mutable
# 값을 조회할 때 => d[key]
# 값을 변경할 때 => d[key] = value
# 값을 추가할 때 => d[new_key] = value
# 값을 삭제할 때 => del d[key]

d = {True: 'v', '3: '삼', (1, 2): '4'}
# 조회
print(d[True])
# 변경
d[3] = 'three'
# 추가
d['new'] = 'new value'
# 삭제
del d[(1, 2)]
print(d)
# Key 리스트 만들기 => list(d.keys())
# Value 리스트 만들기 => list(d.values())
# Key, Value 쌍 리스트 만들기 => list(d.items())
print(list(d.keys()))
print(list(d.values()))
print(list(d.items())
# 모든 아이템 삭제 => d.clear()
d.clear()
print(d)
'''

'''
# 집합(set)
# set(), {}
# 순서가 없다, 중복이 없다.
s = {1, 2, 3, 3, 3}
print(s)
# union(합집합), difference(차집합), interaction(교집합)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)
s3 = s1.difference(s2)
print(s3)
s3 = s1.interaction(s2)
print(s3)

# 중복제거, 오름차순 정렬
a = [3, 2, 1, 3, 4, 6, 7, 6, 6, 7]
b = list[set(a)]
b.sort()
print(b)
'''

'''
# 불(bool)
# 단 두 가지 값만 가진다. True, False
a = 1
b = 2
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a < b and a != b)
print(a > b or a == b)
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print(not(1 in [1, 2, 3]))
'''

'''
# 함수
# def 함수명(매개변수):
#    < 수행할 문장 >
#    < 수행할 문장 >...
# 매개변수가 여러 개일 때는? (*매개변수)
# 키위드 매개변수 (**매개변수)
# 결과값(return)은 항상 하나다.
# 매개변수에는 초기값을 지정할 수 있다.
# 변수의 범위(scope)는 한수 내에서만 유효하다
# 함수 밖의 변수를 함수 내에서 변경 가능하다. (global)
# 한줄 짜리 함수 작성 가능 (lambda)
# 함수는 자기 자신을 호출할 수 있다. (재귀(Recursive)함수라고 함) 재귀함수는 일반항을 구하는 것이 중요
'''

'''
# 클래스 class
# 클래스 - 자신만의 데이터 타입을 정의하는 것 
# 클래스는 붕어빵 틀, 데이터의 형식을 정의하고, 틀에서 나온 붕어빵은 실체가 된다.
# 클래스 -> 붕어빵 틀, 인스턴스(instance) -> 붕어빵
# class 클래스 이름:
#     < 클래스의 내용 >
#     < 클래스의 내용 >...
# 클래스는 자신의 인스턴스를 생성할 때 '생성자'라고 불리는 함수를 호출
# 클래스는 (inheritance)을 받을 수 있다
# class 클래스 이름(상속 받을 클래스 이름):
#     < ... >
# 클래스는 부모의 멤버 메소드(함수)를 재작성 할 수 있다(override)
# 클래스는 연산자의 기능을 재작성 할 수 있다(연산자 override)
'''
