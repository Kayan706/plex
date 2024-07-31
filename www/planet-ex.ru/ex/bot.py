import requests
import sqlite3





def poptelebot():
    db = sqlite3.connect('ex/db.sqlite3')
    c = db.cursor()

    # c.execute("""CREATE TABLE main_orders (
    # id integer,
    # name text,
    # tel text
    # comments text,
    # date date,
    # )""")
    db.commit()


    c.execute("SELECT * FROM main_orders ORDER BY id DESC LIMIT 1")
    last = c.fetchone()
    print(last)
    bot_token = '6874545920:AAH57TAsc92JlQ9g_Nw0Uz4JObV7IaRSZJQ'
    chatID = '-1001961592473'

    def telegram_bot_sendtext(bot_token, chatID, message):
        url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chatID}&parse_mode=Markdown&text={message}'
        response = requests.get(url)
        return response.json()
    response = telegram_bot_sendtext(bot_token, chatID, last)
    
    return response
    db.close()



