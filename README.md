<h1 align="center">🚀 fast_api — Сборник FastAPI решений</h1>
<p align="center">
  <b>Репозиторий с заданиями и примерами на FastAPI</b><br>
  <img src="https://img.shields.io/badge/python-3.10+-blue?logo=python">
  <img src="https://img.shields.io/badge/fastapi-%3E=0.100-green?logo=fastapi">
</p>

---

## 📂 Структура репозитория

```
.
├── .gitignore
├── notes.db
├── task1/
├── task2/
├── task3/
├── task4/
├── task5.py
├── task6.py
├── task7.py
├── task8.py
├── task9.py
├── task10/
├── task11/
├── task12/
├── task13.py
├── task14/
├── task15/
├── task16/
├── task17/
├── task18/
```
> 🔗 [Посмотреть все содержимое на GitHub](https://github.com/BDaaac/fast_api/tree/main/)

- **taskX/** — директории с заданиями и проектами (каждая содержит отдельное решение)
- **taskX.py** — самостоятельные Python-скрипты FastAPI
- **notes.db** — база данных (скорее всего SQLite) для хранения данных приложений
- **.gitignore** — файлы и папки, игнорируемые Git

---

## 🦄 Быстрый старт

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/BDaaac/fast_api.git
   cd fast_api
   ```

2. **Создайте виртуальное окружение и активируйте его:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Установите зависимости (пример):**
   ```bash
   pip install fastapi uvicorn
   ```

4. **Запустите нужное приложение:**
   Например, для запуска `task5.py`:
   ```bash
   uvicorn task5:app --reload
   ```
   > Эндпоинты и детали запуска для каждого задания могут отличаться — смотрите в коде соответствующей папки или файла.

---

## 📑 Полезные ссылки

- [Документация FastAPI](https://fastapi.tiangolo.com/ru/)
- [Uvicorn](https://www.uvicorn.org/)
- [Pydantic](https://docs.pydantic.dev/)

---

## 🤝 Вклад

Pull Requests, предложения и замечания приветствуются!  
Для обсуждения создавайте issue или пишите напрямую [автору](https://github.com/BDaaac).

---

<p align="center">
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" width="120"/>
</p>
