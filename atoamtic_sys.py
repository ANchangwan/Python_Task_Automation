from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.title = "anchangwan"
wb.save("practice.xlsx")
wb.close()