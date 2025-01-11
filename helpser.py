
from data import* 
import random
import time

def fight(current_enemy):
    round = random.randint(1, 2)
    enemy = enemies [current_enemy]
    enemy_hp = enemies[current_enemy]['hp']
    print(f'Противник - {enemy["name"]}: {enemy["script"]}')
    input('Enter чтобы продолжить')
    print()
    while player['hp'] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}.')
            crit = random.randint(1, 100)
            if crit < player['luck']:
                enemy_hp -= player['attack'] * 3
            else:
                enemy_hp -= player['attack']
            time.sleep(1)
            print(f'''{player['name']} - {player['hp']}
    {enemy['name']} - {enemy_hp}''')
            print()
            time.sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}.')
            player['hp'] -= enemy['attack'] * player['armor']
            time.sleep(1)
            print(f'''{player['name']} - {player['hp']}
    {enemy['name']} - {enemy_hp}''')
            print()
            time.sleep(1)
        round += 1

    if player['hp'] > 0:
        print(f'Противник - {enemy["name"]}: {enemy["win"]}')
        current_enemy += 1
    else:
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
    player['hp'] = 100
    return current_enemy


def training(training_type):
    skip = "2"
    if items["2"]["name"] in player["inventory"]:
        skip = input("Желаете пропустить тренировку? 1 - да, 2 - нет")
    if skip == "2":
        for i in range(0, 101, 20):
            print(f'Тренировка завершена на {i}%')
            time.sleep(1.5)
    if training_type == '1':
        player['attack'] += 2
        print(f'Тренировка окончена! Теперь ваша величина атаки равна {player["attack"]}')
    elif training_type == '2':
        player['armor'] -= .09
        print(f'Тренировка окончена! Теперь броня поглощает {100 - player["armor"] * 100}% урона')
    print()


def display_player():
    print(f'Игрок - {player["name"]}')
    print(f'Величина атаки - {player["attack"]}. Шанс критического урона ({player["attack"]}ед.) равен {player["luck"]}')
    print(f'Броня поглощает {(1 - player["armor"]) * 100}% урона')


def display_enemy(current_enemy):
    enemy = enemies[current_enemy]
    print(f'Противник - {enemy["name"]}')
    print(f'Веилична атаки - {enemy["attack"]}')
    print(f'Здоровье - {enemy["hp"]}')


def display_inventory():
    print("У вас есть")
    for value in player["inventory"]:
        print(value)
    print(f"У вас {player['money']} монет")
    print()
    if "Зелье удачи" in player["inventory"]:
        potion = input("Желаете выпить зелье удачи? 1 - да, 2 - нет")
        if potion == "1":
            player["luck"] += 7
            print(f"Готово, теперь шанс нанести критический  урон равен {player['luck']}%")
            player["inventory"].remove("Зелье удачи")

def shop():
    print("Добро пожаловать, путник, что хочешь приобрести?")
    print(f"У тебя есть {player['money']} монет")
    for key, value in items.items():
        print(f"{key} - {value['name']}: {value['price']}")
    
    item = input()
    if item in player["inventory"]:
        print(f"У тебя уже есть {items[item]['name']}")
    elif player['money'] >= items[item]['price']:
        print(f"Ты успешно приобрёл {items[item]['name']}")
        player['inventory'].append(items[item]['name'])
        player['money'] -= items[item]["price"]
    else:
        print("Не хватает монет :(")
    print()
    print("Буду ждать тебя снова, путник!")
    print()
def earn():
    print("добро пожаловать на завод!!! у тебя есть 67% шанс зароботать 500 монет и 33% шанс - потерять")
    result = random.randint(1,100)
    time.sleep(1.5)
    print("результат... ")
    time.sleep (1.5)
    print("страшно???")
    if result < 67:
        print("выйграли 500 монет!")
        player["money"] +=500
    else:
        print("вы проиграли 500 монет")
        player["money"] -=500
        print()
        print(f"осталось монет:{player['money']}")
        print()
        
def plot ():
    plot = input("выбирите историю персонажа 1-история о себе\n 2-история тренировочного монстра\n 3- истоия дикого кабана\n 4-история-разбойника\n 5-история сумашедшего дока\n 6-истоия токсичного чела\n 7-история орды подопотных\n 8-история прототипа бойцебота\n 9-история страного рыцаря\n 10-истоиия сверхрыцарь\n 11-история бойцебот\n 12-история доктора-Х\n")      
    if plot == "1":
        print("ты просто человый парень который решил попробовать себя в роле героя но что то пошло не так как ты хотел ты думал что это будет лёгкой прогулкой по парку но допустил фатальную ошибку подумав так")
    elif plot =="2":
        print("это просто твой 1 противник на котором ты узнал что такое битва")    
    elif plot =="3":
        print("это дикий кабан у него наверное вкусное мясо попробавать не желаешь?")
    elif plot =="4":
        print("разбойник ему охото наживится при этом особо не трудясь вот и грабит таких не очём подозревающих искателей приключений как ты. а видь они и вправду находят себя приключение ) ")
    elif plot =="5": 
        print("сумашедший док хмм не могу о нём особо сказать. Знаю лишь то что он ненормалньный и никогда не сдерживает обещаний")   
    elif plot =="6": 
        print("это одно из произведений сумашедшего дока который ну ужь слижком не цензурно выражается") 
    elif plot =="7": 
        print("это масса туш обьеденоную в одну и ты ксати в случае поражения можешь пополнить эту тушу так как док не когда не сдерживает обещаний")     
    elif plot =="8": 
        print("док пытался когдато давно сделать не попедимую машину ну как ты понял 1 блин всегда комом")   
    elif plot =="9": 
        print("страный рыцарь он не спроста получил это имя доктор и сверх рыцарь его учили несколько лет пока он не научился делать базовые вещи то за что он получил своё прозвище это когда после полугода тренировок он брал меч за клинок\n и пытался забить кабанчика дос мерти рукояткой медсестре потом долго пришлось его латать ") 
    elif plot =="10": 
        print("сверхрыцарь это один из самых преданых людей дока когда тот был маленьким его подобрал ещё на то время нормальный док ему стало жалко этого парня и он сделал из него сверхрыцаря\n а тот в свою очередь стал тренировать других рыцарей")
    elif plot =="11": 
        print("бойцебот это младший братик прототипа и он очень уважает своего старшего брата")     
    else:
        print("это лутшая версия себя он не привык проигрывать и когда ты его одалел он был очень зол и создал зелье которое усовершенствовало его до идеала ")      
