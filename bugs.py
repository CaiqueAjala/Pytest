"""
                       RELATÓRIO DE DEFEITOS (BUGS)

Projeto: Calculadora Científica Simples
Data de Registro: 08/11/2026
Status Geral: Em análise / Aguardando correção via TDD

-------------------------------------------------------------------------------
BUG 01: Erro Lógico no Cálculo da Adição (Soma Duplicada)
-------------------------------------------------------------------------------
1. Identificação do Bug:
   - Localização do Bug: Arquivo `Calculadora.py`, função `adicao(x, y)`

2. Descrição Detalhada:
   - Descrição Clara: A função executa `return x + np.add(x, y)`. O correto seria apenas `np.add(x, y)` ou `x + y`. Do jeito que está implementado, o valor de `x` é somado duas vezes, gerando resultados incorretos em todas as operações de adição.
   - Contexto: Ambiente Python 3.x com biblioteca NumPy.

3. Passos para Reproduzir:
   - Passo a Passo:
     1. Importar o módulo ou executar a calculadora.
     2. Selecionar a opção 1 (Adição).
     3. Informar x = 2 e y = 3.
   - Consistência: Determinístico (ocorre em 100% das execuções).

4. Resultado Esperado vs. Obtido:
   - Resultado Esperado: `adicao(2, 3)` deve retornar `5`.
   - Resultado Obtido: `adicao(2, 3)` retorna `7` (pois calcula 2 + (2 + 3)).

5. Severidade e Impacto:
   - Severidade: Alta.
   - Impacto: Corrompe a operação matemática primária da calculadora.

6. Sugestão para Correção:
   - Alterar o retorno da função para `return np.add(x, y)` ou simplesmente `return x + y`.

7. Registro e Acompanhamento:
   - Data de Identificação: 08/11/2026
   - Status: Não resolvido.


-------------------------------------------------------------------------------
BUG 02: Erro Lógico no Loop do Fatorial (Resultado Sempre Zero)
-------------------------------------------------------------------------------
1. Identificação do Bug:
   - Localização do Bug: Arquivo `Calculadora.py`, função `fatorial(x)`

2. Descrição Detalhada:
   - Descrição Clara: O loop `range(x+1)` gera a sequência começando em `0` (ex: 0, 1, 2, ...). Como a variável acumuladora `fat` começa em 1 e é multiplicada por cada elemento do loop, a primeira multiplicação é por zero (`fat *= 0`), o que anula todo o resultado final independente do valor inserido.
   - Contexto: Estrutura de repetição baseada em `range`.

3. Passos para Reproduzir:
   - Passo a Passo:
     1. Executar a função `fatorial(5)`.
     2. Observar o valor retornado.
   - Consistência: Ocorre em 100% das execuções para qualquer inteiro `x >= 0`.

4. Resultado Esperado vs. Obtido:
   - Resultado Esperado: `fatorial(5)` deve retornar `120`.
   - Resultado Obtido: Retorna `0`.

5. Severidade e Impacto:
   - Severidade: Crítica.
   - Impacto: Impossibilita o uso da funcionalidade de fatorial.

6. Sugestão para Correção:
   - Ajustar o loop para iniciar em 1: `range(1, x + 1)`. Adicionar também tratamento para números negativos.

7. Registro e Acompanhamento:
   - Data de Identificação: 08/11/2026
   - Status: Não resolvido.


-------------------------------------------------------------------------------
BUG 03: Erro de Atributo Inexistente no Logaritmo Natural (`np.ln`)
-------------------------------------------------------------------------------
1. Identificação do Bug:
   - Localização do Bug: Arquivo `Calculadora.py`, função `logaritmo_natural(x)`

2. Descrição Detalhada:
   - Descrição Clara: A biblioteca NumPy não possui a função `ln`. A função correta para logaritmo natural de base $e$ é `np.log()`. Ao tentar chamar `np.ln(x)`, o Python lança uma exceção não tratada e encerra o programa com erro.
   - Contexto: Compatibilidade com a API da biblioteca NumPy.

3. Passos para Reproduzir:
   - Passo a Passo:
     1. Chamar a função `logaritmo_natural(10)`.
     2. O programa interrompe a execução com erro.
   - Consistência: Ocorre sempre.

4. Resultado Esperado vs. Obtido:
   - Resultado Esperado: Retornar o logaritmo natural aproximado de 10 (`2.3025...`).
   - Resultado Obtido: `AttributeError: module 'numpy' has no attribute 'ln'`.

5. Severidade e Impacto:
   - Severidade: Alta (causa Crash da aplicação).
   - Impacto: Impede totalmente a utilização do cálculo de Logaritmo Natural.

6. Sugestão para Correção:
   - Substituir `np.ln(x)` por `np.log(x)`.

7. Registro e Acompanhamento:
   - Data de Identificação: 08/11/2026
   - Status: Não resolvido.


-------------------------------------------------------------------------------
BUG 04: Erro de Validação de Limite Matemático no Logaritmo Base 10
-------------------------------------------------------------------------------
1. Identificação do Bug:
   - Localização do Bug: Arquivo `Calculadora.py`, função `logaritmo_base10(x)`

2. Descrição Detalhada:
   - Descrição Clara: A validação atual `if x < 0:` permite a passagem do valor `0`. No entanto, o logaritmo em qualquer base é indefinido para números menores ou iguais a zero ($x \le 0$). Passar 0 para `np.log()` resulta em `-inf` e um aviso (`RuntimeWarning`) do NumPy, em vez de retornar a mensagem de erro amigável tratada na condição.
   - Contexto: Validação de entradas no domínio dos números reais.

3. Passos para Reproduzir:
   - Passo a Passo:
     1. Executar `logaritmo_base10(0)`.
   - Consistência: Ocorre em todas as tentativas com entrada 0.

4. Resultado Esperado vs. Obtido:
   - Resultado Esperado: Retornar a string `"Erro: Logaritmo de número não positivo"`.
   - Resultado Obtido: Retorna `-inf` (Infinity) acompanhado de `RuntimeWarning: divide by zero encountered in log`.

5. Severidade e Impacto:
   - Severidade: Média.
   - Impacto: Retorno inconsistente de valores matemáticos inválidos para o usuário.

6. Sugestão para Correção:
   - Alterar a condição de validação para `if x <= 0:`.

7. Registro e Acompanhamento:
   - Data de Identificação: 08/11/2026
   - Status: Não resolvido.


-------------------------------------------------------------------------------
BUG 05: Funções Trigonométricas Não Declaradas e Erro de Opção no Menu
-------------------------------------------------------------------------------
1. Identificação do Bug:
   - Localização do Bug: Arquivo `Calculadora.py`, bloco do menu / chamadas das opções 10, 11 e 12

2. Descrição Detalhada:
   - Descrição Clara: O menu exibe as opções: 10 (Seno), 11 (Cosseno) e 12 (Tangente). Contudo:
     1. A opção 10 (Seno) nem sequer foi contemplada na estrutura `elif` da função `calculadora_cientifica()`.
     2. As opções 11 e 12 tentam chamar `cosseno(x)` e `tangente(x)`, porém essas funções **não foram declaradas/definidas** em nenhum lugar do script.
   - Contexto: Executiva/Interface CLI interativa da calculadora.

3. Passos para Reproduzir:
   - Passo a Passo:
     1. Executar o script `Calculadora.py`.
     2. Digitar `10` -> Nada acontece além de ir direto para "Operação inválida".
     3. Digitar `11` ou `12` -> Lança exceção `NameError: name 'cosseno' is not defined`.
   - Consistência: Ocorre sempre.

4. Resultado Esperado vs. Obtido:
   - Resultado Esperado: Calcular os valores trigonométricos de Seno, Cosseno e Tangente.
   - Resultado Obtido: Falha de navegação (opção 10) ou crash com `NameError` (opções 11 e 12).

5. Severidade e Impacto:
   - Severidade: Alta.
   - Impacto: Quebra a execução da interface quando o usuário escolhe opções ofertadas no menu.

6. Sugestão para Correção:
   - Definir as funções `seno(x)`, `cosseno(x)` e `tangente(x)` (lembrando de converter de graus para radianos com `np.radians` caso a entrada seja em graus) e adicionar os respectivos blocos `elif` no menu.

7. Registro e Acompanhamento:
   - Data de Identificação: 08/11/2026
   - Status: Não resolvido.
"""