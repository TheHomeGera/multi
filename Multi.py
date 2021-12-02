import concurrent.futures
import time
from urllib.request import Request, urlopen


def check_link(link):
    try:
        request = Request(
            link,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        response = urlopen(request, timeout=5)
        code = response.code
        print(code)
        response.close()
    except Exception as e:
        print("Exception occurred. URL: ", link, "Exception:", e)


links = open('res.txt', encoding='utf8').read().split('\n')
workers_count = 100
start_time = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=workers_count) as executor:
    future_to_url = {executor.submit(check_link, link): link for link in links}
    for future in concurrent.futures.as_completed(future_to_url):
        link = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (link, exc))
end_time = time.time()
print(str(end_time - start_time))
