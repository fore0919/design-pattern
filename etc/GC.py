import sys
import gc

#### GC 모듈 사용
print(gc.get_count()) # (469, 9, 0)
print(gc.get_threshold()) # (700, 10, 10)

gc.set_threshold(800, 13, 10) # 수동으로 임계치 조절
print(gc.get_threshold()) # (800, 13, 10)

collected = gc.collect()
print(collected) # 0

#### 참조 횟수 출력

x = 'hello, world!'
print(sys.getrefcount(x))

list_ = [x]
print(sys.getrefcount(x))

dic = {'x': x }
print(sys.getrefcount(x))

string = x
print(sys.getrefcount(x))

#### 순환 참조

l = []
l.append(l)
del l

#### 수동 GC
collected = gc.collect()
print(collected)

####  현재 자신을 참조중인 오브젝트를 찾아내어 강제로 자신을 지우기.

def delete_me(obj):
    referrers = gc.get_referrers(obj)
    for referrer in referrers:
        if type(referrer) == dict:
            for key, value in referrer.items():
                if value is obj:
                    referrer[key] = None

def test():            
    class A:
        def __del__(self):
                print("deleted")

    class B:
        def __init__(self, obj): 
            self.obj = obj

    a = A()
    b = B(a)

    print("before : ", b.__dict__)
    delete_me(a)
    print("after : ", b.__dict__)
    print("ref count : ", sys.getrefcount(a))
    gc.collect()
    print("ref count : ", sys.getrefcount(a))
    del(a)

test()