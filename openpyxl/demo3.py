# -*- coding:utf-8 -*-
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, Border, Side, colors, Alignment

wb = load_workbook('balances.xlsx')
ws = wb.active

# 字体
ws['A1'].font = Font(name='Times New Roman', size=16, bold=True, italic=True, color=colors.RGB(1))

# 对齐方式
ws['B1'].alignment = Alignment(horizontal='center', vertical='center')

# 边框
left, right, top, bottom = [Side(style='thin', color='0000')] * 4
ws['C1'] = Border(left=left, right=right, top=top, bottom=bottom)

# 设置行高&列宽
ws.row_dimensions[1].height = 25
ws.column_dimensions['D'].width = 15.5

# 拆分合并单元格
ws.merge_cells('A1:B2')
# ws.unmerge_cells('A1:B2')


