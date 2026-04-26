from vkbottle import Keyboard, Text, KeyboardButtonColor
from vkbottle.bot import Bot, Message


client = Bot("vk1.a.3gkstFj9R0xjkojZ2w46S2ECIfU37peh6N0vOfaJpbhSjY2v_8vdYnrYMobpOGnCvbY0t0TwdQVnQkTpTO1F8mqLfUNTVoy4UGpgXJyYJHigjRJ-kK5jEGvh2GMBocKWLiPEa1nUOfEH7zf8T4Fda8Ed51FOjsD5HbnUYDBI9KD_18a0cAMK8S0GuOc2fCKjwqZTZEzisc7JHqrnPjr8nA")

def setup(bot_client, sessions_dict):
    global client, user_sessions
    client = bot_client
    user_sessions = sessions_dict

QUESTIONS = {}

async def advanced_quiz(message: Message):
    user_sessions[message.from_id] = {"step_advance": 1, "answers": {}}
    await question1(message)


async def question1(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text('Debian-подобные'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Arch-подобные'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Fedora/RHEL/CentOS'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('OpenSUSE'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Gentoo'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Void'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Slackware'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('NixOS'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Свой (LFS)'), color=KeyboardButtonColor.PRIMARY)
        .add(Text('Другое...'), color=KeyboardButtonColor.PRIMARY)
        .add(Text('Не использую Linux'), color=KeyboardButtonColor.PRIMARY)
    )
    await message.answer(f"1. Какой дистрибутив Linux ты используешь сейчас или использовал раньше?", keyboard=kb)

async def question2(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text('GNOME'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('KDE Plasma'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('XFCE'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Cinnamon'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('MATE'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('LXQt'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Другое/своя сборка'), color=KeyboardButtonColor.PRIMARY)
    )
    await message.answer(f"2. Какое окружение рабочего стола (DE) тебе нравится?", keyboard=kb)

async def question3(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text('i3/sway (тайловые)'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Awesome'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Openbox/Fluxbox'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Hyprland'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('bspwm'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('dwm'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Использую полноценное DE, вместо WM'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Другое...'), color=KeyboardButtonColor.PRIMARY)
    )
    await message.answer(f"3. Какие оконные менеджеры (WM) ты предпочитаешь?", keyboard=kb)

async def question4(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text('Systemd (Стандартный)'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('OpenRC (Gentoo, Alpine)'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('runit (Void)'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('s6'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('dinit'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Без разницы'), color=KeyboardButtonColor.PRIMARY)
    )
    await message.answer(f"4. Какая система инициализации тебе ближе?", keyboard=kb)

async def question5(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text('Xorg (X11)'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Wayland'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Оба подходят'), color=KeyboardButtonColor.PRIMARY)
    )
    await message.answer(f"5. Какой протокол графического сервера ты предпочитаешь?", keyboard=kb)

async def question6(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text('apt (Debian)'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('pacman (Arch)'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('zypper (openSUSE)'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('dnf (Fedora/RHEL)'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('portage (Gentoo)'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('xbps (Void)'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('nix (NixOS)'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('flatpak (Flathub-repo)'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('snap (by Canonical)'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('pkg (BSD-like sys)'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Без разницы =/'), color=KeyboardButtonColor.PRIMARY)
        .add(Text('Другое...'), color=KeyboardButtonColor.PRIMARY)
    )
    await message.answer(f"6. Какой пакетный менеджер тебе больше всего нравится?", keyboard=kb)

async def question7(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text('Постоянные обновления (Rolling releases)'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Стабильные релизы (Stable releases)'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Долгосрочная поддержка (LTS)'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Что-то среднее (Semi-rolling releases)'), color=KeyboardButtonColor.SECONDARY)
    )
    await message.answer(f"7. Модель обновления пакетов какая тебе больше нравится?", keyboard=kb)

async def question8(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text('Только бинарные пакеты'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Иногда приходится компилировать'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Постоянно собираю из исходников'), color=KeyboardButtonColor.SECONDARY)
    )
    await message.answer(f"8. Готов ли ты собирать программы из исходных кодов?", keyboard=kb)

async def question9(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text('Только GUI (графический интерфейс)'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('В основном GUI, но CLI тоже умею'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('50/50'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Обожаю CLI! (TTY)'), color=KeyboardButtonColor.SECONDARY)
    )
    await message.answer(f"9. Что ты предпочитаешь: GUI или CLI?", keyboard=kb)

async def question10(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text('GRUB (стандарт)'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('systemd-boot'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('rEFInd'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('LILO'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Другое...'), color=KeyboardButtonColor.PRIMARY)
        .add(Text('Без разницы =/'), color=KeyboardButtonColor.PRIMARY)
    )
    await message.answer(f"10. Какой загрузчик (bootloader) ты предпочитаешь?", keyboard=kb)

async def question11(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text('Полностью устраивает'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Нейтрально. Работает и ладно'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Не нравится, но терплю'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Ненавижу. Использую другой init'), color=KeyboardButtonColor.SECONDARY)
    )
    await message.answer(f"11. Как ты относишься к systemd?", keyboard=kb)

async def question12(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text('Рабочая станция/десктоп'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Сервер (без GUI)'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Программирование/DevOps'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Эксперименты и обучение'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Встраиваемые системы'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Всё и сразу!'), color=KeyboardButtonColor.PRIMARY)
    )
    await message.answer(f"12. Для каких задач тебе нужен Linux?", keyboard=kb)

async def question13(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text('Хорошая документация'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Активное сообщество'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Полный контроль'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Стабильность и надёжность'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Минимализм'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Свежесть ПО'), color=KeyboardButtonColor.SECONDARY)
    )
    await message.answer(f"13. Что для тебя главное в дистрибутиве?", keyboard=kb)

async def question14(message: Message):
    kb = (
        Keyboard(one_time=False, inline=False)
        .add(Text('Да, активно'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Иногда'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Нет, но знаю что это'), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Не знаю, и не использую'), color=KeyboardButtonColor.SECONDARY)
    )
    await message.answer(f"14. Используешь ли ты контейнеры (Docker, podman)?", keyboard=kb)
    
async def question15(message: Message):
    kb = (
        Keyboard(one_time=True, inline=False)
        .add(Text('Минимальные (ставлю только нужное)'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Полные (всё из коробки)'), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Что-то среднее'), color=KeyboardButtonColor.PRIMARY)
    )
    await message.answer(f"15. Предпочитаешь ли ты минимальные установщики (bare bones) или полные (full featured)?", keyboard=kb)



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
QUESTIONS[11] = question11
QUESTIONS[12] = question12
QUESTIONS[13] = question13
QUESTIONS[14] = question14
QUESTIONS[15] = question15
