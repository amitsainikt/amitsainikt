from telebot import telebot
import requests
import random


CHAT_ID1 = '-1001261767165'

api = '2104950249:AAGrNKh8l3ZGtC10DrwyvB_PlFcfZg_ag-08'
bot = telebot.TeleBot(api)


@bot.message_handler(commands=['start'])
def start(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        bot.send_message(message.chat.id, 'Welcome, Type /commands for all commands')

    elif str(result.status) == 'creator':
        bot.send_message(message.chat.id, 'Welcome, Type /commands for all commands')
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')


@bot.message_handler(commands=['crunchy'])
def Crunchy_Roll(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://evilbane.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/MrCracker7100/c9eb5910887e507213718338680bdb97/raw/a5695241cd0b2b3e0983489d6c01a74a727d29c6/CrunchyRoll.txt')
            crunchysave = open("Crunchy Roll.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Crunchy Roll.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://evilbane.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/MrCracker7100/c9eb5910887e507213718338680bdb97/raw/a5695241cd0b2b3e0983489d6c01a74a727d29c6/CrunchyRoll.txt')
            crunchysave = open("Crunchy Roll.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Crunchy Roll.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')
    
    
@bot.message_handler(commands=['clear_limit'])
def clearing_limit(message):
    res = requests.get('https://evilbane.pythonanywhere.com/clear')
    bot.send_message(message.chat.id, "Cleared everyones limit")


@bot.message_handler(commands=['status'])
def checking_gen_status(message):
    status_check = "https://evilbane.pythonanywhere.com/status?uid="+str(message.chat.id)
    res = requests.get(status_check)
    if int(res.text) < 8:
        bot.reply_to(message, str(res.text) + " Accounts Generated yet")
    else:
        bot.reply_to(message, "You Have Generated All Your Accounts [8 Accounts]")


@bot.message_handler(commands=['adda247'])
def aada247(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://evilbane.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/MrCracker7100/e3b4d6e1c7c98f15cde1ef939556a353/raw/6488a536ccc7e349c33ab1f8d44e3845f6753eba/Adda247.txt')
            crunchysave = open("Adda 247.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Adda 247.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://evilbane.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/MrCracker7100/e3b4d6e1c7c98f15cde1ef939556a353/raw/6488a536ccc7e349c33ab1f8d44e3845f6753eba/Adda247.txt')
            crunchysave = open("Adda 247.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Adda 247.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')



@bot.message_handler(commands=['curiosity_steam'])
def curious(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://evilbane.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/MrCracker7100/8ae53eb24c9c07424c9038efef18a94e/raw/5335c8fc0b85046177b984c33121665d531475d9/CuriositySteam.txt')
            crunchysave = open("Curious.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Curious.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://evilbane.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/MrCracker7100/8ae53eb24c9c07424c9038efef18a94e/raw/5335c8fc0b85046177b984c33121665d531475d9/CuriositySteam.txt')
            crunchysave = open("Curious.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Curious.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
     
     
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')




@bot.message_handler(commands=['tunnel_bear'])
def tunnel(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://evilbane.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/MrCracker7100/fc4c7d75a6428425b8ac555028145749/raw/034a0e621529fbd3d84c7b466c03192ba37f2be6/TunnelBear.txt')
            crunchysave = open("tunnel.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("tunnel.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://evilbane.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/MrCracker7100/fc4c7d75a6428425b8ac555028145749/raw/034a0e621529fbd3d84c7b466c03192ba37f2be6/TunnelBear.txt')
            crunchysave = open("tunnel.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("tunnel.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
     
     
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')


@bot.message_handler(commands=['funimation'])
def fun(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://evilbane.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/MrCracker7100/cb90517785c5e3c1f92e8eddec695de4/raw/ccf54b6a4734d4254e862ee174b57e7636587c36/Funimation.txt')
            crunchysave = open("fun.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("fun.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://evilbane.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/MrCracker7100/cb90517785c5e3c1f92e8eddec695de4/raw/ccf54b6a4734d4254e862ee174b57e7636587c36/Funimation.txt')
            crunchysave = open("fun.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("fun.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
     
     
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')


@bot.message_handler(commands=['hulu'])
def hulu(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://evilbane.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/MrCracker7100/3f15db06ada22729debb3a0943840b08/raw/2412364c69ceded6c26f47508f92550856260622/Hulu.txt')
            crunchysave = open("hulu.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("hulu.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://evilbane.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/MrCracker7100/3f15db06ada22729debb3a0943840b08/raw/2412364c69ceded6c26f47508f92550856260622/Hulu.txt')
            crunchysave = open("hulu.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("hulu.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
     
     
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')


@bot.message_handler(commands=['doodly'])
def doodly(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://evilbane.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/MrCracker7100/8d907b9cac0aec7725dd6fbdd5745f16/raw/b2efa93904d79c4b7a8de2ac1f625dd1b503cc2d/Doodly.txt')
            crunchysave = open("doodly.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("doodly.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://evilbane.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/MrCracker7100/8d907b9cac0aec7725dd6fbdd5745f16/raw/b2efa93904d79c4b7a8de2ac1f625dd1b503cc2d/Doodly.txt')
            crunchysave = open("doodly.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("doodly.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
     
     
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')




@bot.message_handler(commands=['creator'])
def creator(message):
    bot.reply_to(message, "This Bot has been made by @Evil_BaneOP, For Paid Reuqests You can DM, can make configs, bots, tools, etc\n\nFor Any issues related to the bot bugs report me for issues like Account is bad report @RagnarLothbrock7100")

@bot.message_handler(commands=['commands'])
def commands(message):
    bot.reply_to(message, '''/crunchy - Generates a Crunchy Roll Account
/doodly - Generates a Doodly Account
/hulu - Generates a Hulu Account
/curiosity_steam - Generates a Curiosity Steam Account
/funimation - Generates a Funimation Account
/tunnel_bear - Generates a Tunnel Bear Account
/adda247 - Generates a Adda247 Account
/status - To check your Account status
/creator - To know about creator of Bot''')

bot.polling()
