
import datetime
from time import strftime

class Cliente:
    CPF = ""
    Nome = ""
    Data_De_Nascimento = ""
    Sexo = ""
    Salario = 0
    Emails = []
    Telefones = []

def ListarTodosCliente(Lista1):
    if len(Lista1) > 0:
        for Objeto in Lista1:
            print(" ")
            print(f"CPF: {Objeto.CPF}")
            print(f"Nome: {Objeto.Nome}")
            print(f"Data de nascimento: {Objeto.Data_De_Nascimento.strftime('%d/%m/%Y')}")
            print(f"Sexo: {Objeto.Sexo}")
            print(f"Salário: R${Objeto.Salario:.2f}")
            if len(Objeto.Emails) > 0:
                i = 0
                for emails in Objeto.Emails:
                    if i == 0:
                        print(f"E-mail: {emails} ", end=" ")
                        i += 1
                    else:
                        print(f"| {emails}", end=" ")
                print()
            else:
                print("Nenhum e-mail cadastrado!")
            if len(Objeto.Telefones) > 0:
                i = 0
                for telefones in Objeto.Telefones:
                    if i == 0:
                        print(f"Telefone: {telefones} ", end=" ")
                        i += 1
                    else:
                        print(f"| {telefones}",end=" ")
            else:
                print("Nenhum telefone cadastrado!")
    else:
        print("Nenhum cliente cadastrado!")

def ListarUmCliente(Lista1, CPF_Unico1):
    print(" ")
    CPF = str(input("Digite o CPF do cliente que você deseja visualizar: "))
    if CPF in CPF_Unico1:
        for Objeto in Lista1:
            if CPF == Objeto.CPF:
                print(f"CPF: {Objeto.CPF}")
                print(f"Nome: {Objeto.Nome}")
                print(f"Data de nascimento: {Objeto.Data_De_Nascimento.strftime('%d/%m/%Y')}")
                print(f"Sexo: {Objeto.Sexo}")
                print(f"Salário: R${Objeto.Salario:.2f}")
                if len(Objeto.Emails) > 0:
                    i = 0
                    for emails in Objeto.Emails:
                        if i == 0:
                            print(f"E-mail: {emails} ", end=" ")
                            i += 1
                        else:
                            print(f"| {emails}", end=" ")
                else:
                    print("Nenhum e-mail cadastrado!")
                print()
                if len(Objeto.Telefones) > 0:
                    i = 0
                    for telefones in Objeto.Telefones:
                        if i == 0:
                            print(f"Telefone: {telefones} ", end=" ")
                            i += 1
                        else:
                            print(f"| {telefones}",end=" ")
                else:
                    print("Nenhum telefone cadastrado!")
    else:
        print("Cliente não cadastrado!")

def IncluirCliente(Lista1, CPF_Unico1):
    print(" ")
    Classe = Cliente()
    # CPFGuardar = True
    # while CPFGuardar != True:
    # Classe.CPF = str(input("Informe o CPF (apenas números) [11]: "))
    # for Objeto in Lista1:
    #     if Objeto.CPF == Classe.CPF:
    #         CPFGuardar = False
    #     else:
    #         CPFGuardar = True
    # if CPFGuardar == False:
    #    print("CPF repetido!")
    while len(Classe.CPF) != 11:
        Classe.CPF = str(input("Informe o CPF (apenas números) [11]: "))
        if len(Classe.CPF) != 11:
            print("CPF inválido!")
    if Classe.CPF in CPF_Unico1:
        print("Cliente já cadastrado!")
    else:
        CPF_Unico1.add(Classe.CPF)
        Classe.Nome = str(input("Informe o Nome: "))
        Data_Guardar = ""
        while len(Data_Guardar) != 10:
            Data_Guardar = str(input("Informe a Data de Nascimento (dd/mm/aaaa): "))
            if len(Data_Guardar) != 10:
                print("Data de Nascimento inválida!")
        Data_Guardar_Split = list(map(int,Data_Guardar.split("/")))
        Classe.Data_De_Nascimento = datetime.datetime(Data_Guardar_Split[2],Data_Guardar_Split[1], Data_Guardar_Split[0])
        while Classe.Sexo != "M" and Classe.Sexo != "F":
            Classe.Sexo = str(input("Informe o Sexo (M ou F): "))
            if Classe.Sexo != "M" and Classe.Sexo != "F":
                print("Sexo inválido!")
        Classe.Salario = float(input("Informe o Salário (R$): "))
        Classe.Emails = []
        EmailInput = int(input("Informe a quantidade de E-mails do Cliente: "))
        i = 1
        while i <= EmailInput:
            Classe.Emails.append(str(input("Informe o E-mail: ")))
            i += 1
        Classe.Telefones = []
        TelefoneInput = int(input("Informe a quantidade de Telefones do Cliente: "))
        i = 1
        while i <= TelefoneInput:
            Classe.Telefones.append(str(input("Informe o Telefone (DD) 91234-5678: ")))
            i += 1
        Lista1.append(Classe)
        print("Cliente inserido com sucesso!")

