# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 23:01:48 2021

@author: Simon
"""

import os
import discord

client = discord.Client()

channelID = 854502157806338078


@client.event
async def on_message(message):
    
    if message.channel.id == channelID:
        
        userID = message.author.id
        
        channel = client.get_channel(channelID)
        
        messageID = []
        
        async for message in channel.history():
            if message.author.id == userID:
                messageID.append(message.id)
        
        if len(messageID) > 1.5:
            msg = await channel.fetch_message(messageID[1])
            await msg.delete()



client.run(os.environ['Token'])