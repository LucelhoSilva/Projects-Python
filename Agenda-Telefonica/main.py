from agenda import Agenda
from contato import Contato
from mensagem import Mensagem

agenda = Agenda()
mensagem = Mensagem()

escolha = 0
while escolha != 7:
    mensagem.print_preto("\n               menu:               ")
    mensagem.print_preto("___________________________________")
    mensagem.print_preto("\n1. Adicionar contato")
    mensagem.print_preto("2. Remover contato")
    mensagem.print_preto("3. Buscar contato por nome")
    mensagem.print_preto("4. Buscar contato por email")
    mensagem.print_preto("5. Buscar contato por telefone")
    mensagem.print_preto("6. Consultar tamanho da Agenda")
    mensagem.print_preto("7. Finalizar")
    mensagem.print_preto("___________________________________")
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        nome = input("\nNome: ")
        email = input("Email: ")
        telefone = int(input("Telefone: "))
        novo_contato = Contato(nome, email, telefone)
        agenda.adicionar_contato(novo_contato)
        mensagem.print_verde("\nContato adicionado com sucesso! :)")

    elif escolha == 2:
        nome_remover = input("\nNome do contato a ser removido: ")
        removido = agenda.remover_contato(nome_remover)
        if removido:
            print("Contato removido com sucesso!")
        else:
            mensagem.print_vermelho("Contato não encontrado. :(")

    elif escolha == 3:
        nome_buscar = input("\nNome do contato a ser buscado: ")
        contato_por_nome = agenda.buscar_contato_por_nome(nome_buscar)
        if contato_por_nome:
            print(
                f"Contato encontrado:\nNome: {contato_por_nome.nome}\nEmail: {contato_por_nome.email}\nTelefone: {contato_por_nome.telefone}")
        else:
            mensagem.print_vermelho("Contato não encontrado. :(")

    elif escolha == 4:
        email_buscar = input("\nEmail do contato a ser buscado: ")
        contato_por_email = agenda.buscar_contato_por_email(email_buscar)
        if contato_por_email:
            print(
                f"Contato encontrado:\nNome: {contato_por_email.nome}\nEmail: {contato_por_email.email}\nTelefone: {contato_por_email.telefone}")
        else:
            mensagem.print_vermelho("Contato não encontrado. :(")

    elif escolha == 5:
        telefone_buscar = int(input("\nTelefone do contato a ser buscado: "))
        contato_por_telefone = agenda.buscar_contato_por_telefone(
            telefone_buscar)
        if contato_por_telefone:
            print(
                f"Contato encontrado:\nNome: {contato_por_telefone.nome}\nEmail: {contato_por_telefone.email}\nTelefone: {contato_por_telefone.telefone}")
        else:
            mensagem.print_vermelho("Contato não encontrado. :(")

    elif escolha == 6:
        tamanho_agenda = agenda.consultar_tamanho()
        print(f"\nTamanho da Agenda: {tamanho_agenda} contatos.")

    elif escolha == 7:
        print("Programa encerrado.")

    else:
        mensagem.print_vermelho("Opção inválida. Tente novamente. >:(")
