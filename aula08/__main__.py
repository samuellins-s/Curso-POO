from classes import Pessoa, Aluno, Professor, Funcionario

def main():
    a1 = Aluno('Arthur Jônatan', 18, 'Redes de Computadores', '2026.2')
    a1.fazer_aniversario() # veio da superclasse
    a1.fazer_matricula()
    a1.estudar()

    p1 = Professor('Samuel', 37, 'Biologia', 'Mestrado')
    p1.fazer_aniversario()
    p1.dar_aula()
    p1.estudar()

    f1 = Funcionario('Joberta', 42, 'Secretaria', 'Setor 02')
    f1.fazer_aniversario()
    f1.bater_ponto()
    f1.estudar()

if __name__ == '__main__':
    main()