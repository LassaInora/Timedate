import datetime
import time
import warnings

import LassaLib

_DICTIONARY = {
    'en': {
        'january': 'January',
        'february': 'February',
        'march': 'March',
        'april': 'April',
        'may': 'May',
        'june': 'June',
        'july': 'July',
        'august': 'August',
        'september': 'September',
        'october': 'October',
        'november': 'November',
        'december': 'December',
        'sunday': 'Sunday',
        'monday': 'Monday',
        'tuesday': 'Tuesday',
        'wednesday': 'Wednesday',
        'thursday': 'Thursday',
        'friday': 'Friday',
        'saturday': 'Saturday',
    },
    'ma': {
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
        'january': 'জানুয়ারী',
        'february': 'ফেব্রুয়ারি',
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

_LANGUAGE = "en"


def set_language(language: str):
    """Choose the program language.

    Langages
    --------
        + en : English
        + ma : Mandarin
        + hi : Hindi
        + sp : Spanish
        + be : Bengali
        + fr : French
        + ru : Russian
        + po : Portuguese

    Parameters:
        language (str) : The chosen language.
    """
    global _LANGUAGE
    if language.lower() in _DICTIONARY.keys():
        _LANGUAGE = language.lower()
    else:
        warnings.warn(Warning("Language not allowed."))


class _Calendar:
    def __init__(self, year, pointeur=...):
        if pointeur is ...:
            pointeur = [1, 1]

        self.year = year
        self.pointeur = pointeur
        self._normalize()

    def __str__(self):
        return f"|{self.year} {self.pointeur[0]} {self.pointeur[1]}|"

    def _normalize(self):
        def normalize_month():
            if 0 > self.pointeur[0] or self.pointeur[0] > 12:
                self.year += self.pointeur[0] // 12
                self.pointeur[0] %= 12
            elif self.pointeur[0] == 0:
                self.year -= 1
                self.pointeur[0] = 12

        normalize_month()
        while self.nb_day_at_this_month <= self.pointeur[1]:
            self.pointeur[1] -= self.nb_day_at_this_month
            self.pointeur[0] += 1
            normalize_month()
        while self.pointeur[1] <= 0:
            self.pointeur[1] += self.calendar[self.pointeur[0] - 1 if self.pointeur[0] > 1 else 12]
            self.pointeur[0] -= 1
            normalize_month()

    def next(self):
        self.pointeur[1] += 1
        self._normalize()

    def previous(self):
        self.pointeur[1] -= 1
        self._normalize()

    def nb_day_for(self, year=1970):
        copy = _Calendar(self.year, self.pointeur)
        days = 0
        while copy.year + 1 != year:
            days += 1
            copy.previous()
        return days

    @property
    def days(self):
        return self.round_year, self.nb_day_for(self.round_year)

    @property
    def round_year(self):
        return (self.year // 20) * 20

    @property
    def is_a_leap_year(self):
        return (
                (
                        self.year % 4 == 0 and
                        self.year % 100 != 0
                ) or
                self.year % 400 == 0
        )

    @property
    def calendar(self):
        return [
            0,
            31,
            29 if self.is_a_leap_year else 28,
            31,
            30,
            31,
            30,
            31,
            31,
            30,
            31,
            30,
            31
        ]

    @property
    def nb_day_at_this_month(self):
        return self.calendar[self.pointeur[0]]

    @property
    def day(self):
        return self.pointeur[1]

    @property
    def month(self):
        return self.pointeur[0]


class _TimeDate:
    def __init__(
            self,
            year=0, month=0, day=0,
            hour=0, minute=0, second=0,
            milli=0, micro=0, nano=0,
            pico=0, femto=0, atto=0,
            zepto=0, yocto=0, *, its_a_date=True
    ):
        self._update(
            year, month, day,
            hour, minute, second,
            milli, micro, nano, pico, femto, atto, zepto, yocto,
            its_a_date
        )

    def _update(
            self,
            year, month, day,
            hour, minute, second,
            milli, micro, nano,
            pico, femto, atto,
            zepto, yocto, its_a_date
    ):
        self.yocto = int(yocto % 1000)
        zepto += yocto // 1000
        self.zepto = int(zepto % 1000)
        atto += zepto // 1000
        self.atto = int(atto % 1000)
        femto += atto // 1000
        self.femto = int(femto % 1000)
        pico += femto // 1000
        self.pico = int(pico % 1000)
        nano += pico // 1000
        self.nano = int(nano % 1000)
        micro += nano // 1000
        self.micro = int(micro % 1000)
        milli += micro // 1000
        self.milli = int(milli % 1000)
        second += milli // 1000
        self.second = int(second % 60)
        minute += second // 60
        self.minute = int(minute % 60)
        hour += minute // 60
        self.hour = int(hour % 24)
        day += hour // 24

        c = _Calendar(year, [month + (0 if its_a_date else 1), day])

        self.day = int(c.day) - (0 if its_a_date else 1)
        self.month = int(c.month) - (0 if its_a_date else 1)
        self.year = int(c.year)

    @property
    def recommended_format(self):
        """Return a recommended format for time or date with format()

        Returns:
            (str): The recommended format.
        """
        if self.year > 0:
            frmt = "_Y_ _M_ _D_ - _hh_:_mm_:_ss_"
        elif self.month > 0:
            frmt = "_M_ _D_ - _hh_:_mm_:_ss_"
        elif self.day > 0:
            frmt = "(_D_) _hh_:_mm_:_ss_"
        elif self.hour > 0:
            frmt = "_h_:_mm_:_ss_"
        elif self.minute > 0:
            frmt = "_m_:_ss_"
        else:
            frmt = "_s_"

        if self.yocto > 0:
            frmt += "._mls__mcs__nns__pcs__fms__ats__zps__yts_"
        elif self.zepto > 0:
            frmt += "._mls__mcs__nns__pcs__fms__ats__zps_"
        elif self.atto > 0:
            frmt += "._mls__mcs__nns__pcs__fms__ats_"
        elif self.femto > 0:
            frmt += "._mls__mcs__nns__pcs__fms_"
        elif self.pico > 0:
            frmt += "._mls__mcs__nns__pcs_"
        elif self.nano > 0:
            frmt += "._mls__mcs__nns_"
        elif self.micro > 0:
            frmt += "._mls__mcs_"
        elif self.milli > 0:
            frmt += "._mls_"

        return frmt

    @property
    def _formats(self):
        return {
            "_YYYY_": LassaLib.position('right', str(self.year), 4, '0'),
            "_YY_": LassaLib.position('right', str(self.year)[-2:], 2, '0'),
            "_Y_": LassaLib.position('right', str(self.year), 1, '0'),

            "_MM_": LassaLib.position('right', str(self.month), 2, '0'),
            "_M_": LassaLib.position('right', str(self.month), 1, '0'),

            "_DD_": LassaLib.position('right', str(self.day), 2, '0'),
            "_D_": LassaLib.position('right', str(self.day), 1, '0'),

            "_hh_": LassaLib.position('right', str(self.hour), 2, '0'),
            "_h_": LassaLib.position('right', str(self.hour), 1, '0'),

            "_mm_": LassaLib.position('right', str(self.minute), 2, '0'),
            "_m_": LassaLib.position('right', str(self.minute), 1, '0'),

            "_ss_": LassaLib.position('right', str(self.second), 2, '0'),
            "_s_": LassaLib.position('right', str(self.second), 1, '0'),

            "_mls_": LassaLib.position('right', str(self.milli), 3, '0'),
            "_mcs_": LassaLib.position('right', str(self.micro), 3, '0'),
            "_nns_": LassaLib.position('right', str(self.nano), 3, '0'),
            "_pcs_": LassaLib.position('right', str(self.pico), 3, '0'),
            "_fms_": LassaLib.position('right', str(self.femto), 3, '0'),
            "_ats_": LassaLib.position('right', str(self.atto), 3, '0'),
            "_zps_": LassaLib.position('right', str(self.zepto), 3, '0'),
            "_yts_": LassaLib.position('right', str(self.yocto), 3, '0'),

            "_en-time_": (  # 8:50 p.m. and 35 seconds.
                f"{self.hour % 12}:{self.minute}"
                f"{'' if self.second == 0 else f''' {self.second} second{'s' if self.second > 1 else ''}'''}"
                f"{' a.m.' if self.hour < 12 else ' p.m.'}"
            ),
            "_ma-time_": (  # 晚上 8 点 50 分 35 秒
                f"{'凌晨 ' if self.hour < 12 else '晚上 '}"
                f"{self.hour % 12} 点 {self.minute} 分"
                f"{'' if self.second == 0 else f' {self.second} 秒'}"
            ),
            "_hi-time_": (  # 8:50 अपराह्न और 35 सेकंड
                f"{self.hour % 12}:{self.minute}"
                f"{' पूर्वाह्न' if self.hour < 12 else ' अपराह्न'}"
                f"{'' if self.second == 0 else f' और {self.second} सेकंड'}"
            ),
            "_sp-time_": (  # 20:50 y 35 segundos
                f"{self.hour}:{self.minute}"
                f"{'' if self.second == 0 else f''' y {self.second} segundo{'s' if self.second > 1 else ''}'''}"
            ),
            "_be-time_": (  # রাত 8:50 এবং 35 সেকেন্ড।
                f"{'' if self.hour < 12 else 'রাত '}"
                f"{self.hour % 12}:{self.minute}"
                f"{'' if self.second == 0 else f' এবং {self.second} সেকেন্ড'}"
            ),
            "_fr-time_": (  # 20 h 50 et 35 secondes
                f"{self.hour} h {self.minute}"
                f"{'' if self.second == 0 else f''' et {self.second} seconde{'s' if self.second > 1 else ''}'''}"
            ),
            "_ru-time_": (  # 20:50 и 35 секунд
                f"{self.hour}:{self.minute}"
                f"{'' if self.second == 0 else f''' и {self.second} секунд{'' if self.second > 1 else 'а'}'''}"
            ),
            "_po-time_": (  # 20h50 e 35 segundos.
                f"{self.hour}h{self.minute}"
                f"{'' if self.second == 0 else f''' e {self.second} segundo{'s' if self.second > 1 else ''}'''}"
            ),
        }

    def __format__(self, format_spec: str):
        for key in self._formats:
            format_spec = format_spec.replace(key, self._formats[key])
        return format_spec

    def __str__(self):
        return format(self, self.recommended_format)

    def __repr__(self):
        return format(self, "_YYYY_ _MM_ _DD_ - _hh_:_mm_:_ss_._mls__mcs__nns__pcs__fms__ats__zps__yts_")

    def __int__(self):
        return (
                self.second +
                self.minute * 60 +
                self.hour * 3600 +
                _Calendar(self.year, [self.month + 1, self.day + 1]).nb_day_for(0) * 86400
        )

    def __float__(self):
        return int(self) + float(format(self, "0._mls__mcs__nns__pcs__fms__ats__zps__yts_"))

    def __iter__(self):
        return iter(
            [
                self.year, self.month, self.day,
                self.hour, self.minute, self.second,
                self.milli, self.micro, self.nano,
                self.pico, self.femto, self.atto,
                self.zepto, self.yocto]
        )

    @property
    def copy_time(self):
        """Create a copy of actual value in Time class.

        Returns:
            (Time): Time value.
        """
        reindex = 0 if isinstance(self, Time) else 1
        return Time(
            self.year, self.month - reindex, self.day - reindex,
            self.hour, self.minute, self.second,
            self.milli, self.micro, self.nano, self.pico, self.femto, self.atto, self.zepto, self.yocto
        )

    @property
    def copy_date(self):
        """Create a copy of actual value in Date class.

        Returns:
            (Date): Date value.
        """
        reindex = 0 if isinstance(self, Date) else 1
        return Date(
            self.year, self.month + reindex, self.day + reindex,
            self.hour, self.minute, self.second,
            self.milli, self.micro, self.nano, self.pico, self.femto, self.atto, self.zepto, self.yocto
        )

    def __sub__(self, other):
        """Retirer une valeur au temps actuelle

        Parameters:
            other (Time): Temps à retirer

        Returns:
            (Time): Temps restant
        """
        return Time(
            self.year - other.year, self.month - other.month, self.day - other.day,
            self.hour - other.hour, self.minute - other.minute, self.second - other.second,
            self.milli - other.milli, self.micro - other.micro, self.nano - other.nano,
            self.pico - other.pico, self.femto - other.femto, self.atto - other.atto,
            self.zepto - other.zepto, self.yocto - other.yocto
        )

    def __add__(self, other):
        """Ajouter une valeur au temps actuelle

        Parameters:
            other (Time): Temps à ajouter

        Returns:
            (Time): Temps restant
        """
        return Time(
            self.year + other.year, self.month + other.month, self.day + other.day,
            self.hour + other.hour, self.minute + other.minute, self.second + other.second,
            self.milli + other.milli, self.micro + other.micro, self.nano + other.nano,
            self.pico + other.pico, self.femto + other.femto, self.atto + other.atto,
            self.zepto + other.zepto, self.yocto + other.yocto
        )

    def __eq__(self, other):
        me = self.copy_time
        other = other.copy_time

        return (
                me.year == other.year and
                me.month == other.month and
                me.day == other.day and
                me.hour == other.hour and
                me.minute == other.minute and
                me.second == other.second and
                me.milli == other.milli and
                me.micro == other.micro and
                me.nano == other.nano and
                me.pico == other.pico and
                me.femto == other.femto and
                me.atto == other.atto and
                me.zepto == other.zepto and
                me.yocto == other.yocto
        )

    def __ne__(self, other):
        return not (self == other)

    def _transform_for_compare(self, other):
        me = self.copy_time
        other = other.copy_time

        ry = min(
            _Calendar(me.year, [me.month + 1, me.day + 1]).round_year,
            _Calendar(other.year, [other.month + 1, other.day + 1]).round_year
        )

        me = (me.second + me.minute * 60 + me.hour * 3600 + _Calendar(me.year, [me.month + 1, me.day + 1]).nb_day_for(
            ry) * 86400) + float(format(me, "0._mls__mcs__nns__pcs__fms__ats__zps__yts_"))
        other = (other.second + other.minute * 60 + other.hour * 3600 + _Calendar(other.year, [other.month + 1,
                                                                                               other.day + 1]).nb_day_for(
            ry) * 86400) + float(format(other, "0._mls__mcs__nns__pcs__fms__ats__zps__yts_"))

        return me, other

    def __lt__(self, other):
        me, other = self._transform_for_compare(other)
        return me < other

    def __le__(self, other):
        me, other = self._transform_for_compare(other)
        return me <= other

    def __gt__(self, other):
        me, other = self._transform_for_compare(other)
        return me > other

    def __ge__(self, other):
        me, other = self._transform_for_compare(other)
        return me >= other


class Time(_TimeDate):
    def __init__(
            self,
            year=0, month=0, day=0,
            hour=0, minute=0, second=0,
            milli=0, micro=0, nano=0,
            pico=0, femto=0, atto=0,
            zepto=0, yocto=0
    ):
        super().__init__(
            year, month, day + 1, hour, minute, second, milli, micro, nano, pico, femto, atto, zepto, yocto,
            its_a_date=False
        )


class Date(_TimeDate):
    class Calendar:
        def __init__(self, year, pointeur=...):
            if pointeur is ...:
                pointeur = [1, 1]

            self.year = year
            self.pointeur = pointeur
            self._normalize()

        def __str__(self):
            return f"{self.pointeur[1]} {['Error', 'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Décembre'][self.pointeur[0]]} {self.year}"

        def _normalize(self):
            def normalize_month():
                if self.pointeur[0] > 12:
                    self.year += self.pointeur[0] // 12
                    self.pointeur[0] %= 12

            while self.nb_day_at_this_month < self.pointeur[1]:
                self.pointeur[1] -= self.nb_day_at_this_month
                self.pointeur[0] += 1
                normalize_month()

        def next(self):
            self.pointeur[1] += 1
            self._normalize()

        @property
        def is_a_leap_year(self):
            return (
                    (
                            self.year % 4 == 0 and
                            self.year % 100 != 0
                    ) or
                    self.year % 400 == 0
            )

        @property
        def calendar(self):
            return [
                0,
                31,
                29 if self.is_a_leap_year else 28,
                31,
                30,
                31,
                30,
                31,
                31,
                30,
                31,
                30,
                31
            ]

        @property
        def nb_day_at_this_month(self):
            return self.calendar[self.pointeur[0]]

    @classmethod
    def NOW(cls):
        """Return the current date.

        Returns:
            (Date): The date of the local computer.
        """
        return cls(timestamp=time.time_ns() / (10 ** 9))

    @staticmethod
    def from_datetime(datetime_):
        """Create a Date from a datetime.datetime.

        Parameters:
            datetime_ (datetime.datetime): The datetime value

        Returns:
            (Date): The Date value
        """
        return Date(
            datetime_.year, datetime_.month, datetime_.day,
            datetime_.hour, datetime_.minute, datetime_.second,
            micro=datetime_.microsecond
        )

    def __init__(
            self, year=400, month=1, day=1, hour=0, minute=0, second=0,
            milli=0, micro=0, nano=0, pico=0, femto=0, atto=0, zepto=0, yocto=0,
            *, timestamp=...
    ):
        if timestamp is not ...:
            data = datetime.datetime.fromtimestamp(int(timestamp // 1))
            sub_second_data = LassaLib.space_number(int(timestamp % 1 * (10 ** 24))).split()

            super().__init__(
                data.year, data.month, data.day, data.hour, data.minute, data.second,
                int(sub_second_data[0]) if len(sub_second_data) > 0 else 0,
                int(sub_second_data[1]) if len(sub_second_data) > 1 else 0,
                int(sub_second_data[2]) if len(sub_second_data) > 2 else 0,
                int(sub_second_data[3]) if len(sub_second_data) > 3 else 0,
                int(sub_second_data[4]) if len(sub_second_data) > 4 else 0,
                int(sub_second_data[5]) if len(sub_second_data) > 5 else 0,
                int(sub_second_data[6]) if len(sub_second_data) > 6 else 0,
                int(sub_second_data[7]) if len(sub_second_data) > 7 else 0,
            )
        else:
            super().__init__(
                year, month, day, hour, minute, second,
                milli, micro, nano, pico, femto, atto, zepto, yocto
            )

    @property
    def _formats(self):
        frmt = super()._formats
        frmt['_NM_'] = self.name_month
        frmt['_ND_'] = self.name_day
        return frmt

    @property
    def recommended_format(self):
        if _LANGUAGE == 'en':
            return f"_ND_, _NM_ _D_, _Y_ at _en-time_"
        elif _LANGUAGE == 'ma':
            return f"_Y_ 年 _M_ 月 _D_ _ND_ _ma-time_"
        elif _LANGUAGE == 'hi':
            return f"_ND_, _NM_ _D_, _Y_ को _hi-time_."
        elif _LANGUAGE == 'sp':
            return f"_ND_, _D_ de _NM_ de _Y_ a las _sp-time_"
        elif _LANGUAGE == 'be':
            return f"_ND_, _NM_ _D_, _Y_ _be-time_"
        elif _LANGUAGE == 'fr':
            return f"_ND_ _D_ _NM_ _Y_ à _fr-time_"
        elif _LANGUAGE == 'ru':
            return f"_ND_, _D_ _NM_ _Y_ г., _ru-time_"
        elif _LANGUAGE == 'po':
            return f"_ND_, _D_ de _NM_ de _Y_ às _po-time_"
        else:
            return f"_ND_, _NM_ _D_, _Y_ at _en-time_"

    @property
    def name_month(self):
        """Return the name of the month

        Returns:
            (str): The name.
        """
        return [
            _DICTIONARY[_LANGUAGE]['january'],
            _DICTIONARY[_LANGUAGE]['february'],
            _DICTIONARY[_LANGUAGE]['march'],
            _DICTIONARY[_LANGUAGE]['april'],
            _DICTIONARY[_LANGUAGE]['may'],
            _DICTIONARY[_LANGUAGE]['june'],
            _DICTIONARY[_LANGUAGE]['july'],
            _DICTIONARY[_LANGUAGE]['august'],
            _DICTIONARY[_LANGUAGE]['september'],
            _DICTIONARY[_LANGUAGE]['october'],
            _DICTIONARY[_LANGUAGE]['november'],
            _DICTIONARY[_LANGUAGE]['december']
        ][self.month - 1]

    @property
    def name_day(self):
        """Return the name of the day

        Returns:
            (str): The name.
        """
        valJ = {
            0: _DICTIONARY[_LANGUAGE]['sunday'],
            1: _DICTIONARY[_LANGUAGE]['monday'],
            2: _DICTIONARY[_LANGUAGE]['tuesday'],
            3: _DICTIONARY[_LANGUAGE]['wednesday'],
            4: _DICTIONARY[_LANGUAGE]['thursday'],
            5: _DICTIONARY[_LANGUAGE]['friday'],
            6: _DICTIONARY[_LANGUAGE]['saturday'],
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
        if self.year in range(400, 9999):
            ab = int(str(self.year)[:2])
            cd = int(str(self.year)[2:])
            k = int(cd / 4)

            if int(f"{self.year:02d}{self.month:02d}{self.day:02d}") > 15821015:
                return valJ[
                    (k + int(ab / 4) + cd +
                     valM[(self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0][
                         self.month] + self.day + 2 + 5 * ab) % 7]
            else:
                return valJ[
                    (k + cd + valM[(self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0][
                        self.month] + self.day + 6 * ab) % 7]

        else:
            raise ValueError("The year must be between 400 and 9999.")

    @property
    def datetime(self):
        """Create a datetime with current values.

        Returns:
            (datetime.datetime): The datetime
        """
        return datetime.datetime(self.year, self.month, self.day, self.hour, self.minute, self.second,
                                 (self.milli * 1000) + self.micro)

    @property
    def timestamp(self):
        """Create a timestamps with current values.

        Returns:
            (float): The timestamps.
        """
        return self.datetime.timestamp() + float(format(self, "0.000000_nns_"))

    @property
    def is_a_leap_year(self):
        """The current year is a leap year?

        Returns:
             (bool): The response.
        """
        return self.its_a_leap_year(self.year)

    @classmethod
    def its_a_leap_year(cls, year):
        """This year is a leap year?

        Returns:
             (bool): The response.
        """
        return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

    def __sub__(self, other):
        """"""
        if isinstance(other, Date):
            return self.copy_time - other.copy_time
        else:
            return (self.copy_time - other).copy_date

    def __add__(self, other):
        return (self.copy_time + other).copy_date

    @property
    def countdown(self):
        """Get the remaining time until this date.

        Returns:
            (Time): The time.
        """
        return self - Date.NOW() if self >= Date.NOW() else None

    @property
    def chrono(self):
        """Get the time passed since this date.

        Returns:
            (Time): The time.
        """
        return Date.NOW() - self if Date.NOW() >= self else None
