# -*- coding:utf-8 -*-
from openpyxl import Workbook
from datetime import datetime


def write_excel(filename):
    wb = Workbook()  # load_work(filename)
    ws = wb.create_sheet('sheet', 0)
    wb.remove('sheet')

    ws = wb.active  # default Sheet
    ws.title = 'Pi'
    ws['A1'] = 3.1415926
    ws['A2'] = datetime.now().strftime('%Y-%m-%d')
    ws['A3'] = '=sum(A1:A5)'

    row = [1, 2, 3, 4]
    ws.append(row)

    rows = [
        ['id', 'name', 'department'],
        ['001', 'lee', 'cs'],
        ['002', 'lee', 'ma']
    ]
    ws.append(rows)

    wb.save(filename)
