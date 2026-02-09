"""Time complexity: 
    - Best case - O(n)
    - Worst case - O(n²)

# Space complexity: 0(n)

"""

# nums = [5,4,3,2,1]

def bubble(nums):
    size = len(nums) # recebe o tamanho de nums, no caso do exemplo 5

    for _ in nums: # para cada elemento de nums eu executo o codigo 
        is_sorted = True # deixo essa variavel como verdadeiro para saber se a lçista ja esta em ordem      
        for i in range(size-1): # para cada elemento no range de size-1, o -1 me garante que eu n vou ter um problema de comparar o ultimo elemento com "nada", ja que ele é o ultimo nao existe nada depois
            if nums[i] > nums[i+1]: # se meu elemento for maior que o seu proximo
                is_sorted = False # coloco minha variavel como falsa, pois a lista nao esta em ordem
                nums[i+1], nums[i]  = nums[i], nums[i+1] # inverto meu lemento com o seu proximo, X,Y passa a ser Y,X
    if is_sorted: # se meu for acima não alterar a variavel para falso, ent esta em ordem e eu retorno que a lista está ok
        return
