



import discord

from discord.ext import commands

import os

import json

import asyncio as asyncio

from discord.ext import *

from discord.ext.commands import *

from ctypes import *

from discord.commands import Option




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


modList = [513072262409355274, 831638031299117096] 

def check_Mod(ctx):
    if ctx.author.id in modList:
        return ctx.author.id in modList

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
                                embed=discord.Embed(title=":mailbox_with_mail:", color=0x1b96ff, description = "A message has been sent by a user!")
                                embed.add_field(name = "User :", value = f"{message.author}")
                                embed.add_field(name = "User-Mention :", value = f"{message.author.mention}")
                                embed.add_field(name = "User-ID :", value = f"{message.author.id}")
                                embed.add_field(name = "Message-Content :", value = f"{message.content}")
                                embed.add_field(name = "Attached-file :", value = f"{file}")
                                embed.set_footer(text = "Bot created by User319183#3149")
                                
                                await bot.get_guild(928100287686774844).get_channel(944672419749167134).send(embed=embed)
                                
                else:
                    await message.add_reaction("📬")
                    embed=discord.Embed(title=":mailbox_with_mail:", color=0x1b96ff, description = "A message has been sent by a user!")
                    embed.add_field(name = "User :", value = f"{message.author}")
                    embed.add_field(name = "User-Mention :", value = f"{message.author.mention}")
                    embed.add_field(name = "User-ID :", value = f"{message.author.id}")
                    embed.add_field(name = "Message-Content :", value = f"{message.content}")
                    embed.set_footer(text = "Bot created by User319183#3149")
                    await bot.get_guild(928100287686774844).get_channel(944672419749167134).send(embed=embed)
    
    
    
    

    
@bot.listen()
async def on_message_edit(before, after):
    if before.author.id == bot.user.id:
        return
    
    if before.author != before.author.bot:
        if not after.guild:
            
            
            if after.author.id not in blacklist:
            
        

                embed=discord.Embed(title=":mailbox_with_mail:", color=0x1b96ff, description = "Your message has been updated!")
                embed.set_footer(text = "Bot created by User319183#3149")
                await after.author.send(embed=embed)
                
                
                embed=discord.Embed(title=":mailbox_with_mail:", color=0x1b96ff, description = "A message has been sent by a user!")
                embed.add_field(name = "User :", value = f"{before.author}")
                embed.add_field(name = "User-Mention :", value = f"{after.author.mention}")
                embed.add_field(name = "User-ID :", value = f"{after.author.id}")
                embed.add_field(name = "Old-Message :", value = f"{before.content}")
                embed.add_field(name = "New-Message :", value = f"{after.content}")
                embed.set_footer(text = "Bot created by User319183#3149")
                await bot.get_guild(928100287686774844).get_channel(944672419749167134).send(embed=embed)
            

        




@bot.slash_command()
@commands.check(check_Mod)
async def pm(ctx, member: discord.Member, *, message, attachment: Option(discord.Attachment,"A file to attach to the message",required=False,),):

    embed=discord.Embed(title=":mailbox_with_mail:", color=0x1b96ff, description = "Message sent to user!")
    embed.set_footer(text = "Bot created by User319183#3149")
    await ctx.respond(embed=embed)

    
    if attachment == None:
        attachment = ""
        
    embed=discord.Embed(title=":mailbox_with_mail:", color=0x1b96ff, description = "You have received a message!")
    embed.add_field(name = "Message :", value = f"{message} {attachment}")
    embed.set_footer(text = "Bot created by User319183#3149")
    await member.send(embed=embed)









@bot.listen() # Bot reconnect
async def on_resumed():
    print('reconnected')
    

bot.run(token)
