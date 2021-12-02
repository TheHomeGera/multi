from hashlib import md5
from random import choice
import time
import concurrent.futures

start_time = time.time()
workers_count = 61
with concurrent.futures.ProcessPoolExecutor(max_workers=workers_count) as executor:
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            print(s, h)
            break
end_time = time.time()
print(end_time - start_time)
