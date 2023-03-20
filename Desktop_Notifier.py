from plyer import notification
import time

def notifyMe(title,message):
    notification.notify(
        title= title,
        message= message,
        app_icon= "C:/Users/Prashansha/Downloads/Ampeross-Qetto-2-Timer.ico",
        timeout = 15
    )

if __name__ == '__main__':
    while True:
        notifyMe("HEY USER, TAKE A BREAK NOW !!", "LOVE YOUR WORK..? SO REST YOUR MIND, CALM YOUR HEART AND TAKE A BREAK NOW !!")
        time.sleep(3600)