# <p id="title">Timedate</p>

Advanced date and time management library.

Python library by LassaInora.

--------
## Summary

- **[Links](#links)**
- **[Contacts](#contact)**
- **[Supported languages](#support_lang)**
- **[Timedate functions and variables](#fonc_timedate)**
- **[Class Time](#class_time)**
  - ***[Time initialization](#time__init__)***
  - ***[Methods](#time_methods)***
- **[Class Date](#class_date)**
  - ***[Date initialization](#date__init__)***
  - ***[Methods](#date_methods)***
--------

## <p id="links">Links</p>

- [Personal GitHub](https://github.com/LassaInora)
- [GitHub project](https://github.com/LassaInora/Timedate)
- [Website project](https://lassainora.fr/projet/librairies/Timedate)

## <p id="contact">Contacts</p>

- [Personal email](mailto:axelleviandier@lassainora.fr)
- [Professional email](mailto:lassainora@lassainora.fr)
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
## <p id="fonc_timedate">Timedate functions and variables:</p>

- DELTA
  - All time zones and their offset with UTC in seconds
- set_language()
  - Change the default language of the library.\
    \[en, ma, hi, sp, be, fr, ru, po] are accepted.
--------
## <p id="class_time">Class Time:</p>

- ### <p id="time__init__">Time initialization.</p>

  - year: The number of year. Default is 0.
  - month: The number of month. Default is 0.
  - day: The number of day. Default is 0.
  - hour: The number of hour. Default is 0.
  - minute: The number of minute. Default is 0.
  - second: The number of second. Default is 0.
  - millisecond: The number of millisecond. Default is 0.
  - microsecond: The number of microsecond. Default is 0.
  - nanosecond: The number of nanosecond. Default is 0.
  - name: The name of the time. Default is None.
  - language: The language for use. Default is LANGUAGE.

- ### <p id="time_methods">Methods:</p>

  - by_date:
    - Static method allowing to convert a Date into Time.
  - by_datetime_date:
    - Static method allowing to convert a datetime.date into Time.
  - by_datetime_time:
    - Static method allowing to convert a datetime.time into Time.
  - by_datetime_datetime:
    - Static method allowing to convert a datetime.datetime into Time.
  - update:
    - Allows to update the attributes.
  - abs(time):
    - Return the absolute value from the current object time.
  - -time:
    - Returns the opposite from the current object time.
  - time + x:
    - Add x nanosecond from the current object time.
  - time + another_time:
    - Add another_time from the current object time.
  - time - x:
    - Remove x nanosecond from the current object time.
  - time - another_time:
    - Remove another_time from the current object time.
  - time == x:
    - Checks equality with x.
  - time != x:
    - Checks inequality with x.
  - str(time):
    - Sends a character string corresponding to the object.
  - print(time):
    - Print a character string corresponding to the object.
  - format(time, "..."):
    - Sends a character string formatted according to the character string. 
    ```
    For an example of Time(year=1985, month=6, day=21, hour=11, minute=1, second=59, millisecond=13, microsecond=541, name='Example')
      format:
        - _name_  -> Example
        - _Y_     -> 1985
        - _M_     -> 6
        - _D_     -> 21
        - _h_     -> 11
        - _m_     -> 1
        - _s_     -> 59
        - _mls_   -> 13
        - _mcs_   -> 541
        - _nns_   -> 800
  - time\[x]:
    - Sends the value of the object according to x.
  - list(time):
    - Returns a list with the values of the object.
  - iter(time):
    - Returns a list with the values of the object.
  - get:
    - Returns the value of the current object in the given unit.
  - get_value:
    - Returns the value of the given unit of the current object.
  - rename:
    - Rename the current object.
  - set_language:
    - Changes the current language of the object.

--------
## <p id="class_date">Class Date:</p>

- ### <p id="date__init__">Date initialization.</p>

  - year: The number of year. Default is None.
  - month: The number of month. Default is None.
  - day: The number of day. Default is None.
  - `/!\ If year, month and day are all None, year will be 400, month and day will be 1 otherwise the None values will be set to 0`
  - hour: The number of hour. Default is 0.
  - minute: The number of minute. Default is 0.
  - second: The number of second. Default is 0.
  - millisecond: The number of millisecond. Default is 0.
  - microsecond: The number of microsecond. Default is 0.
  - nanosecond: The number of nanosecond. Default is 0.
  - name: The name of the date. Default is None.
  - language: The language for use. Default is LANGUAGE.

- ### <p id="date_methods">Methods:</p>

  - by_time:
    - Static method allowing to convert a Time into Date.
  - by_datetime_date:
    - Static method allowing to convert a datetime.date into Date.
  - by_datetime_time:
    - Static method allowing to convert a datetime.time into Date.
  - by_datetime_datetime:
    - Static method allowing to convert a datetime.datetime into Date.
  - now:
    - Static method get the current date.
  - update:
    - Allows to update the attributes.
  - countdown:
    - Returns a Time value of the time remaining until this date.
  - chrono:
    - Returns a Time value of the time elapsed since this date.
  - get_name_month:
    - Give the name of the month.
  - get_name_day:
    - Give the name of the day of the week.
  - abs(time):
    - Return the absolute value from the current object time.
  - -time:
    - Returns the opposite from the current object time.
  - time + x:
    - Add x nanosecond from the current object time.
  - time + another_time:
    - Add another_time from the current object time.
  - time - x:
    - Remove x nanosecond from the current object time.
  - time - another_time:
    - Remove another_time from the current object time.
  - time == x:
    - Checks equality with x.
  - time != x:
    - Checks inequality with x.
  - str(time):
    - Sends a character string corresponding to the object.
  - print(time):
    - Print a character string corresponding to the object.
  - format(time, "..."):
    - Sends a character string formatted according to the character string. 
    ```
    For an example of Date(year=1985, month=6, day=21, hour=11, minute=1, second=59, millisecond=13, microsecond=541, name='Example')
      format:
        - _name_  -> Example
  
        - _YYYY_  -> 1985     [force has 4 characters]
        - _YY_    -> 85       [force has 2 characters]
        - _Y_     -> 1985
  
        - _MM_    -> 06       [force has 2 characters]
        - _NM_    -> June
        - _M_     -> 6
  
        - _DD_    -> 21       [force has 2 characters]
        - _ND_    -> Friday
        - _D_     -> 21
  
        - _hh_    -> 11       [force has 2 characters]
        - _h_     -> 11
  
        - _mm_    -> 01       [force has 2 characters]
        - _m_     -> 1
  
        - _ss_    -> 59       [force has 2 characters]
        - _s_     -> 59
  
        - _mls_   -> 013      [force has 3 characters]
        - _mcs_   -> 541      [force has 3 characters]
        - _nns_   -> 800      [force has 3 characters]
  - time\[x]:
    - Sends the value of the object according to x.
  - list(time):
    - Returns a list with the values of the object.
  - iter(time):
    - Returns a list with the values of the object.
  - get:
    - Returns the value of the current object in the given unit.
  - get_value:
    - Returns the value of the given unit of the current object.
  - rename:
    - Rename the current object.
  - set_language:
    - Changes the current language of the object.