
from app.worker import defered_runner

async def send_notification(message):
    await defered_runner('notifier', message)