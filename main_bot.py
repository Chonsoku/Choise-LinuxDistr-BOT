import os, ollama, asyncio
import beginner, advanced

from typing import Optional
from vkbottle import GroupEventType, GroupTypes, Keyboard, Text, VKAPIError
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink
from vkbottle.tools import DocMessagesUploader
from ollamaL import User_chat_Ollama


client = Bot("vk1.a.3gkstFj9R0xjkojZ2w46S2ECIfU37peh6N0vOfaJpbhSjY2v_8vdYnrYMobpOGnCvbY0t0TwdQVnQkTpTO1F8mqLfUNTVoy4UGpgXJyYJHigjRJ-kK5jEGvh2GMBocKWLiPEa1nUOfEH7zf8T4Fda8Ed51FOjsD5HbnUYDBI9KD_18a0cAMK8S0GuOc2fCKjwqZTZEzisc7JHqrnPjr8nA")
user_sessions = {}

beginner.setup(client, user_sessions)
advanced.setup(client, user_sessions)

async def get_distribution_recommendation(level: str, answers: dict) -> str:
    answers_text = str(answers)
    """
    Получает рекомендацию дистрибутива от Ollama на основе ответов пользователя
    """
    chat = User_chat_Ollama()
    if level == "beginner":
        prompt = f"""Ты дружелюбный и приветливый эксперт по Linux. На основе ответов НОВИЧКА (новичок), который хочет перейти на Linux, 
        дай ему персонализированную рекомендацию дистрибутива.

ВОТ ОТВЕТЫ ПОЛЬЗОВАТЕЛЯ:
{answers_text}

ПРАВИЛА ФОРМАТИРОВАНИЯ ОТВЕТА:
1. Начни с ASCII-логотипа рекомендованного дистрибутива (бери из neofetch; fastfetch; ..)
2. Затем напиши название дистрибутива жирным
3. Дай небольшое описание дистрибутива (2-3 предложения)
4. Объясни, ПОЧЕМУ именно этот дистрибутив подходит этому пользователю (опираясь на его ответы)
5. Затем перечисли 4 других дистрибутива, которые тоже могут подойти, с кратким пояснением

ФОРМАТ ОТВЕТА (используй эмодзи для красоты):

[ASCII-логотип дистрибутива]

Название дистрибутива

📖 Описание:
[небольшое описание]

🎯 Почему именно вам:
• [причина 1, связанная с ответами пользователя]
• [причина 2]
• [причина 3]

🔄 Другие варианты:
• Дистрибутив 2 - [почему может подойти]
• Дистрибутив 3 - [почему может подойти]
• Дистрибутив 4 - [почему может подойти]
• Дистрибутив 5 - [почему может подойти]

💡 Совет: [короткий практический совет]

Порекомендуй ТОЛЬКО дружественные новичкам дистрибутивы: Ubuntu, Linux Mint, Zorin OS, Pop!_OS, Fedora, elementary OS.
Не предлагай Arch, Gentoo, Void и другие сложные дистрибутивы."""
    
    else:  # advanced
        prompt = f"""Ты эксперт по Linux с глубокими знаниями популярных и редких дистрибутивов. 
        На основе ответов ОПЫТНОГО ПОЛЬЗОВАТЕЛЯ дай ему точную рекомендацию.

ВОТ ОТВЕТЫ ПОЛЬЗОВАТЕЛЯ:
{answers_text}

УЧТИ ЭТИ ПАРАМЕТРЫ:
- Предпочитаемое окружение рабочего стола (DE)
- Init system (systemd, OpenRC, runit, s6)
- Протокол графического сервера (Xorg, Wayland)
- Пакетный менеджер
- Модель обновления (rolling, стабильный)
- Готовность к компиляции из исходников
- Предпочтения GUI/CLI

ПРАВИЛА ФОРМАТИРОВАНИЯ ОТВЕТА:
1. Начни с ASCII-логотипа рекомендованного дистрибутива (бери из neofetch; fastfetch; ..)
2. Затем напиши название дистрибутива жирным
3. Дай небольшое описание дистрибутива
4. Объясни, ПОЧЕМУ именно этот дистрибутив подходит (техническое обоснование)
5. Перечисли 4 других дистрибутива (включая нишевые: Gentoo, Void, NixOS, Artix и др.)

ФОРМАТ ОТВЕТА:

[ASCII-логотип дистрибутива]

**Название дистрибутива**

📖 Описание:
[небольшое описание]

🎯 Техническое обоснование:
• [почему подходит под его предпочтения]
• [учёт init system, DE, пакетного менеджера]
• [другие технические причины]

🔄 Альтернативные варианты:
• Дистрибутив 2 - [когда подойдёт лучше]
• Дистрибутив 3 - [когда подойдёт лучше]
• Дистрибутив 4 - [когда подойдёт лучше]
• Дистрибутив 5 - [когда подойдёт лучше]

⚠️ Особенности: [что важно знать перед установкой]

Будь технически точен, но дружелюбен!"""

    try:
        answer = chat.add_question(prompt)
        return answer
    except Exception as e:
        return f"Ошибка при обращении к Ollama: {str(e)}❌"

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
            await asyncio.sleep(1)
            await message.answer("⏲️ | ИДЁТ ФОРМИРОВАНИЕ ОТВЕТА... | ⏲️")
            recommendation = await get_distribution_recommendation("beginner", session["answers"])
            if len(recommendation) > 4000:
                parts = [recommendation[i:i+4000] for i in range(0, len(recommendation), 4000)]
                for part in parts:
                    await message.answer(part)
                    await asyncio.sleep(0.5)
            else:
                await message.answer(recommendation)

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
            await asyncio.sleep(1)
            await message.answer("⏲️ | ИДЁТ ФОРМИРОВАНИЕ ОТВЕТА... | ⏲️")
            recommendation = await get_distribution_recommendation("advanced", session["answers"])
            if len(recommendation) > 4000:
                parts = [recommendation[i:i+4000] for i in range(0, len(recommendation), 4000)]
                for part in parts:
                    await message.answer(part)
                    await asyncio.sleep(0.5)
            else:
                await message.answer(recommendation)
    else:
        del user_sessions[user_id]




if __name__ == "__main__":
    client.run_forever()
