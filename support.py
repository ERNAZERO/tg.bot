from bot import bot as bot1
import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

# Создание экземпляров бота и диспетчера
bot = bot1
dp = Dispatcher(bot)

# ID пользователя, которому будут перенаправляться сообщения
forward_user_id = 1115405384


# Обработчик входящих сообщений от пользователя
async def user_message(message: types.Message):
    # Перенаправление сообщения пользователю с указанным ID
    forwarded_message = await bot.forward_message(chat_id=forward_user_id,
                                                  from_chat_id=message.chat.id,
                                                  message_id=message.message_id)
    await bot.send_message(chat_id=message.chat.id,
                           text='Ваше сообщение отправлено.')

    # Ожидание ответа от пользователя с указанным ID
    response = await bot.wait_for(types.Message, chat_id=forward_user_id)

    # Перенаправление ответа пользователя обратно пользователю
    await bot.send_message(chat_id=message.chat.id,
                           text=response.text)


# async def main():
#     await dp.start_polling()


# # Запуск бота
# if __name__ == '__main__':
#     asyncio.run(main())
