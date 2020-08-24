from openpyxl import load_workbook as lw

doc = lw("episodios.xlsx")
folhas = doc.get_sheet_names()
ep_folha = doc.get_sheet_by_name(folhas[0])

linhas = sum([[cedula for cedula in linha] for linha in ep_folha], [])
print(list(map(lambda x: x.value, linhas)))
