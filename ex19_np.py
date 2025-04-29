import time
import numpy as np

def sum_np():
    list = np.arange(15_000_000, dtype=np.int64)
    total = np.sum(list)
    print('sum is:', total)

def sum_python():
    lista=list(range(15_000_000))

    total=0
    for i in lista:
        total +=1
    print('sum is: ', total)

start_d = time.time()
sum_python()
end_d = time.time()
print(end_d - start_d)

start_d = time.time()
sum_np()
end_d = time.time()
print(end_d - start_d)