def AlterarCliente(Lista1, CPF_Unico1):
    print(" ")
    CPF = str(input("Digite o CPF do cliente que você deseja alterar: "))
    if CPF in CPF_Unico1:
        for Objeto in Lista1:
            if CPF == Objeto.CPF:
                print(f"CPF: {Objeto.CPF}")
                Alterar = ""
                while Alterar != "S" and Alterar != "N":
                    Alterar = str(input("Deseja alterar o CPF?(S ou N): "))
                    if Alterar != "S" and Alterar != "N":
                        print("Opção inválida!")
                if Alterar == "S":
                    Objeto.CPF = ""
                    AlterarCPF = ""
                    while len(AlterarCPF) != 11 and AlterarCPF not in CPF_Unico1:
                        AlterarCPF = str(input("Informe o CPF (apenas números [11]): "))
                        if len(AlterarCPF) != 11:
                            print("CPF inválido!")
                        if AlterarCPF in CPF_Unico1:
                            print("CPF repetido!")
                    CPF_Unico1.discard(CPF)
                    Objeto.CPF = AlterarCPF
                    CPF_Unico1.add(Objeto.CPF)
                    print("CPF alterado com sucesso!")
                print(" ")
                print(f"Nome: {Objeto.Nome}")
                Alterar = ""
                while Alterar != "S" and Alterar != "N":
                    Alterar = str(input("Deseja alterar o Nome?(S ou N): "))
                    if Alterar != "S" and Alterar != "N":
                        print("Opção inválida!")
                if Alterar == "S":
                    Objeto.Nome = str(input("Digite o novo nome: "))
                    print("Nome alterado com sucesso!")
                print(" ")
                print(f"Data de nascimento: {Objeto.Data_De_Nascimento.strftime('%d/%m/%Y')}")
                Alterar = ""
                while Alterar != "S" and Alterar != "N":
                    Alterar = str(input("Deseja alterar a Data de Nascimento?(S ou N): "))
                    if Alterar != "S" and Alterar != "N":
                        print("Opção inválida!")
                Data_Guardar = ""
                while len(Data_Guardar) != 10:
                    Data_Guardar = str(input("Informe a Data de Nascimento (dd/mm/aaaa): "))
                    if len(Data_Guardar) != 10:
                        print("Data de Nascimento inválida!")
                Data_Guardar_Split = list(map(int,Data_Guardar.split("/")))
                Objeto.Data_De_Nascimento = datetime.datetime(Data_Guardar_Split[2],Data_Guardar_Split[1], Data_Guardar_Split[0])
                print(" ")
                print(f"Sexo: {Objeto.Sexo}")
                Alterar = ""
                while Alterar != "S" and Alterar != "N":
                    Alterar = str(input("Deseja alterar o Sexo?(S ou N): "))
                    if Alterar != "S" and Alterar != "N":
                        print("Opção inválida!")
                if Alterar == "S":
                    Objeto.Sexo = ""
                    while Objeto.Sexo != "M" and Objeto.Sexo != "F":
                        Objeto.Sexo = str(input("Informe o Sexo (M ou F): "))
                        if Objeto.Sexo != "M" and Objeto.Sexo != "F":
                            print("Sexo inválido!")
                    print("Sexo alterado com sucesso!")
                print(" ")
                print(f"Salário: R${Objeto.Salario:.2f}")
                Alterar = ""
                while Alterar != "S" and Alterar != "N":
                    Alterar = str(input("Deseja alterar o Salário?(S ou N): "))
                    if Alterar != "S" and Alterar != "N":
                        print("Opção inválida!")
                if Alterar == "S":
                    Objeto.Salario = float(input("Digite o novo salário: "))
                    print("Salário alterado com sucesso!")
                print(" ")
                if len(Objeto.Emails) > 0:
                    i = 0
                    for emails in Objeto.Emails:
                        if i == 0:
                            print(f"E-mail: {emails} ", end=" ")
                            i += 1
                        else:
                            print(f"| {emails}", end=" ")
                    Alterar = ""
                    while Alterar != "S" and Alterar != "N":
                        Alterar = str(input("Deseja alterar algum E-mail?(S ou N): "))
                        if Alterar != "S" and Alterar != "N":
                            print("Opção inválida!")
                    if Alterar == "S":
                        for emails in Objeto.Emails:
                            print(f"E-mail: {emails}?")
                            Alterar = ""
                            while Alterar != "S" and Alterar != "N":
                                Alterar = str(input("Deseja alterar esse E-mail?(S ou N): "))
                                if Alterar != "S" and Alterar != "N":
                                    print("Opção inválida!")
                            if Alterar == "S":
                                emails = str(input("Digite o novo e-mail: "))
                                print("E-mail alterado com sucesso!")
                    print(" ")
                else:
                    print("Nenhum e-mail cadastrado!")
                    print(" ")
                if len(Objeto.Telefones) > 0:
                    i = 0
                    for telefone in Objeto.Telefones:
                        if i == 0:
                            print(f"Telefone: {telefone} ", end=" ")
                            i += 1
                        else:
                            print(f"| {telefone}",end=" ")
                    Alterar = ""
                    while Alterar != "S" and Alterar != "N":
                        Alterar = str(input("Deseja alterar algum Telefone?(S ou N): "))
                        if Alterar != "S" and Alterar != "N":
                            print("Opção inválida!")
                    if Alterar == "S":
                        for telefone in Objeto.Telefones:
                            print(f"Telefone: {telefone}?")
                            Alterar = ""
                            while Alterar != "S" and Alterar != "N":
                                Alterar = str(input("Deseja alterar esse Telefone?(S ou N): "))
                                if Alterar != "S" and Alterar != "N":
                                    print("Opção inválida!")
                            if Alterar == "S":
                                telefone = str(input("Digite o novo telefone: "))
                                print("Telefone alterado com sucesso!")
                else:
                    print("Nenhum telefone cadastrado!")
    else:
        print("Cliente não cadastrado!")

