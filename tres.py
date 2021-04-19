class Aluno:
    # inicializando com nome do aluno e sua matricula
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.nota1 = 0
        self.nota2 = 0
        self.trabalho = 0

    # adicionando notas e trabalhos
    def addNotas(self, nota1, nota2, trabalho):
        self.nota1 = nota1
        self.nota2 = nota2
        self.trabalho = trabalho

    # calculando média
    def media(self):
        res = (((self.nota1*2.5)+(self.nota2*2.5)+(self.trabalho*2))/7)
        print("%.2f"%res)

#exemplo
a = Aluno("daniel", 2018006886)
a.addNotas(10, 9, 7)
a.media()



