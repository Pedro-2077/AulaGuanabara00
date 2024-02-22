def maior(*nums):
    maior = 0
    for valor in nums:
        if valor > maior:
            maior = valor

    print(f'Foram informado {len(nums)} e o  maior é: {maior}')


maior(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
maior(4, 5, 6, 7)
