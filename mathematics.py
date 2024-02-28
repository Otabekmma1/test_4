def day_min_sek(sekund):
    day = sekund / 86400
    hour = (sekund % 86400) / 3600
    minute = (sekund % 86400 % 3600) / 60
    sekunt = sekund % 60
    return f"{sekund} = {int(day)} kun,{int(hour)} soat,{int(minute)} minut,{sekunt} sekund"