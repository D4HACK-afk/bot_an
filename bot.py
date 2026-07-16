# 1. Importamos la librería del sistema (os) y la que lee el archivo .env
import os
import discord
from dotenv import load_dotenv

# 2. Cargamos las variables secretas a la memoria
load_dotenv()
# Buscamos el token dentro del archivo .env y lo guardamos en una variable
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# 3. ¡Aquí está el cambio! En lugar del token de texto, pasamos la variable segura
client.run(DISCORD_TOKEN)
