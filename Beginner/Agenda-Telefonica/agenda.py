class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                return True  # Contato removido com sucesso
        return False  # Contato não encontrado

    def buscar_contato_por_nome(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None  # Contato não encontrado

    def buscar_contato_por_email(self, email):
        for contato in self.contatos:
            if contato.email == email:
                return contato
        return None  # Contato não encontrado

    def buscar_contato_por_telefone(self, telefone):
        for contato in self.contatos:
            if contato.telefone == telefone:
                return contato
        return None  # Contato não encontrado

    def consultar_tamanho(self):
        return len(self.contatos)
