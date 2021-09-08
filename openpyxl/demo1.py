# -*- coding:utf-8 -*-
from openpyxl import load_workbook


def read_excel(filename):
    wb = load_workbook(filename)
    all_ws = wb.get_sheet_names()  # ['sheet1', sheet2']

    ws = wb['sheet1']  # 获取表
    print(ws.title)  # 工作表名

    a = ws['A1']
    print(a.value)  # 单元格值
    print(a.column, a.row)

    for row in ws.iter_rows(min_row=1, max_col=3, max_row=4, values_only=True):
        print(row)  # (1,2,3)
        for cell in row:
            print(cell)  # 1

    for col in ws.iter_cols(min_row=1, max_row=44, min_col=3, max_col=44):
        for cell in col:
            print(cell.value)

    # 特定行, ws.rows is generate
    for cell in list(ws.rows)[2]:
        print(cell.value)

    # 遍历某一单元格范围
    for space in ws['A1': 'C3']:
        for cell in space:
            print(cell.value)

    print(ws.max_row)
    print(ws.max_column)
