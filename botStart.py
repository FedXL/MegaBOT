from aiogram.utils import executor
from create_bot import dp
from utils.exchange import get_exchange
async def on_startup(_):
    print("Бот вышел в онлайн")



if __name__ == "__main__":
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup
                           )

    eur, usd = get_exchange()