#1
import math
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.raio
circulo = Circulo(79)
print(f"Círculo: Raio = {circulo.raio}, Área = {circulo.area():.2f}, Perímetro = {circulo.perimetro():.2f}")


# 2
class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")
conta = ContaBancaria(1234, "Dorival", 500)
conta.deposito(200)
conta.saque(100)
print(f"Conta Bancária: Titular = {conta.titular}, Saldo = {conta.saldo}")


# 3
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)
retangulo = Retangulo(4, 6)
print(f"Retângulo: Largura = {retangulo.largura}, Altura = {retangulo.altura}, Área = {retangulo.area()}, Perímetro = {retangulo.perimetro()}")
# 4
class Aluno:
    def __init__(self, nome, matricula, notas):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas

    def media(self):
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        if self.media() >= 7:
            return "Aprovado"
        else:
            return "Reprovado"
aluno = Aluno("Maria", 98765, [8, 7, 9])
print(f"Aluno: {aluno.nome}, Matrícula = {aluno.matricula}, Média = {aluno.media():.2f}, Situação = {aluno.situacao()}")


#Exercicio 5
class Funcionario():
    def __init__(self, nome, salario,cargo):
        self.nome=nome
        self.salario=salario
        self.cargo=cargo

    def calcular_salario_liquido(self,impostos=0.1,beneficios=0.05):
        desconto_impostos=self.salario*impostos
        desconto_beneficios=self.salario*beneficios
        salario_liquido=self.salario-desconto_impostos-desconto_beneficios
        return salario_liquido

    def exibir_dados(self):
        print(f"\nSeu nome é {self.nome}")
        print(f"\nSeu cargo é {self.cargo}")
        print(f"\nSeu salario é {self.salario}")
        print(f"\nSeu salario liquido é {self.calcular_salario_liquido():.2f}")

funcionario1=Funcionario("Luca",200.,"Dono da bosch")
funcionario1.exibir_dados()


