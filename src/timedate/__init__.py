"""Advanced date and time management library."""

import os
import datetime
from time import time_ns
import typing

DELTA = {  # All time zones and their offset with UTC in seconds
    'Dateline Standard Time': -720,
    'UTC-11': -660,
    'Aleutian Standard Time': -600,
    'Hawaiian Standard Time': -600,
    'Marquesas Standard Time': -570,
    'Alaskan Standard Time': -540,
    'UTC-09': -540,
    'Pacific Standard Time (Mexico)': -480,
    'UTC-08': -480,
    'Pacific Standard Time': -480,
    'US Mountain Standard Time': -420,
    'Mountain Standard Time (Mexico)': -420,
    'Mountain Standard Time': -420,
    'Yukon Standard Time': -420,
    'Central America Standard Time': -360,
    'Central Standard Time': -360,
    'Easter Island Standard Time': -300,
    'Central Standard Time (Mexico)': -360,
    'Canada Central Standard Time': -360,
    'SA Pacific Standard Time': -300,
    'Eastern Standard Time (Mexico)': -300,
    'Eastern Standard Time': -300,
    'Haiti Standard Time': -300,
    'Cuba Standard Time': -300,
    'US Eastern Standard Time': -300,
    'Turks And Caicos Standard Time': -300,
    'Paraguay Standard Time': -180,
    'Atlantic Standard Time': -240,
    'Venezuela Standard Time': -240,
    'Central Brazilian Standard Time': -240,
    'SA Western Standard Time': -240,
    'Pacific SA Standard Time': -180,
    'Newfoundland Standard Time': -210,
    'Tocantins Standard Time': -180,
    'E. South America Standard Time': -180,
    'SA Eastern Standard Time': -180,
    'Argentina Standard Time': -180,
    'Greenland Standard Time': -180,
    'Montevideo Standard Time': -180,
    'Magallanes Standard Time': -180,
    'Saint Pierre Standard Time': -180,
    'Bahia Standard Time': -180,
    'UTC-02': 600,
    'Mid-Atlantic Standard Time': 600,
    'Azores Standard Time': -60,
    'Cape Verde Standard Time': -60,
    'UTC': 0,
    'GMT Standard Time': 0,
    'Greenwich Standard Time': 0,
    'Sao Tome Standard Time': 0,
    'Morocco Standard Time': 60,
    'W. Europe Standard Time': 60,
    'Central Europe Standard Time': 60,
    'Romance Standard Time': 60,
    'Central European Standard Time': 60,
    'W. Central Africa Standard Time': 60,
    'Jordan Standard Time': 120,
    'GTB Standard Time': 120,
    'Middle East Standard Time': 120,
    'Egypt Standard Time': 120,
    'E. Europe Standard Time': 120,
    'Syria Standard Time': 120,
    'West Bank Standard Time': 120,
    'South Africa Standard Time': 120,
    'FLE Standard Time': 120,
    'Israel Standard Time': 120,
    'South Sudan Standard Time': 120,
    'Kaliningrad Standard Time': 120,
    'Sudan Standard Time': 120,
    'Libya Standard Time': 120,
    'Namibia Standard Time': 120,
    'Arabic Standard Time': 180,
    'Turkey Standard Time': 180,
    'Arab Standard Time': 180,
    'Belarus Standard Time': 180,
    'Russian Standard Time': 180,
    'E. Africa Standard Time': 180,
    'Volgograd Standard Time': 180,
    'Iran Standard Time': 210,
    'Arabian Standard Time': 240,
    'Astrakhan Standard Time': 240,
    'Azerbaijan Standard Time': 240,
    'Russia Time Zone 3': 240,
    'Mauritius Standard Time': 240,
    'Saratov Standard Time': 240,
    'Georgian Standard Time': 240,
    'Caucasus Standard Time': 240,
    'Afghanistan Standard Time': 270,
    'West Asia Standard Time': 300,
    'Ekaterinburg Standard Time': 300,
    'Pakistan Standard Time': 300,
    'Qyzylorda Standard Time': 300,
    'India Standard Time': 330,
    'Sri Lanka Standard Time': 330,
    'Nepal Standard Time': 345,
    'Central Asia Standard Time': 360,
    'Bangladesh Standard Time': 360,
    'Omsk Standard Time': 360,
    'Myanmar Standard Time': 390,
    'SE Asia Standard Time': 420,
    'Altai Standard Time': 420,
    'W. Mongolia Standard Time': 420,
    'North Asia Standard Time': 420,
    'N. Central Asia Standard Time': 420,
    'Tomsk Standard Time': 420,
    'China Standard Time': 480,
    'North Asia East Standard Time': 480,
    'Singapore Standard Time': 480,
    'W. Australia Standard Time': 480,
    'Taipei Standard Time': 480,
    'Ulaanbaatar Standard Time': 480,
    'Aus Central W. Standard Time': 525,
    'Transbaikal Standard Time': 540,
    'Tokyo Standard Time': 540,
    'North Korea Standard Time': 540,
    'Korea Standard Time': 540,
    'Yakutsk Standard Time': 540,
    'Cen. Australia Standard Time': -810,
    'AUS Central Standard Time': -150,
    'E. Australia Standard Time': -120,
    'AUS Eastern Standard Time': -780,
    'West Pacific Standard Time': -120,
    'Tasmania Standard Time': -780,
    'Vladivostok Standard Time': -120,
    'Lord Howe Standard Time': -780,
    'Bougainville Standard Time': -780,
    'Russia Time Zone 10': -780,
    'Magadan Standard Time': -780,
    'Norfolk Standard Time': -720,
    'Sakhalin Standard Time': -780,
    'Central Pacific Standard Time': -780,
    'Russia Time Zone 11': -720,
    'New Zealand Standard Time': -660,
    'UTC+12': -720,
    'Fiji Standard Time': -720,
    'Kamchatka Standard Time': -720,
    'Chatham Islands Standard Time': -615,
    'UTC+13': -660,
    'Tonga Standard Time': -660,
    'Samoa Standard Time': -600,
    'Line Islands Standard Time': -600
}

