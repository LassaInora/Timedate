# Timedate

#### _Advanced date and time management library._

Author:
-------
- [Axelle (LassaInora) VIANDIER](mailto:axelleviandier@lassainora.fr)

License:
--------
- GNU General Public License v3.0

Version:
--------
- `3.0.0`

--------
## Summary

- **[Links](#links)**
- **[Supported languages](#support_lang)**
- **[Timedate functions and variables](#fonc_timedate)**
  - ***[set_language](#fonc_timedate)***
- **[For Time and Date](#timedate_methods)**
  - ***[Methods](#timedate_methods)***
- **[Class Time](#class_time)**
  - ***[Time initialization](#time__init__)***
  - ***[Formats](#time_formats)***
- **[Class Date](#class_date)**
  - ***[Date initialization](#date__init__)***
  - ***[Methods](#date_methods)***
  - ***[Formats](#date_formats)***
--------

## Links

- [Personal GitHub](https://github.com/LassaInora)
- [GitHub project](https://github.com/LassaInora/Timedate)
- [Website project](https://lassainora.fr/projets/librairies/Timedate)
- [Pypi project](https://pypi.org/project/advanced-timedate/)

--------

## <p id="support_lang">Supported languages:</p>

- English (en)
- Mandarin Chinese (ma)
- Hindi (hi)
- Spanish (sp)
- Bengali (be)
- French (fr)
- Russian (ru)
- Portuguese (po)

--------

## <p id="fonc_timedate">Timedate functions:</p>

- set_language()
  - Change the default language of the library.\
    \[en, ma, hi, sp, be, fr, ru, po] are accepted.
--------
## For Time and Date:

- ### <p id="timedate_methods">Methods:</p>
  - (Property) recommended_format
    - Return a recommended format for time or date with format()
  - (Property) copy_time
    - Return a copy of current value in Time class
  - (Property) copy_date
    - Return a copy of current value in Date class
  - < / > / <= / >= / == / != comparator
    - Return the result of comparaison with each comparator.
  - int(value)
    - Return the numbers of second since years 0.
  - float(value)
    - Return the numbers of second since years 0 with a precision of 24 decimal places.
  - str(value)
    - Return the current value with the recommended format.
  - repr(value)
    - Return the current value with "YYYY MM DD - hh:mm:ss.mls mcs nns pcs fms ats zps yts" format
  - iter(value) / list(value)
    - Return each sub-value of current value.
  - current value - other value
    - Remove the other value on current value
  - current value + other value
    - Add the other value on current value

## <p id="class_time">Class Time:</p>

- ### <p id="time__init__">Time initialization.</p>

  - year: The number of years.
  - month: The number of months.
  - day: The number of days.
  - hour: The number of hours.
  - minute: The number of minutes.
  - second: The number of seconds.
  - milli: The number of milliseconds.
  - micro: The number of microseconds.
  - nano: The number of nanoseconds.
  - pico: The number of picoseconds.
  - femto: The number of femtosecondes.
  - atto: The number of attosecondes.
  - zepto: The number of zeptosecondes.
  - yocto: The number of yoctosecondes.
  </br></br>
  For each value, the default value is 0.

- ### <p id="time_formats">Formats: </p>
  - \_YYYY_: The years in 4 digits.
  - \_YY_: The years in 2 digits.
  - \_Y_: The years.
  - \_MM_: The months in 2 digits.
  - \_M_: The months

  - \_DD_: The days in 2 digits.
  - \_D_: The day

  - \_hh_: The hours in 2 digits.
  - \_h_: The hour

  - \_mm_: The minutes in 2 digits.
  - \_m_: The minute

  - \_ss_: The secondes in 2 digits.
  - \_s_: The seconde

  - \_mls_: The milliseconds in 3 digits.
  - \_mcs_: The microseconds in 3 digits.
  - \_nns_: The nanoseconds in 3 digits.
  - \_pcs_: The picosecondes in 3 digits.
  - \_fms_: The femtosecondes in 3 digits.
  - \_ats_: The attosecondes in 3 digits.
  - \_zps_: The zeptosecondes in 3 digits.
  - \_yts_: The yoctosecondes in 3 digits.

  - \_en-time_: The time in english format
  - \_ma-time_: The time in Mandarin format
  - \_hi-time_: The time in Hindi format
  - \_sp-time_: The time in Spanish format
  - \_be-time_: The time in Bengali format
  - \_fr-time_: The time in French format
  - \_ru-time_: The time in Russian format.
  - \_po-time_: The time in Portuguese format.

--------
## <p id="class_date">Class Date:</p>

- ### <p id="date__init__">Date initialization.</p>

  - year: The number of year. Default is 400.
  - month: The number of month. Default is 1.
  - day: The number of day. Default is 1.
  - hour: The number of hour.
  - minute: The number of minute.
  - second: The number of second.
  - millisecond: The number of millisecond.
  - microsecond: The number of microsecond.
  - nanosecond: The number of nanosecond.
  - pico: The number of picoseconds.
  - femto: The number of femtosecondes.
  - atto: The number of attosecondes.
  - zepto: The number of zeptosecondes.
  - yocto: The number of yoctosecondes.
  </br></br>
  - timestamp: You can ignore all previously value and use a timestamp for initialize the Date.
  </br></br>
  For each unspecified value, the default value is 0.\
  Year cannot be less than 400.

- ### <p id="date_methods">Methods:</p>

  - (Static Method) from_datetime(datetime_)
    - Return a Date class create by datetime value
  - (Class Method) NOW()
    - Return the current Date
  - (Class Method) its_a_leap_year(year)
    - Return if year is a leap year.
  - (Property) name_month
    - Return the name of the month in the library langage (English in default).
  - (Property) name_day
    - Return the name of the day in the library langage (English in default).
  - (Property) datetime
    - Return a datetime with current value
  - (Property) timestamp
    - Return a timestamp with current value
  - (Property) is_a_leap_year
    - Return if current year is a leap year
  - (Property) countdown
    - Return the remaining time until the date.
  - (Property) chrono
    - Returns the time passed since the date.

- ### <p id="date_formats">Formats: </p>
  - \_YYYY_: The years in 4 digits.
  - \_YY_: The years in 2 digits.
  - \_Y_: The years.
  
  - \_MM_: The months in 2 digits.
  - \_M_: The months
  - \_NM_: The name of the month.

  - \_DD_: The days in 2 digits.
  - \_D_: The day
  - \_ND_: The name of the day.

  - \_hh_: The hours in 2 digits.
  - \_h_: The hour

  - \_mm_: The minutes in 2 digits.
  - \_m_: The minute

  - \_ss_: The secondes in 2 digits.
  - \_s_: The seconde

  - \_mls_: The milliseconds in 3 digits.
  - \_mcs_: The microseconds in 3 digits.
  - \_nns_: The nanoseconds in 3 digits.
  - \_pcs_: The picosecondes in 3 digits.
  - \_fms_: The femtosecondes in 3 digits.
  - \_ats_: The attosecondes in 3 digits.
  - \_zps_: The zeptosecondes in 3 digits.
  - \_yts_: The yoctosecondes in 3 digits.

  - \_en-time_: The time in english format
  - \_ma-time_: The time in Mandarin format
  - \_hi-time_: The time in Hindi format
  - \_sp-time_: The time in Spanish format
  - \_be-time_: The time in Bengali format
  - \_fr-time_: The time in French format
  - \_ru-time_: The time in Russian format.
  - \_po-time_: The time in Portuguese format.
