from vkbottle.bot import Bot, Message
from ollama import chat

client = Bot("vk1.a.3gkstFj9R0xjkojZ2w46S2ECIfU37peh6N0vOfaJpbhSjY2v_8vdYnrYMobpOGnCvbY0t0TwdQVnQkTpTO1F8mqLfUNTVoy4UGpgXJyYJHigjRJ-kK5jEGvh2GMBocKWLiPEa1nUOfEH7zf8T4Fda8Ed51FOjsD5HbnUYDBI9KD_18a0cAMK8S0GuOc2fCKjwqZTZEzisc7JHqrnPjr8nA")

@client.on.private_message(text="<msg>")
async def echo_answer(ans: Message, msg):
  await ans.answer("Ты написал: %s"%(msg))

if __name__ == "__main__":
  client.run_forever()