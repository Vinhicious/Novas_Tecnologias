from datetime import date
from contato import Contato
from contato_emergencia import ContatoEmergencia
from evento import Evento
from agenda import Agenda

def criar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    datanasc = date(*map(int, input("Data de Nascimento (dd/mm/aaaa): ").split('/')))
    email = input("E-mail: ")
    return Contato(nome, telefone, datanasc, email)

def criar_contato_emergencia():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    datanasc = date(*map(int, input("Data de Nascimento (dd/mm/aaaa): ").split('/')))
    email = input("E-mail: ")
    return ContatoEmergencia(nome, telefone, datanasc, email)

def criar_evento():
    descricao = input("Descrição do Evento: ")
    data_inicio = date(*map(int, input("Data de Início (dd/mm/aaaa): ").split('/')))
    data_fim = date(*map(int, input("Data de Fim (dd/mm/aaaa): ").split('/')))
    contato = criar_contato()  
    return Evento(descricao, data_inicio, data_fim, contato)

def menu():
    while True:
        print("\nMenu:")
        print("1. Criar contato")
        print("2. Criar contato de emergência")
        print("3. Criar evento")
        print("4. Listar eventos")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                contato = criar_contato()
                Agenda(contato=contato)
            case "2":
                contato_emergencia = criar_contato_emergencia()
                Agenda(contato=contato_emergencia)
            case "3":
                evento = criar_evento()
                Agenda(evento=evento)
            case "4":
                for evento in Agenda.eventos():
                    print(evento.get_informacoes())
            case "5":
                print(f"Total de eventos: {Evento.get_total_eventos()}")
                break
            case _:
                print("Opção inválida.")

if __name__ == "__main__":
    menu()
