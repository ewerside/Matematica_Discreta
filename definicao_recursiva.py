'''
Grupo:
Daniel Maffezzoli
Ewerton Peixoto de Alencar Arrais
Gabriel Mathias do Carmo Sica
Luiz Fabiano Merino
Miguel Veiga Gonçalves
'''

# OBS: No geral, além dos termos para n de 1 até 15 pedidos, também mostramos o
# termo "a0", que seria o equivalente ao n=0 que dá início à recursão.
def primeiro_slide(n_max):
    f_valores = [3]
    n = 1
    while n <= n_max:
        termo = 2*f_valores[n- 1] + 3
        f_valores.append(termo)
        n += 1
    print(f_valores)
    return f_valores[-1]

print(f'Resultado Primeira Função: {primeiro_slide(15)}\n')


def exponencial(base, expoente):
    f_valores = [1]
    n = 1
    while n <= expoente:
        termo = base * f_valores[n - 1]
        f_valores.append(termo)
        n +=1
    print(f_valores)
    return f_valores[-1]

print(f'Resultado Função Exponencial: {exponencial(5, 15)}\n')


# Mudei o nome da função para melhor representá-la.
def fibonacci(n_max):
    f_valores = [1,1]
    n = 2
    while n <= n_max:
        termo = f_valores[n - 1] + f_valores[n - 2]
        f_valores.append(termo)
        n += 1
    print(f_valores)
    return f_valores[-1]

print(f'Resultado Fibonacci: {fibonacci(15)}\n')


def somatorio(n_max):
    soma = 1
    # Colocamos soma=1 (diferente de soma=0 do slide), pois a ideia para essa
    # função parece ser a de apresentar a soma dos n primeiros números ímpares.
    # Assim começa em 1, não em 3. Se esse não for o caso, favor desconsiderar.
    # O mesmo vale para o produtório.
    n = 1
    f_valores = [1]
    while n <= n_max:
        termo = 2 * n + 1
        soma += termo
        f_valores.append(soma)
        n += 1
    print(f_valores)
    return f_valores[-1]

print(f'Resultado Somatório: {somatorio(15)}\n')

def produtorio(n_max):
    produto = 1
    n = 1
    f_valores = [1]
    while n <= n_max:
        termo = 2 * n + 1
        produto *= termo
        f_valores.append(produto)
        n += 1
    print(f_valores)
    return f_valores[-1]


print(f'Resultado Produtório: {produtorio(15)}')