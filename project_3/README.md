# My data science projects

From the [Skillfactory Data Science course](https://skillfactory.ru/data-science-specialization) 

# Проект 3. EDA + Feature Engineering. Соревнование на Kaggle.

## Оглавление
[1. Описание проекта](https://github.com/Ulyana-Is/data_science_sf/tree/main/project_3#1-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)

[2. Какой кейс решаем](https://github.com/Ulyana-Is/data_science_sf/tree/main/project_3#2-%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%BA%D0%B5%D0%B9%D1%81-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC)

[3. Краткая информация о данных](https://github.com/Ulyana-Is/data_science_sf/tree/main/project_3#3-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)

[4. Этапы работы над проектом](https://github.com/Ulyana-Is/data_science_sf/tree/main/project_3#4-%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)

[5. Результат](https://github.com/Ulyana-Is/data_science_sf/tree/main/project_3#5-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82)

[6. Выводы](https://github.com/Ulyana-Is/data_science_sf/tree/main/project_3#6-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)

### 1. Описание проекта.
Построение модели для  [Booking](https://www.booking.com/), которая предсказывает рейтинг отеля, для выявления отелей, которые накручивают себе рейтинг.

[к оглавлению](https://github.com/Ulyana-Is/data_science_sf/tree/main/project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 2. Какой кейс решаем?
Необходимо исследовать данные базы отелей:
+ провести предварительный анализ данных, определить структуру данных, провести очистку;
+ преобразовать признаки и создать новые, влияющие на рейтинг отелей;
+ осуществить отбор признаков;
+ провести обучение модели;
+ разместить результат в соревновании на *[Kaggle](https://www.kaggle.com/competitions/sf-booking)*.  

**Условия соревнования:**
Определены на *[Kaggle](https://www.kaggle.com/competitions/sf-booking)*.

**Метрика качества:**
+ Качество кода (соблюдение стандартов оформления PEP-8, комментирование кода, README к проекту). Оформление проекта на GitHub, GitLab, Kaggle.
+ Очистка данных.
+ Исследование данных (качество визуализации, наличие идей, гипотез, комментариев).
+ Генерация признаков.
+ Отбор признаков.
+ Преобразование признаков.
+ Качество решения: результат метрики MAPEР.

**Что практикуем:**
Отбор и проектирование признаков, их моделирование.

[к оглавлению](https://github.com/Ulyana-Is/data_science_sf/tree/main/project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 3. Краткая информация о данных:

Входящие данные: информация по отелям с их рейтингом.

[к оглавлению](https://github.com/Ulyana-Is/data_science_sf/tree/main/project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 4. Этапы работы над проектом:
1) Импорт библиотек и данных (датасета для обучения, датасет для предсказания):
    + 1.1) проверка наличия дубликатов, анализ числовых выбросов;
    + 1.2) дополнительный анализ признаков, влияющих на рейтинг отеля;
    + 1.3) объединение датасета для обучения с датасетов для предсказания.
2)  Проектирование и обработка нечисловых признаков:
    + 2.1) адрес отеля;
    + 2.2) страна ревьюера;
    + 2.3) дата отзыва; 
    + 2.4) тэги, изучение и преобразование;
    + 2.5) 'Negative_review', изучение и преобразование;
    + 2.6) 'Positive_review', изучение и преобразование.
3) Проектирование признаков, аналих мультиколлениарности.
4) Обучение модели и получение предсказания.


[к оглавлению](https://github.com/Ulyana-Is/data_science_sf/tree/main/project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 5. Результат
Подробная инфомация приведена в [Jupyter Notebook](https://github.com/Ulyana-Is/data_science_sf/blob/main/project_3/Project_3_EDA_model.ipynb), размещена на *[Kaggle](https://www.kaggle.com/code/ulyanais/eda-3-project-booking-rating-score-isakova)*.

[к оглавлению](https://github.com/Ulyana-Is/data_science_sf/tree/main/project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)
 
### 6. Выводы
В результате проведенного исследования построили модель, определяющую рейтинг модель с точностью (92,23%), а также определили, что максимальную точность результата дает модель с всеми призаками.  В результате проведенного исследования построили модель, определяющую рейтинг модель с точностью (92,23%), а также определили, что максимальную точность результата дает модель с всеми признаками.

[к оглавлению](https://github.com/Ulyana-Is/data_science_sf/tree/main/project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)
