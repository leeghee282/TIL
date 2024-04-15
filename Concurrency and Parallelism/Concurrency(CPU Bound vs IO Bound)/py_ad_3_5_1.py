"""
Section 3
Concurrency, CPU Bound vs I/O Bound - I/O Bound(2) - Threading vs Asyncio vs Multiprocessing
Keyword - I/O Bound, requests, threading
"""

import concurrent.futures
import threading
import requests
import time

# I/O Bound Threading 예제

# 각 스레드에 생성되는 객체(독립된 네임스페이스)
thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
    return thread_local.session


# 실행 함수1 (다운로드)
def request_site(url):
    # 세션 획득
    session = get_session()

    # 세션 확인
    # print(session)
    # print(session.headers)

    with session.get(url) as response:
        print(f'[Read Contents: {len(response.content)}, Status Code: {response.status_code} from {url}]')


# 실행 함수2 (요청)
def request_all_sites(urls):
    # 멀티 스레드 실행
    # 반드시 max_worker 개수 조절 후 session 객체 확인
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(request_site, urls)


def main():
    # 테스트 URLS
    urls = [
        'http://www.jython.org',
        'http://olympus.realpython.org/dice',
        'https://realpython.com'
    ] * 3

    # 실행 시간 측정
    start_time = time.time()

    # 실행
    request_all_sites(urls)

    # 실행 시간 종료
    duration = time.time() - start_time

    print()

    # 결과 출력
    print(f'Downloaded {len(urls)} sites in {duration} seconds')


if __name__ == '__main__':
    main()
