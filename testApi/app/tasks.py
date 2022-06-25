import datetime
from app.models import Data
from celery import shared_task
import gspread
import pandas as pd
import requests

# считываем текущую котировку
def parse_xml():
    url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req='
    dt_now = datetime.datetime.now()
    date = str(dt_now).split('-')[2].split(' ')[0] + '/' + str(dt_now).split('-')[1] + '/' + str(dt_now).split('-')[0]
    r = requests.get(url + date)
    df = pd.read_xml(r.text)
    usd = 0
    for i in df.index:
        if df.CharCode[i] == 'USD':
            usd = df.Value[i]
    return usd


@shared_task
def get_data():
    # подключение к Google Sheets и получение данных
    gc = gspread.service_account(filename='robust-doodad-317409-fc66f62c89c7.json')
    sh = gc.open("test")
    worksheet = sh.get_worksheet(0)
    ss_list = worksheet.get_all_records()
    # если данные уже есть в базе, то обновляем, если нет, то записываем
    for i in range(0, len(ss_list)):
        Data.objects.update_or_create(id=ss_list[i]['№'], order=ss_list[i]['заказ №'], price=ss_list[i]['стоимость, $'], date=ss_list[i]['срок поставки'], price_rub=float(ss_list[i]['стоимость, $']) * float(parse_xml().replace(',', '.')))


