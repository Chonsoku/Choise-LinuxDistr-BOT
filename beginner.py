from vkbottle import Keyboard, Text, KeyboardButtonColor
from vkbottle.bot import Bot, Message


client = Bot("vk1.a.3gkstFj9R0xjkojZ2w46S2ECIfU37peh6N0vOfaJpbhSjY2v_8vdYnrYMobpOGnCvbY0t0TwdQVnQkTpTO1F8mqLfUNTVoy4UGpgXJyYJHigjRJ-kK5jEGvh2GMBocKWLiPEa1nUOfEH7zf8T4Fda8Ed51FOjsD5HbnUYDBI9KD_18a0cAMK8S0GuOc2fCKjwqZTZEzisc7JHqrnPjr8nA")

def setup(bot_client, sessions_dict):
    global client, user_sessions
    client = bot_client
    user_sessions = sessions_dict

QUESTIONS = {}

async def beginner_quiz(message: Message):
    user_sessions[message.from_id] = {"step_begin": 1, "answers": {}}
    await question1(message)


async def question1(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text('Windows 10/11'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Windows 7/8'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('MacOS'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Linux'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('BSD'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('ReactOS'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Android'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('IOS'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('TempleOS'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Другое...'), color=KeyboardButtonColor.PRIMARY)
    )
    await message.answer(f"1. Какая операционная система у тебя сейчас установлена?", keyboard=kb)

async def question2(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text('Редко (раз в неделю)'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Пару раз в неделю'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Каждый день понемногу'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Целыми днями'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Это моя работа'), color=KeyboardButtonColor.SECONDARY)
    )
    await message.answer(f"2. Как часто ты пользуешься компьютером?", keyboard=kb)

async def question3(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text('Привычный интерфейс'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Много программ и игр'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Всё работает из коробки'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Стабильность'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Ничего не нравится'), color=KeyboardButtonColor.PRIMARY)
    )
    await message.answer(f"3. Что тебе НРАВИТСЯ в твоей текущей ОС?", keyboard=kb)
      
async def question4(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text('Сложность установки'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Боязнь терминала'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Несовместимость с программами'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Сложности с драйверами'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Ничего не пугает'), color=KeyboardButtonColor.PRIMARY)
    )
    await message.answer(f"4. Что тебя ПУГАЕТ в переходе на Linux?", keyboard=kb)
    
async def question5(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text("Сёрфинг и общение в интернете"), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Работа с документами (Word, Excel'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Программирование'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Игры'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Работа с графикой/видео'), color=KeyboardButtonColor.SECONDARY)
		.add(Text('Все и сразу!'), color=KeyboardButtonColor.PRIMARY)
    )
    await message.answer(f"5. Для каких задач тебе нужен Linux?", keyboard=kb)

async def question6(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text("Хочу чтобы всё работало сразу"), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text("Могу немного покопаться в настройках"), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text("Люблю настраивать всё вручную под себя"), color=KeyboardButtonColor.SECONDARY)
    )
    await message.answer(f"6. Как ты относишься к настройке системы под себя?", keyboard=kb)

async def question7(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text("Очень важен (хочу красивый интерфейс)"), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Главное чтобы работало стабильно'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text("Что-то среднее"), color=KeyboardButtonColor.SECONDARY)
    )
    await message.answer(f"7. Внешний вид системы для тебя важен?", keyboard=kb)
      
async def question8(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text("Старый/слабый"), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Средний'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text("Мощный"), color=KeyboardButtonColor.SECONDARY)
        .add(Text("Не знаю характеристик"), color=KeyboardButtonColor.PRIMARY)
    )
    await message.answer(f"8. Какой у тебя компьютер?", keyboard=kb)

async def question9(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text("Никогда"), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Пару раз по инструкции в интернете'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text("Да, уверенно работаю"), color=KeyboardButtonColor.SECONDARY)
        .add(Text("Что это вообще такое?"), color=KeyboardButtonColor.PRIMARY)
    )
    await message.answer(f"9. Пользовался ли ты командной строкой (терминалом)?", keyboard=kb)

async def question10(message: Message):
    kb = (
        Keyboard(one_time=True, inline=False)
        .add(Text("Стабильность"), color=KeyboardButtonColor.PRIMARY)
        .add(Text('Простота использования'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text("Красивый интерфейс"), color=KeyboardButtonColor.SECONDARY)
        .add(Text("Быстродействие"), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text("Совместимость с программами"), color=KeyboardButtonColor.SECONDARY)
    )
    await message.answer(f"10. Что для тебя важнее всего в операционной системе?", keyboard=kb)



QUESTIONS[1] = question1
QUESTIONS[2] = question2
QUESTIONS[3] = question3
QUESTIONS[4] = question4
QUESTIONS[5] = question5
QUESTIONS[6] = question6
QUESTIONS[7] = question7
QUESTIONS[8] = question8
QUESTIONS[9] = question9
QUESTIONS[10] = question10
