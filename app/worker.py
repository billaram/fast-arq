import asyncio
from arq import create_pool
from arq.connections import RedisSettings
import os 
task_queue = None

REDIS_ARQ_HOST = os.getenv('REDIS_ARQ_HOST') or 'localhost'
REDIS_ARQ_PORT = os.getenv('REDIS_ARQ_PORT') or 6379

from arq.connections import RedisSettings
REDIS_ARQ_SETTINGS = RedisSettings(
    host=REDIS_ARQ_HOST,
    port=REDIS_ARQ_PORT
)

async def get_task_queue():
    global task_queue
    if task_queue is not None:
        return task_queue
    task_queue = await create_pool(REDIS_ARQ_SETTINGS)
    return task_queue

async def main():
    print('worker started')
    task_queue = get_task_queue()
    print('worker started', task_queue)

async def notifier(ctx, message, **kwargs):
    print("Sent Notification")

async def defered_runner(fn, *args, **kwargs):
    task_queue = await get_task_queue()
    print(defered_runner, *args)
    await task_queue.enqueue_job(fn, *args, **kwargs)

class WorkerSettings:
    functions = [notifier]
    redis_settings = REDIS_ARQ_SETTINGS

if __name__ == '__main__':
    asyncio.run(main())
    
