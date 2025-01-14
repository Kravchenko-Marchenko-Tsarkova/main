# Описание
Репозиторий для публикации решений домашних задач по дисциплине "Разработка приложений на Python", выполненных студентами группы 5130203/20102 Кравченко Софьей, Марченко Кристиной, Царьковой Алиной

xristosina - Марченко Кристина,
mayerife - Кравченко Софья,
arftot - Царькова Алина

В папке tasks находятся решения задач 1.1 Кватернионы,  1.2 Кэширующий декоратор, 1.3 Фигуры на плоскости.
В папке project находятся файлы проекта по задаче 4. Система распознавания лиц по фотографиям с телеграма или любого источника и хранение в базу данных какая личность сколько раз отсканировалась (любая БД)
Разбиение на задачи:
а) бот телеграма - Марченко Кристина

б) хранение в базу - Царькова Алина

ц) система распознавания лиц по фотографиям - Кравченко Софья.

Бот расположен в телеграм по адресу @FaceDetectionSystemBot . Функционал включает в себя прием фотографии от пользователя, распознавание человека на фотографии, сохранение в базу данных информации о количестве сканирований для каждой личности и вывод пользователю информации из базы данных. Обучение проводилось на датасете, расположенном по ссылке https://www.kaggle.com/datasets/vasukipatel/face-recognition-dataset. Датасет включает в себя фотографии 31 знаменитой личности: Akshay Kumar, Alexandra Daddario, Alia Bhatt, Amitabh Bachchan, Andy Samberg, Anushka Sharma, Billie Eilish, Brad Pitt, Camila Cabello, Charlize Theron, Claire Holt, Courtney Cox, Dwayne Johnson, Elizabeth Olsen, Ellen Degeneres, Henry Cavill, Hrithik Roshan, Hugh Jackman, Jessica Alba, Kashyap, Lisa Kudrow, Margot Robbie, Marmik, Natalie Portman, Priyanka Chopra, Robert Downey Jr, Roger Federer, Tom Cruise, Vijay Deverakonda, Virat Kohli, Zac Efron. При получении изображения с личностью, не входящей в этот список, сканирование сохраняется в базу данных под именем Unknown.
