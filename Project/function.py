import requests, bs4, random, datetime
from bs4 import BeautifulSoup

def get_weather():
    city = "Astana"
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    return response.text

def password_generate():
    symbols = ("!", "@", "#", "$", "%", "^", "&", "*")
    random_symbol = random.sample(symbols, 4)
    
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random_num = random.sample(nums, 4)
    
    strings = list(map(str, random_num))
    result = random_symbol + strings
    return ("".join(random.sample(result, len(result))))

#Напоминание о разминке или же обо встрече
def alarm():
    #get_time = input("Введите время планируемой стречи")
    pass


