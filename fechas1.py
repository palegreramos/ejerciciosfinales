from datetime import date
import locale
locale.setlocale(locale.LC_ALL, ("es_ES", "UTF-8"))

print(date.today())
print(f"Hoy es {date.today().day} del {date.today().month} de {date.today().year}")

print(f'{date.today():%d - %B - %Y}')

locale.setlocale(locale.LC_ALL, ("en_EN", "UTF-8"))

print(f'{date.today():%d - %B - %Y}')