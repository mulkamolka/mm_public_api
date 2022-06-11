import json
from flask import Response
from timeit import time
from functools import wraps

def calc_time(func):
    """함수 실행 시간를 출력하는 함수"""
    def wrap_func(*args, **kwargs):
        start_time = time.time()
        val = func(*args, **kwargs)
        end_time = time.time()
        print('\n-------------')
        print('Function Name:', func.__name__)
        print('Response Time: %fs' % (end_time - start_time))
        print('-------------')
        return val
    return wrap_func

# def as_json(f):

#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         res = f(*args, **kwargs)
#         res = json.dumps(res, ensure_ascii=False).encode('utf8')
#         return Response(res, content_type='application/json; charset=utf-8')

#     return decorated_function

