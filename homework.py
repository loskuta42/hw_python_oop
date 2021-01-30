import datetime as dt


class Calculator:
    """Parent class which get only limit."""
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def __float__(self):
        return self.limit

    def add_record(self, Record):
        self.records.append(Record)

    def get_today_stats(self):
        stat = []
        now = dt.datetime.now().date()
        for i in self.records:
            if i.date == now:
                stat.append(i.amount)
        return sum(stat)

    def get_week_stats(self):
        week_stat = []
        start_week = dt.datetime.now().date() - dt.timedelta(days=7)
        now = dt.datetime.now().date()
        for i in self.records:
            date = i.date
            if date > start_week and date <= now:
                week_stat.append(i.amount)
        return sum(week_stat)


class CaloriesCalculator(Calculator):
    """Child class of class Calculator for count calories."""
    def get_calories_remained(self):
        stat_tmp = Calculator.get_today_stats(self)
        if stat_tmp < self.limit:
            additive = self.limit - stat_tmp
            return (f"Сегодня можно съесть что-нибудь ещё, "
                    f"но с общей калорийностью не более {additive} кКал")
        return "Хватит есть!"


class CashCalculator(Calculator):
    """Child class of class Calculator for count cash."""
    USD_RATE = 76.24
    EURO_RATE = 92.46

    def get_today_cash_remained(self, currency):
        dict_curr = {
            "rub": [1.00, "руб"],
            "usd": [self.USD_RATE, "USD"],
            "eur": [self.EURO_RATE, "Euro"]
        }
        rate = dict_curr[currency][0]
        curr_name = dict_curr[currency][1]
        if Calculator.get_today_stats(self) < self.limit:
            additive = self.limit - Calculator.get_today_stats(self)
            additive_r = round(additive / rate, 2)
            return f"На сегодня осталось {additive_r} {curr_name}"

        elif Calculator.get_today_stats(self) == self.limit:
            return "Денег нет, держись"

        elif Calculator.get_today_stats(self) > self.limit:
            debt = Calculator.get_today_stats(self) - self.limit
            debt__r = round(debt / rate, 2)
            return f"Денег нет, держись: твой долг - {debt__r} {curr_name}"


class Record:
    """Class for records."""
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        self.date = date
        if self.date is None:
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


cash_calculator = CashCalculator(1000)

# дата в параметрах не указана,
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment="кофе"))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))

print(cash_calculator.get_today_cash_remained("usd"))
print(cash_calculator.get_today_cash_remained("eur"))