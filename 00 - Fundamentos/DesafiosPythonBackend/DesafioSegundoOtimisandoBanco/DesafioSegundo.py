class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.limite = 500
        self.extrato = []
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3
    
    def depositar(self, valor):
        """Realiza um depósito na conta."""
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
            return True
        else:
            print("\nOperação falhou! O valor informado é inválido.")
            return False
    
    def sacar(self, valor):
        """Realiza um saque da conta, respeitando as regras estabelecidas."""
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES
        
        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")
            return False
        elif excedeu_limite:
            print("\nOperação falhou! O valor do saque excede o limite.")
            return False
        elif excedeu_saques:
            print("\nOperação falhou! Número máximo de saques excedido.")
            return False
        elif valor > 0:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.numero_saques += 1
            print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
            return True
        else:
            print("\nOperação falhou! O valor informado é inválido.")
            return False
    
    def exibir_extrato(self):
        """Exibe o extrato bancário com todas as movimentações."""
        print("\n" + "=" * 50)
        print("EXTRATO BANCÁRIO".center(50))
        print("=" * 50)
        
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimento in self.extrato:
                print(movimento)
        
        print("=" * 50)
        print(f"Saldo atual: R$ {self.saldo:.2f}".center(50))
        print("=" * 50)
    
    def executar(self):
        """Executa o sistema bancário."""
        menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

        => """
        
        while True:
            opcao = input(menu).strip().lower()
            
            if opcao == "d":
                try:
                    valor = float(input("\nInforme o valor do depósito: R$ "))
                    self.depositar(valor)
                except ValueError:
                    print("\nErro: Por favor, digite um valor numérico válido.")
            
            elif opcao == "s":
                try:
                    valor = float(input("\nInforme o valor do saque: R$ "))
                    self.sacar(valor)
                except ValueError:
                    print("\nErro: Por favor, digite um valor numérico válido.")
            
            elif opcao == "e":
                self.exibir_extrato()
            
            elif opcao == "q":
                print("\nObrigado por utilizar nosso sistema bancário!")
                break
            
            else:
                print("\nOperação inválida, por favor selecione novamente a operação desejada.")

# Executar o sistema bancário
if __name__ == "__main__":
    sistema = SistemaBancario()
    sistema.executar()