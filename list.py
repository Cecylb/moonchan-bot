import discord
from lxml import etree
from enum import Enum

class Parameters(Enum):
    RANK = 1
    TECH = 2
    TONE = 3
    PRICE = 4
    SETUP = 5

def getParam(message):
    param = message.content.split("$list ",1)[1]
    if param.startswith('rank='):
        return [Parameters.RANK, param.split('rank=',1)[1]]
    elif param.startswith('tech='):
        return [Parameters.TECH, param.split('tech=',1)[1]]
    elif param.startswith('tone='):
        return [Parameters.TONE, param.split('tone=',1)[1]]
    elif param.startswith('setup='):
        return [Parameters.SETUP, param.split('setup=',1)[1]]
    elif param.startswith('price'):
        parameters = param.split('price',1)[1]
        return [Parameters.PRICE, parameters[1:], parameters[:1]]

def compare (value1, value2, operand):
    if operand == '<':
        return value1 < value2
    elif operand == '>':
        return value1 > value2
    elif operand == '=':
        return value1 == value2

async def formListAnswer(selected, parameter, value, answer):
    if selected.lower() == parameter.lower():
        model = value + '\n'
        if len(answer + model) >= 2000:
            await message.channel.send(answer)
            answer = model
        else:
            answer = answer + model
    return answer

async def getList(message, rows):
    param = getParam(message)
    answer = ''
    for r in rows:
      cells = r.findChildren('td', {"class":"column-3"})
      for cell in cells:
        link = cell.findChildren('a')
        for l in link:
            value = l.string
            if value is None:
                value = 'xxx'
            param2 = ''
            if param[0] == Parameters.PRICE:
                price = r.find('td', {"class":"column-4"}).string or '99999'
                if price == 'Discontinued':
                    price = 99999;
                if compare(int(price), int(param[1]), param[2]):
                    model = value + '\n'
                    if len(answer + model) >= 2000:
                        await message.channel.send(answer)
                        answer = model
                    else:
                        answer = answer + model
                continue
            elif param[0] == Parameters.RANK:
                param2 = r.find('span').string or ''
            elif param[0] == Parameters.TECH:
                param2 = r.find('td', {"class":"column-8"}).string or ''
            elif param[0] == Parameters.TONE:
                param2 = r.find('td', {"class":"column-7"}).string or ''
            elif param[0] == Parameters.SETUP:
                param2 = r.find('td', {"class":"column-9"}).string or ''
            answer = await formListAnswer(param[1], param2, value, answer)
    await message.channel.send(answer)
