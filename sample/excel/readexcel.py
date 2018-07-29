#!/usr/bin/env python

from xlrd import *

book = open_workbook('test.xls', formatting_info = 1)
sheet = book.sheet_by_index(0)

print("NCOLS: ", sheet.ncols)
print("NROWS: ", sheet.nrows)
# print "FORMATS: ", book.xf_list
# print sheet.cell_xf_index
print

for i in range(sheet.nrows):
    cell = sheet.cell(i, 0)
    xfx = sheet.cell_xf_index(i, 0)
    xf = book.xf_list[xfx]
    if cell.ctype == XL_CELL_EMPTY:
        print("Emtpy")
    elif cell.ctype == XL_CELL_TEXT:
        print("Text: ", cell.value)
    elif cell.ctype == XL_CELL_NUMBER:
        print("Number: ", cell.value)
    elif cell.ctype == XL_CELL_DATE:
        print("Date: ", cell.value)
    elif cell.ctype == XL_CELL_BOOLEAN:
        print("Bool: ", cell.value)
    elif cell.ctype == XL_CELL_ERROR:
        print("Error: ", cell.value)
    elif cell.ctype == XL_CELL_BLANK:
        print("Emtpy: ", cell.value)
    print("       HOR_ALIGN:  ", xf.alignment.hor_align)  # 0 unaligned, 1 left, 2 center, 3 right
    print("       VERT_ALIGN: ", xf.alignment.vert_align) # 0 top, 1 center, 2 bottom
    print("       BG_FIL_IDX: ", xf.background.fill_pattern)
    print("       BG_BGC_IDX: ", xf.background.background_colour_index)
    print("       ", xf.font_index)