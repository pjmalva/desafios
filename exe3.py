schedule = """Mon 01:00-23:00
Tue 01:00-23:00
Wed 01:00-23:00
Thu 01:00-23:00
Fri 01:00-23:00
Sat 01:00-23:00
Sun 01:00-21:00"""

from datetime import datetime, timedelta

data_formater = "%a %H:%M"

inicio = datetime.strptime("Mon 00:00", data_formater)
fim = datetime.strptime("Sun 00:00", data_formater)

def ler_agenda(agenda):
    c = []
    for linha in agenda.split('\n'):
        c.append(ler_compromisso(linha))
    return c

def ler_compromisso(linha):
    return {"i": datetime.strptime("{} {}:{}".format(linha[:3], linha[4:6], linha[7:9]), data_formater), 
            "f": datetime.strptime("{} {}:{}".format(linha[:3], linha[10:12], linha[13:]), data_formater)}

def intervalo_compromisso(base, compara):
    inicio = base["f"]
    fim = compara["i"]
    print(inicio, fim)
    intervalo = inicio - fim
    print(intervalo)
    return (inicio - fim).seconds//60

def solution(S):
    x = ler_agenda(S)
    intervalos = []

    for i, comp in enumerate(x):
        if i + 1 == len(x):
            intervalos.append(intervalo_compromisso(comp, {"i": fim})+1)
        else:
            intervalos.append(intervalo_compromisso(comp, x[i + 1]))

    return intervalos

print(solution(schedule))