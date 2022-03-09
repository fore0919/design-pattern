import threading 
import time
import random

# GIL (Global Interpreter Lock) 
# 예제 1) 파이썬이 hread-safe 하지 않은 이유 알아보기 

x = 0 # 공유 값 선언
def foo(): 
    global x 
    for i in range(100000000): 
        x += 1 

def bar(): 
    global x 
    for i in range(100000000): 
        x -= 1 

# 결과는 0 으로 예상 되지만 엉뚱한 결과가 나온다.        
t1 = threading.Thread(target=foo) 
t2 = threading.Thread(target=bar) 

t1.start() 
t2.start() 

t1.join() 
t2.join() 

print(x)
# 첫번째 시도 결과 값 : -3780005
# 두번째 시도 결과 값 : -3517680
# 세번째 시도 결과 값 : 6957599


# # 예제2) 파이썬에서의 싱글스레딩과 멀티스레딩 비교
# def loop():
#     for i in range(500000000):
#         pass

# # Single Thread
# start = time.time()
# loop()
# loop()
# end = time.time()
# print('Single Thread : {}'.format(end - start))

# # Multi Thread
# start = time.time()
# thread1 = threading.Thread(target=loop)
# thread2 = threading.Thread(target=loop)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# end = time.time()
# print('Multi Thread : {}'.format(end - start))
# # 싱글스레드 결과 값 : 
# # 멀티스레드 결과 값 : 
######## 싱글 스레드가 빠르고 멀티스레드가 오래 걸릴 줄 알았는데 반대의 결과가 나왔다 ...


# 예제 3) sleep 매서드로 멀티스레드 성능개선 
def loop2():
    time.sleep(0.1)
    max([random.random() for i in range(10000000)])
    time.sleep(0.1)
    max([random.random() for i in range(10000000)])
    time.sleep(0.1)
    max([random.random() for i in range(10000000)])
    time.sleep(0.1)
    max([random.random() for i in range(10000000)])
    time.sleep(0.1)
    max([random.random() for i in range(10000000)])
    time.sleep(0.1)

# Single Thread
start = time.time()
loop2()
loop2()
end = time.time()
print('Single Thread: {}'.format(end - start))

# Multi Thread
start = time.time()
threads = []
for i in range(2):
    threads.append(threading.Thread(target=loop2))
    threads[-1].start()

for t in threads:
    t.join()

end = time.time()
print('Multi Thread : {}'.format(end - start))
# 싱글스레드 결과 값 : 9.312692880630493
# 멀티스레드 결과 값 : 7.911287069320679 -> 성능이 개선된 것을 알 수 있다


# 예제4) 
def sleep_for_2s():
    time.sleep(2)

# Single Thread
start = time.time()
sleep_for_2s()
sleep_for_2s()
end = time.time()
print('Single Thread: {}'.format(end - start))

# Multi Thread
start = time.time()
thread1 = threading.Thread(target=sleep_for_2s)
thread2 = threading.Thread(target=sleep_for_2s)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()
print('Multi Thread : {}'.format(end - start))
# 싱글스레드 결과 값 : 4.0100319385528564
# 멀티스레드 결과 값 : 2.005458354949951
