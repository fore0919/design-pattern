import time, asyncio, requests
from bs4 import BeautifulSoup

s = time.time()
results = []

#### 비동기식으로 웹사이트 크롤링 하기
async def getpage(url):
    req = await loop.run_in_executor(None,requests.get,url)
    html = req.text 
    soup = await loop.run_in_executor(None,BeautifulSoup,html,'lxml')

    return soup

async def main():
    urls = ["https://velog.io/@fore0919/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-K%EB%B2%88%EC%A7%B8-%EC%88%98-%EC%A0%95%EB%A0%AC-Python",
            "https://velog.io/@fore0919/TIL-WEB-TCPIP-%EA%B0%9C%EB%85%90-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0",
            "https://velog.io/@fore0919/TIL-Python-sleep-%ED%95%A8%EC%88%98",
            "https://velog.io/@fore0919/TIL-Middleware",
            "https://velog.io/@fore0919/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC-%EC%99%84%EC%A0%84-%ED%83%90%EC%83%89-Python"
            "https://velog.io/@fore0919/DB-Data-Type%EC%9E%90%EB%A3%8C%ED%98%95-MySQL"
            "https://velog.io/@fore0919/DB-SQL-Constaint-%EC%A0%9C%EC%95%BD-%EC%A1%B0%EA%B1%B4"]

    fts = [asyncio.ensure_future(getpage(u)) for u in urls]
    r = await asyncio.gather(*fts)
    global results
    results = r 

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close
e = time.time()

print (results)
print ("{0:.2f}초 걸렸습니다".format(e-s))