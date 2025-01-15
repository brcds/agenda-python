contatos = []


def menu():
    """
        Exibe menu da agenda
        :return:
    """
    print("\n*** Agenda Telefonica ***")
    print("1. Visualizar contatos")
    print("2. Visualizar contatos favoritos")
    print("3. Adicionar contato")
    print("4. Editar contato")
    print("5. Marcar/Desmarcar contato Favorito")
    print("6. Deletar contatos")
    print("0. Sair")
    return


def salvar_contato(novo_contato):
    """
        salvar contato na agenda
        :param novo_contato:
        :return:
    """
    contatos.append(novo_contato)
    print("Contato salvo com sucesso!")
    return


def visualizar_contatos(somente_favoritos=False):
    """
        Visualizar todos os contatos da agenda ou somente os favoritos.
        :param somente_favoritos:
        :return:
    """
    lista_contatos_favoritos = []
    lista_contatos = []
    for indice, contato in enumerate(contatos, start=1):
        emoji_favorito = " 💓 " if contato.get('favorito') else ""
        if contato.get("favorito"):
            contato_favorito = (
                f"{indice}. {contato.get('nome')} {contato.get('telefone')} {contato.get('email')} {emoji_favorito}")
            lista_contatos_favoritos.append(contato_favorito)
        contato = (
            f"{indice}. {contato.get('nome')} {contato.get('telefone')} {contato.get('email')} {emoji_favorito}")
        lista_contatos.append(contato)

    if somente_favoritos:
        print(f"\n↳ Contatos Favoritos: {len(lista_contatos_favoritos)}")
        for contato in lista_contatos_favoritos:
            print(contato)
    else:
        print(f"\n↳ Todos os contatos: {len(lista_contatos)}")
        for contato in lista_contatos:
            print(contato)
    return


def ajusta_indice_contato(indice):
    """
        Ajusta indice de contato
        :param indice:
        :return:
    """
    indice_ajustado = int(indice) - 1
    return indice_ajustado


def indice_contato_valido(indice):
    """
        Verifica se indice de contato é valido
        :param indice:
        :return:
    """
    if (int(indice) >= 0) and (int(indice) <= len(contatos)):
        return True
    return False


def editar_contato(indice_contato, contato_editado):
    """
        Editar contato na agenda
        :param contato:
        :return:
    """
    if indice_contato_valido(indice_contato):
        contato_atual = contatos[ajusta_indice_contato(indice_contato)].get("telefone")
        contatos[ajusta_indice_contato(indice_contato)] = contato_editado
        print(f"\n↳ Contato {contato_atual}, foi atualizado para {contato_editado}, com sucesso!")
    else:
        print(f"↳ Indice {indice_contato} invalido ou inexistente!")
    return


def marcar_desmarcar_favorito(indice_contato):
    """
        Marcar/Desmarcar contato favorito na agenda
        :param indice_contato:
        :return:
    """
    try:
        contato = contatos[ajusta_indice_contato(indice_contato)]
        desc_atualizado = "Desmarcado como favorito" if contato["favorito"] else "Marcado como favorito"

        if contato.get("favorito"):
            contato["favorito"] = False
        else:
            contato["favorito"] = True

        print(f"\n ↳ O contato foi {desc_atualizado}!")
        visualizar_contatos()
    except IndexError as e:
        print("\n ↳ Indice de contato Inexistente!")
    except ValueError as e:
        print("\n ↳ Informe o indice de contato Valido!")
    return


def deletar_contato(indice_contato):
    """
        Deletar contato na agenda
        :param contato:
        :return:
    """
    try:
        if indice_contato_valido(indice_contato):
            contatos.remove(contatos[ajusta_indice_contato(indice_contato)])
            print("\n↳ Contato deletado com sucesso!")
        else:
            print(f"↳ Indice {indice_contato} invalido ou inexistente!")
    except ValueError as e:
        print("\n ↳ Informe o indice de contato Valido!")
    return
