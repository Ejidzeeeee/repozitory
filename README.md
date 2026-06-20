Репозиторий: https://github.com/Ejidzeeeee/repozitory

Собственные модули (папка modules/)

| Модуль | Назначение |
|--------|------------|
| eda.py | Разведочный анализ: пропуски, статистика, гистограммы, boxplot, корреляции |
| preprocessing.py | Масштабирование (StandardScaler), LabelEncoder, разделение train/test |
| time_series.py | Создание лагов, скользящее среднее, извлечение частей даты |
| clustering.py | KMeans, DBSCAN, метод локтя для выбора числа кластеров |
| classification.py | Сравнение моделей: дерево, случайный лес, логистическая регрессия |
| regression.py | Линейная регрессия, случайный лес, метрики (MAE, RMSE, R2) |
| anomaly.py | Обнаружение аномалий: Isolation Forest, IQR, Z-score |
| one-hot.py | One-hot encoding, Apriori, ассоциативные правила |
| text_vectorizer.py | TF-IDF, CountVectorizer для векторизации текста |
| nlp_utils.py | Токенизация, NER, анализ тональности (через transformers) |
| word2vec_graph.py | Word2Vec, граф знаний (networkx), поиск близких слов |
| rag.py | Простой RAG: поиск похожих чанков через TF-IDF |
| report.py | Генерация HTML-отчётов с таблицами и графиками |
| lda_model.py | Тематическое моделирование LDA (обёртка для sklearn) |
| llm_utils.py | HTTP-клиент для локальной LLM (без готовых промптов) |
| data_structures.py | Уникальные списки, LRU-кэш, быстрая сортировка |
| mapping_utils.py | Преобразование структур данных (словари, списки) |
| math_utils.py | Рекуррентные последовательности, площади фигур |
| validators.py | Валидация данных по схеме, безопасная запись в файл |
| decorators.py | Логирование вызовов, замер времени выполнения |
| grid_utils.py | Работа с матрицами: строки, столбцы, транспонирование |

Как использовать 

1. Установить зависимости: pip install -r requirements.txt
2. В своём скрипте добавить путь к модулям:

   import sys
   sys.path.append('путь_к_папке_modules')
   from eda import quick_eda

3. Использовать функции как вспомогательные инструменты, подставляя свои названия столбцов и файлов.

Внешние библиотеки (устанавливаются через requirements.txt)

| Библиотека | GitHub | Назначение |
|------------|--------|------------|
| pandas | https://github.com/pandas-dev/pandas | Таблицы, CSV, статистика |
| NumPy | https://github.com/numpy/numpy | Массивы, матрицы |
| scikit-learn | https://github.com/scikit-learn/scikit-learn | ML-алгоритмы, метрики |
| Matplotlib | https://github.com/matplotlib/matplotlib | Графики |
| Seaborn | https://github.com/mwaskom/seaborn | Тепловая карта, boxplot |
| transformers | https://github.com/huggingface/transformers | NLP-модели |
| gensim | https://github.com/RaRe-Technologies/gensim | Word2Vec, LDA |
| networkx | https://github.com/networkx/networkx | Графы знаний |
| mlxtend | https://github.com/rasbt/mlxtend | Apriori, one-hot |
| pyLDAvis | https://github.com/bmabey/pyLDAvis | Визуализация LDA |
| requests | https://github.com/psf/requests | HTTP-запросы |
| wordcloud | https://github.com/amueller/word_cloud | Облако слов |
| nltk | https://github.com/nltk/nltk | Токенизация, стоп-слова |
