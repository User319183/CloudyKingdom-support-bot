



import discord

from discord.ext import commands

import os

import json

import asyncio as asyncio

from discord.ext import *

from discord.ext.commands import *

from ctypes import *






if os.path.exists(os.getcwd() + "/config.json"):
    
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

token = configData["Token"]








intents = discord.Intents.default()
# intents.typing = False
# intents.presences = False
intents.members = True
intents.reactions = True



bot = commands.Bot(command_prefix="cl-", intents=intents, activity=discord.Activity(type=discord.ActivityType.watching, name="support tickets"))

bot.remove_command('help')

for fn in os.listdir('./cogs'):
	if fn.endswith('.py'):
		bot.load_extension(f"cogs.{fn[:-3]}")
  
  
  


@bot.listen()
async def on_ready():
    print(f'Bot has been activated! Modules loaded.')
    print(f'---------------------------------------')
    
    



def check_team(ctx):

    return bot.get_guild(928100287686774844)

@bot.listen()
async def on_connect():
    print('ready')








blacklist = []



@bot.listen()
async def on_message(message):
    pic_ext = ['.jpg','.png','.jpeg']
    if message.author.id == bot.user.id:
        return
    
    if message.author != message.author.bot:
        if not message.guild:
            
            
            if message.author.id not in blacklist:
                
            
                if len(message.attachments) > 0: #Checks if there are attachments
                    for file in message.attachments:
                        for ext in pic_ext:
                            if file.filename.endswith(ext):
                                print(file)
                                await message.add_reaction("📬")
                                await bot.get_guild(928100287686774844).get_channel(944672419749167134).send(f"User mention {message.author.mention}\nUsername: {message.author}\nUser-ID: {message.author.id}\n__**User Message:**__\n{message.content}__**File:**__\n{file}")
                                await bot.get_guild(928100287686774844).get_channel(944672419749167134).send("**------------------------------------**")
                        
                else:
                    await message.add_reaction("📬")
                    await bot.get_guild(928100287686774844).get_channel(944672419749167134).send(f"User mention {message.author.mention}\nUsername: {message.author}\nUser-ID: {message.author.id}\n__**User Message:**__\n{message.content}")
                    await bot.get_guild(928100287686774844).get_channel(944672419749167134).send("**------------------------------------**")
            
    
    
    
    

    
@bot.listen()
async def on_message_edit(before, after):
    if before.author.id == bot.user.id:
        return
    
    if before.author != before.author.bot:
        if not after.guild:
            
            
            if after.author.id not in blacklist:
            
                await after.author.send(":incoming_envelope: your message has been updated.")
                await bot.get_guild(928100287686774844).get_channel(944672419749167134).send(f"User mention {after.author.mention}\nUsername: {before.author}\nUser-ID: {after.author.id}\n\n__**Users old Message:**__ {before.content}\n__**Users new Message:**__ {after.content}")
                await bot.get_guild(928100287686774844).get_channel(944672419749167134).send("**------------------------------------**")
            
        


from discord.commands import Option

@bot.slash_command()
@commands.check(check_team)
async def pm(ctx, member: discord.Member, *, message, attachment: Option(discord.Attachment,"A file to attach to the message",required=False,),):

    
    channel = bot.get_channel(944672419749167134)
    await channel.send("Message sent to user.")
    
    if attachment == None:
        attachment = "Attachment status: None"
    await member.send(f":mailbox_with_mail: {message} {attachment}")

@bot.listen() # Bot reconnect
async def on_resumed():
    print('reconnected')
    
    
    
bot.run(token)