# 1. Importamos la librería del sistema (os) y la que lee el archivo .env
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# 2. Cargamos las variables secretas a la memoria
load_dotenv()
# Buscamos el token dentro del archivo .env y lo guardamos en una variable
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
#eventos 
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
#evento que le dice al bot que al leer su propio mensaje corte la funcion
@client.event
async def on_message(message):
    if message.author == client.user:
        return
#cuando el bot detecte el mensaje pasara a travez de el y lo enviara con retraso
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# 3. ¡Aquí está el cambio! En lugar del token de texto, pasamos la variable segura
client.run(DISCORD_TOKEN)
