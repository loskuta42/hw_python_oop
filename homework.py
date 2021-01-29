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
        stat=0
        now = dt.datetime.now().date()
        for i in range(0,len(self.records)):
            if self.records[i].date == now:
                stat+=self.records[i].amount
        return stat

    def get_week_stats(self):
        week_stat=0
        start_week = dt.datetime.now().date() - dt.timedelta(days=7)
        now = dt.datetime.now().date()
        for i in range(0,len(self.records)):
            if (self.records[i].date > start_week) and (self.records[i].date <= now):
                week_stat += self.records[i].amount
        return week_stat


class CaloriesCalculator(Calculator):
    """Child class of class Calculator for count calories."""
    def get_calories_remained(self):
        if Calculator.get_today_stats(self) < self.limit:
            additive = self.limit - Calculator.get_today_stats(self)
            return (f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью "
            f"не более {additive} кКал")
        elif Calculator.get_today_stats(self) >= self.limit:
            return f"Хватит есть!"


class CashCalculator(Calculator):
    """Child class of class Calculator for count cash."""
    USD_RATE = 76.24
    EURO_RATE = 92.46
    def get_today_cash_remained(self, currency):
        if Calculator.get_today_stats(self) < self.limit:
            additive = self.limit - Calculator.get_today_stats(self)
            if currency == "rub":
                return f"На сегодня осталось {additive} руб"
            elif currency == "usd":
                usd_additive = float(additive)/self.USD_RATE
                r_usd_additive = round(usd_additive, 2)
                return f"На сегодня осталось {r_usd_additive} USD"
            elif currency == "eur":
                eur_additive = float(additive)/self.EURO_RATE
                r_eur_additive = round(eur_additive, 2)
                return f"На сегодня осталось {r_eur_additive} Euro"

        elif Calculator.get_today_stats(self) == self.limit:
            return f"Денег нет, держись"

        elif Calculator.get_today_stats(self) > self.limit:
            debt = Calculator.get_today_stats(self) - self.limit
            if currency == "rub":
                return f"Денег нет, держись: твой долг - {debt} руб"
            elif currency == "usd":
                usd_debt = float(debt)/self.USD_RATE
                r_usd_debt = round(usd_debt, 2)
                return f"Денег нет, держись: твой долг - {r_usd_debt} USD"
            elif currency == "eur":
                eur_debt = float(debt)/self.EURO_RATE
                r_eur_debt = round(eur_debt, 2)
                return f"Денег нет, держись: твой долг - {r_eur_debt} Euro"



class Record:
    """Class for records."""
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        self.date = date
        if self.date == None:
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
