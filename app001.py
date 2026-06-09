import numpy as np

# 1. numpy 배열 생성
py_list = [1, 2, 3, 4, 5]
print(f'py_list: {py_list}')

np_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f'np_arr: {np_arr}')
print(f'np_arr type: {type(np_arr)}')

# n차원 numpy 배열 생성
# 2차원 numpy 배열
np_arr = np.array(
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 0]
    ])
print(f'np_arr: \n{np_arr}')
print(f'np_arr type: {type(np_arr)}') 
print(np_arr[1][3]) # 9

for idx, arr in enumerate(np_arr):
    print(f'idx: {idx}')
    for num in arr:
        print(f'num: {num}')

# 3차원 배열
np_arr = np.array(
    [
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 0]
        ],
        [
            [10, 20, 30, 40, 50],
            [60, 70, 80, 90, 100]
        ],
        [
            [100, 200, 300, 400, 500],
            [600, 700, 800, 900, 1000]
        ]
    ]
)

for arr1th in np_arr:
    for arr2th in arr1th:
        for arr3th in arr2th:
            print(f'arr3th: {arr3th}')

# numpy 복사
np_arr = np.array([1, 2, 3, 4, 5])
print(f'np_arr: {np_arr}')

np_arr_copy = np_arr.copy()                 # 깊은 복사

print(np_arr is np_arr_copy)                # 메모리 주소 비교: False
print(np.array_equal(np_arr, np_arr_copy))  # 값 자체를 비교: True
print(np_arr == np_arr_copy)                # 원소(item) 마다 비교 [True, True, True, True, True]

# numpy 배열 연산
np_arr = np.array([10, 20, 30, 40, 50])
print(f'np_arr: {np_arr}')

print(f'np_arr + 10: {np_arr + 10}') # [20 30 40 50 60]
print(f'np_arr - 10: {np_arr - 10}') # [ 0 10 20 30 40]
print(f'np_arr * 5: {np_arr * 5}') # [ 50 100 150 200 250]
print(f'np_arr / 10: {np_arr / 10}') # [1. 2. 3. 4. 5.] # 실수타입으로 나온다
print(f'np_arr % 10: {np_arr % 10}') # [0 0 0 0 0]
print(f'np_arr // 10: {np_arr // 10}') # [1 2 3 4 5]

# numpy 배열 속성 확인
# 1. 배열 원소 데이터 타입(dtype) 설정
np_arr = np.array([1, 2, 3], dtype=float)
print(f'np_arr: {np_arr}')

np_arr = np_arr.astype(np.int64)
print(f'np_arr: {np_arr}')              # [1 2 3]
print(f'np_arr_type: {type(np_arr)}')   # numpy.ndarray

# 2. numpy 배열 속성(차원, 형태, 데이터타입) 확인
np_arr = np.array(
    [
        [1., 2., 3., 4., 5.],
        [10, 20, 30, 40, 50],   
        [100, 200, 300, 400, 500],   
    ]
)

# 배열 차원
print(f'차원: {np_arr.ndim}')   # 2


# 배열 형태
print(f'형태: {np_arr.shape}')  # (3, 5)


# 배열 데이터타입
print(f'데이터 타입: {np_arr.dtype}')   # float64  정수와 실수가 만나면 실수가 나온다

# 모든 원소가 X인 배열 만들기
# 1. ones() & ones_like()
np_arr = np.ones((3, 5), dtype=int)
print(f'np_arr: {np_arr}')
'''
[[1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]]
 '''

py_list = [1, 2, 3]
np_arr = np.ones_like(py_list, dtype=float)
print(f'np_arr: {np_arr}')
'''
[1. 1. 1.]
'''

py_list = [[1, 2, 3], [4, 5, 6]]
np_arr = np.ones_like(py_list, dtype=float)
print(f'np_arr: {np_arr}')
'''
[[1. 1. 1.]
 [1. 1. 1.]]
 '''

# 2. zeros() & zeros_like()
# 모든 원소가 0인 배열 만들기
np_arr = np.zeros((3, 5), dtype=int)
print(f'np_arr: {np_arr}')
'''
[[0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]]
 '''

py_list = [1, 2, 3]
np_arr = np.zeros_like(py_list, dtype=int)
print(f'np_arr: {np_arr}')
'''
[0 0 0]
'''

py_list = [[1, 2, 3], [4, 5, 6]]
np_arr = np.zeros_like(py_list, dtype=int)
print(f'np_arr: {np_arr}')
'''
[[0 0 0]
 [0 0 0]]
 '''

# 3. empty() & empty_like()
np_arr = np.empty((3, 5), dtype=int)
print(f'np_arr: {np_arr}')
'''
[[0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]]
'''

py_list = [1, 2, 3]
np_arr = np.empty_like(py_list, dtype=int)
print(f'np_arr: {np_arr}')
'''
[1 2 3]
'''


# zerros_like
# ones
# ones_like