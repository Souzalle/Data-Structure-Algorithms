"""
Left shift (<<) → desloca bits para a esquerda
    equivale a multiplicar por 2

    
Right shift (>>) → desloca bits para a direita
    equivale a dividir por 2 (parte inteira)


    
          32 16 8 4 2 1 ---> Valor da casa              
 Binario: 0 0 0 0 0 0 0 

Ex: 5 em binario
          !   ! = 4 + 1 = 5
  32 16 8 4 2 1 
> 0 0 0 0 1 0 1 - 5 binario

Sempre que eu uso um shift é como se eu andasse para esquerda ou direita(dependendo do shit) o valor atruibuito

5 << 1  -> Me diz q estou andando 1 casa binaria para a esquerda utilziando o binario de 5:

    32 16 8 4 2 1 
> 0 0 0 0 1 0 1   - Na casa vazia é adicionado um  0, agora o 5 n é mais 5 e sim 10, ja que agora o 1 esta na casa de 8 e 2

Regra geral para facilitar entendimento:

| Operação | Equivalente     |
| -------- | --------------- |
|  x << 1  |     x * 2       |
|  x << n  |   x * (2 ** n)  |
|  x >> 1  |     x // 2      |
|  x >> n  |   x // (2 ** n) |


"""

5 << 1  # 10