if event.type == VkEventType.MESSAGE_NEW:
 if event.to_me:
            # ключевые слова для реакций бота
            delivery = ['Сколько стоит доставка', 'доставка', 'стоимость', 'Сколько стоит доставка?']
            helloWorld = ['Начать', 'начать', 'привет', 'Привет', 'Добрый день']

            # Сообщение от пользователя
            request = event.text
            words = request.split(" ")  # разбивает предлжение на строки
            print(words)
            # логика ответа
            if request in helloWorld == "Начать":
                write_msg(event.user_id, "Привет! Я - бот. Готов ответить на ваши вопросы.")
            elif request in delivery:
                write_msg(event.user_id, "Доставка до любой станции метро и МЦК стоит 350₽;")
            elif request in helloWorld:
                write_msg(event.user_id, "Привет! Я - бот. Готов ответить на ваши вопросы.")
            else:
                write_msg(event.user_id, "Затрудняюсь ответить на ваш вопрос.")
if any(word in request for word in helloWorld):