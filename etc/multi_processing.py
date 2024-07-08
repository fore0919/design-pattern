import multiprocessing as mp
from multiprocessing import Process, Queue
import time 
import concurrent.futures

#### 기본 사용 
def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',)) # Process 객체를 생성하고, f 함수를 할당하고 그 인자로 ('bob',)를 넘긴다
    p.start() # start()매서드를 호출해서 spawn함
    p.join() # 프로세스가 완전히 끝나길 기다림


#### 프로세스 정보 얻기 
if __name__ == "__main__":
    processing = mp.current_process()
    print(processing.name) # MainProcess
    print(processing.pid) # 43496


#### 프로세스 스포닝 
def worker():
    print('SubProcess End!')

if __name__ == "__main__":
    p = mp.Process(name='SubProcess', target=worker) #process spawning
    p.start()


def worker2():
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)
    time.sleep(5)
    print('SubProcess End')

if __name__ == '__main__':
    proc = mp.current_process() # main process
    print(proc.name) 
    print(proc.pid)

    p = mp.Process(name='SubProcess', target=worker2)
    p.start()

    print('MainProcess End')


#### 함수에 인자 전달하기
def work3(value):
    pname = mp.current_process().name
    print(pname, value)

if __name__ == "__main__":
    p = mp.Process(name="Sub Process", target=work3, args=("hello",))
    p.start()
    p.join()
    print("Main Process")


#### 클래스안에 있는 함수에 인자 전달하기
class Worker:
    def __init__(self):
        pass 

    def run(self, value):
        pname = mp.current_process().name
        print(pname, value)


if __name__ == "__main__":
    w = Worker()
    p = mp.Process(name="Sub Process", target=w.run, args=("hello",))
    p.start()
    p.join()
    print("Main Process")


#### join을 사용 했을 때와 사용하지 않았을 때의 차이
#### 사용 했을 때 
def work4():
    print("Sub Process start")
    time.sleep(5) 
    print("Sub Process end")

if __name__ == "__main__":
    print("Main Process start")
    proc = mp.Process(name="Sub Process", target=work4)
    proc.start()
    proc.join() 
    print("Main Process end")
# 메인 프로세스가 서브 프로세스의 작업이 끝나길 기다림 


#### 사용하지 않았을 때
def work5():
    print("Sub Process start")
    time.sleep(5) 
    print("Sub Process end")

if __name__ == "__main__":
    print("Main Process start")
    proc = mp.Process(name="Sub Process", target=work5)
    proc.start() 
    print("Main Process end")


#### Queues 클래스 사용하기 
def queue(q):
    q.put([5, False, 'Queue'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=queue, args=(q,))
    p.start()
    print(q.get())
    p.join()
   

#### 카운트 시간 비교 
start_time = time.time()
def count(name):
    for i in range(1, 50001):
        print (name, ':', i)

num_list = ['p1','p2','p3','p4']

for num in num_list:
    count(num)

print (time.time() - start_time) # 1.4645321369171143


#### 멀티프로세싱을 이용한 카운트
def count2(name):
    for i in range(1,50001):
        print (name, ':', i)

num_list2 = ['p1','p2','p3','p4']

if __name__ == '__main__':
    pool = mp.Pool(processes=2) # 현재 시스템에서 사용할 프로세스 개수
    pool.map(count2, num_list2)
    pool.close()
    pool.join()

print (time.time() - start_time) # 1.2373881340026855


#### sleep을 이용한 비교 
def sleep():
    print ('sleeping 1 sec')
    time.sleep(1)
    print ('wake up')

if __name__ == '__main__':
    start_time = time.perf_counter() 
    # perf_counters는 함수를 호출하여 대기한 시간 포함하여 측정 
    # process_time은 실제로 연산하는데 걸린 시간만 측정
    for i in range(4):
        sleep()
    end_time = time.perf_counter()
    print (f"{round(end_time-start_time,2)} finished") # 4.01 finished


#### 멀티프로세싱 이용 
def sleep_mp():
    print('sleeping 1 sec')
    time.sleep(1)
    print('wake up')

if __name__ == '__main__':
    start_time = time.perf_counter()

    processes = [] # 프로세스를 담을 리스트 (초기화)
    for i in range(4): # for 루프를 돌며 프로세스를 만듬 
        p = mp.Process(target=sleep_mp) # 각 프로세스에 작업을 등록하기 # target 인자에 해당 프로세스가 해야할 작업(함수) 등록
        p.start()
        processes.append(p)

    for process in processes:
        process.join() # 프로세스가 끝날 때까지 다음 코드는 실행시키지 못하도록 각 프로세스마다 join 호출 

    end_time = time.perf_counter()
    print (f"{round(end_time-start_time,2)} finished") #  1.11 finished


#### concurrent 모듈 이용
def sleep_curr():
    print('sleeping 1 sec')
    time.sleep(1)
    return 'wake up' # 리턴값을 이용해 출력하기 위해 print 사용하지 않음 
 
if __name__ == '__main__':
 
    start_time = time.perf_counter()
 
    with concurrent.futures.ProcessPoolExecutor() as executor: # with문으로 ProcessPoolExecutor클래스의 인스턴스(excutor)만들어줌. 
        futures = [executor.submit(sleep_curr) for _ in range(4)] # submit을 이용해 프로세스 Pool에 작업 제출 ->future 객체 반환
 
    for future in futures:
        print(future.result()) # 작업 결과를 Future 객체의 result 메서드를 호출하여 얻음 
 
    end_time = time.perf_counter()
    print(f"{round(end_time-start_time,2)} finished") # 1.15 finished
