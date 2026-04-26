from typing import Optional
from vkbottle import GroupEventType, GroupTypes, Keyboard, Text, VKAPIError
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink
from vkbottle.tools import DocMessagesUploader
import os, ollama, asyncio
import beginner, advanced


client = Bot("vk1.a.3gkstFj9R0xjkojZ2w46S2ECIfU37peh6N0vOfaJpbhSjY2v_8vdYnrYMobpOGnCvbY0t0TwdQVnQkTpTO1F8mqLfUNTVoy4UGpgXJyYJHigjRJ-kK5jEGvh2GMBocKWLiPEa1nUOfEH7zf8T4Fda8Ed51FOjsD5HbnUYDBI9KD_18a0cAMK8S0GuOc2fCKjwqZTZEzisc7JHqrnPjr8nA")
user_sessions = {}

beginner.setup(client, user_sessions)
advanced.setup(client, user_sessions)

@client.on.private_message(text=['Привет', 'привет', 'Ку', 'ку', 'хай', 'Хай', 'ПРИВЕТ', 'КУ', 'ХАЙ'])
async def hello_message(message: Message):
    await message.answer("Привет! 👋")
    await asyncio.sleep(1)
    await message.answer("Это чат-бот, который тебе задаст вопросы о твоих предпочтениях и знаниях линукса.\nТем самым, подобрав лучший для тебя!")
    await asyncio.sleep(4)
    await message.answer("| Напиши «Меню» или «Начать», чтобы чат-бот приступил к работе | =>")


@client.on.private_message(text=['Начать', 'начать', 'НАЧАТЬ', 'Меню', 'меню', 'МЕНЮ'])
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
@client.on.private_message(text=['😎 | ОПЫТНЫЙ ПОЛЬЗОВАТЕЛЬ | 😎'])
async def start_advanced(message: Message):
    await advanced.advanced_quiz(message)


@client.on.private_message()
async def beginner_next_question(message: Message):
    user_id = message.from_id    
    session = user_sessions[user_id]
    if "step_begin" in session:
        step_begin = session["step_begin"]
        session["answers"][f"q{step_begin}"] = message.text
        session["step_begin"] += 1
        now_step_begin = session["step_begin"]
        print(f"Текущий вопрос: {now_step_begin}")
        if now_step_begin in beginner.QUESTIONS:
            await beginner.QUESTIONS[now_step_begin](message)
        else:
            del user_sessions[user_id]
            await message.answer("✅ | ОПРОС НОВИЧКА ЗАВЕРШЁН | ✅")
            print("| ОПРОС НОВИЧКА ЗАВЕРШЁН |\n")

    elif "step_advance" in session:
        step_advance = session["step_advance"]
        session["answers"][f"q{step_advance}"] = message.text
        session["step_advance"] += 1
        now_step_advance = session["step_advance"]
        print(f"Текущий вопрос: {now_step_advance}")
        if now_step_advance in advanced.QUESTIONS:
            await advanced.QUESTIONS[now_step_advance](message)
        else:
            del user_sessions[user_id]
            await message.answer("✅ | ОПРОС ОПЫТНОГО ПОЛЬЗОВАТЕЛЯ ЗАВЕРШЁН | ✅")
            print("| ОПРОС ОПЫТНОГО ПОЛЬЗОВАТЕЛЯ ЗАВЕРШЁН |\n")
    else:
        del user_sessions[user_id]




if __name__ == "__main__":
    client.run_forever()
