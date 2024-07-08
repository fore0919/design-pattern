#### map함수
#### 리스트에 +1 씩한 새로운 리스트 반환
my_list = [1,2,3,4]
result_for = []
result_map = []

# for문 사용
for number in my_list:
	result_for.append(number+1)
    
# map함수 사용
def add(number):
	return number + 1
result_map = list(map(add, my_list))

print(result_for) #[2,3,4,5]
print(result_map) #[2,3,4,5]

#### 리스트의 모든 요소 정수로 변환
arr_for = [1.2, 2.3, 3.4, 4.5]
arr_map = [1.2, 2.3, 3.4, 4.5]

# for문
for i in range(len(arr_for)):
	arr_for[i] = int(arr_for[i])

# map함수
arr_map = list(map(int, arr_map))

print (arr_for) # [1,2,3,4]
print (arr_map) # [1,2,3,4]

#### 리스트의 5제곱 구하기 
def func_pow(num):
    return pow(num,5)
result_pow = list(map(func_pow, my_list))
print (result_pow)



#### 람다 함수 
#### def키워드이용
def add2(x,y):
	return x+y
print (add2(10,20)) # 30

#### 람다 사용
n = (lambda x,y:x+y)(10,20)
print (n) # 30

#### 람다함수와 map함수 함께 사용 (제곱)
print (list(map(lambda x: x ** 2, range(5))))

#### 문자열 길이의 공백 무시하고 정렬 
def my_key(string):
     return len(string.strip())
target = ['  cats ', ' tiger ', '    dog', 'snake   ']
print(sorted(target, key=my_key))

#### 람다 사용
target = ['  cats ', ' tiger ', '    dog', 'snake   ']
print(sorted(target, key=lambda x : len(x.strip())))



#### 리스트 컴프리헨션
# 수식 적용
[i*10 for i in range(5)] # [0,10,20,30,40]

# 함수 적용
def test(x):
    x = str(x)+'a'
    return x
 
[test(i) for i in range(5)] # [0a,1a,2a,3a,4a]

# 조건문 
# 오른쪽에 if문 사용
[i for i in range(5) if i%2==0]

# 왼쪽에 if문 사용(else 같이 사용)
[i if i%2==0 else 'odd' for i in range(5)]

# 이중 포문
# 리스트 생성 후 이중 for문
li=[]
for i in range(2):
    for j in range(3):
        li.append((i,j))
        
# 리스트 컴프리핸션 
[(i,j) for i in range(2) for j in range(3)]
# [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2)]
