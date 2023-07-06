import sqlite3
import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Создание экземпляров бота и диспетчера
bot = Bot(token='6130355398:AAE3xEdR7kRPUOaaIeoGB6DjG3W1GQBQTH8')
dp = Dispatcher(bot)


# Callback-функция для обработки нажатий на кнопки
async def button_callback_handler(query: types.CallbackQuery):
    button_text = query.data

    if button_text == 'call_phone':
        phone = '+996508145050'
        await query.message.answer_contact(phone, first_name='Softech')

    if button_text == 'discounts':
        await show_discount_item_info(query.message, button_text)
    
    if button_text == 'maps':
        latitude = 42.87526958560487 
        longitude = 74.58539928084825  
        await bot.send_location(chat_id=1115405384, latitude=latitude, longitude=longitude)

        
    
    if button_text == 'smartphones':
        await query.message.answer(text='Выберите бренд смартфона:',
                                   reply_markup=generate_brand_keyboard())

    elif button_text =='iphone':
        await show_iphone_model_info(query.message, button_text)

    elif button_text =='nothing_phone':
        await show_nothin_phone_model_info(query.message, button_text)

    elif button_text == 'xiaomi':
         await show_xiaomi_phone_model_info(query.message, button_text)

    
    
    # Ответить на callback-запрос, чтобы убрать уведомление
    await query.answer()






# Функция для генерации клавиатуры с брендами смартфонов
def generate_brand_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(InlineKeyboardButton(text='iphone 🍏', callback_data='iphone'),
                 InlineKeyboardButton(text='Xiaomi', callback_data='xiaomi'),
                 InlineKeyboardButton(text='Realme', callback_data='realme'),
                 InlineKeyboardButton(text='Nothing', callback_data='nothing_phone'))

    return keyboard


# Функция для отображения информации о модели
async def show_iphone_model_info(message: types.Message, brand):
    conn = sqlite3.connect('softech_database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT model, context, price, link, img FROM iphone")
    models = cursor.fetchall()

    for model in models:
        model_name = model[0]
        model_context = model[1]
        model_price = model[2]
        model_link = model[3]
        model_img = model[4]

        await message.answer_photo(model_img)
        await message.answer(text=f'Модель: {model_name}\n'
                                  f'Описание: {model_context}\n'
                                  f'Цена: {model_price}\n',
                             reply_markup=generate_link_button(model_link))

    conn.close()


async def show_xiaomi_phone_model_info(message: types.Message, brand):
    conn = sqlite3.connect('softech_database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT model, context, price, link, img FROM xiaomi")
    models = cursor.fetchall()

    for model in models:
        model_name = model[0]
        model_context = model[1]
        model_price = model[2]
        model_link = model[3]
        model_img = model[4]

        await message.answer_photo(model_img)
        await message.answer(text=f'Модель: {model_name}\n'
                                  f'Описание: {model_context}\n'
                                  f'Цена: {model_price}\n',
                             reply_markup=generate_link_button(model_link))

    conn.close()


async def show_nothin_phone_model_info(message: types.Message, brand):
    conn = sqlite3.connect('softech_database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT model, context, price, link, img FROM nothing_phone")
    models = cursor.fetchall()

    for model in models:
        model_name = model[0]
        model_context = model[1]
        model_price = model[2]
        model_link = model[3]
        model_img = model[4]

        await message.answer_photo(model_img)
        await message.answer(text=f'Модель: {model_name}\n'
                                  f'Описание: {model_context}\n'
                                  f'Цена: {model_price}\n',
                             reply_markup=generate_link_button(model_link))

    conn.close()

async def show_discount_item_info(message: types.Message, brand):
    conn = sqlite3.connect('softech_database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT model, price_new, price_old, price_sale, description,link, img FROM discount_items")
    models = cursor.fetchall()

    for model in models:
        model_name = model[0]
        model_price_new = model[1]
        model_price_old = model[2]
        model_price_sale = model[3]
        model_description = model[4]
        model_link = model[5]
        model_img = model[6]
        
        await message.answer_photo(model_img)
        await message.answer(text=f'Модель: {model_name}\n'
                                  f'Описание: {model_description}\n'
                                  f'📈 Cтарая цена: {model_price_old}\n'
                                  f'📉 Новая цена: {model_price_new}\n'
                                  f'Cкидка: {model_price_sale}\n',
                             reply_markup=generate_link_button(model_link))

    conn.close()


    


# Функция для генерации кнопки-ссылки
def generate_link_button(link):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text='Перейти', url=link)
    keyboard.add(button)
    return keyboard


# Регистрация callback-функции
dp.register_callback_query_handler(button_callback_handler)


# Обработчик команды /start
@dp.message_handler(commands=['start', 'menu'])
async def handle_start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(text='🎁  Скидки  🎁', callback_data='discounts'))
    keyboard.add(InlineKeyboardButton(text='📱  Смартфоны  📱', callback_data='smartphones'))
    keyboard.add(InlineKeyboardButton(text='📺  Телевизоры  📺', callback_data='tv'))
    keyboard.add(InlineKeyboardButton(text='💻  Ноутбуки  💻', callback_data='laptop'))
    keyboard.add(InlineKeyboardButton(text='🏮  Продукция Xiaomi  🏮', callback_data='xiaomiProduction'))
    keyboard.add(InlineKeyboardButton(text='🍎  Продукция Apple  🍎' , callback_data='xiaomiProduction'))
    keyboard.add(InlineKeyboardButton(text='🔥  Мультибрендовые товары  🔥', callback_data='xiaomiProduction'))
    keyboard.add(InlineKeyboardButton(text='📞  Консультация по звонку  📞', callback_data='call_phone'))
    keyboard.add(InlineKeyboardButton(text='📌  Наше местоположение  📌', callback_data='maps'))
 

    await message.answer(text='Вас приветствует меню Softech!\n Выберите меню пожалуйста:', reply_markup=keyboard)


async def main():
    await dp.start_polling()


# Запуск бота
if __name__ == '__main__':
    asyncio.run(main())


# change checking







