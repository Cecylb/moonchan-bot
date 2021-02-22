import discord

async def getHelp(message):
    answer = '[commands]\n' + '$ranking *model* - iem ranking info\n' + '$list tech/rank/tone/setup/price=*value* - search by parameter (WIP)\n' + '$graph - graph tool page\n' + '$harman - show harman curve\n' + '$range - show tone range'
    with open('help.png', 'rb') as f:
        picture = discord.File(f)
        await message.channel.send(answer, file=picture)
