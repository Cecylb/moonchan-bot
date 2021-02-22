import discord
from bs4 import BeautifulSoup

async def rank(message, rows):
    model = message.content.split("$ranking ",1)[1]
    isResult = False
    for r in rows:
        cells = r.findChildren('td', {"class":"column-3"})
        for cell in cells:
            link = cell.findChildren('a')
            for l in link:
                value = l.string
                if value is None:
                  value = 'xxx'
                if model.lower() in value.lower():
                    price = r.find('td', {"class":"column-4"}).string or ''
                    rank = r.find('span').string or ''
                    tonality = r.find('td', {"class":"column-7"}).string or ''
                    tech = r.find('td', {"class":"column-8"}).string or ''
                    setup = r.find('td', {"class":"column-9"}).string or ''
                    comment = r.find('td', {"class":"column-6"}).string or ''
                    answer = '[' + value + ']' + '\n' + 'Price: ' + price + '\n'+ 'Rank: ' +  rank + '\n' + 'Tonality: ' + tonality  + '\n' + 'Technicalities: ' + tech + '\n' + 'Setup: ' + setup + '\n' + comment
                    isResult = True;
                    await message.channel.send(answer)
    if not isResult:
        answer = 'Not found. Sorry...'
        with open('error.png', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(answer, file=picture)                
