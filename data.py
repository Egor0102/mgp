player = {
    "name": "",
    "armor": 0.95,
    "hp": 100,
    "attack": 5,
    "luck": 10,
    "money": 10_000,
    "inventory": []
}



enemies = [
    {
        "name": "физрук",
        "hp": 15,
        "attack": 10,
        "script": "Ты щас 10 кругов побежишь",
        "win":"Ты достойный противник",
        "loss":"Побежал"

        
    },
    {"name": "Математиматичка",
        "hp": 20,
        "attack": 10,
        "script": "К доске быстро",
        "win":"Я пишу докладную",
        "loss":"Садись 2 "},


        {"name": "Историчка",
        "hp": 50,
        "attack": 20,
        "script": "А ты что самый умный?",
        "win":"Вон из класса",
        "loss":"Я звоню твоей маме"},

        {"name": "Директор",
        "hp": 70,
        "attack": 25,
        "script": "Ну вот мы и сотались 1 на 1",
        "win":"Поздравляю ты всех победил,теперь ты отчислен",
        "loss":"это было хорошие сражение"}
]

items = {
    "1" : {"name": "Зелье удачи", "price": 1500},
    "2" : {"name": "Пицца (Пропуск тренировки)", "price": 1000},
}