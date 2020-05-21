import discord 

#create a discord client  
client = discord.Client()

#on message event handler 
@client.event
async def on_message(message):
	 #Ignore if he bot is the author 
	 if message.author == client.user:
	 	return
	 await message.channel.send(message.content)

#run our bot
client.run('your token here')
