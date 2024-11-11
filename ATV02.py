def saudacao_por_horario(horario):
    if 0 <= horario < 12:
        print("Bom dia!")
    elif 12 <= horario < 18:
        print("Boa tarde!")
    elif 18 <= horario < 24:
        print("Boa noite!")
    else:
        print("Horário inválido!")

saudacao_por_horario(15)  