from win10toast_click import ToastNotifier
import time
import schedule
import webbrowser

url = 'https://app.tangerino.com.br/Tangerino'

def open_url():
    try: 
        webbrowser.open_new(url)
        print('Opening URL...')  
    except: 
        print('Failed to open URL. Unsupported variable type.')

toaster = ToastNotifier()

def bater_ponto():
    toaster.show_toast('Bater ponto!', 'Clique aqui para abrir o Tangerino', duration=10, threaded=True, callback_on_click = open_url)

def sextou():
    toaster.show_toast('Sextou!', 'Bom fim de semana!', duration=10, threaded=True)


for i in ["09:00", "12:00", "13:00", "18:00"]:
    schedule.every().monday.at(i).do(bater_ponto)
    schedule.every().tuesday.at(i).do(bater_ponto)
    schedule.every().wednesday.at(i).do(bater_ponto)
    schedule.every().thursday.at(i).do(bater_ponto)
    schedule.every().friday.at(i).do(bater_ponto)

schedule.every().friday.at("18:00:30").do(sextou)


while True:
    schedule.run_pending()
    time.sleep(10)