_LANGUAGE = "en"

_DICTIONARY = {
    'en': {
        'and': 'and',
        'to': 'to',
        'year': 'year',
        'month': 'month',
        'day': 'day',
        'hour': 'hour',
        'minute': 'minute',
        'second': 'second',
        'millisecond': 'millisecond',
        'microsecond': 'microsecond',
        'nanosecond': 'nanosecond',
        'years': 'years',
        'months': 'months',
        'days': 'days',
        'hours': 'hours',
        'minutes': 'minutes',
        'seconds': 'seconds',
        'milliseconds': 'milliseconds',
        'microseconds': 'microseconds',
        'nanoseconds': 'nanoseconds',
        'time remaining until': 'Time remaining until ',
        'time elapsed since': 'Time elapsed since ',
        'january': 'january',
        'february': 'february',
        'march': 'march',
        'april': 'april',
        'may': 'may',
        'june': 'june',
        'july': 'july',
        'august': 'august',
        'september': 'september',
        'october': 'october',
        'november': 'november',
        'december': 'december',
        'sunday': 'Sunday',
        'monday': 'Monday',
        'tuesday': 'Tuesday',
        'wednesday': 'Wednesday',
        'thursday': 'Thursday',
        'friday': 'Friday',
        'saturday': 'Saturday',
    },
    'ma': {
        'and': '和',
        'to': '到',
        'year': '年',
        'month': '月',
        'day': '天',
        'hour': '小时',
        'minute': '分钟',
        'second': '秒',
        'millisecond': '毫秒',
        'microsecond': '微秒',
        'nanosecond': '纳秒',
        'years': '年',
        'months': '月',
        'days': '天',
        'hours': '小时',
        'minutes': '分钟',
        'seconds': '秒',
        'milliseconds': '毫秒',
        'microseconds': '微秒',
        'nanoseconds': '纳秒',
        'time remaining until': '剩余时间至 ',
        'time elapsed since': '自以来经过的时间 ',
        'january': '一月',
        'february': '二月',
        'march': '三月',
        'april': '四月',
        'may': '五月',
        'june': '六月',
        'july': '七月',
        'august': '八月',
        'september': '九月',
        'october': '十月',
        'november': '十一月',
        'december': '十二月',
        'sunday': '星期日',
        'monday': '星期一',
        'tuesday': '星期二',
        'wednesday': '星期三',
        'thursday': '星期四',
        'friday': '星期五',
        'saturday': '星期六',
    },
    'hi': {
        'and': 'और',
        'to': 'को',
        'year': 'साल',
        'month': 'महीना',
        'day': 'दिन',
        'hour': 'घंटा',
        'minute': 'मिनट',
        'second': 'दूसरा',
        'millisecond': 'मिलीसेकंड',
        'microsecond': 'माइक्रोसेकंड',
        'nanosecond': 'नैनोसेकंड',
        'years': 'वर्षों',
        'months': 'महीने',
        'days': 'दिन',
        'hours': 'घंटे',
        'minutes': 'मिनट',
        'seconds': 'सेकंड',
        'milliseconds': 'मिलीसेकेंड',
        'microseconds': 'माइक्रोसेकंड',
        'nanoseconds': 'नैनोसेकंड',
        'time remaining until': 'शेष समय ',
        'time elapsed since': 'समय बीत गया ',
        'january': 'जनवरी',
        'february': 'फ़रवरी',
        'march': 'मार्च',
        'april': 'अप्रैल',
        'may': 'मई',
        'june': 'जून',
        'july': 'जुलाई',
        'august': 'अगस्त',
        'september': 'सितंबर',
        'october': 'अक्टूबर',
        'november': 'नवंबर',
        'december': 'दिसंबर',
        'sunday': 'रविवार',
        'monday': 'सोमवार',
        'tuesday': 'मंगलवार',
        'wednesday': 'बुधवार',
        'thursday': 'गुरूवार',
        'friday': 'शुक्रवार',
        'saturday': 'शनिवार',
    },
    'sp': {
        'and': 'y',
        'to': 'para',
        'year': 'año',
        'month': 'mes',
        'day': 'día',
        'hour': 'hora',
        'minute': 'minuto',
        'second': 'segundo',
        'millisecond': 'milisegundo',
        'microsecond': 'microsegundo',
        'nanosecond': 'nanosegundo',
        'years': 'años',
        'months': 'meses',
        'days': 'dias',
        'hours': 'horas',
        'minutes': 'minutos',
        'seconds': 'segundos',
        'milliseconds': 'milisegundos',
        'microseconds': 'microsegundos',
        'nanoseconds': 'nanosegundos',
        'time remaining until': 'Tiempo restante hasta ',
        'time elapsed since': 'Tiempo transcurrido desde ',
        'january': 'enero',
        'february': 'febrero',
        'march': 'marcha',
        'april': 'abril',
        'may': 'puede',
        'june': 'junio',
        'july': 'julio',
        'august': 'agosto',
        'september': 'septiembre',
        'october': 'octubre',
        'november': 'noviembre',
        'december': 'diciembre',
        'sunday': 'domingo',
        'monday': 'lunes',
        'tuesday': 'martes',
        'wednesday': 'miércoles',
        'thursday': 'jueves',
        'friday': 'viernes',
        'saturday': 'sábado',
    },
    'be': {
        'and': 'এবং',
        'to': 'প্রতি',
        'year': 'বছর',
        'month': 'মাস',
        'day': 'দিন',
        'hour': 'ঘন্টা',
        'minute': 'মিনিট',
        'second': 'দ্বিতীয়',
        'millisecond': 'মিলিসেকেন্ড',
        'microsecond': 'মাইক্রোসেকেন্ড',
        'nanosecond': 'ন্যানোসেকেন্ড',
        'years': 'বছর',
        'months': 'মাস',
        'days': 'দিন',
        'hours': 'ঘন্টার',
        'minutes': 'মিনিট',
        'seconds': 'সেকেন্ড',
        'milliseconds': 'মিলিসেকেন্ড',
        'microseconds': 'মাইক্রোসেকেন্ড',
        'nanoseconds': 'ন্যানোসেকেন্ড',
        'time remaining until': 'পর্যন্ত সময় বাকি ',
        'time elapsed since': 'সেই থেকে সময় কেটে গেছে ',
        'january': 'জানুয়ারী',
        'february': 'ফেব্রুয়ারী',
        'march': 'মার্চ',
        'april': 'এপ্রিল',
        'may': 'মে',
        'june': 'জুন',
        'july': 'জুলাই',
        'august': 'আগস্ট',
        'september': 'সেপ্টেম্বর',
        'october': 'অক্টোবর',
        'november': 'নভেম্বর',
        'december': 'ডিসেম্বর',
        'sunday': 'রবিবার',
        'monday': 'সোমবার',
        'tuesday': 'মঙ্গলবার',
        'wednesday': 'বুধবার',
        'thursday': 'বৃহস্পতিবার',
        'friday': 'শুক্রবার',
        'saturday': 'শনিবার',
    },
    'fr': {
        'and': 'et',
        'to': 'à',
        'year': 'an',
        'month': 'mois',
        'day': 'jour',
        'hour': 'heure',
        'minute': 'minute',
        'second': 'seconde',
        'millisecond': 'milliseconde',
        'microsecond': 'microseconde',
        'nanosecond': 'nanoseconde',
        'years': 'ans',
        'months': 'mois',
        'days': 'jours',
        'hours': 'heures',
        'minutes': 'minutes',
        'seconds': 'secondes',
        'milliseconds': 'millisecondes',
        'microseconds': 'microsecondes',
        'nanoseconds': 'nanosecondes',
        'time remaining until': "Temps restant jusqu'à ",
        'time elapsed since': 'Temps écoulé depuis ',
        'january': 'janvier',
        'february': 'février',
        'march': 'mars',
        'april': 'avril',
        'may': 'mai',
        'june': 'juin',
        'july': 'juillet',
        'august': 'août',
        'september': 'septembre',
        'october': 'octobre',
        'november': 'novembre',
        'december': 'décembre',
        'sunday': 'dimanche',
        'monday': 'lundi',
        'tuesday': 'mardi',
        'wednesday': 'mercredi',
        'thursday': 'jeudi',
        'friday': 'vendredi',
        'saturday': 'samedi',
    },
    'ru': {
        'and': 'и',
        'to': 'к',
        'year': 'год',
        'month': 'месяц',
        'day': 'день',
        'hour': 'час',
        'minute': 'минута',
        'second': 'второй',
        'millisecond': 'миллисекунда',
        'microsecond': 'микросекунда',
        'nanosecond': 'наносекунда',
        'years': 'годы',
        'months': 'месяцы',
        'days': 'дни',
        'hours': 'часы',
        'minutes': 'минуты',
        'seconds': 'секунды',
        'milliseconds': 'миллисекунды',
        'microseconds': 'микросекунды',
        'nanoseconds': 'наносекунды',
        'time remaining until': 'Оставшееся время до ',
        'time elapsed since': 'Прошло время с ',
        'january': 'январь',
        'february': 'февраль',
        'march': 'Маршировать',
        'april': 'апрель',
        'may': 'Мая',
        'june': 'Июнь',
        'july': 'Июль',
        'august': 'Август',
        'september': 'Сентябрь',
        'october': 'Октябрь',
        'november': 'ноябрь',
        'december': 'Декабрь',
        'sunday': 'Воскресенье',
        'monday': 'Понедельник',
        'tuesday': 'Вторник',
        'wednesday': 'Среда',
        'thursday': 'Четверг',
        'friday': 'Пятница',
        'saturday': 'Суббота',
    },
    'po': {
        'and': 'e',
        'to': 'para',
        'year': 'ano',
        'month': 'mês',
        'day': 'dia',
        'hour': 'hora',
        'minute': 'minuto',
        'second': 'segundo',
        'millisecond': 'milissegundo',
        'microsecond': 'microssegundo',
        'nanosecond': 'nanossegundo',
        'years': 'anos',
        'months': 'meses',
        'days': 'dias',
        'hours': 'horas',
        'minutes': 'minutos',
        'seconds': 'segundos',
        'milliseconds': 'milissegundos',
        'microseconds': 'microssegundos',
        'nanoseconds': 'nanossegundos',
        'time remaining until': 'Tempo restante até ',
        'time elapsed since': 'Tempo decorrido desde ',
        'january': 'Janeiro',
        'february': 'Fevereiro',
        'march': 'Marchar',
        'april': 'Abril',
        'may': 'Maio',
        'june': 'Junho',
        'july': 'Julho',
        'august': 'Agosto',
        'september': 'Setembro',
        'october': 'Outubro',
        'november': 'Novembro',
        'december': 'Dezembro',
        'sunday': 'Domingo',
        'monday': 'Segunda-feira',
        'tuesday': 'Terça-feira',
        'wednesday': 'Quarta-feira',
        'thursday': 'Quinta-feira',
        'friday': 'Sexta-feira',
        'saturday': 'Sábado',
    }
}


