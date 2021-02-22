import discord
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

async def graph(message):
    answer = 'under construction'
    with open('wip.png', 'rb') as f:
        picture = discord.File(f)
        await message.channel.send(answer, file=picture)
        return
    driver = webdriver.Firefox()
    driver.get(graphUrl)
    elem = driver.find_elements_by_xpath("//*[@type='submit']")#put here the content you have put in Notepad, ie the XPath
    button = driver.find_element_by_id('buttonID')
    print(elem.get_attribute("class"))
    driver.close()
