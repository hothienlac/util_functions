import time
from typing import Callable



def timing(f: Callable) -> None:

    def timing_wrapper(*args, **kw):
        print(f'Start function {f.__name__}, begin timing...')
        begin_time = time.time()
        result = f(*args, **kw)
        end_time = time.time()
        print(f'Finished function {f.__name__}, end timing...')
        print(f'Estimated elapsed time: {end_time - begin_time}')
        return result
    
    return timing_wrapper


