import discord
from discord.ext import commands
import os

f = open("token.txt", "r")
TOKEN = f.read()
f.close()
client = commands.Bot(command_prefix=["/", ".", "-"])

if __name__ == "__main__":
    for file in os.listdir(os.getcwd() + "/modules/"):
        if file[-3:] == ".py" and file[:2] != "__":
            client.load_extension("modules." + file[:-3])

@client.event
async def on_ready():
    print("Estou funcionando perfeitamente, para me desligar basta fechar o console. Em caso de bugs envie uma mensagem para o criador: viniciushora#3413.")

client.run(TOKEN)