import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from sqlite import db_start, create_profile, edit_profile
from config import TOKEN_API


async def on_startap(_):
    await db_start()

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

class ProfileStatesGroup(StatesGroup):

    photo = State()
    name = State()
    age = State()
    description = State()



@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):

    await create_profile(user_id=message.from_user.id)
    
    kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Личный кабинет 📁')
    b2 = KeyboardButton('NFT 🎆')
    b3 = KeyboardButton('Инфо ℹ️')
    b4 = KeyboardButton('Тех.Поддержка 🌐')
    kb1.add(b1).add(b2).add(b3).insert(b4)

    kb2 = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton(text = "🗞Новости", 
                                       url='https://twitter.com/NFT-Market')
    
    item2 = types.InlineKeyboardButton(text = "📄 Соглашение", 
                                       url='https://telegra.ph/Polzovatelskoe-soglashenie-NFT-Market-06-18')
    
    kb2.add(item1,item2)

    await bot.send_message(chat_id=message.from_user.id, 
                           text=f'Приветствую, <b>{message.from_user.first_name}!</b>\n\nЭто телеграм бот для безопасной торговли NFT',
                           parse_mode='html',
                           reply_markup=kb1)
    
    await bot.send_message(chat_id=message.from_user.id, 
                           text='Используя сервисы проекта вы соглашаетесь с                         .\nпользовательским соглашением\nУзнайте о других продуктах NFT-Market', 
                           parse_mode="HTML", 
                           reply_markup=kb2)




@dp.message_handler(content_types=['text'])
async def text_all(message):
    if message.text != None:
        #команда Личный кабинет
        if message.text == 'Личный кабинет 📁':
            await bot.send_message(chat_id=message.from_user.id, 
                                   text="⚡️")
            kb3 = types.InlineKeyboardMarkup(row_width=2)
            #     
            item1 = types.InlineKeyboardButton(text = "📥 Пополнить", 
                                               callback_data="📥 Пополнить")
            item2 = types.InlineKeyboardButton(text = "📤 Вывести", 
                                               callback_data="📤 Вывести")
            item3 = types.InlineKeyboardButton(text = "📝 Верификация", 
                                               callback_data="📝 Верификация")
            item4 = types.InlineKeyboardButton(text = "❤️ Избранное", 
                                               callback_data="❤️ Избранное")
            item5 = types.InlineKeyboardButton(text = "🌌 Мои NFT", 
                                               callback_data="🌌 Мои NFT")
            item6 = types.InlineKeyboardButton(text = "⚙️ Настройки", 
                                               callback_data="⚙️ Настройки")
            kb3.insert(item1).insert(item2).insert(item3).insert(item4).add(item5).add(item6)
            time.sleep(1)
            balance = "0.0 RUB"
            vivod = "0.0 RUB"
            verificatione = "⚠️ Не верифицирован"
            times = "nihua"
            await bot.send_photo(chat_id=message.from_user.id, 
                                 photo='https://ru-static.z-dn.net/files/d76/5047612cfe27d63450deea4ab58ae54c.jpg',
                                 caption=f' ⭐️ <b>Личный кабинет</b>\n\nБаланс: <b>{balance}</b>\nНа выводе: <b>{vivod}</b>\n\nВерификация: <b>{verificatione}</b>\n ⭐️ Ваш айди: <b>{message.from_user.id}</b>\n\nДата и время: {times}',
                                 parse_mode='html',
                                 reply_markup=kb3)
        #команда НФТ
        elif message.text == 'NFT 🎆':
            kb3 = types.InlineKeyboardMarkup(row_width=2)
            #     
            item1 = types.InlineKeyboardButton(text = "NFT", 
                                               callback_data="NFT")
            kb3.add(item1)

            await bot.send_photo(chat_id=message.from_user.id, 
                                 photo='https://ru-static.z-dn.net/files/d76/5047612cfe27d63450deea4ab58ae54c.jpg',
                                 caption='💠 Всего на маркетплейсе 91 коллекция',
                                 parse_mode='html',
                                 reply_markup=kb3)
        # команда инфо
        elif message.text == 'Инфо ℹ️':
            kb3 = types.InlineKeyboardMarkup(row_width=2)
            #     
            item1 = types.InlineKeyboardButton(text = "Соглашение 📄", 
                                               url='https://telegra.ph/Polzovatelskoe-soglashenie-NFT-06-18')
            item2 = types.InlineKeyboardButton(text = "Поддержка 👩‍💻", 
                                               url='https://telegra.ph/Polzovatelskoe-soglashenie-NFT-06-18')
            item3 = types.InlineKeyboardButton(text = "Сообщить об ошибке", 
                                               url='https://telegra.ph/Polzovatelskoe-soglashenie-NFT-06-18')
            item4 = types.InlineKeyboardButton(text = "Партнерская программа ⚙️", 
                                               callback_data="Партнерская программа ⚙️")

            kb3.insert(item1).insert(item2).insert(item3).insert(item4)

            await bot.send_photo(chat_id=message.from_user.id, 
                                 photo='https://ru-static.z-dn.net/files/d76/5047612cfe27d63450deea4ab58ae54c.jpg',
                                 caption=' ⭐️ <b>О Сервисе\n\nOpenSea — торговая площадка для невзаимозаменяемых токенов (NFT).Покупайте, продавайте и открывайте для себя эксклюзивные цифровые предметы.</b>',
                                 parse_mode='html',
                                 reply_markup=kb3)
            # команда тех потдержки
        elif message.text == 'Тех.Поддержка 🌐':
            kb3 = types.InlineKeyboardMarkup(row_width=2)
            #     
            item1 = types.InlineKeyboardButton(text = "Поддержка ⚙️", 
                                               url='https://telegra.ph/Polzovatelskoe-soglashenie-NFT-06-18')
            kb3.add(item1)

            await bot.send_photo(chat_id=message.from_user.id, 
                                 photo='https://ru-static.z-dn.net/files/d76/5047612cfe27d63450deea4ab58ae54c.jpg',
                                 caption='Правила обращения в Техническую Поддержку:\n\n1. Представьтесь, изложите проблему своими словами - мы постараемся Вам помочь.\n\n2. Напишите свой ID - нам это нужно, чтобы увидеть Ваш профиль, и узнать актуальность Вашей проблемы.\n\n3. Будьте вежливы, наши консультанты не роботы, мы постараемся помочь Вам, и сделать все возможное, чтобы сберечь Ваше время и обеспечить максимальную оперативность в работе.\n\nНапишите нам, ответ Поддержки, не заставит Вас долго ждать!',
                                 reply_markup=kb3)


