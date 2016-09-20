import os
import re
import time
import asyncio
from aiohttp import ClientSession
from pyquery import PyQuery as q



headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2431.0 Safari/537.36"}
async def down(url):
    async with ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            response = await response.text()
            response = q(response)
            print('小爬爬正在努力爬取中......')
            link = response('a').filter('.view_img_link')
            pic = re.findall(r'http.+?(?=")',str(link))
            for i in pic:
                f.write(i+'\n')

if __name__ == '__main__':
    if not os.path.exists('picture'):
        os.mkdir('picture')
    f = open('picture.txt','w')
    start = time.clock()
    loop = asyncio.get_event_loop()
    tasks = []
    url = 'http://jandan.net/pic/page-{}{}'
    for i in range(1,1910):
        task = asyncio.ensure_future(down(url.format(i,'#comments')))
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    f.close()
    end = time.clock()
    print('read: %f s' % (end - start))
