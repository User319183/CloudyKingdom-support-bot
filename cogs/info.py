import discord

from discord.ext import commands

from discord import activity

from discord.commands import Option

import os
import sys

import json

import asyncio as asyncio

import re
import string


from discord.ext import *
from discord.ext.commands import *
from ctypes import *
import datetime

from discord import Message

import aiohttp





class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    
    
    
    
    
    @commands.command()
    async def info(self, ctx: commands.Context):               
                        
        embed = discord.Embed(title="Bot Info", description="My help panel", color=0xD708CC)
        embed.add_field(name="__Bot Creator:__", value="User319183#3149", inline=True) # please don't remove credits!!


        await ctx.send(embed=embed)
 




       
       
             
                    
def setup(bot):
	bot.add_cog(Info(bot))