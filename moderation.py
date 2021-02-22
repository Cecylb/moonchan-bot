import discord
import validators

async def moderate(message, client):
    if message.content != '':
        if not validators.url(message.content):
            oldChannel = message.channel.name
            channel = client.get_channel(784098859919081475)
            await channel.send(message.author.mention + ' only pics in #' + oldChannel)
            await message.delete()
