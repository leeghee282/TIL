"""
Section 3
Concurrency, CPU Bound vs I/O Bound - I/O Bound(2) - Threading vs Asyncio vs Multiprocessing
Keyword - I/O Bound, requests, threading
"""

import multiprocessing
import requests
import time

# I/O Bound Multiprocessing Pool 예제

# 각 프로세스 메모리 영역에 생성되는 객체(독립적)
# 함수 실행 할 때마다 객체 생성은 좋지 않음 -> 각 프로세스마다 할당
session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


# 실행 함수1 (다운로드)
def request_site(url):
    # 세션 확인
    # print(session)
    # print(session.headers)

    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f'[{name} -> Read Contents: {len(response.content)}, Status Code: {response.status_code} from {url}]')


# 실행 함수2 (요청)
def request_all_sites(urls):
    # 멀티 프로세싱 실행
    # 반드시 processes 개수 조절 후 session 객체 및 실행 시간 확인
    with multiprocessing.Pool(initializer=set_global_session, processes=4) as pool:
        pool.map(request_site, urls)


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
