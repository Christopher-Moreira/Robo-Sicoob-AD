import holidays


feriados_brasil = holidays.Brazil(years=2025)

for date, name in sorted(feriados_brasil.items()):
    print(date, name)
