import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
import time
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

token = "8dbb86259b9a1fdf0bd53d621642952cf717f73510075eeac1d4dab5b96b80e28410ba2316217cc80405f"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

admin = str(430500693)
admin1 = str(0)
admin2 = str(0)
admin3 = str(0)

keyboard = VkKeyboard(one_time=True)

def start():
    keyboard.add_button('Как купить в магазине?', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Как продать аккаунт?', color=VkKeyboardColor.PRIMARY)

    keyboard.add_line()
    keyboard.add_button('Через сколько прийдет товар?', color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button('Получить ссылку на магазин', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Отзывы', color=VkKeyboardColor.PRIMARY)

    keyboard.add_line()
    keyboard.add_button('Вызвать техподдержку!', color=VkKeyboardColor.NEGATIVE)



while True:
    start()
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('----------------------------')
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            print('----------------------------')
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "привет":

                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Выберите ваш вопрос:',
                                       'keyboard': keyboard.get_keyboard(), 'random_id': 0})

                elif response == "как купить в магазине?":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Внимательно посмотрите видеоролик!\n В нем полностью описана оплата на нашем сайте!','keyboard': keyboard.get_keyboard(), 'attachment': "video-181246182_456239017", 'random_id': 0})

                elif response == "вызвать техподдержку!":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Ищем свободного агента...',
                                       'random_id': 0})
                    time.sleep(3)
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Агент найден!',
                                       'random_id': 0})
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Вы соеденены, ждем его ответа...',
                                       'random_id': 0})
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': '🐩Расскажите о вашей проблеме! \n 🐩Мы '
                                                                            'попробуем в ней разобраться! \n 🐩Сразу '
                                                                            'извините за долгое ожидание(подготовка '
                                                                            'ответа может занять время)\n Или вы '
                                                                            'можете написать сюда - '
                                                                            'https://vk.com/goldshopstand',
                                       'keyboard': keyboard.get_keyboard(),
                                       'random_id': 0})
                    vk_session.method('messages.send',
                                      {'user_id': admin, 'message': '💥💥Вас вызывает - vk.com/id' + str(event.user_id),
                                       'random_id': 0})
                elif response == "как продать аккаунт?":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Чтобы продать аккаунт напишите ему - https://vk.com/mryaz11','keyboard': keyboard.get_keyboard(), 'random_id': 0})
                elif response == "через сколько прийдет товар?":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Обычно товар приходит через 20-50 минут.\n Если товар так и не пришел вы всегда можете вызвать техподдержку!','keyboard': keyboard.get_keyboard(), 'random_id': 0})
                elif response == "получить ссылку на магазин":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Магазин всегда доступен только по этой ссылке - https://vk.cc/9knmij','keyboard': keyboard.get_keyboard(), 'random_id': 0})
                elif response == "отзывы":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Отзывы находятся у нас в группе под одним из постов!\n Если не можете найти то вот - https://vk.com/wall-181637677_22','keyboard': keyboard.get_keyboard(), 'random_id': 0})
                elif response == "начать":

                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Выберите ваш вопрос:',
                                       'keyboard': keyboard.get_keyboard(), 'random_id': 0})
                elif response == "помощь":

                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Выберите ваш вопрос:',
                                       'keyboard': keyboard.get_keyboard(), 'random_id': 0})
                else:
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Я вас не понимаю... Выберите:',
                                       'keyboard': keyboard.get_keyboard(), 'random_id': 0})
