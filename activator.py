from pyrogram import Client, filters, idle
import threading
import pyrogram
from datetime import datetime
import time
import os
from pyrogram.errors import FloodWait
lock = threading.Lock()
autoactivate = True
send_to_channel = True
to_channel_base = -672133124
channel_for_checks = -834347471
my_apps = [
    Client('#name', "api id" , "api hash"),
]

app = my_apps[0]

used_checks = []
a3 = False
def check_checks(link):
    global used_checks
    if link in used_checks:
        return True
    else:
        return False


def send_to_channel_func(chat_id, msg_id, link):
    try:
        app.send_message(to_channel_base,f'Найден новый чек, ссылка на чек: https://t.me/{app.get_chat(chat_id).username}/{msg_id}')
    except FloodWait as e:
        print(f"Telegram is sending too many requests! Waiting {e.x}s...")
        time.sleep(e.x)
        send_to_channel_func(chat_id, msg_id, link)


def send_to_bot_wallet(link):
    global used_checks
    global autoactivate
    if autoactivate and not check_checks(link):
        for app in my_apps:
            app.send_message("wallet", f"/start {link.split('=')[1]}")
    else:
        print('Yzeuzali')
def send_to_bot_crypto(link):
    for app in my_apps:
        global autoactivate
        if autoactivate:
            if not check_checks(link):
                aaaa = app.send_message("CryptoBot", f"/start {link.split('=')[1]}").id + 1

                timing = 100
                iiii = 0
                while iiii < timing:
                    if app.get_messages("CryptoBot", aaaa).empty == True:
                        iiii = iiii + 1
                    else:
                        iiii = timing + 1
                arara = app.get_messages("CryptoBot", aaaa).text.find("получили")
                brbrb = app.get_messages("CryptoBot", aaaa).text.find("подпишитесь")
                if arara >= 0:
                    print(app.get_messages("CryptoBot", aaaa).text)
                elif brbrb >= 0:
                    print('brbrbr')
                    iii = 0
                    while app.get_messages("CryptoBot", aaaa).reply_markup.inline_keyboard[iii][0].url != None:
                        print(iii, app.get_messages("CryptoBot", aaaa).reply_markup.inline_keyboard[iii][0].url)
                        try:
                            app.join_chat(app.get_messages("CryptoBot", aaaa).reply_markup.inline_keyboard[iii][0].url)
                        except Exception as e:
                            print(e)
                        iii = iii + 1
                    send_to_bot_crypto(link)
                else:
                    pass
            else:
                print('Yzeuzali')

def otpravka_chekov(link):
    global a3
    a3=False
    for app in my_apps:
        global autoactivate
        if autoactivate:
            aaaa = app.send_message("TonRocketBot", f"/cheques").id + 1
            process_response(app, aaaa)
            sssss = app.get_messages("TonRocketBot", aaaa)
            app.request_callback_answer(sssss.chat.id, sssss.id, sssss.reply_markup.inline_keyboard[0][0].callback_data)
            sssss = app.get_messages("TonRocketBot", aaaa)
            app.request_callback_answer(sssss.chat.id, sssss.id, sssss.reply_markup.inline_keyboard[0][0].callback_data)
            sssss = app.get_messages("TonRocketBot", aaaa)
            proverka = sssss.reply_markup.inline_keyboard[0][0].text.find("чеки")
            proverka2 = sssss.reply_markup.inline_keyboard[0][0].text.find("Пополнение")
            if proverka == -1 and proverka2 == -1:
                app.request_callback_answer(sssss.chat.id, sssss.id,
                                            sssss.reply_markup.inline_keyboard[0][0].callback_data)
                sssss = app.get_messages("TonRocketBot", aaaa)
                app.request_callback_answer(sssss.chat.id, sssss.id,
                                            sssss.reply_markup.inline_keyboard[0][0].callback_data)
                sssss = app.get_messages("TonRocketBot", aaaa)
                app.request_callback_answer(sssss.chat.id, sssss.id,
                                            sssss.reply_markup.inline_keyboard[0][0].callback_data)
                sssss = app.get_messages("TonRocketBot", aaaa)
                app.send_message(channel_for_checks, f"Нажми получить {sssss.text}")
            else:
                pass
def process_response(app, aaaa):
    timing = 100
    iiii = 0
    while iiii < timing:
        response = app.get_messages("TonRocketBot", aaaa)
        if response.empty:
            iiii = iiii + 1
        else:
            iiii = timing + 1
            return response
def handle_photo_response(app, response):
    for i1 in range(2):
        for j in range(2):
            le = 0
            for letter in response.reply_markup.inline_keyboard[i1][j].text:
                le += 1
                if (letter == "🎮" or letter == "🇳") and le == 1:
                    app.request_callback_answer(response.chat.id, response.id,
                                                response.reply_markup.inline_keyboard[i1][j].callback_data)
                    break
            if le == 1:
                break
        if le == 1:
            break

def join_groups(app, response):
    iii = 0
    while response.reply_markup.inline_keyboard[iii][0].url:
        try:
            group_name = response.reply_markup.inline_keyboard[iii][0].url.split('https://t.me/')[1]
            app.join_chat(group_name)
        except Exception as e:
            print(e)
        iii = iii + 1