@dp.callback_query_handler()
async def callback(call):
    if call.data == '📥 Пополнить':
        kb = types.InlineKeyboardMarkup(row_width=1)
        b1 = types.InlineKeyboardButton(text = "🥝 Пополнить через QIWI кошелек", 
                                            callback_data="QIWI")
        kb.add(b1)
        await bot.send_photo(chat_id=call.from_user.id, 
                                 photo='https://zwebra.com.ua/bot-01.jpg',
                                 caption="Выберите удобный для вас метод пополнения.",
                                 reply_markup=kb)
    elif call.data == '📤 Вывести':
        await bot.send_message(chat_id=call.from_user.id,
                               text="❌ Минимальная сумма для вывода: 1000.0 RUB\n💸 Ваш баланс: 00.0 RUB, меньше чем нужно!")
    elif call.data == 'Партнерская программа ⚙️':
        kb = types.InlineKeyboardMarkup(row_width=1)
        b1 = types.InlineKeyboardButton(text = "Вернуться", 
                                            callback_data="Вернуться")
        kb.add(b1)
        await bot.send_photo(chat_id=call.from_user.id, 
                                 photo='https://zwebra.com.ua/bot-01.jpg',
                                 caption='⭐️ Как присоединиться к партнерской программе и стать партнером NFT-Market\n\n 🔥 Партнерская программа NFT-Market позволяет привлекать трейдеров на платформу и зарабатывать дополнительные деньги на основе их активности.\n\n ⭐️ Количество друзей, которых можно пригласить в одном аккаунте, не ограничено.\n\n ⭐️ NFT-Market запрещает пользователям приглашать самих себя путем создания нескольких аккаунтов.\n\n 💥 Если мы зафиксируем подобные действия, все рефералы, реферальные бонусы и кешбэки для аккаунтов приглашенного будут отменены.\n\n 🔥 NFT-Market оставляет за собой право по своему усмотрению продлевать срок, в течение которого приглашающие смогут получать реферальные бонусы.\n\n ⭐️Ваша реферальная ссылка для приглашения партнеров: https://t.me/NFT-Market_nftbot?start=300659',
                                 reply_markup=kb)
    elif call.data == '📝 Верификация':
        kb = types.InlineKeyboardMarkup(row_width=1)
        b1 = types.InlineKeyboardButton(text = "Поддержка", 
                                            url="https://www.youtube.com")
        b2 = types.InlineKeyboardButton(text = "назад", 
                                            callback_data="назад")
        kb.add(b1).add(b2)
        await bot.send_photo(chat_id=call.from_user.id, 
                                 photo='https://zwebra.com.ua/bot-01.jpg',
                                 caption='⭐️ <b>Ваш аккаунт не верифицирован.</b>\n\nПолучить статус «Верифицирован» можно написав фразу «Верификация» в общий чат технической поддержки.\n\nДля перехода в общий чат поддержки понадобится перейти в раздел «Тех. Поддержка», либо воспользоваться кнопкой ниже.',
                                 parse_mode='html',
                                 reply_markup=kb)
    elif call.data == '⚙️ Настройки':
        kb = types.InlineKeyboardMarkup(row_width=1)
        b1 = types.InlineKeyboardButton(text = "🌍 Язык", 
                                            callback_data="🌍 Язык")
        b2 = types.InlineKeyboardButton(text = "💲Валюта", 
                                            callback_data="💲Валюта")
        b3 = types.InlineKeyboardButton(text = "Вернуться", 
                                            callback_data="Вернуться")
        kb.add(b1).add(b2).add(b3)
        await bot.send_photo(chat_id=call.from_user.id, 
                                 photo='https://zwebra.com.ua/bot-01.jpg',
                                 caption='<b>⚙️ Настройки</b>',
                                 parse_mode='html',
                                 reply_markup=kb)

#Конец
if __name__ == '__main__':
    executor.start_polling(dp, 
                           skip_updates=True, 
                           on_startup=on_startap)