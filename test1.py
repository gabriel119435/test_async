import time, asyncio, threading, logging
from functools import wraps, partial
from datetime import datetime
from newclass import NewClass
logging.basicConfig(level = logging.INFO,format='%(asctime)s %(levelname)s - %(message)s')

# https://stackoverflow.com/a/50450553/3026886
# https://github.com/yifeikong/aioify/blob/master/aioify/__init__.py#L19 same logic
def to_async(func):
    @wraps(func)
    async def run(*args, **kwargs):
        # using the get_running_loop() function is preferred to get_event_loop() in coroutines
        # https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.get_event_loop

        # The default executor is used if executor is None.
        # https://stackoverflow.com/a/60204208/3026886

        # This default value preserves at least 5 workers for I/O bound tasks.
        # https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
        return await asyncio.get_running_loop().run_in_executor(None, partial(func, *args, **kwargs))
    return run

def thread_id():
    return str(threading.get_ident())[-5:]

same_instance = NewClass()

@to_async
def sync_wait(info):
    same_instance.wait_from_newclass(info)


async def producer(n, queue):
    i = 1
    while True:
        info = f'{n}pro msg {i}' 
        logging.info(f'{info} thread {thread_id()}')
        await sync_wait(info)
        await queue.put(i)
        i+=1

async def consumer(n, queue):
    while True:
        i = await queue.get()
        info = f'{n}con msg {i}'
        await sync_wait(info)

async def main():
    # asyncio queues are not thread-safe, they are designed to be used specifically in async/await code
    # https://docs.python.org/3/library/asyncio-queue.html
    queue = queue = asyncio.Queue(10)
    producers = [producer(n+1, queue) for n in range(3)]
    consumers = [consumer(n+1, queue) for n in range(3)]
    # Run awaitable objects in the aws sequence concurrently.
    # https://docs.python.org/3/library/asyncio-task.html#asyncio.gather
    await asyncio.gather(*(producers + consumers))

# https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.get_event_loop
# Consider also using the asyncio.run() function instead of using lower level functions to manually create and close an event loop.
asyncio.run(main())

'''
example output (split manually by time):

2022-03-09 14:47:07,164 INFO - 1pro msg 1 thread 69088
2022-03-09 14:47:07,166 INFO - 1pro msg 1 thread 32000 instance 10320 waiting
2022-03-09 14:47:07,166 INFO - 2pro msg 1 thread 69088
2022-03-09 14:47:07,166 INFO - 2pro msg 1 thread 39296 instance 10320 waiting
2022-03-09 14:47:07,166 INFO - 3pro msg 1 thread 69088
2022-03-09 14:47:07,166 INFO - 3pro msg 1 thread 46592 instance 10320 waiting

2022-03-09 14:47:10,170 INFO - 1pro msg 2 thread 69088
2022-03-09 14:47:10,171 INFO - 2pro msg 2 thread 69088
2022-03-09 14:47:10,172 INFO - 1pro msg 2 thread 39296 instance 10320 waiting
2022-03-09 14:47:10,172 INFO - 2pro msg 2 thread 32000 instance 10320 waiting
2022-03-09 14:47:10,173 INFO - 3pro msg 2 thread 69088
2022-03-09 14:47:10,174 INFO - 1con msg 1 thread 46592 instance 10320 waiting
2022-03-09 14:47:10,175 INFO - 2con msg 1 thread 61184 instance 10320 waiting
2022-03-09 14:47:10,175 INFO - 3pro msg 2 thread 53888 instance 10320 waiting
2022-03-09 14:47:10,176 INFO - 3con msg 1 thread 68480 instance 10320 waiting

2022-03-09 14:47:13,175 INFO - 2pro msg 3 thread 69088
2022-03-09 14:47:13,175 INFO - 2pro msg 3 thread 39296 instance 10320 waiting
2022-03-09 14:47:13,176 INFO - 1pro msg 3 thread 69088
2022-03-09 14:47:13,177 INFO - 1pro msg 3 thread 32000 instance 10320 waiting
2022-03-09 14:47:13,177 INFO - 2con msg 2 thread 61184 instance 10320 waiting
2022-03-09 14:47:13,179 INFO - 3pro msg 3 thread 69088
2022-03-09 14:47:13,180 INFO - 1con msg 2 thread 46592 instance 10320 waiting
2022-03-09 14:47:13,180 INFO - 3pro msg 3 thread 53888 instance 10320 waiting
2022-03-09 14:47:13,181 INFO - 3con msg 2 thread 68480 instance 10320 waiting
'''