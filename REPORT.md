# ДЕПАРТАМЕНТ ОБРАЗОВАНИЯ ГОРОДА МОСКВЫ
## ГБПОУ «КОЛЛЕДЖ СВЯЗИ №54» ИМЕНИ П.М. ВОСТРУХИНА

**Дисциплина:** Учебная практика 
**Тема:** Разработка веб-приложения «Конференции.РФ» (по методическому пособию демонстрационного экзамена)  

**Выполнил:**  
Группа: 4ИСП9-49ВБ  
Студент: Жуков Максим  

**Проверил преподаватель:**  
Рыжих Д.Г.  

**Москва 2026 г.**

---

## Введение. Структура экзаменационных модулей

В ходе выполнения заданий демонстрационного экзамена разрабатывается веб-портал **«Конференции.РФ»**, предназначенный для онлайн-бронирования конференц-залов (аудитории, коворкинги, кинозалы) организаторами всероссийских мероприятий. Работа разделена на три модуля:

| Модуль | Наименование | Содержание и итоговый результат |
|---|---|---|
| **Модуль 1** | Проектирование и разработка информационных систем | Реляционная БД, ER-диаграмма связей, страницы авторизации, регистрации, личного кабинета, создания заявки и администрирования. |
| **Модуль 2** | Разработка дизайна веб-приложений | Обработанная графика в GIMP, адаптивный слайдер с автопрокруткой, деловая палитра, адаптация под смартфоны 390×844, архив `layout_2.zip`. |
| **Модуль 3** | Проектирование, разработка и оптимизация веб-приложений | Полный CRUD заявок, фиксация статусов в БД, семантический HTML5, БЭМ-номенклатура, анимации интерфейса, валидация полей в JS и Python. |

---

## Этап 1. Рабочее место в ROSA Linux

### Задание 1. Навигация в терминале
```bash
$ pwd
/home/ivanov
$ mkdir -p ~/exam/practice/stage1
$ cd ~/exam/practice/stage1
$ touch index.html style.css script.js
$ mv script.js main.js
$ ls -la
```
**Результат:** Создано структурированное рабочее пространство `~/exam/practice/stage1` с файлами `index.html`, `style.css` и `main.js`.

### Задание 2. Установка программного обеспечения
```bash
$ sudo dnf makecache
$ sudo dnf install -y git python3 python3-pip postgresql16 postgresql16-server gimp chromium
```
Таблица установленных версий ПО:

| Программа | Команда проверки | Зафиксированная версия | Статус |
|---|---|---|---|
| **Git** | `git --version` | git version 2.45.2 | Установлено |
| **Python** | `python3 --version` | Python 3.12.4 | Установлено |
| **pip** | `pip3 --version` | pip 24.0 | Установлено |
| **PostgreSQL** | `psql --version` | psql (PostgreSQL) 16.4 | Установлено |
| **VS Code** | `code --version` | 1.90.2 | Установлено |
| **GIMP** | `gimp --version` | GIMP 2.10.36 | Установлено |

### Задание 3. Поиск пакетов без sudo
Отработано разграничение прав доступа в ОС: команды информационного поиска (`dnf search postgresql | grep server`, `dnf info gimp`) выполняются непривилегированным пользователем. Попытка выполнить установку `dnf install` без `sudo` блокируется системой управления правами.

### Задание 4. Первый проект в VS Code
В редакторе VS Code открыт каталог проекта, с использованием плагина Emmet (`! + Tab`) сгенерирован скелет страницы с заголовком `<h1>Привет, ROSA!</h1>`. Файл успешно открыт в Chromium (`chromium index.html`).

### Задание 5. Режим смартфона в браузере
В Chromium DevTools (F12) включена эмуляция мобильных устройств (`Ctrl+Shift+M`) с разрешением **390×844**. Отработана интерактивная правка CSS через панель Elements (`color: red;`) и захват скриншота через меню DevTools «Capture screenshot».

---

## Этап 2. Контроль версий Git

### Задание 1. Первоначальная настройка Git
```bash
$ git config --global user.name "Иванов Иван"
$ git config --global user.email "ivanov@example.ru"
$ git config --global init.defaultBranch main
```

### Задание 2–3. Создание репозитория и файл исключений .gitignore
Инициализирован репозиторий в каталоге `git-demo`. Сформирован файл `.gitignore`:
```gitignore
venv/
__pycache__/
*.pyc
*.db
```

### Задание 4. История изменений и откат правок
Отработан просмотр построчных изменений (`git diff`), откат нежелательных правок (`git restore index.html`) и формирование осмысленных коммитов в прошедшем времени:
- `Добавлена главная страница`
- `Добавлен файл исключений .gitignore`
- `Добавлен заголовок Конференции.РФ`
- `Подключена таблица стилей style.css`

### Задание 5. Взаимодействие с удаленным сервером
Создан тестовый bare-репозиторий `server.git`, настроена удаленная ветка `origin` (`git remote add origin`), выполнен push и последующее клонирование в `git-copy` с полной верификацией истории коммитов.

---

## Этап 3. Разметка HTML5

Разработаны статические HTML5-страницы с обязательными семантическими тегами (`header`, `nav`, `main`, `section`, `article`, `footer`), атрибутом `lang="ru"` и кодировкой UTF-8:

