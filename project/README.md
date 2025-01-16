## Описание задачи

Реализован телеграм бот по задаче 4. Система распознавания лиц по фотографиям с телеграма или любого источника и хранение в базу данных какая личность сколько раз отсканировалась (любая БД) 

Разбиение на задачи:

а) бот телеграма - Марченко Кристина

б) хранение в базу - Царькова Алина

ц) система распознавания лиц по фотографиям - Кравченко Софья.

Бот расположен в телеграм по адресу @FaceDetectionSystemBot . 

## Функциональность бота

Функционал включает в себя 

- прием фотографии от пользователя,
- распознавание человека на фотографии,
- сохранение в базу данных информации о количестве сканирований для каждой личности,
- вывод пользователю информации из базы данных. 

## Система распознавания лиц

Обучение проводилось на датасете, расположенном по ссылке https://www.kaggle.com/datasets/vasukipatel/face-recognition-dataset. Датасет включает в себя фотографии 31 знаменитой личности: Akshay Kumar, Alexandra Daddario, Alia Bhatt, Amitabh Bachchan, Andy Samberg, Anushka Sharma, Billie Eilish, Brad Pitt, Camila Cabello, Charlize Theron, Claire Holt, Courtney Cox, Dwayne Johnson, Elizabeth Olsen, Ellen Degeneres, Henry Cavill, Hrithik Roshan, Hugh Jackman, Jessica Alba, Kashyap, Lisa Kudrow, Margot Robbie, Marmik, Natalie Portman, Priyanka Chopra, Robert Downey Jr, Roger Federer, Tom Cruise, Vijay Deverakonda, Virat Kohli, Zac Efron. При получении изображения с личностью, не входящей в этот список, сканирование сохраняется в базу данных под именем Unknown.

## Запуск бота

### Требования к среде

- Python версии 3.10 или выше.
- Установленные зависимости (см. requirements.txt).

### Установка и запуск

Необходимо клонировать репозиторий и установить зависимости из файла requirements.txt

```
git clone <https://github.com/Kravchenko-Marchenko-Tsarkova/main.git>
cd <main>
pip install -r requirements.txt
```

В файле telegrambot_MKT.py необходимо указать токен вашего бота, полученный от BotFather в Telegram.


## Использование бота

- Найдите бот по его ID;
- В меню выберите одну из возможных команд: /photo для загрузки фотографии или /database для получения данных из базы;
- После выбора команды /photo загрузите вашу фотографию и дождитесь ответа от бота;
- После выбора команды /database  бот отправит информацию о всех сохраненных сканированиях.
