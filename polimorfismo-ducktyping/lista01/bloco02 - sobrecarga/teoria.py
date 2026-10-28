'''
1. A sobrecarga de metodos é quando há vários metodos com o mesmo nome e parametros diferentes em uma mesma classe, e as chamadas do metodo (apos um objeto criado) vão se adaptando (trocando de metodos de mesmo nome) de acordo com os parametros colocados. O python não possui sobrecarga pois ele sobrescreve metodos de nomes iguais em uma classe, essa "adaptação" não funciona no python. O python sobrescreve os dois métodos na mesma classe.

2. para se resolver isso em python, tem algumas maneiras. 
    2.1 colocando um parametro do metodo com valor padrão (nomeado), exemplo:
    ```
    def somar(self, a, b, c=0):
        return a+b+c
    ```
    Ou seja, se o c não for colocado na chamada do metodo, o parametro c tem como padrão o valor 0.

    2.2 usando *args, exemplo:
    ```
    def somar(*args):
        return sum(args)
    ```
    
    2.3 usando *kwargs, aceitando argumentos nomeados exemplo:
    ```
    def criar_usuario(nome, **kwargs):
        print(nome, kwargs)
    ```

    Continuando,
    def enviar -> definicao do metodo dentro de uma classe
    self -> referencia do objeto a ser instanciado
    msg: str -> parametro tipado como string
    copia: str | None = None -> parametro tipado como string ou None, se não houver argumento preenchendo o parametro copia, este será None.

3. Sobrecarga de operadores é quando damos outros significados a operações básica do python como (==,<,>,), etc. por exemplo, não conseguimos por padrão somar 2 objetos com operador "+" e ter como resultado um valor float, mas podemos resignificar utilizando operadores como __add__, conseguindo, assim, retornar um valor float de acordo como desejamos. Isso é polimorfismo. 

'''