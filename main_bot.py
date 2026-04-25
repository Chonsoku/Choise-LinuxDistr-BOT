from typing import Optional
from vkbottle import GroupEventType, GroupTypes, Keyboard, Text, VKAPIError
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink
from vkbottle.tools import DocMessagesUploader
import os, ollama, asyncio
import beginner


client = Bot("vk1.a.3gkstFj9R0xjkojZ2w46S2ECIfU37peh6N0vOfaJpbhSjY2v_8vdYnrYMobpOGnCvbY0t0TwdQVnQkTpTO1F8mqLfUNTVoy4UGpgXJyYJHigjRJ-kK5jEGvh2GMBocKWLiPEa1nUOfEH7zf8T4Fda8Ed51FOjsD5HbnUYDBI9KD_18a0cAMK8S0GuOc2fCKjwqZTZEzisc7JHqrnPjr8nA")
user_sessions = {}

beginner.setup(client, user_sessions)

@client.on.private_message(text=['Привет', 'привет', 'Ку', 'ку', 'хай', 'Хай', 'ПРИВЕТ', 'КУ', 'ХАЙ'])
async def hello_message(message: Message):
    await message.answer("Привет! 👋")
    await asyncio.sleep(1)
    await message.answer("Это чат-бот, который тебе задаст вопросы о твоих предпочтениях и знаниях линукса.\nТем самым, подобрав лучший для тебя!")
    await asyncio.sleep(4)
    await message.answer("| Напиши «Меню» или «Начать», чтобы чат-бот приступил к работе | =>")


@client.on.private_message(text=['Начать', 'начать', 'Меню', 'меню'])
@client.on.private_message(payload={'cmd': 'menu'})
async def menu(message: Message):
    await message.answer(
        message = '- Ты новичок, и хочешь опробовать что-то новое?\n - Или ты уже опытный пользователь дистрибутивов линукса?',
        keyboard = (
            # one_time - True - одноразовая клавиатура, False - постоянная клавиатура
            # inline - True - клавиатура прикрепляется к сообщению(РАССМОТРИМ), False - клавиаутра в стандартном положении
            # .add - добавить кнопку
            # .row - отступ
            # Цвета: POSITIVE - Ярко зеленый, SECONDARY(можно нечего не указывать) - БЛЕДНО БЕЛЫЙ
            # PRIMARY - СИНИЙ, NEGATIVE - КРАСНЫЙ

            Keyboard(one_time = False, inline = False)
            .add(Text('😶‍🌫️ | НОВИЧОК | 😶‍🌫️'), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text('😎 | ОПЫТНЫЙ ПОЛЬЗОВАТЕЛЬ | 😎'), color=KeyboardButtonColor.NEGATIVE)
            )
    )

@client.on.private_message(text=['😶‍🌫️ | НОВИЧОК | 😶‍🌫️'])
async def start_beginner(message: Message):
    await beginner.beginner_quiz(message)

# @client.on.private_message(text=['😎 | ОПЫТНЫЙ ПОЛЬЗОВАТЕЛЬ | 😎'])
# async def start_advanced(message: Message):
#     await advanced.advanced_quiz(message)


@client.on.private_message()
async def handle_next_question(message: Message):
    user_id = message.from_id
    if user_id in user_sessions:
        session = user_sessions[user_id]
        step = session["step"]
        session["answers"][f"q{step}"] = message.text
        session["step"] += 1
    
        now_step = session["step"]
        print(f"Текущий вопрос: {now_step}")
        if now_step in beginner.QUESTIONS:
            await beginner.QUESTIONS[now_step](message)
        else:
            del user_sessions[user_id]
            await message.answer("✅ | ОПРОС НОВИЧКА ЗАВЕРШЁН | ✅")
            print(beginner.QUESTIONS)

if __name__ == "__main__":
    client.run_forever()
