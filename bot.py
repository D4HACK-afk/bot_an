# 1. Importamos las librerías necesarias (incluyendo tu data_base)
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import data_base  

# 2. Cargamos las variables secretas del archivo .env
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

# Configuración de permisos (Intents)
intents = discord.Intents.default()
intents.message_content = True

# CAMBIO CLAVE: Usamos 'bot = commands.Bot' en lugar de 'client'
# Definimos el prefijo "$" para que coincida con tu "$hello"
bot = commands.Bot(command_prefix="$", intents=intents)

#  EVENTOS
@bot.event
async def on_ready():
    print(f'¡Bot listo! Conectado como {bot.user}')

# COMANDOS REALES

# Tu comando original '$hello' convertido a formato de comando real
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

# Tu nuevo comando de escaneo integrado con tu base de datos
@bot.command()
async def scan(ctx):
    # 1. Verificamos si el usuario subió un archivo
    if not ctx.message.attachments:
        await ctx.send("Por favor, sube un archivo junto con el comando `$scan`.")
        return

    # 2. Tomamos el archivo y guardamos su nombre real
    archivo = ctx.message.attachments[0]
    nombre_temporal = archivo.filename

    await ctx.send(f"Recibiendo `{nombre_temporal}`... Analizando huella dactilar.")

    # 3. Descargamos el archivo temporalmente en tu computadora para poder leerlo
    await archivo.save(nombre_temporal)

    # 4. USAMOS TU CÓDIGO: Calculamos la huella (SHA-256)
    huella = data_base.calcular_hash(nombre_temporal)

    # 5. USAMOS TU CÓDIGO: Buscamos en tu cuaderno de notas (scans.db)
    resultado = data_base.obtain_resultado_local(huella) if hasattr(data_base, 'obtain_resultado_local') else data_base.obtener_resultado_local(huella)

    if resultado:
        # CASO A: Ya estaba registrado en tu base de datos
        await ctx.send(f"**¡Ya conozco este archivo!**\n**Resultado guardado:** {resultado}")
    else:
        # CASO B: Es un archivo nuevo
        await ctx.send(f"**Archivo nuevo detectado.**\n**Hash:** `{huella}`\n*(Aquí es donde llamaremos a Pablo para usar la API de VirusTotal)*")
        
        # Simulamos que lo guardamos para la próxima vez
        data_base.guardar_resultado(huella, nombre_temporal, "Limpio (Simulado - Falta API)")

    # 6. Limpieza: Borramos el archivo de tu PC para no acumular basura
    if os.path.exists(nombre_temporal):
        os.remove(nombre_temporal)

# 3. Arrancamos el bot usando la variable que cargó el .env (¡sin comillas!)
bot.run(DISCORD_TOKEN)