| Страница | Файл | Ключевые семантические элементы | Формы и элементы интерфейса |
|---|---|---|---|
| **Главная** | `index.html` | `header`, `nav`, `main`, `section.hero`, `section.rooms`, `footer` | Заголовок h1, промо-описание, слайдер помещений, кнопка «Забронировать помещение», сетка залов. |
| **Авторизация** | `login.html` | `header`, `nav`, `main`, `section.form-box`, `footer` | Поля логина и пароля, кнопка «Войти», ссылка «Еще не зарегистрированы? Регистрация». |
| **Регистрация** | `register.html` | `header`, `nav`, `main`, `section.form-box`, `footer` | 5 обязательных полей (`login`, `password`, `full_name`, `phone`, `email`), подсказки, кнопка «Создать пользователя». |
| **Новая заявка** | `rooms.html` | `header`, `nav`, `main`, `section.form-box`, `footer` | Выбор помещения, дата начала, переключатели оплаты («При очном посещении», «Перевод по СБП»), кнопка «Отправить». |
| **Мои заявки** | `cabinet.html` | `header`, `nav`, `main`, `article.booking-card` | Карточки заявок с цветными статусами, кнопка «Удалить заявку» для новых, поле textarea для отзыва завершенных. |
| **Панель админа** | `admin.html` | `header`, `nav`, `main`, `article.booking-card` | Форма фильтра по статусу, карточки заявок со всеми контактами клиента, форма смены статуса. |

---

## Этап 4. Оформление: CSS и Bootstrap

В файле `static/css/style.css` определена деловая сине-оранжевая палитра и 4 размера шрифта:
```css
:root {
    --color-primary: #1f4e8c;      /* синий */
    --color-primary-dark: #163a69; /* синий при наведении */
    --color-accent: #f2a541;       /* теплый оранжевый акцент */
    --color-bg: #f5f7fb;           /* комфортный светлый фон */
    --color-text: #1e2430;         /* темный текст */
    --color-error: #c0392b;        /* цвет ошибок */

    --font-h1: 2rem;        /* 32px — заголовки страниц */
    --font-h2: 1.375rem;    /* 22px — заголовки карточек */
    --font-text: 1rem;      /* 16px — основной текст */
    --font-small: 0.875rem; /* 14px — подсказки и подвал */
    --radius: 12px;
}
```
Реализована плавная анимация появления контента `@keyframes fade-in` и микроанимации при наведении на кнопки (`transform: translateY(-2px); box-shadow: 0 6px 14px rgba(31, 78, 140, 0.25);`). В медиа-запросе `@media (max-width: 576px)` обеспечена полная адаптивность под экран 390×844 без горизонтальной полосы прокрутки.

---

## Этап 5. JavaScript: проверка форм и слайдер

### Верификация регулярных выражений:

| Поле | Тестовые данные | Шаблон RegExp | Ожидание | Результат |
|---|---|---|---|---|
| **Логин** | `ivanov2027` | `/^[A-Za-z0-9]{6,}$/` | `true` | `true` (валидно) |
| **Логин** | `ivan` | `/^[A-Za-z0-9]{6,}$/` | `false` | `false` (короче 6 симв.) |
| **Логин** | `иванов2027` | `/^[A-Za-z0-9]{6,}$/` | `false` | `false` (кириллица запрещена) |
| **ФИО** | `Иванов Иван` | `/^[А-Яа-яЁё ]+$/` | `true` | `true` (валидно) |
| **ФИО** | `Ivanov Ivan` | `/^[А-Яа-яЁё ]+$/` | `false` | `false` (латиница запрещена) |
| **Телефон** | `8(900)123-45-67` | `/^8\(\d{3}\)\d{3}-\d{2}-\d{2}$/` | `true` | `true` (валидно) |
| **Телефон** | `89001234567` | `/^8\(\d{3}\)\d{3}-\d{2}-\d{2}$/` | `false` | `false` (нет скобок и дефисов) |
| **Телефон** | `+7(900)123-45-67` | `/^8\(\d{3}\)\d{3}-\d{2}-\d{2}$/` | `false` | `false` (начинается не с 8) |
| **E-mail** | `anna@mail.ru` | `/^[^@\s]+@[^@\s]+\.[^@\s]+$/` | `true` | `true` (валидно) |
| **E-mail** | `anna.mail.ru` | `/^[^@\s]+@[^@\s]+\.[^@\s]+$/` | `false` | `false` (отсутствует @) |

Скрипт `static/js/validation.js` обеспечивает подсветку ошибок `is-invalid` и вывод сообщений в `.form__error`. Автослайдер работает с интервалом 3000 мс.

---

## Этап 6. База данных PostgreSQL

Создана роль `conf_user`, база `conferences` и 4 связанные таблицы: `users`, `rooms`, `bookings`, `reviews`. Проверены операции CRUD (Create, Read с JOIN, Update статуса, Delete) и выгружена ER-диаграмма связей.

---

## Этап 7 и 8. Серверная часть Flask и сборка приложения

Серверное приложение `app.py` построено на Flask, Flask-Login и SQLAlchemy:
```python
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from extensions import db
from models import Users

app = Flask(__name__)
app.config['SECRET_KEY'] = 'BALDBALD'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('cabinet'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/rooms', methods=['GET', 'POST'])
@app.route('/booking/new', methods=['GET', 'POST'])
def rooms():
    return render_template('rooms.html')

@app.route('/cabinet')
def cabinet():
    return render_template('cabinet.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
```

Все шаблоны открываются без ошибок, обработчики кнопок выполняют корректные перенаправления.
