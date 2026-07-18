# 1. Importamos las librerías necesarias (incluyendo tu data_base)
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import data_base  
import re
# 2. Cargamos las variables secretas del archivo .env
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)



#*  EVENTOS........................................................................./
@bot.event
async def on_ready():
    print(f'¡Bot listo! Conectado como {bot.user}')

#*  COMANDOS........................................................................./

#! comando $hello
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

#! comando $scan 
@bot.command()
async def scan(ctx):
   
    if not ctx.message.attachments:
        await ctx.send("Por favor, sube un archivo junto con el comando `$scan`.")
        return

    archivo = ctx.message.attachments[0]
    nombre_temporal = archivo.filename

    await ctx.send(f"Recibiendo `{nombre_temporal}`... Analizando huella dactilar.")

    await archivo.save(nombre_temporal)

    huella = data_base.calcular_hash(nombre_temporal)

    resultado = data_base.obtain_resultado_local(huella) if hasattr(data_base, 'obtain_resultado_local') else data_base.obtener_resultado_local(huella)

    if resultado:
        await ctx.send(f"**¡Ya conozco este archivo!**\n**Resultado guardado:** {resultado}")
    else:
        await ctx.send(f"**Archivo nuevo detectado.**\n**Hash:** `{huella}`\n*(Aquí es donde llamaremos a Pablo para usar la API de VirusTotal)*")
        
        # Simulamos que lo guardamos para la próxima vez
        data_base.guardar_resultado(huella, nombre_temporal, "Limpio (Simulado - Falta API)")

    # 6. Limpieza: Borramos el archivo de tu PC para no acumular basura
    if os.path.exists(nombre_temporal):
        os.remove(nombre_temporal)

#! comando $quiensoy
@bot.command()
async def quiensoy(ctx):
    usuario = ctx.author.name
    canal = ctx.channel.name
    servidor = ctx.guild.name
    await ctx.send(f"jelouda, su nombre es **{usuario}**, usted esta escribiendo desde el canal **#{canal}** en el servidor **'{servidor}'**")

#! comando $calcula = ['calcular', 'restar', 'multiplicar', 'dividir', 'sumar', 'resta', 'suma', 'divide', 'multiplica', 'multiplicacion', 'division']
@bot.command(aliases=['calcular', 'restar', 'multiplicar', 'dividir', 'sumar', 'resta', 'suma', 'divide', 'multiplica', 'multiplicacion', 'division'])
async def calcula(ctx, *, operacion: str):
    patron = r"(\d+)\s*([\+\-\*/])\s*(\d+)" 
    busqueda = re.search(patron, operacion)

    if not busqueda:
        await ctx.send("El formato que usaste para para ejecutar tu operacion es incorrecto usa mejor el siguiente Ejemplo: $calcular 20+20 o tambien $calcular 40  +  40")
        return

    numero1 = int(busqueda.group(1))
    simbolo = busqueda.group(2)
    numero2 = int(busqueda.group(3))

    calculo_final = 0 
    if simbolo == "+": 
        calculo_final = numero1+numero2

    elif simbolo == "-":
        calculo_final = numero1-numero2

    elif simbolo == "/":
        if numero2 == 0:
            await ctx.send("Error: No se puede dividir entre cero. Es literalmente imposible las reglas de nuestro universo no lo permiten.")
            return
        calculo_final = numero1/numero2

    elif simbolo == "*":
        calculo_final = numero1*numero2

    await ctx.send(f"resultado = **{calculo_final}**")

bot.run(DISCORD_TOKEN)