# Nome: Felipe de Sanatana    RA:1901648

class Aluno:
    nome = str()
    ra = int()
    nota_ac = []
    nota_prova = float()
    faltas = int()
    media = float()
    aprovado = bool()

    def __init__(self, arquivo):
        self.arquivo = arquivo
        f = open(self.arquivo, 'r')
        a = f.read()
        c = a.split('.')
        lista = []
        f.seek(0)
        for name in f:
            lista.append(name)
        nome = str(lista[0])
        ra = int(lista[1])
        ac1 = float(lista[2])
        ac2 = float(lista[3])
        ac3 = float(lista[4])
        ac4 = float(lista[5])
        ac5 = float(lista[6])
        self.nome = nome
        self.ra = ra
        self.nota_ac.append(ac1)
        self.nota_ac.append(ac2)
        self.nota_ac.append(ac3)
        self.nota_ac.append(ac4)
        self.nota_ac.append(ac5)
        self.nota_prova = float(lista[7])
        porcent_falta = int(lista[8]) * 100 / 60
        self.faltas = int(porcent_falta - 100) * -1
        f.close()

    def calculo_aprovacao(self):
        a = self.nota_acs()
        b = self.nota_prove()
        c = a + b
        d = self.falta()
        if c >= 6 and d <= 15:
            self.media = c
            self.aprovado = True
        else:
            self.media = c
            self.aprovado = False

    def escrever_situacao(self, nome_arquivo):
        f = open(nome_arquivo, 'w')
        f.write(f'{self.ra} : {self.nome}')
        f.write('%.1f'% self.media)
        f.write('\n')
        f.write('%.1f'% self.faltas)
        f.write('%')
        f.write('\n')
        if self.aprovado == True:
            f.write('aprovado')
        else:
            f.write('reprovado')
        f.close()

    def nota_acs(self):
        f = open(self.arquivo, 'r')
        a = f.read()
        c = a.split('.')
        lista = []
        f.seek(16)
        for name in f:
            lista.append(float(name))
        lista_real = lista[1 : 6]
        menor = min(lista_real)
        lista_real.remove(menor)
        final = (sum(lista_real) / 4) * 0.5
        f.close()
        return final

    def nota_prove(self):
        f = open(self.arquivo, 'r')
        a = f.read()
        c = a.split('.')
        lista = []
        f.seek(16)
        for name in f:
            lista.append(float(name))
        lista_real = float(lista [6])
        final = lista_real * 0.5
        f.close()
        return final

    def falta(self):
        f = open(self.arquivo, 'r')
        a = f.read()
        c = a.split('.')
        lista = []
        f.seek(16)
        for name in f:
            lista.append(float(name))
        lista_real = lista[7]
        f.close()
        return lista_real
