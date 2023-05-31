import telebot
bot = telebot.TeleBot("5867240937:AAEqBIfP4IUwERMHfKQ3QOW20xawiS1jFdM")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привіт, я бот, який допомогає притулкам та нашим волонтерам комунікувати. Перед початком внесення даних про тварину додайте інформацію про ваш притулок та його адресу, натиснувши відповідну кнопку.', reply_markup=create_keyboard())

def create_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    add_info_button = telebot.types.InlineKeyboardButton(text='🐶Нова тварина', callback_data='add info')
    add_info_button1 = telebot.types.InlineKeyboardButton(text='🔄Оновити інформацію про тварину', callback_data='add info1')
    site_button = telebot.types.InlineKeyboardButton(text='Our site', url='https://www.figma.com/proto/bRK9SZkxlQiJqyro67Feuh/Untitled?node-id=110%3A2729&scaling=scale-down&page-id=0%3A1&starting-point-node-id=110%3A2731')
    shelter_button = telebot.types.InlineKeyboardButton(text='🏠Притулок та адреса',callback_data="shelter")
    keyboard.add(add_info_button, site_button,shelter_button,add_info_button1)
    return keyboard
def delete(message):
    bot.delete_message(message.chat.id, message.message_id)
@bot.callback_query_handler(func=lambda call: call.data == 'add info1')
def handle_add_zabrali(call):
    delete(call.message)
    bot.send_message(call.message.chat.id, 'Статус тварини(Забрали/....)')
    bot.register_next_step_handler(call.message, handle_add_imya1)
def handle_add_imya1(message):
    global zabrali
    zabrali = message.text
    bot.send_message(message.chat.id, 'Як її звати?')
    bot.register_next_step_handler(message, handle_add_vid1)
def handle_add_vid1(message):
    global imya1
    imya1 = message.text
    bot.send_message(message.chat.id, 'Що це за тварина')
    bot.register_next_step_handler(message, handle_infa1)
def handle_infa1(message):
    global vid1
    vid1 = message.text
    bot.send_message(message.chat.id, 'Статус тварини: {}\nЇї звуть: {}\nЦе: {}'.format(zabrali,imya1,vid1))
    bot.send_message(message.chat.id,"Я відправив ці дані нашим спеціалістам :D")
    start(message)
@bot.callback_query_handler(func=lambda call: call.data == 'shelter')
def handle_add_info(call):
    delete(call.message)
    bot.send_message(call.message.chat.id,"Щоб змінити інфу про притулок достатньо ще раз нажати на кнопу 'Вкажіть ваш притулок та адрес притулку',та вказати інші данні")
    bot.send_message(call.message.chat.id, 'Введіть назву вашого притулку')
    bot.register_next_step_handler(call.message, handle_add_area)
def handle_add_area(message):
    global location
    location = message.text
    bot.send_message(message.chat.id, 'Введіть адрес притулку')
    bot.register_next_step_handler(message, infa_pro_prutylok)
def infa_pro_prutylok(message):
    global area
    area = message.text
    bot.send_message(message.chat.id, 'Назва вашого притулку {}, і його адреса {}'.format(location, area))
    start(message)
@bot.callback_query_handler(func=lambda call: call.data == 'add info')
def handle_add_imya(call):
    delete(call.message)
    bot.send_message(call.message.chat.id, 'Як звати вашу тварину?')
    bot.register_next_step_handler(call.message, handel_add_vid)
def handel_add_vid(message):
    global imya
    imya = message.text
    bot.send_message(message.chat.id, 'Що це за тварина?')
    bot.register_next_step_handler(message, handle_add_razmer)
def handle_add_razmer(message):
    global vid
    vid = message.text
    bot.send_message(message.chat.id, 'Вкажіть розмір?')
    bot.register_next_step_handler(message, handle_add_stat)
def handle_add_stat(message):
    global razmer
    razmer = message.text
    bot.send_message(message.chat.id, 'Вкажіть стать?')
    bot.register_next_step_handler(message, handle_add_vik)
def handle_add_vik(message):
    global stat
    stat = message.text
    bot.send_message(message.chat.id, 'Вкажіть вік тварини')
    bot.register_next_step_handler(message, handle_add_vaga)
def handle_add_vaga(message):
    global vik
    vik = message.text
    bot.send_message(message.chat.id, 'Вкажіть вагу тварини')
    bot.register_next_step_handler(message, handle_add_poroda)
def handle_add_poroda(message):
    global vaga
    vaga = message.text
    bot.send_message(message.chat.id, 'Вкажіть породу тварини')
    bot.register_next_step_handler(message, handle_add_problem)
def handle_add_problem(message):
    global poroda
    poroda = message.text
    bot.send_message(message.chat.id, 'Чи є в неї проблеми?')
    bot.register_next_step_handler(message, handle_infa)
def handle_infa(message):
    global problem
    problem = message.text
    bot.send_message(message.chat.id, 'Назва притулку : {}\nАдрес притулку : {}\nТварину звати : {}\nЦе : {}\nЇї розмір : {}\nЇї стать : {}\nЇї вік : {}\nЇї вага: {}\nЇї порода: {}\nЧи є в неї проблеми?: {}\nВсе правильно?'.format(location, area,imya,vid,razmer,stat,vik,vaga,poroda,problem),reply_markup=create_keyboard1())
def create_keyboard1():
    keyboard = telebot.types.InlineKeyboardMarkup()
    false_button = telebot.types.InlineKeyboardButton(text='❌', callback_data='false button')
    true_button = telebot.types.InlineKeyboardButton(text='✅', callback_data='true button')
    keyboard.add(false_button, true_button)
    return keyboard
@bot.callback_query_handler(func=lambda call: call.data == 'true button')
def sendsend(call):
    delete(call.message)
    bot.send_message(call.message.chat.id,"Я відправив ці дані нашим спеціалістам :D")
    start(call.message)
#def sendsend(message):
    #bot.send_message(message.chat.id,"Я відправив ці данні нашим спеціалістим :D")
    #start(message)
@bot.callback_query_handler(func=lambda call: call.data == 'false button')
def otvet_false(call):
    delete(call.message)
    start(call.message)
bot.polling()