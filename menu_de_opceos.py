def switch_dia(dia):
  dias = {
      1: "Domingo",
      2: "Segunda-feira",
      3: "Terça-feira",
      4: "Quarta-feira",
      5: "Quinta-feira",
      6: "Sexta-feira",
      7: "Sábado"
  }
  return dias.get(dia, "Dia inválido")

dia_selecionado = switch_dia(6)
print("O dia é:", dia_selecionado)