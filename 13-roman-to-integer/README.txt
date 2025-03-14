##O programa rodou em um tempo de execução de 4ms (supera 65.01%) e usou 17.94 MB (supera 21,28%)

###Minha solução se resumiu em:

1. Mapear os caracteres em romanos para serem chaves dos seus equivalentes em decimal.

2. Criar uma variavel lista para armazenar os numeros inteiros

3. Fazer um loop na string convertendo os equivalentes para a lista, de modo que se um valor for maior que o anterior, torna o valor do anterior negativo.

4. Somar todos os itens da lista com o Sum()

###Complexidade de Tempo

O loop na string é O(n) mais a soma da lista que é de tamanho igual ao input também é O(n)

O(n) + O(n) = **O(n)**