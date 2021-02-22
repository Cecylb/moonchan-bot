import discord
import os
import requests
from bs4 import BeautifulSoup

from ranking import rank
from graph import graph
from help import getHelp
from list import getList
from moderation import moderate

client = discord.Client()
rankUrl = 'https://crinacle.com/rankings/iems/'
graphUrl = 'https://crinacle.com/graphs/iems/graphtool/'
harmanUrl = 'https://cdn2.jazztimes.com/2020/05/1_Harman-curve-target-response.png'
rangeUrl = 'https://reference-audio-analyzer.pro/img/frd1e.png'

headers = {'User-Agent': 'Mozilla/5.0'}

ranking = True
list = True
reply = True
link = True
moderation = True

def getTable():
    session = requests.Session()
    response = session.get(rankUrl, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    tables = soup.findChildren('table')
    table = tables[0]
    rows = []
    for r in table.findChildren(['th', 'tr']):
        rows.append(r)
    return rows

rows = getTable()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('$help'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$'):
        if message.content.startswith('$toggle '):
            if message.author.id == 267906078950293514:
                function = message.content.split("$toggle ",1)[1]
                if function == 'ranking':
                    global ranking
                    ranking = not ranking
                    await message.channel.send('ranking ' + ('enabled' if ranking else 'disabled'))
                elif function == 'list':
                    global list
                    list = not list
                    await message.channel.send('list ' + ('enabled' if list else 'disabled'))
                elif function == 'reply':
                    global reply
                    reply = not reply
                    await message.channel.send('reply ' + ('enabled' if reply else 'disabled'))
                elif function == 'link':
                    global link
                    link = not link
                    await message.channel.send('link ' + ('enabled' if link else 'disabled'))
                elif function == 'moderation':
                    global moderation
                    moderation = not moderation
                    await message.channel.send('moderation ' + ('enabled' if moderation else 'disabled'))
            else:
                await message.channel.send(message.author.mention + ' you don\'t have permission to use this function')

        if message.content.startswith('$ranking') and ranking:
            await rank(message, rows)

        if message.content.startswith('$list') and list:
            await getList(message, rows)

        if message.content.startswith('$graph'):
            await graph(message)

        if message.content.startswith('$harman') and link:
            await message.channel.send(harmanUrl)

        if message.content.startswith('$range') and link:
            await message.channel.send(rangeUrl)

        if message.content.startswith('$help'):
            await getHelp(message)

    if message.channel.name in ('iem-pics', 'headphone-pics') and moderation:
        await moderate(message, client)
    if "qt2" in message.content.lower() and reply:
        await message.channel.send('>qt2 \n cringe ')
    if "zishan " in message.content.lower() and reply:
        await message.channel.send('>zishan \n cringe ')
    if "dsd" in message.content.lower() and reply:
        await message.channel.send('>DSD \n take your meds ')

client.run('ODExOTk5NDI4NjcxMTc2NzY1.YC6XZg.cQ-fsexGzHCXU5rimH5xCdtDY2s')