def ExcluirCliente(Lista1, CPF_Unico1):
    print(" ")
    CPF = str(input("Digite o CPF do cliente que você deseja excluir: "))
    if CPF in CPF_Unico1:
        i = 0
        for Objeto in Lista1:
            if CPF == Objeto.CPF:
                Excluir = ""
                while Excluir != "S" and Excluir != "N":
                    Excluir = str(input("Deseja excluir esse Cliente?(S ou N): "))
                    if Excluir != "S" and Excluir != "N":
                        print("Opção inválida!")
                if Excluir == "S":
                    del Lista1[i]
                    CPF_Unico1.discard(CPF)
                print("Cliente excluído com sucesso!")
            i += 1
    else:
        print("Cliente não cadastrado!")

class Produto:
    Codigo = ""
    Descricao = ""
    Peso = 0
    Preco = 0
    Desconto = 0
    Data_De_Validade = ""

def ListarTodosProduto(Produtos1):
    if len(Produtos1) > 0:
        for Objeto in Produtos1:
            print(" ")
            print(f"Código: {Objeto.Codigo}")
            print(f"Descrição: {Objeto.Descricao}")
            print(f"Peso (g): {Objeto.Peso:.2f}")
            print(f"Preço (R$): {Objeto.Preco:.2f}")
            print(f"Desconto (R$): {Objeto.Desconto:.2f}")
            print(f"Data de validade: {Objeto.Data_De_Validade.strftime('%d/%m/%Y')}")
    else:
        print(" ")
        print("Nenhum produto cadastrado!")