def send_to_bot_rocket(link):
    global a3
    for app in my_apps:
        global autoactivate
        if autoactivate:
            if not check_checks(link):
                aaaa = app.send_message("TonRocketBot", f"/start {link.split('=')[1]}").id + 1
                response = process_response(app, aaaa)
                if response.photo:
                    while response.photo:
                        handle_photo_response(app, response)
                        response = app.get_messages("TonRocketBot", aaaa)
                    response = app.get_messages("TonRocketBot", aaaa + 2)
                    if not response.empty and response.text.find("получили"):
                        a3 = True
                elif response.text.find('необходимо'):
                    join_groups(app, response)
                    aaaa = app.send_message("TonRocketBot", f"/start {link.split('=')[1]}").id + 1
                    response = process_response(app, aaaa)
                    if response.photo:
                        while response.photo:
                            handle_photo_response(app, response)
                            response = app.get_messages("TonRocketBot", aaaa)
                        response = app.get_messages("TonRocketBot", aaaa + 2)
                        if not response.empty and response.text.find("получили"):
                            a3 = True
            else:
                print('Yzeuzali')

@app.on_message(filters.command('aa', prefixes='.') & filters.me)
def aa(_, msg):
    global autoactivate
    if autoactivate == True:
        autoactivate = False
        print('== AUT0 ACT1VATE 0FF ==')
    else:
        autoactivate = True
        print('== AUT0 ACT1VATE 0N ==')
    msg.delete()


@app.on_message(filters.command('sc', prefixes='.') & filters.me)
def sc(_, msg):
    global send_to_channel
    if send_to_channel == True:
        send_to_channel = False
        print('== SEND T0 CHANNEL 0FF ==')
    else:
        send_to_channel = True
        print('== SEND T0 CHANNEL 0N ==')
    msg.delete()


@app.on_message(filters.command('usedchecks', prefixes='.') & filters.me)
def usedchecks(_, msg):
    print(used_checks)


@app.on_message(filters.command('info', prefixes='.') & filters.me)
def info(_, msg):
    print(msg.reply_to_message)
    msg.delete()


@app.on_message(filters.command('fromchatid', prefixes='.') & filters.me)
def fromchatid(_, msg):
    msg.edit(msg.reply_to_message.forward_from_chat.id)
try:
    print(f" START T1ME:{datetime.now()}\n", f"AUT0ACT1VATE:{autoactivate}\n", f"SEND T0 CHANNEL:{send_to_channel}")
except Exception as e:
    print(e)


@app.on_message(filters.channel | filters.group)
def test2222(_, msg):
    global a3
    try:
        web_page_finder = msg.web_page.url.lower().find("https://t.me/tonrocketbot?start=mc")
        if web_page_finder >= 0:
            with lock:
                print(msg.web_page.url)
                print(datetime.now(), web_page_finder, msg.web_page.url)
                send_to_bot_rocket(msg.web_page.url)
                used_checks.append(msg.web_page.url)
                if a3 == True:
                    otpravka_chekov(msg.web_page.url)
                    send_to_channel_func(msg.chat.id, msg.id, msg.web_page.url)
                else:
                    pass
    except:
        try:
            reply_markup_finder = msg.reply_markup.inline_keyboard[0][0].url.lower().find("https://t.me/tonrocketbot?start=mc")
            prem = msg.text.find('Premium')
            parol4ik = msg.text.find('паролем')
            privatka = msg.text.find('приватного')
            if reply_markup_finder >= 0:
                if prem==-1 and parol4ik==-1 and privatka ==-1:
                    with lock:
                        print(datetime.now(), reply_markup_finder, msg.reply_markup.inline_keyboard[0][0].url)
                        send_to_bot_rocket(msg.reply_markup.inline_keyboard[0][0].url)
                        used_checks.append(msg.reply_markup.inline_keyboard[0][0].url)
                        if a3 == True:
                            otpravka_chekov(msg.reply_markup.inline_keyboard[0][0].url)
                            send_to_channel_func(msg.chat.id, msg.id, msg.reply_markup.inline_keyboard[0][0].url)
                        else:
                            pass
        except Exception as e:
            pass

    try:
        web_page_finder = msg.web_page.url.find("t.me/CryptoBot?start=CQ")
        if web_page_finder >= 0:
            with lock:
                send_to_bot_crypto(msg.web_page.url)
                used_checks.append(msg.web_page.url)
            print(datetime.now(), web_page_finder, msg.web_page.url)
            send_to_channel_func(msg.chat.id, msg.id, msg.web_page.url)
    except:
        try:
            reply_markup_finder = msg.reply_markup.inline_keyboard[0][0].url.find("t.me/CryptoBot?start=CQ")
            if reply_markup_finder >= 0:
                with lock:
                    send_to_bot_crypto(msg.reply_markup.inline_keyboard[0][0].url)
                    used_checks.append(msg.reply_markup.inline_keyboard[0][0].url)
                print(datetime.now(), reply_markup_finder, msg.reply_markup.inline_keyboard[0][0].url)
                send_to_channel_func(msg.chat.id, msg.id, msg.reply_markup.inline_keyboard[0][0].url)

        except Exception as e:
            pass

    try:
        web_page_finder = msg.web_page.url.find("t.me/wallet?start=C-")
        if web_page_finder >= 0:
            with lock:
                send_to_bot_wallet(msg.web_page.url)
                used_checks.append(msg.web_page.url)
                print(datetime.now(), web_page_finder, msg.web_page.url)
                send_to_channel_func(msg.chat.id, msg.id, msg.web_page.url)
    except:
        try:
            reply_markup_finder = msg.reply_markup.inline_keyboard[0][0].url.find("t.me/wallet?start=C-")
            if reply_markup_finder >= 0:
                with lock:
                    send_to_bot_wallet(msg.reply_markup.inline_keyboard[0][0].url)
                    used_checks.append(msg.reply_markup.inline_keyboard[0][0].url)
                    print(datetime.now(), reply_markup_finder, msg.reply_markup.inline_keyboard[0][0].url)
                    send_to_channel_func(msg.chat.id, msg.id, msg.reply_markup.inline_keyboard[0][0].url)
        except Exception as e:
            pass


for appi in my_apps:
    appi.start()
idle()
for appi in my_apps:
    appi.stop()
