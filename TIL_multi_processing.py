import multiprocessing as mp
import time 

#### 기본 사용 
if __name__ == "__main__":
    processing = mp.current_process()
    print(processing.name) # MainProcess
    print(processing.pid) # 43496


start_time = time.time()
#### 카운트 시간 비교 
# def count(name):
#     for i in range(1, 50001):
#         print (name, ':', i)

# num_list = ['p1','p2','p3','p4']

# for num in num_list:
#     count(num)

# print (time.time() - start_time) # 1.4645321369171143


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