def ListarUmProduto(Produtos1, Codigo_Unico1):
    print(" ")
    Codigo = str(input("Digite o código do produto que você deseja visualizar:"))
    if Codigo in Codigo_Unico1:
        for Objeto in Produtos1:
            if Codigo == Objeto.Codigo:
                print(f"Código: {Objeto.Codigo}")
                print(f"Descrição: {Objeto.Descricao}")
                print(f"Peso (g): {Objeto.Peso:.2f}")
                print(f"Preço (R$): {Objeto.Preco:.2f}")
                print(f"Desconto (R$): {Objeto.Desconto:.2f}")
                print(f"Data de validade: {Objeto.Data_De_Validade.strftime('%d/%m/%Y')}")
    else:
        print("Produto não cadastrado!")

def IncluirProduto(Produtos1, Codigo_Unico1):
    print(" ")
    Classe = Produto()
    while len(Classe.Codigo) != 13:
        Classe.Codigo = str(input("Informe o código (apenas números [13]): "))
        if len(Classe.Codigo) != 13:
            print("Código inválido!")
    if Classe.Codigo in Codigo_Unico1:
        print("Código já cadastrado!")
    else:
        Codigo_Unico1.add(Classe.Codigo)
        Classe.Descricao = str(input("Informe a descrição: "))
        Classe.Peso = float(input("Informe o peso (g): "))
        Classe.Preco = float(input("Informe o preço (R$): "))
        Classe.Desconto = float(input("Informe o desconto (R$): "))
        Data_Guardar = ""
        while len(Data_Guardar) != 10:
            Data_Guardar = str(input("Informe a Data de Validade (dd/mm/aaaa): "))
            if len(Data_Guardar) != 10:
                print("Data de Validade inválida!")
        Data_Guardar_Split = list(map(int,Data_Guardar.split("/")))
        Classe.Data_De_Validade = datetime.datetime(Data_Guardar_Split[2],Data_Guardar_Split[1], Data_Guardar_Split[0])
        Produtos1.append(Classe)
        print("Produto inserido com sucesso!")

def AlterarProduto(Produtos1, Codigo_Unico1):
    print(" ")
    Codigo = str(input("Digite o código do produto que você deseja alterar: "))
    if Codigo in Codigo_Unico1:
        for Objeto in Produtos1:
            if Codigo == Objeto.Codigo:
                print(" ")
                print(f"Código: {Objeto.Codigo}")
                Alterar = ""
                while Alterar != "S" and Alterar != "N":
                    Alterar = str(input("Deseja alterar o Código?(S ou N): "))
                    if Alterar != "S" and Alterar != "N":
                        print("Opção inválida!")
                if Alterar == "S":
                    Objeto.Codigo = ""
                    AlterarCodigo = ""
                    while len(AlterarCodigo) != 13 and AlterarCodigo not in Codigo_Unico1:
                        AlterarCodigo = str(input("Informe o Código (apenas números): "))
                        if len(AlterarCodigo) != 13:
                            print("Código inválido!")
                        if AlterarCodigo in Codigo_Unico1:
                            print("Código repetido!")
                    Codigo_Unico1.discard(Codigo)
                    Objeto.Codigo = AlterarCodigo
                    Codigo_Unico1.add(AlterarCodigo)
                    print("Código alterado com sucesso!")
                print(" ")
                print(f"Descrição: {Objeto.Descricao}")
                Alterar = ""
                while Alterar != "S" and Alterar != "N":
                    Alterar = str(input("Deseja alterar o Descrição?(S ou N): "))
                    if Alterar != "S" and Alterar != "N":
                        print("Opção inválida!")
                if Alterar == "S":
                    Objeto.Descricao = str(input("Digite o novo descrição: "))
                    print("Descrição alterado com sucesso!")
                print(" ")
                print(f"Preço: R${Objeto.Preco:.2f}")
                Alterar = ""
                while Alterar != "S" and Alterar != "N":
                    Alterar = str(input("Deseja alterar o Preço?(S ou N): "))
                    if Alterar != "S" and Alterar != "N":
                        print("Opção inválida!")
                if Alterar == "S":
                    Objeto.Preco = float(input("Digite o novo preço: "))
                    print("Preço alterado com sucesso!")
                print(" ")
                print(f"Desconto: R${Objeto.Desconto:.2f}")
                Alterar = ""
                while Alterar != "S" and Alterar != "N":
                    Alterar = str(input("Deseja alterar o Desconto?(S ou N): "))
                    if Alterar != "S" and Alterar != "N":
                        print("Opção inválida!")
                if Alterar == "S":
                    Objeto.Desconto = float(input("Digite o novo desconto: "))
                    print("Desconto alterado com sucesso!")
                print(" ")
                print(f"Data de validade: {Objeto.Data_De_Validade.strftime('%d/%m/%Y')}")
                Alterar = ""
                while Alterar != "S" and Alterar != "N":
                    Alterar = str(input("Deseja alterar a Data de Validade?(S ou N): "))
                    if Alterar != "S" and Alterar != "N":
                        print("Opção inválida!")
                if Alterar == "S":
                    Data_Guardar = ""
                    while len(Data_Guardar) != 10:
                        Data_Guardar = str(input("Informe a Data de Validade (dd/mm/aaaa): "))
                        if len(Data_Guardar) != 10:
                            print("Data de Validade inválida!")
                    Data_Guardar_Split = list(map(int,Data_Guardar.split("/")))
                    Objeto.Data_De_Validade = datetime.datetime(Data_Guardar_Split[2],Data_Guardar_Split[1], Data_Guardar_Split[0])
    else:
        print("Produto não cadastrado!")

