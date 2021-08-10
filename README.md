# hw_python_oop

Sprint 2. Итоговый проект. Калькулятор денег и калорий

# Установка:
после клонирования, находясь в склонированном каталоге прописать в консоли:
pip install -r requirements.txt

# Описание проекта

Калькулятор денег(класс CashCalculator(класс-родитель Calculator)):
1. Сохраняет новую запись о расходах методом add_record()
2. Считает, сколько денег потрачено сегодня методом get_today_stats()
3. Определяет, сколько ещё денег можно потратить сегодня в рублях, долларах или евро — метод get_today_cash_remained(currency)
4. Считает, сколько денег потрачено за последние 7 дней — метод get_week_stats()

Калькулятор калорий (класс CaloriesCalculator(класс-родитель Calculator)):
1. Сохраняет новую запись о приёме пищи— метод add_record()
2. Считает, сколько калорий уже съедено сегодня — метод get_today_stats()
3. Определяет, сколько ещё калорий можно/нужно получить сегодня — метод get_calories_remained()
4. Считает, сколько калорий получено за последние 7 дней — метод get_week_stats()

Конструктор класса Calculator принимает один аргумент — число limit (дневной лимит трат/калорий, который задал пользователь). В конструкторе создан пустой список records, в котором потом будут храниться записи. 

Чтобы было удобнее создавать записи, для них создан отдельный класс Record. В нем сохраняются:
1. число amount (денежная сумма или количество килокалорий),
2. дата создания записи date (передаётся в явном виде в конструктор, либо присваивается значение по умолчанию — текущая дата),
3. комментарий comment, поясняющий, на что потрачены деньги или откуда взялись калории.

Метод get_calories_remained() класса CaloriesCalculator возвращает ответ:
- «Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более N кКал», если лимит limit не достигнут,
- или «Хватит есть!», если лимит достигнут или превышен.

Метод get_today_cash_remained(currency) класса CashCalculator принимает на вход код валюты: одну из строк "rub", "usd" или "eur".
Возвращает он сообщение о состоянии дневного баланса в этой валюте, округляя сумму до двух знаков после запятой (до сотых):
- «На сегодня осталось N руб/USD/Euro» — в случае, если лимит limit не достигнут,
- или «Денег нет, держись», если лимит достигнут,
- или «Денег нет, держись: твой долг - N руб/USD/Euro», если лимит превышен.
Курс валют указан константами USD_RATE и EURO_RATE, в теле класса CashCalculator.