#Exercicio 6
class Produto():
    def __init__(self,nome,preco,quantidade_estoque):
        self.nome=nome
        self.preco=preco
        self.quantidade_estoque=quantidade_estoque

    def calcular_valor_total_estoque(self):
        return self.preco*self.quantidade_estoque

    def verificar_disponibilidade(self):
        return self.quantidade_estoque>0
    def exibir_dados(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Quantidade em estoque: {self.quantidade_estoque}")
        print(f"Valor total em estoque: R${self.calcular_valor_total_estoque():.2f}")
        disponibilidade = "Disponível" \
            if self.verificar_disponibilidade() \
            else "Indisponível"
        print(f"Disponibilidade: {disponibilidade}")

produto1 = Produto("Cadeira de escritório", 350.00, 10)
produto1.exibir_dados()
produto2 = Produto("Teclado Mecânico", 300.00, 0)
produto2.exibir_dados()


#Exercicio 7
import math

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def verificar_triangulo(self):
        return (self.lado1 + self.lado2 > self.lado3 and
                self.lado1 + self.lado3 > self.lado2 and
                self.lado2 + self.lado3 > self.lado1)

    def calcular_area(self):
        if self.verificar_triangulo():
            semiperimetro = (self.lado1 + self.lado2 + self.lado3) / 2  # semiperímetro
            area = math.sqrt(semiperimetro * (semiperimetro - self.lado1) *
                             (semiperimetro - self.lado2) * (semiperimetro - self.lado3))
            return area
        else:
            return None 

    def exibir_dados(self):

        print(f"Lados do triângulo: {self.lado1}, {self.lado2}, {self.lado3}")
        if self.verificar_triangulo():
            area = self.calcular_area()
            print("É um triângulo válido.")
            print(f"Área do triângulo: {area:.2f} unidades quadradas")
        else:
            print("Não é um triângulo válido.")

triangulo1 = Triangulo(3, 4, 5)
triangulo1.exibir_dados()
triangulo2 = Triangulo(1, 2, 10)
triangulo2.exibir_dados()



#exercicio 8
class Carro:
    def __init__(self, marca, modelo, velocidade_atual=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_atual = velocidade_atual

    def acelerar(self, incremento):
        self.velocidade_atual += incremento
        print(f"O carro acelerou! Sua velocidade: {self.velocidade_atual} km/h")

    def frear(self, decremento):
        if self.velocidade_atual - decremento < 0:
            self.velocidade_atual = 0
        else:
            self.velocidade_atual -= decremento
        print(f"O carro freou! Nova velocidade: {self.velocidade_atual} km/h")

    def exibir_velocidade(self):
        print(f"A velocidade atual do carro é: {self.velocidade_atual} km/h")


carro1 = Carro("Fusca", "1976")
print(carro1.marca,carro1.modelo)
carro1.exibir_velocidade()

carro1.acelerar(50)
carro1.frear(20)
carro1.acelerar(30)
carro1.frear(70)
carro1.exibir_velocidade()


#exercicio 9
class Paciente:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
        self.historico=None
    def nova_consulta(self,especialidade,data,medico):
        self.especialidade=especialidade
        self.data=data
        self.medico=medico
        historico_consulta={"especialidade":self.especialidade, "data":self.data,"medico":self.medico}
        historico=historico_consulta

    def mostrar_dados(self):
        return self.historico
paciente1 = Paciente("Maria", 30)
paciente1.nova_consulta("Cardiologia", "2025-01-15", "Dr. João")
paciente1.nova_consulta("Dermatologia", "2025-01-20", "Dra. Ana")
print(paciente1.mostrar_dados())

#10
class Livro:
    def __init__(self, nome, autor, paginas):
        self.nome = nome
        self.autor = autor
        self.paginas = paginas
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.nome}' foi emprestado com sucesso.")
        else:
            print(f"O livro '{self.nome}' não está disponível para empréstimo.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro '{self.nome}' foi devolvido com sucesso.")
        else:
            print(f"O livro '{self.nome}' já estava disponível.")

    def verificar_disponibilidade(self):
        return "disponível" if self.disponivel else "indisponível"

    def mostrar_dados(self):
        return f"Nome: {self.nome}, Autor: {self.autor}, Páginas: {self.paginas}, Disponibilidade: {self.verificar_disponibilidade()}"

livro1 = Livro("1984", "George Orwell", 328)
print(livro1.mostrar_dados())
livro1.emprestar()
print(livro1.mostrar_dados())
livro1.devolver()
print(livro1.mostrar_dados())

#11
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class ContaBancaria:
    def __init__(self, cliente, numero_conta, saldo_inicial=0):
        self.cliente = cliente
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor

    def transferir(self, conta_destino, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            conta_destino.saldo += valor

    def exibir_saldo(self):
        print(f"Saldo da conta {self.numero_conta}: R${self.saldo}")

class Banco:
    def __init__(self):
        self.clientes = {}
        self.contas = {}

    def cadastrar_cliente(self, nome, cpf):
        if cpf not in self.clientes:
            self.clientes[cpf] = Cliente(nome, cpf)

    def abrir_conta(self, cpf, numero_conta, saldo_inicial=0):
        if cpf in self.clientes:
            cliente = self.clientes[cpf]
            self.contas[numero_conta] = ContaBancaria(cliente, numero_conta, saldo_inicial)

    def buscar_conta(self, numero_conta):
        return self.contas.get(numero_conta)

    def buscar_cliente(self, cpf):
        return self.clientes.get(cpf)
banco = Banco()
banco.cadastrar_cliente("Yasmin Silva", "12345678900")
banco.abrir_conta("12345678900", "0001", 1000)
conta_yasmin = banco.buscar_conta("0001")
conta_yasmin.exibir_saldo()
conta_yasmin.depositar(500)
conta_yasmin.sacar(200)
conta_yasmin.exibir_saldo()

#12
class LojaVirtual:
    def __init__(self):
        self.produtos = {}
        self.carrinho = {}

    def cadastrar_produto(self, nome, preco):

        self.produtos[nome] = preco
        print(f"Produto '{nome}' cadastrado com sucesso!")

    def adicionar_ao_carrinho(self, nome, quantidade):

        if nome in self.produtos:
            if nome in self.carrinho:
                self.carrinho[nome] += quantidade
            else:
                self.carrinho[nome] = quantidade
            print(f"Adicionado {quantidade} unidade(s) de '{nome}' ao carrinho.")
        else:
            print(f"O produto '{nome}' não está disponível.")

    def aplicar_desconto(self, porcentagem):

        desconto = self.calcular_total() * (porcentagem / 100)
        total_com_desconto = self.calcular_total() - desconto
        print(f"Desconto de {porcentagem}% aplicado. Total com desconto: R${total_com_desconto:.2f}")
        return total_com_desconto

    def calcular_total(self):

        total = sum(self.produtos[nome] * quantidade for nome, quantidade in self.carrinho.items())
        return total

    def exibir_carrinho(self):

        print("\nCarrinho de compras:")
        for nome, quantidade in self.carrinho.items():
            print(f"{nome} - {quantidade} unidade(s) - R${self.produtos[nome] * quantidade:.2f}")
        print(f"Total: R${self.calcular_total():.2f}\n")


loja = LojaVirtual()
loja.cadastrar_produto("Camiseta", 50.00)
loja.cadastrar_produto("Calça", 100.00)
loja.cadastrar_produto("Tênis", 200.00)
loja.adicionar_ao_carrinho("Camiseta", 2)
loja.adicionar_ao_carrinho("Calça", 1)
loja.exibir_carrinho()
loja.aplicar_desconto(10)

#13
class Agenda:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        self.contatos[nome] = telefone

    def editar_contato(self, nome, novo_telefone):
        if nome in self.contatos:
            self.contatos[nome] = novo_telefone
        else:
            print("Contato não encontrado!")

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
        else:
            print("Contato não encontrado!")

    def buscar_contato(self, nome=None, telefone=None):
        if nome:
            return self.contatos.get(nome, "Contato não encontrado!")
        elif telefone:
            for nome, tel in self.contatos.items():
                if tel == telefone:
                    return nome
            return "Contato não encontrado!"
        else:
            return self.contatos


agenda = Agenda()
agenda.adicionar_contato("Luca", "123456789")
agenda.adicionar_contato("Yasmin", "987654321")
agenda.editar_contato("Luca", "111222333")
agenda.remover_contato("Yasmin")
print(agenda.buscar_contato(nome="Luca"))
print(agenda.buscar_contato(telefone="111222333"))


#14
class MaquinaDeVendas:
    def __init__(self):
        self.produtos = {}
        self.estoque = {}

    def cadastrar_produto(self, nome, preco, estoque):
        self.produtos[nome] = preco
        self.estoque[nome] = estoque

    def selecionar_produto(self, nome_produto):
        if nome_produto in self.produtos and self.estoque[nome_produto] > 0:
            return nome_produto, self.produtos[nome_produto]
        else:
            return None, "Produto não disponível ou fora de estoque."

    def inserir_dinheiro(self, valor_produto, valor_inserido):
        if valor_inserido >= valor_produto:
            return valor_inserido - valor_produto
        else:
            return "Valor insuficiente."

    def exibir_estoque(self):
        for produto, estoque in self.estoque.items():
            print(f"{produto}: {estoque} unidades")


maquina = MaquinaDeVendas()
maquina.cadastrar_produto("Refrigerante", 5.0, 10)
maquina.cadastrar_produto("Chocolate", 3.0, 5)
produto, preco = maquina.selecionar_produto("Refrigerante")
print(f"Produto selecionado: {produto}, Preço: R${preco}")
troco = maquina.inserir_dinheiro(preco, 10)
print(f"Troco: R${troco}")
maquina.exibir_estoque()

#15
import random

class JogoCartas:
    def __init__(self):
        self.cartas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
        self.jogadores = {}
        self.jogo_ativo = False

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir_cartas(self, jogador, numero_cartas):
        if jogador not in self.jogadores:
            self.jogadores[jogador] = []
        for _ in range(numero_cartas):
            if self.cartas:
                self.jogadores[jogador].append(self.cartas.pop())

    def jogar(self, jogador, carta):
        if carta in self.jogadores[jogador]:
            self.jogadores[jogador].remove(carta)
            print(f"{jogador} jogou a carta {carta}")
        else:
            print(f"{jogador} não tem a carta {carta}")
jogo = JogoCartas()
jogo.embaralhar()
jogo.distribuir_cartas("Luca", 5)
jogo.jogar("Luca", "3")


#16
class RedeSocial:
    def __init__(self):
        self.usuarios = {}
        self.posts = {}

    def adicionar_amigo(self, usuario, amigo):
        if usuario not in self.usuarios:
            self.usuarios[usuario] = []
        self.usuarios[usuario].append(amigo)

    def publicar_mensagem(self, usuario, mensagem):
        if usuario not in self.posts:
            self.posts[usuario] = []
        self.posts[usuario].append(mensagem)

    def comentar_em_post(self, usuario, comentario):
        print(f"{usuario} comentou: {comentario}")

    def buscar_usuario(self, nome):
        return nome in self.usuarios
rede_social = RedeSocial()
rede_social.adicionar_amigo("Luca", "Yasmim")
rede_social.publicar_mensagem("Luca", "Olá, estou aprendendo Python!")
rede_social.comentar_em_post("Yasmim", "Muito bom!")
print(rede_social.buscar_usuario("Luca"))

#17
class Biblioteca:
    def __init__(self):
        self.livros = {}

    def cadastrar_livro(self, nome, autor, disponivel=True):
        self.livros[nome] = {'autor': autor, 'disponivel': disponivel}

    def emprestar_livro(self, nome):
        if nome in self.livros and self.livros[nome]['disponivel']:
            self.livros[nome]['disponivel'] = False
            print(f"{nome} foi emprestado!")
        else:
            print(f"{nome} não está disponível.")

    def devolver_livro(self, nome):
        if nome in self.livros:
            self.livros[nome]['disponivel'] = True
            print(f"{nome} foi devolvido!")

    def verificar_disponibilidade(self, nome):
        if nome in self.livros:
            return "Disponível" if self.livros[nome]['disponivel'] else "Indisponível"
        return "Livro não encontrado"
biblioteca = Biblioteca()
biblioteca.cadastrar_livro("Python para Iniciantes", "Dorival")
biblioteca.emprestar_livro("Python para Iniciantes")
print(biblioteca.verificar_disponibilidade("Python para Iniciantes"))


#18
from datetime import datetime

class Calendario:
    def __init__(self):
        self.feriados = ["01-01", "25-12"]

    def exibir_calendario(self, mes, ano):
        print(f"Calendário do mês {mes}/{ano}")

    def verificar_feriado(self, data):
        data_formatada = data.strftime("%d-%m")
        if data_formatada in self.feriados:
            return "Feriado!"
        return "Não é feriado."

    def calcular_diferenca_dias(self, data1, data2):
        delta = data2 - data1
        return delta.days
calendario = Calendario()
print(calendario.verificar_feriado(datetime(2025, 12, 25)))
print(calendario.calcular_diferenca_dias(datetime(2025, 1, 1), datetime(2025, 12, 25)))


#19
class JogoAdivinhacao:
    def _init_(self):
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0

    def jogar(self, palpite):
        self.tentativas += 1
        if palpite == self.numero_secreto:
            return f"Parabéns! Você acertou em {self.tentativas} tentativa(s)."
        elif palpite < self.numero_secreto:
            return "O número é maior."
        else:
            return "O número é menor."

jogo = JogoAdivinhacao()
print(jogo.jogar(50))

#20
class Peca:
    def _init_(self, tipo, cor):
        self.tipo = tipo
        self.cor = cor

    def movimento(self):
        if self.tipo == "peao":
            return "Move-se para frente 1 casa."
        elif self.tipo == "torre":
            return "Move-se em linha reta."
        elif self.tipo == "bispo":
            return "Move-se na diagonal."
        elif self.tipo == "rainha":
            return "Move-se em qualquer direção."
        elif self.tipo == "rei":
            return "Move-se uma casa em qualquer direção."
        elif self.tipo == "cavalo":
            return "Move-se em L."
        else:
            return "Peça desconhecida."
peao = Peca("peao", "branco")
print(peao.movimento())

#21
class Produto:
    def _init_(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Cliente:
    def _init_(self, nome):
        self.nome = nome
        self.historico_compras = []

    def comprar(self, produto):
        self.historico_compras.append(produto)

class Pedido:
    def _init_(self, cliente, produto):
        self.cliente = cliente
        self.produto = produto
        self.status = "Pendente"
cliente = Cliente("Maria")
produto = Produto("Celular", 1200)
cliente.comprar(produto)
print(f"{cliente.nome} comprou {produto.nome} por R${produto.preco}.")

#22
class Produto:
    def _init_(self, nome, categoria, preco, quantidade):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidade = quantidade

    def atualizar_estoque(self, qtd):
        self.quantidade += qtd
produto = Produto("Arroz", "Alimentos", 20, 100)
produto.atualizar_estoque(-10)  # Vendendo 10 unidades
print(f"Estoque de {produto.nome}: {produto.quantidade} unidades.")

#23
class Tarefa:
    def _init_(self, titulo, prioridade):
        self.titulo = titulo
        self.prioridade = prioridade
        self.status = "Pendente"

    def concluir(self):
        self.status = "Concluída"

tarefa = Tarefa("Estudar Python", "Alta")
tarefa.concluir()
print(f"Tarefa: {tarefa.titulo}, Status: {tarefa.status}.")


#24
class Animal:
    def _init_(self, nome, especie, dieta):
        self.nome = nome
        self.especie = especie
        self.dieta = dieta

class Funcionario:
    def _init_(self, nome, funcao):
        self.nome = nome
        self.funcao = funcao
animal = Animal("Leão", "Felino", "Carnívoro")
funcionario = Funcionario("João", "Veterinário")
print(f"O {funcionario.funcao} {funcionario.nome} cuida do {animal.especie} chamado {animal.nome}.")

#25
class Personagem:
    def _init_(self, nome, saude, forca):
        self.nome = nome
        self.saude = saude
        self.forca = forca

    def atacar(self, outro):
        outro.saude -= self.forca
        return f"{self.nome} atacou {outro.nome}. Saúde de {outro.nome}: {outro.saude}."

heroi = Personagem("Herói", 100, 20)
vilao = Personagem("Vilão", 80, 15)
print(heroi.atacar(vilao))

#DESAFIO
class Evento:
    def __init__(self, nome, data, hora, local, descricao):
        self.nome = nome
        self.data = data
        self.hora = hora
        self.local = local
        self.descricao = descricao
        self.tarefas = []
        self.fornecedores = []
        self.pagamentos = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def adicionar_fornecedor(self, fornecedor):
        self.fornecedores.append(fornecedor)

    def adicionar_pagamento(self, pagamento):
        self.pagamentos.append(pagamento)

class Tarefa:
    def __init__(self, descricao, responsavel, prazo, status="Pendente"):
        self.descricao = descricao
        self.responsavel = responsavel
        self.prazo = prazo
        self.status = status

    def atualizar_status(self, novo_status):
        self.status = novo_status

class Fornecedor:
    def __init__(self, nome, servico, contato):
        self.nome = nome
        self.servico = servico
        self.contato = contato
class Pagamento:
    def __init__(self, valor, data_vencimento, status="Pendente"):
        self.valor = valor
        self.data_vencimento = data_vencimento
        self.status = status

    def atualizar_status(self, novo_status):
        self.status = novo_status

evento = Evento(
    nome="Casamento",
    data="2025-02-15",
    hora="18:00",
    local="Espaço de Eventos Jardim",
    descricao="Cerimônia de casamento com recepção para 200 convidados."
)

tarefa1 = Tarefa("Reservar espaço", "Ana", "2025-01-30")
tarefa2 = Tarefa("Contratar catering", "João", "2025-01-25")
evento.adicionar_tarefa(tarefa1)
evento.adicionar_tarefa(tarefa2)

fornecedor1 = Fornecedor("Buffet Gourmet", "Catering", "contato@buffetgourmet.com")
fornecedor2 = Fornecedor("Floricultura Bela", "Decoração", "floricultura@bela.com")
evento.adicionar_fornecedor(fornecedor1)
evento.adicionar_fornecedor(fornecedor2)

pagamento1 = Pagamento(5000, "2025-01-20")
pagamento2 = Pagamento(2000, "2025-01-25")
evento.adicionar_pagamento(pagamento1)
evento.adicionar_pagamento(pagamento2)

print(f"Evento: {evento.nome}")
print(f"Data: {evento.data} Hora: {evento.hora}")
print(f"Local: {evento.local}")
print(f"Descrição: {evento.descricao}\n")

print("Tarefas:")
for tarefa in evento.tarefas:
    print(f"- {tarefa.descricao}, Responsável: {tarefa.responsavel}, Prazo: {tarefa.prazo}, Status: {tarefa.status}")

print("\nFornecedores:")
for fornecedor in evento.fornecedores:
    print(f"- {fornecedor.nome}, Serviço: {fornecedor.servico}, Contato: {fornecedor.contato}")

print("\nPagamentos:")
for pagamento in evento.pagamentos:
    print(f"- Valor: R${pagamento.valor}, Vencimento: {pagamento.data_vencimento}, Status: {pagamento.status}")