class Time:
    """Documentation from Time:

     • __init__ -> Can be called empty to initialize to 0
     • by_date() -> static method allowing to convert a Date into Time
     • by_datetime_date() -> static method allowing to convert a datetime.date into Time
     • by_datetime_time() -> static method allowing to convert a datetime.time into Time
     • by_datetime_datetime() -> static method allowing to convert a datetime.datetime into Time
     • update() -> allows to update the attributes
     • -self -> returns the opposite
     • self - x -> remove x nanosecond from the current object
     • self == x -> checks equality with x
     • self != x -> checks inequality with x
     • str(self) -> sends a character string corresponding to the object
     • print(self) -> print a character string corresponding to the object
     • format(self, "...") -> sends a character string formatted according to the character string
     • self[x] -> sends the value of the object according to x
     • list(self) -> returns a list with the values of the object
"""

    @staticmethod
    def by_date(date) -> __class__:
        """Create a Time variable from a Date variable.

        :param date: A Date variable.
        :return: A Time variable.
        """
        if isinstance(date, Date):
            return Time(date[1], date[2], date[3], date[4], date[5], date[6], date[7],
                        date[8], date[9], date[0], date[10])
        else:
            raise TypeError('A Date type variable is expected')

    @staticmethod
    def by_datetime_date(date: datetime.date) -> __class__:
        """Create a Time variable from a datetime.date variable.

        :param date: A datetime.date variable.
        :return: A Time variable.
        """
        return Time(date.year, date.month, date.day)

    @staticmethod
    def by_datetime_time(date: datetime.time) -> __class__:
        """Create a Time variable from a datetime.time variable.

        :param date: A datetime.time variable.
        :return: A Time variable.
        """
        return Time(0, 0, 0, date.hour, date.minute, date.second,
                    date.microsecond // 1000, date.microsecond % 1000)

    @staticmethod
    def by_datetime_datetime(date: datetime.datetime) -> __class__:
        """Create a Time variable from a datetime.datetime variable.

        :param date: A datetime.datetime variable.
        :return: A Time variable.
        """
        return Time(date.year, date.month, date.day, date.hour, date.minute, date.second,
                    date.microsecond // 1000, date.microsecond % 1000)

    def __init__(
            self,
            year: int = 0,
            month: int = 0,
            day: int = 0,
            hour: int = 0,
            minute: int = 0,
            second: int = 0,
            millisecond: int = 0,
            microsecond: int = 0,
            nanosecond: int = 0,
            name: str = None,
            language: str = None
    ):
        """Time object initialization.

        :param year: The number of year. Default is 0.
        :param month: The number of month. Default is 0.
        :param day: The number of day. Default is 0.
        :param hour: The number of hour. Default is 0.
        :param minute: The number of minute. Default is 0.
        :param second: The number of second. Default is 0.
        :param millisecond: The number of millisecond. Default is 0.
        :param microsecond: The number of microsecond. Default is 0.
        :param nanosecond: The number of nanosecond. Default is 0.
        :param name: The name of the time. Default is None.
        :param language: The language for use. Default is LANGUAGE.
        """

        self._name = name
        self._language = _LANGUAGE

        try:
            self.set_language(language)
        except ValueError:
            pass
        except TypeError:
            pass

        self._year = year
        self._month = month
        self._day = day
        self._hour = hour
        self._minute = minute
        self._second = second
        self._millisecond = millisecond
        self._microsecond = microsecond
        self._nanosecond = nanosecond

        self.update()

    def update(self) -> None:
        """Update the attributes.

        :return: None
        """
        if self._nanosecond >= 1000:
            self._microsecond += self._nanosecond // 1000
            self._nanosecond = self._nanosecond % 1000
        elif self._nanosecond <= -1000:
            self._microsecond -= self._nanosecond // -1000
            self._nanosecond = self._nanosecond % -1000

        if self._microsecond >= 1000:
            self._millisecond += self._microsecond // 1000
            self._microsecond = self._microsecond % 1000
        elif self._microsecond <= -1000:
            self._millisecond -= self._microsecond // -1000
            self._microsecond = self._microsecond % -1000

        if self._millisecond >= 1000:
            self._second += self._millisecond // 1000
            self._millisecond = self._millisecond % 1000
        elif self._millisecond <= -1000:
            self._second -= self._millisecond // -1000
            self._millisecond = self._millisecond % -1000

        if self._second >= 60:
            self._minute += self._second // 60
            self._second = self._second % 60
        elif self._second <= -60:
            self._minute -= self._second // -60
            self._second = self._second % -60

        if self._minute >= 60:
            self._hour += self._minute // 60
            self._minute = self._minute % 60
        elif self._minute <= -60:
            self._hour -= self._minute // -60
            self._minute = self._minute % -60

        if self._hour >= 24:
            self._day += self._hour // 24
            self._hour = self._hour % 24
        elif self._hour <= -24:
            self._day -= self._hour // -24
            self._hour = self._hour % -24

        if self._day >= 30.436875:
            self._month += int(self._day // 30.436875)
            self._day = round(self._day % 30.436875)

        elif self._day <= -30.436875:
            self._month -= int(self._day // -30.436875)
            self._day = round(self._day % -30.436875)

        if self._month >= 12:
            self._year += self._month // 12
            self._month = self._month % 12
        elif self._month <= -12:
            self._year -= self._month // -12
            self._month = self._month % -12

    def __abs__(self) -> __class__:
        """The absolute value."""
        if self.get('nanosecond') < 0:
            return -self
        else:
            return self

    def __neg__(self) -> __class__:
        """The opposite value."""
        return Time() - self

    def _get_this_and_that(self, other) -> tuple[int, int]:
        if isinstance(self, Time):
            this = self.get('nanosecond')
        elif isinstance(self, Date):
            this = Time.by_date(self).get('nanosecond')
        else:
            raise ValueError

        if isinstance(other, Time):
            that = other.get('nanosecond')
        elif isinstance(other, Date):
            that = Time.by_date(other).get('nanosecond')
        elif isinstance(other, int):
            that = other * 1000000000
        else:
            raise ValueError

        return this, that

    def __add__(self, other) -> __class__:
        """Add other."""
        this, that = self._get_this_and_that(other)
        res = this + that
        return Time(nanosecond=res)

    def __sub__(self, other):
        this, that = self._get_this_and_that(other)
        res = this - that
        return Time(nanosecond=res)

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Time) or isinstance(o, Date):
            if isinstance(o, Date):
                o = Time.by_date(o)
            return self.get('nanosecond') == o.get('nanosecond')
        else:
            return False

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)

    def __str__(self) -> str:
        def printDigit(x, d: int) -> str:
            t = str(x)
            while len(t) < d:
                t = '0' + t
            return t

        time = str(self._second)

        numberMLS, numberMCS, numberNNS = abs(self._millisecond), abs(self._microsecond), abs(self._nanosecond)

        if self._millisecond != 0:
            time += '.' + printDigit(numberMLS, 3)

        if self._microsecond != 0:
            if '.' in time:
                time += printDigit(numberMCS, 3)
            else:
                time += '.000' + printDigit(numberMCS, 3)

        if self._nanosecond != 0:
            time += printDigit(numberNNS, 3)

        try:
            time += f" {_DICTIONARY[self._language]['seconds'] if float(str(self._second) + '.' + printDigit(numberMLS, 3) + printDigit(numberMCS, 3) + printDigit(numberNNS, 3)) > 1 else _DICTIONARY[self._language]['second']}."
        except:
            pass
        if self._year != 0 or self._month != 0 or self._day != 0 or self._hour != 0 or self._minute != 0:
            time = f"{self._minute} {_DICTIONARY[self._language]['minutes'] if self._minute > 1 else _DICTIONARY[self._language]['minute']} {_DICTIONARY[self._language]['and']} {time}"
            if self._year != 0 or self._month != 0 or self._day != 0 or self._hour != 0:
                time = f"{self._hour} {_DICTIONARY[self._language]['hours'] if self._hour > 1 else _DICTIONARY[self._language]['hour']}, {time}"
                if self._year != 0 or self._month != 0 or self._day != 0:
                    time = f"{self._day} {_DICTIONARY[self._language]['days'] if self._day > 1 else _DICTIONARY[self._language]['day']}, {time}"
                    if self._year != 0 or self._month != 0:
                        time = f"{self._month} {_DICTIONARY[self._language]['months'] if self._month > 1 else _DICTIONARY[self._language]['month']}, {time}"
                        if self._year != 0:
                            time = f"{self._year} {_DICTIONARY[self._language]['years'] if self._year > 1 else _DICTIONARY[self._language]['year']}, {time}"
        return (self._name + " : " if self._name else '') + time

    def __repr__(self) -> str:
        return f"Time(year={self._year}, month={self._month}, day={self._day}, hour={self._hour}, minute={self._minute}, second={self._second}, millisecond={self._millisecond}, microsecond={self._microsecond}, nanosecond={self._nanosecond}, name={self._name})"

    def __format__(self, format_spec: str) -> str:
        """
        for an example of Time(year=1985, month=6, day=21, hour=11, minute=1, second=59, millisecond=13, microsecond=541, name='Time')
        format:
            _name_  -> Time     Returns the name of the variable

            _Y_     -> 1985
            _M_     -> 6
            _D_     -> 21

            _h_     -> 11
            _m_     -> 1
            _s_     -> 59
            _mls_   -> 13
            _mcs_   -> 541
            _nns_   -> 800
        """
        keys = {
            "name": self._name,
            "Y": str(self._year),
            "M": str(self._month),
            "D": str(self._day),
            "h": str(self._hour),
            "m": str(self._minute),
            "s": str(self._second),
            "mls": str(self._millisecond),
            "mcs": str(self._microsecond),
            "nns": str(self._nanosecond)
        }
        time = ""
        key = ""
        lock = False
        for l in format_spec:
            if l == "_":
                if lock:
                    if key in keys:
                        time += keys[key]
                    else:
                        time += "_" + key + "_"
                else:
                    key = ""
                lock = not lock
            elif lock:
                key += l
            else:
                time += l
        return time

    def __getitem__(self, item) -> typing.Any:
        if item > 10 or item < -11:
            raise IndexError("time index out of range")
        else:
            return [
                self._name,
                self._year,
                self._month,
                self._day,
                self._hour,
                self._minute,
                self._second,
                self._millisecond,
                self._microsecond,
                self._nanosecond,
                self._language
            ][item]

    def __dir__(self) -> typing.Iterable[str]:
        return [self._name, str(self._year), str(self._month), str(self._day), str(self._hour), str(self._minute),
                str(self._second), str(self._millisecond), str(self._microsecond), str(self._nanosecond)]

    def __iter__(self):
        return iter([
            ["name", self._name],
            ["year", self._year],
            ["month", self._month],
            ["day", self._day],
            ["hour", self._hour],
            ["minute", self._minute],
            ["second", self._second],
            ["millisecond", self._millisecond],
            ["microsecond", self._microsecond],
            ["nanosecond", self._nanosecond]
        ])

    def _get_years(self) -> int:
        return self._year

    def _get_months(self) -> int:
        return self._get_years() * 12 + self._month

    def _get_days(self) -> int:
        return round(self._get_months() * 30.436875 + self._day)

    def _get_hours(self) -> int:
        return self._get_days() * 24 + self._hour

    def _get_minutes(self) -> int:
        return self._get_hours() * 60 + self._minute

    def _get_seconds(self) -> int:
        return self._get_minutes() * 60 + self._second

    def _get_milliseconds(self) -> int:
        return self._get_seconds() * 1000 + self._millisecond

    def _get_microseconds(self) -> int:
        return self._get_milliseconds() * 1000 + self._microsecond

    def _get_nanoseconds(self) -> int:
        return self._get_microseconds() * 1000 + self._nanosecond

    def get(self, time) -> int:
        return {
            "year": self._get_years,
            "month": self._get_months,
            "day": self._get_days,
            "hour": self._get_hours,
            "minute": self._get_minutes,
            "second": self._get_seconds,
            "millisecond": self._get_milliseconds,
            "microsecond": self._get_microseconds,
            "nanosecond": self._get_nanoseconds
        }[time]()

    def get_value(self, time) -> int:
        return {
            "year": self._year,
            "month": self._month,
            "day": self._day,
            "hour": self._hour,
            "minute": self._minute,
            "second": self._second,
            "millisecond": self._millisecond,
            "microsecond": self._microsecond,
            "nanosecond": self._nanosecond
        }[time]

    def rename(self, name: str):
        self._name = name

    def set_language(self, language: str):
        code = language[0:2]
        if code in _DICTIONARY:
            self._language = code
        else:
            raise ValueError(f'{code} is not in supported languages')


class Date(Time):
    @staticmethod
    def __doc__():
        return """\

        Documentation of Date:

     • __init__ -> Can be called empty to initialize to 0
     • by_time() -> static method allowing to convert a Time into a Date
     • by_datetime_datetime() -> static method allowing to convert a datetime.datetime into Date
     • by_datetime_date() -> static method allowing to convert a datetime.date into Date
     • by_datetime_time() -> static method allowing to convert a datetime.time into Date
     • now() -> static method that returns the current date
     • update() -> allows to update the attributes
     • countdown() -> Returns a Time value of the time remaining until this date
     • chrono() -> Returns a Time value of the time elapsed since this date
     • get_name_month() -> Give the name of the month
     • get_name_day() -> Give the name of the day of the week
     • -self -> returns the opposite
     • self - x -> remove x from the current object
     • self == x -> checks for equality with x
     • self != x -> checks the inequality with x
     • str(self) -> sends a character string corresponding to the object
     • print(self) -> sends a character string corresponding to the object
     • format(self, "~") -> sends a character string formatted according to the character string
     • self[x] -> sends the value of the object according to x
     • list(self) -> returns a list with the values of the object
"""

    @staticmethod
    def by_time(time):
        return Date(time[1], time[2], time[3], time[4], time[5], time[6], time[7], time[8], time[9], time[0], time[10])

    @staticmethod
    def by_date(date):
        return date

    @staticmethod
    def by_datetime_date(date: datetime.date):
        return Date(date.year, date.month, date.day)

    @staticmethod
    def by_datetime_time(date: datetime.time):
        return Date(0, 0, 0, date.hour, date.minute, date.second,
                    date.microsecond // 1000, date.microsecond % 1000)

    @staticmethod
    def by_datetime_datetime(date: datetime.datetime):
        return Date(date.year, date.month, date.day, date.hour, date.minute, date.second,
                    date.microsecond // 1000, date.microsecond % 1000)

    @staticmethod
    def now():
        return Date(
            # time_ns() -> UTC time since epoch + compensation to arrive at today
            nanosecond=(time_ns() + Date(year=1970).get('nanosecond') + Time(
                minute=DELTA[os.popen('tzutil /g').read()]).get('nanosecond')),
            name="NOW"
        )

    def __init__(
            self,
            year: int = None,
            month: int = None,
            day: int = None,
            hour: int = 0,
            minute: int = 0,
            second: int = 0,
            millisecond: int = 0,
            microsecond: int = 0,
            nanosecond: int = 0,
            name: str = None,
            language: str = None
    ):

        if year is None and month is None and day is None and hour + minute + second + millisecond + microsecond + nanosecond == 0:
            year = 400
            month = 1
            day = 1
        else:
            if year is None:
                year = 0
            if month is None:
                month = 0
            if day is None:
                day = 0

        super().__init__(year, month, day, hour, minute, second, millisecond, microsecond, nanosecond, name, language)

        self._name = name
        self._language = _LANGUAGE

        try:
            self.set_language(language)
        except ValueError:
            pass
        except TypeError:
            pass

        self._year = year
        self._month = month
        self._day = day
        self._hour = hour
        self._minute = minute
        self._second = second
        self._millisecond = millisecond
        self._microsecond = microsecond
        self._nanosecond = nanosecond

        self.update()

        if self._month == 0:
            self._month = 1
        if self._day == 0:
            self._day = 1

    def update(self):
        if self._nanosecond >= 1000:
            self._microsecond += self._nanosecond // 1000
            self._nanosecond = self._nanosecond % 1000
        elif self._nanosecond <= -1000:
            self._microsecond -= self._nanosecond // -1000
            self._nanosecond = self._nanosecond % -1000

        if self._microsecond >= 1000:
            self._millisecond += self._microsecond // 1000
            self._microsecond = self._microsecond % 1000
        elif self._microsecond <= -1000:
            self._millisecond -= self._microsecond // -1000
            self._microsecond = self._microsecond % -1000

        if self._millisecond >= 1000:
            self._second += self._millisecond // 1000
            self._millisecond = self._millisecond % 1000
        elif self._millisecond <= -1000:
            self._second -= self._millisecond // -1000
            self._millisecond = self._millisecond % -1000

        if self._second >= 60:
            self._minute += self._second // 60
            self._second = self._second % 60
        elif self._second <= -60:
            self._minute -= self._second // -60
            self._second = self._second % -60

        if self._minute >= 60:
            self._hour += self._minute // 60
            self._minute = self._minute % 60
        elif self._minute <= -60:
            self._hour -= self._minute // -60
            self._minute = self._minute % -60

        if self._hour >= 24:
            self._day += self._hour // 24
            self._hour = self._hour % 24
        elif self._hour <= -24:
            self._day -= self._hour // -24
            self._hour = self._hour % -24

        if self._day > 30.436875:
            self._month += int(self._day // 30.436875)
            self._day = int(self._day % 30.436875)

        elif self._day < -30.436875:
            self._month -= int(self._day // -30.436875)
            self._day = int(self._day % -30.436875)

        if self._month > 12:
            self._year += self._month // 12
            self._month = self._month % 12
        elif self._month < -12:
            self._year -= self._month // -12
            self._month = self._month % -12

    def countdown(self) -> Time:
        r = self - Date.now()
        r.rename(f"{_DICTIONARY[self._language]['time remaining until']}{self._name}")
        r.set_language(self._language)
        return r

    def chrono(self):
        c = Date.now() - self
        c.rename(f"{_DICTIONARY[self._language]['time elapsed since']}{self._name}")
        c.set_language(self._language)
        return c

    def get_name_month(self):
        return \
            [
                _DICTIONARY[self._language]['january'],
                _DICTIONARY[self._language]['february'],
                _DICTIONARY[self._language]['march'],
                _DICTIONARY[self._language]['april'],
                _DICTIONARY[self._language]['may'],
                _DICTIONARY[self._language]['june'],
                _DICTIONARY[self._language]['july'],
                _DICTIONARY[self._language]['august'],
                _DICTIONARY[self._language]['september'],
                _DICTIONARY[self._language]['october'],
                _DICTIONARY[self._language]['november'],
                _DICTIONARY[self._language]['december']
            ][self._month - 1]

    def get_name_day(self):
        valJ = {
            0: _DICTIONARY[self._language]['sunday'],
            1: _DICTIONARY[self._language]['monday'],
            2: _DICTIONARY[self._language]['tuesday'],
            3: _DICTIONARY[self._language]['wednesday'],
            4: _DICTIONARY[self._language]['thursday'],
            5: _DICTIONARY[self._language]['friday'],
            6: _DICTIONARY[self._language]['saturday'],
        }
        valM = {
            False: {
                1: 4,
                2: 0,
                3: 0,
                4: 3,
                5: 5,
                6: 1,
                7: 3,
                8: 6,
                9: 2,
                10: 4,
                11: 0,
                12: 2
            },
            True: {
                1: 3,
                2: 6,
                3: 0,
                4: 3,
                5: 5,
                6: 1,
                7: 3,
                8: 6,
                9: 2,
                10: 4,
                11: 0,
                12: 2
            }
        }
        if self._year in range(400, 9999):
            ab = int(str(self._year)[:2])
            cd = int(str(self._year)[2:])
            k = int(cd / 4)

            if int(f"{self._year:02d}{self._month:02d}{self._day:02d}") > 15821015:
                return valJ[
                    (k + int(ab / 4) + cd +
                     valM[(self._year % 4 == 0 and self._year % 100 != 0) or self._year % 400 == 0][
                         self._month] + self._day + 2 + 5 * ab) % 7]
            else:
                return valJ[
                    (k + cd + valM[(self._year % 4 == 0 and self._year % 100 != 0) or self._year % 400 == 0][
                        self._month] + self._day + 6 * ab) % 7]

        else:
            raise ValueError("The year must be between 400 and 9999.")

    def __format__(self, format_spec: str):
        f"""
        for an example of Date(year=1985, month=6, day=21, hour=11, minute=31, second=59, millisecond=13, microsecond=541, name='Date')
        format:
            _name_  -> Time     Returns the name of the variable

            _YYYY_  -> 1985     [force has 4 characters]
            _YY_    -> 85       [force has 2 characters]
            _Y_     -> 1985

            _MM_    -> 06       [force has 2 characters]
            _NM_    -> {_DICTIONARY[self._language]['June']}
            _M_     -> 6

            _DD_    -> 21       [force has 2 characters]
            _ND_    -> {_DICTIONARY[self._language]['Friday']}
            _D_     -> 21

            _hh_    -> 11       [force has 2 characters]
            _h_     -> 11
            _mm_    -> 31       [force has 2 characters]
            _m_     -> 31
            _ss_    -> 59       [force has 2 characters]
            _s_     -> 59
            _mls_   -> 013      [force has 3 characters]
            _mcs_   -> 541      [force has 3 characters]
            _nns_   -> 800      [force has 3 characters]
        """

        def intToString(integer: int, nb_digit: int) -> str:
            ret = str(integer)
            while len(ret) != nb_digit:
                if len(ret) > nb_digit:
                    ret = ret[-nb_digit:]
                else:
                    ret = "0" + ret
            return ret

        keys = {
            "name": self._name,

            "YYYY": intToString(self._year, 4),
            "YY": intToString(self._year, 2),
            "Y": str(self._year),

            "MM": intToString(self._month, 2),
            "M": str(self._month),
            "NM": self.get_name_month(),

            "DD": intToString(self._day, 2),
            "D": str(self._day),
            "ND": self.get_name_day(),

            "hh": intToString(self._hour, 2),
            "h": str(self._hour),

            "mm": intToString(self._minute, 2),
            "m": str(self._minute),

            "ss": intToString(self._second, 2),
            "s": str(self._second),

            "mls": intToString(self._millisecond, 3),
            "mcs": intToString(self._microsecond, 3),
            "nns": intToString(self._nanosecond, 3)
        }
        date = ""
        key = ""
        lock = False
        for l in format_spec:
            if l == "_":
                if lock:
                    if key in keys:
                        date += keys[key]
                    else:
                        date += "_" + key + "_"
                else:
                    key = ""
                lock = not lock
            elif lock:
                key += l
            else:
                date += l
        return date

    def __str__(self):
        return self.__format__("_ND_ _D_ _NM_ _Y_ " + _DICTIONARY[self._language]['to'] +
                               " _h_h_mm_ " + _DICTIONARY[self._language]['and'] +
                               " _s_,_mls__mcs__nns_ " + _DICTIONARY[self._language]['seconds'])

    def __repr__(self) -> str:
        return f"Date(year={self._year}, month={self._month}, day={self._day}, hour={self._hour}, minute={self._minute}, second={self._second}, millisecond={self._millisecond}, microsecond={self._microsecond}, nanosecond={self._nanosecond}, name={self._name})"


def set_language(language: str):
    code = language[0:2]
    if code in _DICTIONARY:
        global _LANGUAGE
        _LANGUAGE = code
    else:
        raise ValueError(f'{code} is not in supported languages')


if __name__ == '__main__':
    if Date.now().get_value('month') > 9 or (Date.now().get_value('month') == 9 and Date.now().get_value('day') > 7):
        birthday = Date(year=Date.now().get_value('year') + 1, month=9, day=7, hour=20, minute=50)
    else:
        birthday = Date(year=Date.now().get_value('year'), month=9, day=7, hour=20, minute=50)

    test: Time

    print(f"{str(Date.now())}\n"
          f"{str(birthday.countdown())}\n"
          f"{str(Date.now() + birthday.countdown())}\n\n")
    test = Date.now() + birthday.countdown()
    print(f"My birthday is in {str(birthday.countdown()).split(':')[1][1:]}\n"
          f"the {str(Date.by_time(test))}\n")

    birthday.set_language('fr')
    test.set_language('fr')
    print(f"Mon anniversaire est dans {str(birthday.countdown()).split(':')[1][1:]}\n"
          f"le {str(Date.by_time(test))}\n")

    birthday.set_language('sp')
    test.set_language('sp')
    print(f"Mi cumpleaños es en {str(birthday.countdown()).split(':')[1][1:]}\n"
          f"la {str(Date.by_time(test))}\n")
