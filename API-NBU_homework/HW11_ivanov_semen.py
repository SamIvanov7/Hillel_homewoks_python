import requests

# Задание 1. Подключитесь к API НБУ ( документация тут https://bank.gov.ua/ua/open-data/api-dev ) и получите
# текущий курс валют. Запишите его в TXT-файл в таком формате:
#  "{дата создания запроса}"
# 1. {название ввалюты 1} to UAH: {начение курса к валюте 1}
# 2. {название ввалюты 2} to UAH: {значение курса к валюте 2}
# 3. {название ввалюты 3} to UAH: {значение курса к валюте 3}
# ...
# n. {название ввалюты n} to UAH: {значение курса к валюте n}

date = input('Введите дату в формате YYYYMMDD:')
lst1 = []
lst2 = []


def requestNBU(reqDate):  # даем запрос
    res = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json / '
                       f'?valcode=CAD&date={reqDate}')
    res.raise_for_status()
    print(f'statuscode: {res.status_code}')
    print(f'HEADERS: {res.headers}')
    j_res = res.json()
    return j_res  # возвращаем list с данными о курсах валют на нужную дату


def reqListOperation(reqReslt, myList4Key, myList4Value):  # обрабатываем полученный list
    for i in reqReslt:
        for key, value in i.items():
            if key == 'txt':
                myList4Key.append(value)
            if key == 'rate':
                myList4Value.append(value)
    return dict(zip(myList4Key, myList4Value))  # возвращаем отсортированный dict с нужными нам данными


def writeResultsTXT(curLst, curDct):  # записываем результат в TXT файл в нужном формате
    dateOfReq = curLst[0]['exchangedate']
    text = dateOfReq + '\r\n'  # под стиль windows
    for k, v in curDct.items():
        currencyRate = ("%s to UAH: %s" % (k, v))
        text += currencyRate + '\r\n'
    with open('currencyRate.txt', 'a+', encoding='utf-8') as f:
        f.write(text)


myList = requestNBU(date)
reqDictReslt = reqListOperation(myList, lst1, lst2)
writeResultsTXT(myList, reqDictReslt)


# 2. * Реализовать с помощью ООП! Пользователь вводит название валюты и дату, программа
# записывает в файл, а затем показывает пользователю курс гривны к этой валюте за указаную дату
# используя API НБУ. Формат ввода пользователем данных - на ваше усмотрение.


class ExchangeNBU:
    requestDate = ''
    currencyName = ''
    link = ''

    def __init__(self, name, date):
        if not isinstance(name, str) and not isinstance(date, str):
            raise Exception
        self.link = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json / ' \
                    f'?valcode=CAD&date={date}'
        self.currencyName, self.requestDate = name, date

    def checkStatus(self):
        res = requests.get(self.link)
        res.raise_for_status()
        print(f'statuscode: {res.status_code}')
        print(f'HEADERS: {res.headers}')

    def requestSend(self):
        res = requests.get(self.link)
        j_res = res.json()
        return j_res

    def listProcessing(self, lst):
        myList4Key = []
        myList4Value = []
        for i in lst:
            for key, value in i.items():
                if key == 'txt':
                    myList4Key.append(value)
                if key == 'rate':
                    myList4Value.append(value)
        return dict(zip(myList4Key, myList4Value))

    def writeRes(self, curLst, curDct):
        date = curLst[0]['exchangedate']
        text = date + '\r\n'
        for k, v in curDct.items():
            currencyRate = ("%s to UAH: %s" % (k, v))
            text += currencyRate + '\r\n'
        with open('currencyRate.txt', 'a+', encoding='utf-8') as f:
            f.write(text)

    def __str__(self):
        dateOfRequest = self.requestSend()[0]['exchangedate']
        myDict = self.listProcessing(self.requestSend())
        for name in myDict:
            if name == self.currencyName:
                myDict.get(self.currencyName)
        return f'{dateOfRequest} Курс {self.currencyName} к UAH: {myDict.get(self.currencyName)}'


cur1 = ExchangeNBU('Канадський долар', '20201016')
cur1.checkStatus()
cur1.writeRes(cur1.requestSend(), cur1.listProcessing(cur1.requestSend()))
print(cur1)

cur2 = ExchangeNBU('Чеська крона', '20210101')
cur2.checkStatus()
cur2.writeRes(cur2.requestSend(), cur2.listProcessing(cur2.requestSend()))
print(cur2)
