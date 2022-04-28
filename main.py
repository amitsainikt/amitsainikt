from telebot import telebot
import requests
import random

list1 = []

CHAT_ID1 = '-1001261767165'

api = '2104950249:AAGrNKh8l3ZGtC10DrwyvB_PlFcfZg_ag-0'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def start(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        bot.send_message(message.chat.id, 'Welcome, Type /commands for all commands')

    elif str(result.status) == 'creator':
        bot.send_message(message.chat.id, 'Welcome, Type /commands for all commands')
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarBKB_bot.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['crunchy'])
def Crunchy_Roll(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/4f86914c567061119e22463208c87bba/raw/2f15e25e4fd9deb9cedd79d74174a287ec95098a/Crunchy')
            crunchysave = open("Crunchy Roll.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Crunchy Roll.txt").read().splitlines()
            while True:
                
                account = random.choice(crunchysend)
                list1.append(account)
                counting_account = list1.count(account)
                if counting_account < 3:
                    break
                else:
                    continue
            
            
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/4f86914c567061119e22463208c87bba/raw/2f15e25e4fd9deb9cedd79d74174a287ec95098a/Crunchy')
            crunchysave = open("Crunchy Roll.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Crunchy Roll.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')
    
    
@bot.message_handler(commands=['Clear_sdfsdff'])
def clearing_limit(message):
    res = requests.get('https://aditisaini607080.pythonanywhere.com/clear')
    bot.send_message(message.chat.id, "Cleared everyones limit")


@bot.message_handler(commands=['status'])
def checking_gen_status(message):
    status_check = "https://aditisaini607080.pythonanywhere.com/status?uid="+str(message.chat.id)
    res = requests.get(status_check)
    if int(res.text) < 8:
        bot.reply_to(message, str(res.text) + " Accounts Generated yet")
    else:
        bot.reply_to(message, "You Have Generated All Your Accounts [8 Accounts]")

@bot.message_handler(commands=['Zee5'])
def Zee5(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/625e725c78152ea88bd934ee14982a55/raw/291655834e4442d4325ee905d1b0a0e8f95b6b3c/Zee5')
            crunchysave = open("Zee5.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Zee5.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/625e725c78152ea88bd934ee14982a55/raw/291655834e4442d4325ee905d1b0a0e8f95b6b3c/Zee5')
            crunchysave = open("Zee5.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Zee5.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')


@bot.message_handler(commands=['Altbalaji'])
def Altbalaji(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/dc3e2a2176db71c5f274a90ace39a5b2/raw/4278d1419a65c1d21947e32ec958aa601eba74c1/Altbalaji')
            crunchysave = open("Altbalaji.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Altbalaji.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/dc3e2a2176db71c5f274a90ace39a5b2/raw/4278d1419a65c1d21947e32ec958aa601eba74c1/Altbalaji')
            crunchysave = open("Altbalaji.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Altbalaji.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['UbiSoft'])
def UbiSoft(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://www.toptal.com/developers/hastebin/raw/ahoteyerom')
            crunchysave = open("UbiSoft.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("UbiSoft.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://www.toptal.com/developers/hastebin/raw/ahoteyerom')
            crunchysave = open("UbiSoft.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("UbiSoft.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['ParamountPlus'])
def ParamountPlus(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/6c96849e9557f178fa923633befa9030/raw/d850ae102e4983793d0ef7d81114b61b07ab492c/ParamountPlus')
            crunchysave = open("ParamountPlus.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("ParamountPlus.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/6c96849e9557f178fa923633befa9030/raw/d850ae102e4983793d0ef7d81114b61b07ab492c/ParamountPlus')
            crunchysave = open("ParamountPlus.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("ParamountPlus.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')
       

@bot.message_handler(commands=['IndianExpress'])
def IndianExpress(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/d8e2d62f29ee99a0c6549771e846d8ac/raw/7b93a41d6ca21a864e6d6b9f570468c170dfb0b8/IndianExpress')
            crunchysave = open("IndianExpress.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("IndianExpress.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/d8e2d62f29ee99a0c6549771e846d8ac/raw/7b93a41d6ca21a864e6d6b9f570468c170dfb0b8/IndianExpress')
            crunchysave = open("IndianExpress.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("IndianExpress.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')
       
@bot.message_handler(commands=['DisneyPlus'])
def DisneyPlus(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/7b338b1a0b4b84fbe28879137a45655a/raw/b6da75927058b97e87182c841edcb0a5c0c71882/DisneyPlus')
            crunchysave = open("DisneyPlus.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("DisneyPlus.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/7b338b1a0b4b84fbe28879137a45655a/raw/b6da75927058b97e87182c841edcb0a5c0c71882/DisneyPlus')
            crunchysave = open("DisneyPlus.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("DisneyPlus.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')
       
@bot.message_handler(commands=['Voot'])
def Voot(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/fc250a835ba0542685146c1ebeaf1e15/raw/f773f3acc9f9e3ccb74a07fd4b5a527173974631/Voot')
            crunchysave = open("Voot.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Voot.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/fc250a835ba0542685146c1ebeaf1e15/raw/f773f3acc9f9e3ccb74a07fd4b5a527173974631/Voot')
            crunchysave = open("Voot.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Voot.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')
       
@bot.message_handler(commands=['VisionIASss'])
def VisionIASss(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://www.toptal.com/developers/hastebin/raw/ilapehogey')
            crunchysave = open("VisionIAS.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("VisionIAS.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://www.toptal.com/developers/hastebin/raw/ilapehogey')
            crunchysave = open("VisionIAS.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("VisionIAS.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')
       
@bot.message_handler(commands=['Kooku'])
def Kooku(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/d9095c3f11a7f0696ee80d19c49b30e9/raw/002291ec5f0a4beecbae07749fac7e2de37b3b5b/Kooku')
            crunchysave = open("Kooku.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Kooku.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/d9095c3f11a7f0696ee80d19c49b30e9/raw/002291ec5f0a4beecbae07749fac7e2de37b3b5b/Kooku')
            crunchysave = open("Kooku.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Kooku.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')
       
@bot.message_handler(commands=['Careerwillllll'])
def Careerwill(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Amitt0134/a6940e19e753a4d4d1d2fde05b319892/raw/cb6ac7dba5912b88cd86cd57cc9398fc839a36b9/Careerwill')
            crunchysave = open("Careerwill.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Careerwill.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Amitt0134/a6940e19e753a4d4d1d2fde05b319892/raw/cb6ac7dba5912b88cd86cd57cc9398fc839a36b9/Careerwill')
            crunchysave = open("Careerwill.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Careerwill.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')
       
@bot.message_handler(commands=['SunNxt'])
def SunNxt(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/d8a5efa393f2be289aaad3210de6835e/raw/66273326056eb43145ede88d02966e5405918da9/Sunnxt')
            crunchysave = open("SunNxt.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("SunNxt.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/d8a5efa393f2be289aaad3210de6835e/raw/66273326056eb43145ede88d02966e5405918da9/Sunnxt')
            crunchysave = open("SunNxt.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("SunNxt.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')
       

@bot.message_handler(commands=['TheHindu'])
def TheHindu(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Amitt0134/ca478340085efec4c79fa3f52992a875/raw/fa56ec939f74904d2f4a65d73bbd7738e4ff90c5/The%2520Hindu')
            crunchysave = open("TheHindu.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("TheHindu.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Amitt0134/ca478340085efec4c79fa3f52992a875/raw/fa56ec939f74904d2f4a65d73bbd7738e4ff90c5/The%2520Hindu')
            crunchysave = open("TheHindu.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("TheHindu.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')
       

@bot.message_handler(commands=['SmartKeeda'])
def SmartKeeda(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/a6e5882f0223b9b33cfac1f3fc4f1d5a/raw/87965d7f9f1a9650e767a8d802453ca46cc229d6/SmartKeeda')
            crunchysave = open("SmartKeeda.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("SmartKeeda.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/a6e5882f0223b9b33cfac1f3fc4f1d5a/raw/87965d7f9f1a9650e767a8d802453ca46cc229d6/SmartKeeda')
            crunchysave = open("SmartKeeda.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("SmartKeeda.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')
       
@bot.message_handler(commands=['HoiChoi'])
def HoiChoi(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/225c06b8e84c5c95617869812815ebc2/raw/93972eae6c51551424454caf495ea212aa0ba393/Hoichoi')
            crunchysave = open("HoiChoi.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("HoiChoi.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/225c06b8e84c5c95617869812815ebc2/raw/93972eae6c51551424454caf495ea212aa0ba393/Hoichoi')
            crunchysave = open("HoiChoi.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("HoiChoi.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')
       

@bot.message_handler(commands=['Adda247'])
def Adda247(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/f26bf2303e0bd784b6d9a617f9e31a91/raw/7be2fc96a110c200871aa56848469c443f0b02f9/Adda247')
            crunchysave = open("Adda247.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Adda247.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/f26bf2303e0bd784b6d9a617f9e31a91/raw/7be2fc96a110c200871aa56848469c443f0b02f9/Adda247')
            crunchysave = open("Adda247.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Adda247.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')
       
@bot.message_handler(commands=['Testbook'])
def Testbook(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/ca8540ef3924a85e0ad3dff9e36412be/raw/0fc34879e01989e96682af0688a71977886dedd6/Testbook')
            crunchysave = open("Testbook.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Testbook.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/ca8540ef3924a85e0ad3dff9e36412be/raw/0fc34879e01989e96682af0688a71977886dedd6/Testbook')
            crunchysave = open("Testbook.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Testbook.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['TotalAntivirus'])
def TotalAntivirus(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/f9321a083cd6c3797ca398eb20a7078a/raw/15dbe8d3522d29ceb35795643a8aac405c37da73/TotalAntivirus')
            crunchysave = open("TotalAntivirus.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("TotalAntivirus.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/f9321a083cd6c3797ca398eb20a7078a/raw/15dbe8d3522d29ceb35795643a8aac405c37da73/TotalAntivirus')
            crunchysave = open("TotalAntivirus.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("TotalAntivirus.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['RojgarWithAnkit'])
def RojgarWithAnkit(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/72227d40f730970ede7750adb8873bb7/raw/6c5e36e60cab41f930bd8a70a6caa267039c4659/RWA')
            crunchysave = open("RojgarWithAnkit.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("RojgarWithAnkit.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/72227d40f730970ede7750adb8873bb7/raw/6c5e36e60cab41f930bd8a70a6caa267039c4659/RWA')
            crunchysave = open("RojgarWithAnkit.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("RojgarWithAnkit.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['Ullu'])
def Ullu(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/69abf7719f1b3ab003a02ef1fd19ca9c/raw/f28abf6978844940f16ac8603bd95911863667b2/Ullu')
            crunchysave = open("Ullu.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Ullu.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/69abf7719f1b3ab003a02ef1fd19ca9c/raw/f28abf6978844940f16ac8603bd95911863667b2/Ullu')
            crunchysave = open("Ullu.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Ullu.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['VisionIASsss'])
def VisionIASsss(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/f66b84031fc834488f4e6be9a19a3009/raw/1afb98b88c8b347f772f0aa5007f8669f18eba51/VisionIAS')
            crunchysave = open("VisionIASsss.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("VisionIASsss.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/f66b84031fc834488f4e6be9a19a3009/raw/1afb98b88c8b347f772f0aa5007f8669f18eba51/VisionIAS')
            crunchysave = open("VisionIASsss.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("VisionIASsss.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')


@bot.message_handler(commands=['Adda247P2'])
def Adda247P2(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/feeb7890b5d648262cfc611ceaf6e56b/raw/56afee00bec9b04fde00ca62214f67674ccb02ed/Adda247P2')
            crunchysave = open("Adda247P2.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Adda247P2.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/feeb7890b5d648262cfc611ceaf6e56b/raw/56afee00bec9b04fde00ca62214f67674ccb02ed/Adda247P2')
            crunchysave = open("Adda247P2.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Adda247P2.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['McAfeeAntivirus'])
def McAfeeAntivirus(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Amitt0134/abe647d1f880f904d272eccdf9ae4d5a/raw/a6371b5b600439c171faaa833e2d24f138cbd9e6/Mcafee')
            crunchysave = open("McAfeeAntivirus.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("McAfeeAntivirus.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Amitt0134/abe647d1f880f904d272eccdf9ae4d5a/raw/a6371b5b600439c171faaa833e2d24f138cbd9e6/Mcafee')
            crunchysave = open("McAfeeAntivirus.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("McAfeeAntivirus.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['JeevanSathi'])
def JeevanSathi(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://www.toptal.com/developers/hastebin/raw/irekuwupup')
            crunchysave = open("JeevanSathi.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("JeevanSathi.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://www.toptal.com/developers/hastebin/raw/irekuwupup')
            crunchysave = open("JeevanSathi.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("JeevanSathi.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['MeetMe'])
def MeetMe(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://www.toptal.com/developers/hastebin/raw/uxomelofam')
            crunchysave = open("MeetMe.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("MeetMe.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://www.toptal.com/developers/hastebin/raw/uxomelofam')
            crunchysave = open("MeetMe.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("MeetMe.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['Paytm'])
def Paytm(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://www.toptal.com/developers/hastebin/raw/xequzarige')
            crunchysave = open("Paytm.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Paytm.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://www.toptal.com/developers/hastebin/raw/xequzarige')
            crunchysave = open("Paytm.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Paytm.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['YuppTv'])
def YuppTv(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/e0e9835df848b39f4fb7535613b0c8d9/raw/48e62ddda89092f8e12e861481a75c65fe0d3e78/YuppTv')
            crunchysave = open("YuppTv.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("YuppTv.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/e0e9835df848b39f4fb7535613b0c8d9/raw/48e62ddda89092f8e12e861481a75c65fe0d3e78/YuppTv')
            crunchysave = open("YuppTv.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("YuppTv.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['EduTap'])
def EduTap(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/83cfe69022b7db700e004c3bc6341a6e/raw/46b1856f73eedfec5d668d2d021815fca1b58ad8/EduTap')
            crunchysave = open("EduTap.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("EduTap.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/83cfe69022b7db700e004c3bc6341a6e/raw/46b1856f73eedfec5d668d2d021815fca1b58ad8/EduTap')
            crunchysave = open("EduTap.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("EduTap.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['Spotify'])
def Spotify(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/19KwmwNMBX2iWXa9Zs63vcH86LK7Mw8vpL/raw/e65445a094c166dd8c0f38a68ab9c07d5e653686/Spotify')
            crunchysave = open("Spotify.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Spotify.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/19KwmwNMBX2iWXa9Zs63vcH86LK7Mw8vpL/raw/e65445a094c166dd8c0f38a68ab9c07d5e653686/Spotify')
            crunchysave = open("Spotify.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Spotify.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['AakashiTutor'])
def AakashiTutor(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://www.toptal.com/developers/hastebin/raw/zinoyowipa')
            crunchysave = open("AakashiTutor.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("AakashiTutor.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://www.toptal.com/developers/hastebin/raw/zinoyowipa')
            crunchysave = open("AakashiTutor.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("AakashiTutor.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['Exampur'])
def Exampur(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Amitt0134/d7a0baf7c2d91aec0150142feab6a5b4/raw/2a7ad28d21c98ff16ba6fbe80f649cc5e988b40e/Exampur')
            crunchysave = open("Exampur.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Exampur.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Amitt0134/d7a0baf7c2d91aec0150142feab6a5b4/raw/2a7ad28d21c98ff16ba6fbe80f649cc5e988b40e/Exampur')
            crunchysave = open("Exampur.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Exampur.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')


@bot.message_handler(commands=['Symbolab'])
def Symbolab(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://www.toptal.com/developers/hastebin/raw/ugayeharud')
            crunchysave = open("Symbolab.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Symbolab.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://www.toptal.com/developers/hastebin/raw/ugayeharud')
            crunchysave = open("Symbolab.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Symbolab.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')


@bot.message_handler(commands=['NetflixMIX'])
def NetflixMIX(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/743db6d46f6ec48db09cedd5d57d305e/raw/14c528afad34e8a6ba81125f4f0f0d3229f200d6/NetflixMIX')
            crunchysave = open("NetflixMIX.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("NetflixMIX.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/743db6d46f6ec48db09cedd5d57d305e/raw/14c528afad34e8a6ba81125f4f0f0d3229f200d6/NetflixMIX')
            crunchysave = open("NetflixMIX.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("NetflixMIX.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['Nba'])
def Nba(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/daff9a7ea5cf28b7e014a3e8936f029a/raw/b6bb8784125cc6fbef8f0e76e17560ce9fb64be6/NBA')
            crunchysave = open("Nba.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Nba.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/daff9a7ea5cf28b7e014a3e8936f029a/raw/b6bb8784125cc6fbef8f0e76e17560ce9fb64be6/NBA')
            crunchysave = open("Nba.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Nba.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['Spicejet'])
def Spicejet(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Amitt0134/4d2fac086994d822bf5ece2272cf6453/raw/9b0f9e0c060a903ed2d9283894ca38a1039fa7ca/Spicejet')
            crunchysave = open("Spicejet.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Spicejet.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Amitt0134/4d2fac086994d822bf5ece2272cf6453/raw/9b0f9e0c060a903ed2d9283894ca38a1039fa7ca/Spicejet')
            crunchysave = open("Spicejet.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Spicejet.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['Vooks'])
def Vooks(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Amitt0134/792e476989986877c0359020c7e11983/raw/5918d1878d4b91f364ed7a9f728fa357bdcf14e2/Vooks')
            crunchysave = open("Vooks.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Vooks.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Amitt0134/792e476989986877c0359020c7e11983/raw/5918d1878d4b91f364ed7a9f728fa357bdcf14e2/Vooks')
            crunchysave = open("Vooks.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Vooks.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['Hungama'])
def Hungama(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Amitt0134/32046208c57e579e8230c48907226f73/raw/e5ce5c7983ee8a0132f281c4b9423bf9f522bfeb/Hungama')
            crunchysave = open("Hungama.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Hungama.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Amitt0134/32046208c57e579e8230c48907226f73/raw/e5ce5c7983ee8a0132f281c4b9423bf9f522bfeb/Hungama')
            crunchysave = open("Hungama.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Hungama.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['VirtualDJ'])
def VirtualDJ(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Amitt0134/c0163476c6c5d69a2f980e299dbab96d/raw/193021dee12a979c4193f028e3fcee28b63def8d/VirtualDJ')
            crunchysave = open("VirtualDJ.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("VirtualDJ.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Amitt0134/c0163476c6c5d69a2f980e299dbab96d/raw/193021dee12a979c4193f028e3fcee28b63def8d/VirtualDJ')
            crunchysave = open("VirtualDJ.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("VirtualDJ.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['EduRev'])
def EduRev(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/pihukk7100/c6db1f729af7642a01839a727a9b3818/raw/6003381241ded309eadafd54befcd33e1f568368/EduRev')
            crunchysave = open("EduRev.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("EduRev.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/pihukk7100/c6db1f729af7642a01839a727a9b3818/raw/6003381241ded309eadafd54befcd33e1f568368/EduRev')
            crunchysave = open("EduRev.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("EduRev.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['Aha'])
def Aha(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/pihukk7100/70b791b41ca8e4f1f7a222653228b735/raw/15e3b9215a91b966e4b45a2940deac1f0239ec02/Aha')
            crunchysave = open("Aha.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Aha.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/pihukk7100/70b791b41ca8e4f1f7a222653228b735/raw/15e3b9215a91b966e4b45a2940deac1f0239ec02/Aha')
            crunchysave = open("Aha.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Aha.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['LifeSelector'])
def LifeSelector(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/e8c11d621b29ff8f1149b3184e0fac9a/raw/7b21766dae5dd53b137bedd032409a4a2a44f6e9/Life')
            crunchysave = open("LifeSelector.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("LifeSelector.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/e8c11d621b29ff8f1149b3184e0fac9a/raw/7b21766dae5dd53b137bedd032409a4a2a44f6e9/Life')
            crunchysave = open("LifeSelector.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("LifeSelector.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['NetflixBasic'])
def NetflixBasic(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/55ae75697605450c50ce3beb1664788f/raw/bcaaecdd6094e72453e3856264bf8e1e2cd9ba89/NetflixBasic')
            crunchysave = open("NetflixBasic.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("NetflixBasic.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/55ae75697605450c50ce3beb1664788f/raw/bcaaecdd6094e72453e3856264bf8e1e2cd9ba89/NetflixBasic')
            crunchysave = open("NetflixBasic.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("NetflixBasic.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['Breethe'])
def Breethe(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/4632dae3f45e4fd20341aec4112037a9/raw/fcc3c4b81eef862e7b2775095d5ec2eb873c6685/Breethe')
            crunchysave = open("Breethe.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Breethe.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/4632dae3f45e4fd20341aec4112037a9/raw/fcc3c4b81eef862e7b2775095d5ec2eb873c6685/Breethe')
            crunchysave = open("Breethe.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Breethe.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['Wondershare'])
def Wondershare(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://www.toptal.com/developers/hastebin/raw/ohamahuduy')
            crunchysave = open("Wondershare.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Wondershare.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://www.toptal.com/developers/hastebin/raw/ohamahuduy')
            crunchysave = open("Wondershare.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Wondershare.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['MoneyControl'])
def MoneyControl(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/c4f8143864ff63535d768bf2ff7eafa3/raw/531db53b5b7e25115863643e47c10ae4b9edc4a8/MoneyControl')
            crunchysave = open("MoneyControl.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("MoneyControl.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/c4f8143864ff63535d768bf2ff7eafa3/raw/531db53b5b7e25115863643e47c10ae4b9edc4a8/MoneyControl')
            crunchysave = open("MoneyControl.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("MoneyControl.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['RachanaRanade'])
def RachanaRanade(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/d96b9566fd038077d66da8c48251d94d/raw/1417e2c88ca87738b9e1e4ba65feb08451bb3a98/Rachna')
            crunchysave = open("RachanaRanade.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("RachanaRanade.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/d96b9566fd038077d66da8c48251d94d/raw/1417e2c88ca87738b9e1e4ba65feb08451bb3a98/Rachna')
            crunchysave = open("RachanaRanade.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("RachanaRanade.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['CuriosityStream'])
def CuriosityStream(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/4f61e8abb77a34dbc4f4cb66828c0971/raw/472ddd5e3f415d3538f9a3727bd75d72d7796a84/CuriositySteam')
            crunchysave = open("CuriosityStream.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("CuriosityStream.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/4f61e8abb77a34dbc4f4cb66828c0971/raw/472ddd5e3f415d3538f9a3727bd75d72d7796a84/CuriositySteam')
            crunchysave = open("CuriosityStream.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("CuriosityStream.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['KhanGS'])
def KhanGS(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/5b0e95008b95d536a429a3191dcae4b4/raw/43c70a0c7525a121cc685b2d2369bfc69f971187/KhanGS')
            crunchysave = open("KhanGS.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("KhanGS.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/5b0e95008b95d536a429a3191dcae4b4/raw/43c70a0c7525a121cc685b2d2369bfc69f971187/KhanGS')
            crunchysave = open("KhanGS.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("KhanGS.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['Fox'])
def Fox(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/f22469f95e56a3718d6277f8c2d88177/raw/5d48c51fd2e3ad33c8a6807574c8f5b952e8a4f5/Fox')
            crunchysave = open("Fox.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Fox.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/f22469f95e56a3718d6277f8c2d88177/raw/5d48c51fd2e3ad33c8a6807574c8f5b952e8a4f5/Fox')
            crunchysave = open("Fox.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Fox.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['Nfhs'])
def Nfhs(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/6c722be941b1567896d2ab12081ca651/raw/6a5d3407050559f4803385d347e783e42147b633/NFHS')
            crunchysave = open("Nfhs.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Nfhs.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/6c722be941b1567896d2ab12081ca651/raw/6a5d3407050559f4803385d347e783e42147b633/NFHS')
            crunchysave = open("Nfhs.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Nfhs.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['SleepCycle'])
def SleepCycle(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/fa8a6a95e2c812bc4be3a65071628701/raw/4dfae4b21f55a67943ede05b85fb6ab33b0375ca/SleepCycle')
            crunchysave = open("SleepCycle.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("SleepCycle.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/fa8a6a95e2c812bc4be3a65071628701/raw/4dfae4b21f55a67943ede05b85fb6ab33b0375ca/SleepCycle')
            crunchysave = open("SleepCycle.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("SleepCycle.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['LionsgatePlay'])
def LionsgatePlay(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/8275254b159d35085b352270537eb5ff/raw/dd76558a082b0166650579c28c335427a9fef21e/LionsgatePlay')
            crunchysave = open("LionsgatePlay.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("LionsgatePlay.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/8275254b159d35085b352270537eb5ff/raw/dd76558a082b0166650579c28c335427a9fef21e/LionsgatePlay')
            crunchysave = open("LionsgatePlay.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("LionsgatePlay.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['Imvu'])
def Imvu(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/ea28d16767acb30cc549958370916169/raw/4878190aac3507b3ad1a5d2165869e41d88c569a/Imvu')
            crunchysave = open("Imvu.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Imvu.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/ea28d16767acb30cc549958370916169/raw/4878190aac3507b3ad1a5d2165869e41d88c569a/Imvu')
            crunchysave = open("Imvu.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Imvu.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['Unacademy'])
def Unacademy(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/e0349740006e225c3ce7664f63760ce1/raw/60f07f39411c1253fb60bbe6217815dc80b0f3d7/Unacademy')
            crunchysave = open("Unacademy.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Unacademy.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/e0349740006e225c3ce7664f63760ce1/raw/60f07f39411c1253fb60bbe6217815dc80b0f3d7/Unacademy')
            crunchysave = open("Unacademy.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("Unacademy.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['ATT'])
def ATT(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/d30652e135e48a896fa626f4960a3a09/raw/6de3e2bf1f3055b7149f4c2e7abf29576c25b830/ATT')
            crunchysave = open("ATT.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("ATT.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/Aditisaini001100/d30652e135e48a896fa626f4960a3a09/raw/6de3e2bf1f3055b7149f4c2e7abf29576c25b830/ATT')
            crunchysave = open("ATT.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("ATT.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')

@bot.message_handler(commands=['VmartAcademy'])
def VmartAcademy(message):
    result = bot.get_chat_member(CHAT_ID1, message.chat.id)
    if str(result.status) == 'member':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/e5b03f8c6cba2ef6c7309402b887a54f/raw/0eb70b581c80661d21bcddd3f9940aec7065a49d/VmartAcademy')
            crunchysave = open("VmartAcademy.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("VmartAcademy.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)

    elif str(result.status) == 'creator':
        limiting = 'https://aditisaini607080.pythonanywhere.com/limit?uid='+str(message.chat.id)
        reslimit = requests.get(limiting)
        print(reslimit.text)
        if 'Success' not in reslimit.text:
            bot.reply_to(message, "Today's Limit Reached")
        else:
            res = requests.get('https://gist.githubusercontent.com/amitkumar3596/e5b03f8c6cba2ef6c7309402b887a54f/raw/0eb70b581c80661d21bcddd3f9940aec7065a49d/VmartAcademy')
            crunchysave = open("VmartAcademy.txt", 'w')
            crunchysave.write(res.text)
            crunchysave.close()
            crunchysend = open("VmartAcademy.txt").read().splitlines()
            account = random.choice(crunchysend)
            bot.reply_to(message,account)
    
    else:
        bot.send_message(message.chat.id, 'This is a Private Bot, You cannot use this Bot until the owner of bot gives you permission.\nTo use this bot please contact the owner @RagnarLothbrok7100.\n\nCreator of Bot: @Evil_BaneOP')



        
@bot.message_handler(commands=['creator'])
def creator(message):
    bot.reply_to(message, "This Bot has been made by @Evil_BaneOP, For Paid Reuqests You can DM, can make configs, bots, tools, etc\n\nFor Any issues related to the bot bugs report me for issues like Account is bad report @RagnarLothbrock7100")

@bot.message_handler(commands=['commands'])
def commands(message):
    bot.reply_to(message, '''Streaming
/NetflixMIX
/NetflixBasic
/ATT
/Nba
/Fox
/Aha
/Nfhs
/Zee5
/Ullu
/Voot
/Kooku
/YuppTv
/SunNxt
/Hungama
/HoiChoi
/crunchy
/VirtualDJ
/Altbalaji
/DisneyPlus
/ParamountPlus
/LionsgatePlay
/CuriosityStream

Education
/Vooks
/KhanGS
/EduTap
/EduRev
/Adda247
/Adda247P2
/SscTube
/Exampur
/Symbolab
/Testbook
/TheHindu
/Unacademy
/SmartKeeda
/VmartAcademy
/AakashiTutor
/IndianExpress
/RachanaRanade
/RojgarWithAnkit

Antivirus
/TotalAntivirus
/McAfeeAntivirus

Dating
/Imvu
/MeetMe
/JeevanSathi

Porn
/LifeSelector

Mix
/Paytm
/UbiSoft
/Spicejet
/Breethe
/SleepCycle
/Wondershare
/MoneyControl
''')

bot.polling()
