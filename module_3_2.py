# Рассылка писем

def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    email_strings = ['.com', '.ru', '.net']
    if find_string_email(email_strings, recipient) == True:
        if recipient == sender:
            print(f'\nНельзя отправить письмо самому себе!')
        elif sender == "university.help@gmail.com":
            print(f'\nПисьмо успешно отправлено с адреса {sender} '
                  f'на адрес {recipient}.')
        else:
            print(f'\nНЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено '
                  f'с адреса {sender} на адрес {recipient}.')
    else:
        print(f'\nНевозможно отправить письмо с адреса {sender} '
              f'на адрес {recipient}')

def find_string_email (string, email):
    find_email = False
    for i in range(len(string)):
        if (email.find(string[i]) != -1) and (email.find('@') != -1):
            find_email = True
            break
    return(find_email)

send_email('Это сообщение для проверки связи',
           'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!',
           'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание',
           'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре',
           'urban.teacher@gmail.com', sender='urban.teacher@gmail.com')
