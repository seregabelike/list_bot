import telebot, mysql.connector; #разобраться с регистрацией пользователя
from random import randint 
from mysql.connector import Error
from telebot import types
bot = telebot.TeleBot('6210050644:AAF4wzzj9c9bQ5sQNLKLQLhptyNKm6zb7iM');
#Вот тут начало кода бота==================================================
#Кнопочки
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("Посмотреть список")
btn2 = types.KeyboardButton("Дополнить список")
btn3 = types.KeyboardButton("Уменьшить список")
markup.add(btn1)
markup.add(btn2)
markup.add( btn3)
#ВСЕ ФУНЦИИ В БОТЕ!!!

#ФУНКЦИЯ ДЛЯ ВЫВОДА СОДЕРЖИМОГО СПИСКА##################################################################################
#def request_in_base в разработке
def show_list(message):
    connection = mysql.connector.connect(user='admin', password='S3re_gg_A22!', host='127.0.0.1', database='list_bot')
    look_list_query = "SELECT `product_name` FROM `list_table` WHERE `user_id`='" + str(message.from_user.id) + "'"
    with connection.cursor() as cursor:
        cursor.execute(look_list_query)
        result = cursor.fetchall()
        list_array = []
        num = 0
        lists = ""
        for x in result:
            list_array += x
        for punkt in list_array:
            num += 1
            lists += (str(num) + ") " + punkt.title()) + "\n"
        if len(lists) == 0:
            bot.send_message(message.chat.id, text="Список пуст")
        else:
            bot.send_message(message.chat.id, text="В списке сейчас:\n" + str(lists), reply_markup=markup)
########################################################################################################################
#ФУНКЦИЯ ДЛЯ ЗАПОЛНЕНИЯ СПИСКА
def add_product(message):
    product=message.text
    try:
        connection = mysql.connector.connect(user='admin', password='S3re_gg_A22!', host='127.0.0.1', database='list_bot')
        create_user_query = "INSERT INTO `list_table` (`user_id`, `product_name`) VALUES ('" + str(message.from_user.id) + " ', '" + str(product.lower()) + "');"
        connection.cursor().execute(create_user_query)
        connection.commit()
        try:
            show_list(message)
        except:
            print("ERROR SHOW LIST")
    except:
        print("ERROR ADD")
#ФУНКЦИЯ ДЛЯ УДАЛЕНИЯ ПРОДУКТА##########################################################################################
def delete_product(message):
    product_num=message.text
    connection = mysql.connector.connect(user='admin', password='S3re_gg_A22!', host='127.0.0.1', database='list_bot')
    look_list_query = "SELECT `product_name` FROM `list_table` WHERE `user_id`='" + str(message.from_user.id) + "'"
    try:
        list_array = []
        del_array = product_num.strip('[]').replace(' ', '').split(',')
        with connection.cursor() as cursor:
            cursor.execute(look_list_query)
            result = cursor.fetchall()
            for x in result:
                 list_array += x
        for x in del_array:
            try:
                del_product_query = "DELETE FROM `list_table` WHERE `user_id`='" + str(message.from_user.id) + "' AND `product_name`='" +str(list_array[int(x)-1]) + "'"
                print(del_product_query)
                connection.cursor().execute(del_product_query)
                connection.commit()
                connection.close()
            except:
                print("такого пункта нет")
        try:
            show_list(message)
        except:
            print("ERROR SHOW LIST")
    except:
        print("ERROR DELETE")
#ФУНКЦИЯ ДЛЯ РЕГИСТРАЦИИ ПОЛЬЗОВАТЕЛЕЙ##################################################################################
def user_reg(message):
    connection = mysql.connector.connect(user='admin', password='S3re_gg_A22!', host='127.0.0.1', database='list_bot')
    user_id = message.from_user.id
    username = message.text
    create_user_query = "INSERT INTO `name_table` (`user_id`, `user_name`) VALUES ('"+ str(user_id) +" ', '"+ str(username) +"');"
    connection.cursor().execute(create_user_query)
    connection.commit()
    connection.close()
    bot.send_message(message.chat.id, text="Приятно познакомиться, " + username)
    bot.send_message(message.chat.id,
                     text="Расскажу тебе немного о своих возможностях, я умею:\n1)Составлять списки;\n2)Дополнять списки;\n3)Уменьшать списки.")
    bot.send_message(message.chat.id, text="Что ты хочешь сделать?",reply_markup=markup)

########################################################################################################################

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    connection = mysql.connector.connect(user='admin', password='S3re_gg_A22!', host='127.0.0.1', database='list_bot')
    examination_user_query="SELECT * FROM `name_table` where `user_id`='"+str(message.from_user.id)+"'"
    try:
        with connection.cursor() as cursor:
            cursor.execute(examination_user_query)
            result = cursor.fetchone()
            username=result[2]
            connection.close()
            bot.send_message(message.chat.id,text="Привет, "+username+"!\nНапомню тебе о своих возможностях, я умею:\n1)Просматривать списки;\n2)Дополнять списки;\n3)Уменьшать списки.")
            bot.send_message(message.chat.id,text="Что ты хочешь сделать?",reply_markup=markup)
    except:
        bot.send_message(message.chat.id,text="Привет! Я список-бот, а как зовут тебя?" )
        bot.register_next_step_handler(message, user_reg)

@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    if(message.text).lower()=="посмотреть список":
        try:
            show_list(message)
        except:
            bot.send_message(message.chat.id, text="Список пуст")

#ДОБАВЛЕНИЕ ПРОДУКТА
    elif(message.text).lower()=="дополнить список":
        bot.send_message(message.chat.id, text="Что ты хочешь добавить?",reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message,add_product)


#УДАЛЕНИЕ ПРОДУКТА
    elif(message.text).lower()=="уменьшить список":
        print("уменьшаем список")
        bot.send_message(message.chat.id, text="Выбери пункты которые хочешь удалить")
        bot.register_next_step_handler(message, delete_product)


#ТАКИХ КОМАНД МЫ НЕ ЗНАЕМ
    else:
        bot.send_message(message.chat.id, text="Увы, такой команды я не знаю.")


bot.infinity_polling()
