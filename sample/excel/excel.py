#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd

# Excel ファイル（ブック）を読み込み
book = xlrd.open_workbook('data.xlsx')

print("----- SETUP01 -----")
# ブック内のシート数を取得
num_of_worksheets = book.nsheets
print(num_of_worksheets)  #=> 3

print("----- SETUP02 -----")
# 全シートの名前を取得
sheet_names = book.sheet_names()
print(sheet_names)  #=> ['Sheet1', 'Sheet2', 'Sheet3']

print("----- SETUP03 -----")
book = xlrd.open_workbook('data.xlsx')
for i in range(book.nsheets):
    sheet = book.sheet_by_index(i)
    print('{} has {} rows and {} cols'.format(sheet.name, sheet.nrows, sheet.ncols))


book = xlrd.open_workbook('data.xlsx')
sheet = book.sheet_by_index(0)

print("----- SETUP04 -----")
for row_index in range(sheet.nrows):
    for col_index in range(sheet.ncols):
        val = sheet.cell_value(rowx=row_index, colx=col_index)
        print('cell[{},{}] = {}'.format(row_index, col_index, val))

print("----- SETUP05 -----")
for row_index in range(sheet.nrows):
    row = sheet.row(row_index)  # 一行分の xlrd.sheet.Cell のリスト
    print(row)

print("----- SETUP06 -----")
for row_index in range(sheet.nrows):
    row = sheet.row(row_index)  # 一行分の xlrd.sheet.Cell のリスト
    for cell in row:
        print(cell.value)

print("----- SETUP07 -----")
for row_index in range(sheet.nrows):
    row = sheet.row_values(row_index)  # 一行分の「値」のリスト
    print(row[0], row[1], row[2], row[3])



