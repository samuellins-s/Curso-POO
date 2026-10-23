'''
1. É quando háuma hieranquia consecutivas de herança. D herda de B e C, e B e C herdam de A.

2. É o Method Resolution Order. Há uma fila que obedece uma ordem de escrita das bases. Importa sim, é da esquerda para direita, a ordem primeiro é a da superclasse B.

3. é executada a de A (que B herda), pois a ordem é D(B, C). a prioridade começa no B e suas superclasses (o python vai procurando da classe especializada para a generalizada).


'''