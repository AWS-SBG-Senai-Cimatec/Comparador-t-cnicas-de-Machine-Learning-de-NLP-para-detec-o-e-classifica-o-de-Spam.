# Aula 02 - Analisar texto no terminal

Ler uma mensagem, remover espaços das pontas, contar caracteres e verificar se contém "urgente", ignorando maiúsculas.

- `len()` conta caracteres da mensagem limpa, não palavras.
- `strip()` remove espaços das pontas, preservando os internos.
- `lower()` permite buscar "urgente" sem diferenciar maiúsculas.
- `analise()` retorna a mensagem limpa, o tamanho e o indicador; para entrada vazia retorna `None`.
- `main()` lê a entrada e mostra o resultado.

O código da entrega foi preservado em [aula-02/analise.py](aula-02/analise.py), com a indentação corrigida na revisão técnica.

Na raiz do repositório:

```bash
python exercicios/rodrigo/aula-02/analise.py
```

Casos conferidos na revisão técnica: `"  Ola  "` → tamanho 3 e indicador falso; `"URGENTE"` → tamanho 7 e indicador verdadeiro; `"   "` → entrada recusada.

O indicador é apenas didático e não detecta phishing. Esses testes da revisão não substituem a explicação individual do autor.
