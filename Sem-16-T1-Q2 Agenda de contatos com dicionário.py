def cria_agenda(qntd):
    contatos = {}
    for pessoa in range(qntd):
        nome = input().strip()
        cidade = input().strip()
        estado = input().strip()
        telefone = input().strip()
        contatos[pessoa] = (nome, cidade, estado, telefone)
    return contatos
    
def main():
    #entrada
    qntd_contatos = int(input())
    agenda_telefonica = cria_agenda(qntd_contatos)

    #saída
    for contato in agenda_telefonica:
        print(f'{agenda_telefonica[contato][0]:<25}{agenda_telefonica[contato][1] + "(" + agenda_telefonica[contato][2] + ")":<30}{agenda_telefonica[contato][3]}')
        
if __name__ == '__main__':
    main()