def ExcluirProduto(Produtos1, Codigo_Unico1):
    print(" ")
    Codigo = str(input("Digite o código do produto que você deseja excluir: "))
    if Codigo in Codigo_Unico1:
        i = 0
        for Objeto in Produtos1:
            if Codigo == Objeto.Codigo:
                Excluir = ""
                while Excluir != "S" and Excluir != "N":
                    Excluir = str(input("Deseja excluir esse Produto?(S ou N): "))
                    if Excluir != "S" and Excluir != "N":
                        print("Opção inválida!")
                if Excluir == "S":
                    del Produtos1[i]
                    Codigo_Unico1.discard(Codigo)
                print("Produto excluído com sucesso!")
            i += 1
    else:
        print("Produto não cadastrado!")

def main():
    Lista = []
    Produtos = []
    # Compra_Venda = []
    # Relatorio = []
    CPF_Unico = set()
    Codigo_Unico = set()
    Menu = ""
    while Menu != "0":
        Menu = SubMenuClasse()
        if Menu == "1" or Menu == "2" or Menu == "3" or Menu == "4":
            SubMenuInterface(Menu, Lista, Produtos, CPF_Unico, Codigo_Unico)
        elif Menu == "0":
            print(" ")
            print("Obrigado por usar nosso sistema!")
        else:
            print("Opção inválida!")

def SubMenuClasse():
    print(" ")
    print("Cliente..............1")
    print("Produto..............2")
    print("Compra/Venda.........3")
    print("Relatório............4")
    print("Sair.................0")
    Menu = input("-> ")
    return Menu 

def SubMenuInterface(Menu1, Lista1, Produtos1, CPF_Unico1, Codigo_Unico1):
    SubMenu = ""
    while SubMenu != "0":
        SubMenu = SubMenuOpcao()
        if SubMenu == "1":
            if Menu1 == "1":
                ListarTodosCliente(Lista1)
            elif Menu1 == "2":
                ListarTodosProduto(Produtos1)
        elif SubMenu == "2":
            if Menu1 == "1":
                ListarUmCliente(Lista1, CPF_Unico1)
            elif Menu1 == "2":
                ListarUmProduto(Produtos1, Codigo_Unico1)
        elif SubMenu == "3":   
            if Menu1 == "1":
                IncluirCliente(Lista1, CPF_Unico1)
            elif Menu1 == "2":
                IncluirProduto(Produtos1, Codigo_Unico1)
        elif SubMenu == "4":
            if Menu1 == "1":
                AlterarCliente(Lista1, CPF_Unico1)
            if Menu1 == "2":
                AlterarProduto(Produtos1, Codigo_Unico1)
        elif SubMenu == "5":
            if Menu1 == "1":
                ExcluirCliente(Lista1, CPF_Unico1)
            elif Menu1 == "2":
                ExcluirProduto(Produtos1, Codigo_Unico1)
        elif SubMenu == "0":
            SubMenu = "0"
        else:
            print("Opção inválida!")

def SubMenuOpcao():
    print(" ")
    print("Listar Todos...1")
    print("Listar Um......2")
    print("Incluir........3")
    print("Alterar........4")
    print("Excluir........5")
    print("Sair...........0")
    SubMenu_cliente = input("-> ")
    return SubMenu_cliente

main()