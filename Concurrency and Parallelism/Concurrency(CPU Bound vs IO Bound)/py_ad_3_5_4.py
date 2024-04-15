"""
Section 3
Concurrency, CPU Bound vs I/O Bound - I/O Bound(2) - Threading vs Asyncio vs Multiprocessing
Keyword - I/O Bound, asyncio
"""

import asyncio
import aiohttp
import time

# I/O Bound Asyncio 예제
# threading 보다 높은 코드 복잡도 -> async, await 적절하게 코딩


# 실행 함수1 (다운로드)
async def request_site(session, url):
    # 세션 확인
    # print(session)
    # print(session.headers)

    async with session.get(url) as response:
        print(f'Read Contents: {0}, from {1}'.format(response.content_length, url))


# 실행 함수2 (요청)
async def request_all_sites(urls):
    async with aiohttp.ClientSession() as session:
        # 작업 목록
        tasks = []
        for url in urls:
            # 태스크 목록 생성
            task = asyncio.ensure_future(request_site(session, url))
            tasks.append(task)

        # 태스크 확인
        # print(*tasks)
        # print(tasks)

        await asyncio.gather(*tasks, return_exceptions=True)


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
    # 파이썬 3.7 이상
    asyncio.run(request_all_sites(urls))
    # asyncio.get_event_loop().run_until_complete(request_all_sites(urls))

    # 실행 시간 종료
    duration = time.time() - start_time

    print()

    # 결과 출력
    print(f'Downloaded {len(urls)} sites in {duration} seconds')


if __name__ == '__main__':
    main()
