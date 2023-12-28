vel_inicial = int(input('Qual a velocidade inicial? '))
vel_final = int(input('Qual a velocidade final? '))
aceleracao = int(input('Qual a aceleração? '))
deslocamento = (vel_final ** 2 - vel_inicial ** 2) / (2 * aceleracao)
print(f'O deslocamento com velocidade inicial de {vel_inicial}, '
      f'velocidade final de {vel_final} e aceleração de {aceleracao} '
      f'é: {deslocamento}')
