import agenda

while True:
    agenda.menu()
    escolha = int(input(" ⇨ Selecione uma opção: "))

    if escolha == 1:
        agenda.visualizar_contatos()

    if escolha == 2:
        agenda.visualizar_contatos(True)

    if escolha == 3:
        nome = input("\nDigite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        novo_contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
        agenda.salvar_contato(novo_contato)

    if escolha == 4:
        agenda.visualizar_contatos()

        indice_contato = input("\nDigite o indice de contato: ")
        contato_editado = input("Digite o contato: ")
        agenda.editar_contato(indice_contato, contato_editado)

    if escolha == 5:
        agenda.visualizar_contatos()
        indice_contato = input("\nDigite o indice de contato que deseja favoritar/desfavoritar: ")
        agenda.marcar_desmarcar_favorito(indice_contato)

    if escolha == 6:
        agenda.visualizar_contatos()
        indice_contato = input("\nDigite o indice de contato que deseja deletar: ")
        agenda.deletar_contato(indice_contato)

    if escolha == 0:
        break
