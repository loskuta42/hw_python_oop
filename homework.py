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
        now = dt.datetime.now().date()
        return sum(record.amount for record in self.records
                   if record.date == now)

    def get_week_stats(self):
        start_week = dt.datetime.now().date() - dt.timedelta(days=7)
        now = dt.datetime.now().date()
        return sum(record.amount for record in self.records
                   if now >= record.date > start_week)


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
        rate, curr_name = dict_curr[currency]

        if Calculator.get_today_stats(self) < self.limit:
            additive = self.limit - Calculator.get_today_stats(self)
            additive_r = round(additive / rate, 2)
            return f"На сегодня осталось {additive_r} {curr_name}"

        elif Calculator.get_today_stats(self) == self.limit:
            return "Денег нет, держись"

        else:
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
