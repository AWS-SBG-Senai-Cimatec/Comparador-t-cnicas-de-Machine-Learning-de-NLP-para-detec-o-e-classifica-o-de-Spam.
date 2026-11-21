# Casos de entrada - Aula 02

## B - Validação da futura interface

`validar_mensagem(texto)`, em `src/validation.py`, recebe texto ou `None` e retorna `resultVal`, com `validacao` (bool), `texto` (str) e `orientacao` (str).

A função remove espaços das pontas, preserva o conteúdo e os espaços internos e recusa uma entrada que fique vazia. Não classifica mensagens por palavras nem identifica spam/phishing.

| Entrada | validacao | texto | orientacao |
| --- | --- | --- | --- |
| `None` | `False` | `""` | Digite uma mensagem para continuar. |
| `""` | `False` | `""` | Digite uma mensagem para continuar. |
| `"   "` | `False` | `""` | Digite uma mensagem para continuar. |
| `" Ola "` | `True` | `"Ola"` | `""` |
| `"URGENTE"` | `True` | `"URGENTE"` | `""` |
| `"  Olá  mundo  "` | `True` | `"Olá  mundo"` | `""` |

Na futura interface, chamar a validação antes da inferência. Se `validacao` for falsa, mostrar `orientacao` e interromper a análise. Se for verdadeira, encaminhar `texto` ao pipeline quando estiver disponível. O campo `orientacao` contém o aviso ao usuário, não a mensagem a ser analisada.

### Como conferir

Com Python instalado, abrir o terminal na raiz do repositório:

```bash
python -c "from src.validation import validar_mensagem; print(validar_mensagem('   ')); print(validar_mensagem(' Ola '))"
```

Saída:

```text
resultVal(validacao=False, texto='', orientacao='Digite uma mensagem para continuar.')
resultVal(validacao=True, texto='Ola', orientacao='')
```

Executar apenas `python src/validation.py` não solicita entrada: o arquivo define uma função reutilizável.

## A - Exercícios individuais no terminal

Na raiz do repositório:

```bash
python exercicios/lilian/aula-02.py
python exercicios/rodrigo/aula-02/analise.py
```

Executar um script por vez e digitar uma mensagem quando solicitado.

| Entrada | Tamanho após strip() | Contém urgente | Resultado |
| --- | --- | --- | --- |
| `"  Ola  "` | 3 | `False` | Aceita |
| `"URGENTE"` | 7 | `True` | Aceita |
| `"uRgEnTe"` | 7 | `True` | Aceita |
| `"   "` | — | — | Recusada |
| `" Preciso de ajuda "` | 16 | `False` | Aceita |

A busca por "urgente" pertence apenas ao exercício A e não representa detecção de fraude.

## Registro de revisão técnica

As contribuições de documentação de Lilian e Rodrigo foram consolidadas; a revisão do Moisés identificou problemas de construção do resultado e de orientação. Na revisão técnica de 21/11/2026 foram corrigidos a orientação para vazio, a busca por "urgente" no exercício da Lilian e a indentação do exercício do Rodrigo.

Os testes de integração não substituem a atividade A individual do Moisés nem a explicação dos ajustes pelos autores.
