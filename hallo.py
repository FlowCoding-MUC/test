import datetime

def begruessung(name:str):
    print("Hallo", name, "!")

def tschuess(name:str):
    print("Auf Wiedersehen,", name, "!")

def saytime():
    print("Es ist "+str(datetime.datetime.now().strftime('%H:%M:%S')+"Uhr"))

name = input("Bitte seien Sie so freundlich und geben Sie ihren Vornamen ein: ")

begruessung(name)
saytime()
tschuess(name)
