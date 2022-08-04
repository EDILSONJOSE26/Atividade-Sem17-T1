def matriculas():
    dados_matricula = {}
    while True:
        matricula = input().strip()
        if matricula == '': break
        nome = input().strip()
        nota1 = float(input())
        nota2 = float(input())
        dados_matricula[matricula] = (nome, nota1, nota2)

    return dados_matricula

def main():
    alunos = matriculas()

    while True:
        key = input().strip()
        if key == '': break
        print(f'{alunos[key][0]}: {(alunos[key][1] + alunos[key][2]) / 2:.1f}')

if __name__ == '__main__':
    main()