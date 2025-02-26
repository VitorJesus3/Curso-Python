tipoEscola = input("Tipo do Colegio: \n [1]Publico \n [2]Particular")
nota01 = input("Qual a nota do 1º Bimestre: ")
nota02 = input("Qual a nota do 2º Bimestre: ")
nota03 = input("Qual a nota do 3º Bimestre: ")
nota04 = input("Qual a nota do 4º Bimestre: ")
freqAluno = int(input("Qual a frequencia: "))
nomeAluno = input("Nome do aluno: ")
mediaAluno = int(int(nota01) + int(nota02) + int(nota03) + int(nota04)) / 4

'''
!= Diferente 
== igual
<= menor ou igual
>= Maior ou igual
> Maior
< Menor
'''

if tipoEscola == "1":
    print("-----Escola Publica-----")
    if mediaAluno >= 7 or freqAluno >= 70 :
        print("O Aluno " + nomeAluno + " foi aprovado com média" + str(mediaAluno))
    
    else:
        print("O Aluno " + nomeAluno + " foi reprovado com média" + str(mediaAluno))
if tipoEscola == "2":
    print("-----Escola Particular-----")
    if mediaAluno >= 7 and freqAluno >= 70 :
        print("O Aluno " + nomeAluno + " foi aprovado com média" + str(mediaAluno))
    else:
        print("O Aluno " + nomeAluno + " foi reprovado com média" + str(mediaAluno))
print("--- Fim do Sistema ---")


#print("O aluno(a) " + nomeAluno + " possui media de :" + str(mediaAluno))