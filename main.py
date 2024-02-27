print("Ola seja bem-vindo!!")

jogar = input("Você gostaria de Jogar?  -")
if jogar.lower() != "sim":
    quit()

print("Ok,vamos começar...")
score = 0

Resposta = input("qual o ano que foi lançado o primeiro half-life  -")
if Resposta.lower() == "1998":
    print("Correto!!!")
    print("Proxima pergunta...")
    score += 1

else:
    print("Resposta errada :( ")

Resposta = input("em qual ano foi criado a steam?  -")
if Resposta.lower() == "2003":
    print("Correto!!!")
    print("Proxima pergunta...")
    score += 1
else:
    print("Resposta errada :( ")


Resposta = input("qual o nome do dono da valve?  -")
if Resposta.lower() == "gabe newell":
    print("Correto!!!")
    print("Proxima pergunta...")
    score += 1
else:
    print("Resposta errada :( ")

Resposta = input("counter-strike é um mod de qual jogo  -")
if Resposta.lower() == "half-life":
    print("Correto!!!")
    print("Proxima pergunta...")
    score += 1
else:
    print("Resposta errada :( ")

Resposta = input("qual o nome da tag brasileira lendaria de cs?  -")
if Resposta.lower() == "mibr":
    print("Correto!!!")
    print("Parabens, você acertou todas as questões!!!!")
    score += 1
else:
    print("Resposta errada :( ")


if score>=5:
    print("Fim do jogo... ")
    print("Parabens, você atingiu a maior pontuação, que é de "+str(score)+" Pontos")
elif score >=4:
    print("Parabens, voce quase atingiu a pontuação maxima, que foi "+str(score)+" Pontos")
elif score <=3:
    print("Você conseguiu "+str(score)+" Pontos")
else:
    print("Você obiteve "+ str(score)+ " Pontos")
