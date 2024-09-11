# Рассылка писем
def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    email_strings = ('.com', '.ru', '.net', '@')
    for i in range(len(email_strings)):
        if email_strings[i] in recipient or email_strings[i] in sender:
            if recipient == sender:
                print(f'\nНельзя отправить письмо самому себе!')
                break
            elif sender == "university.help@gmail.com":
                print(f'\nПисьмо успешно отправлено с адреса {sender} '
                      f'на адрес {recipient}.')
                break
            else:
                print(f'\nНЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено '
                      f'с адреса {sender} на адрес {recipient}.')
                break
        else:
            print(f'\nНевозможно отправить письмо с адреса {sender} '
                  f'на адрес {recipient}')
            break

send_email('Это сообщение для проверки связи',
           'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!',
           'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание',
           'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре',
           'urban.teacher@gmail.com', sender='urban.teacher@gmail.com')