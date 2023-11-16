class Mensagem:
    @staticmethod
    def print_vermelho(mensagem):
        print("\033[91m" + mensagem + "\033[0m")

    @staticmethod
    def print_verde(mensagem):
        print("\033[92m" + mensagem + "\033[0m")

    @staticmethod
    def print_preto(mensagem):
        print("\033[30m" + mensagem + "\033[0m")
