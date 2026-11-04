# Como contribuir

## Uma tarefa por vez

Escolha uma issue com `status:pronto`. Confirme quem integra, quem revisa e o critério de conclusão. Se houver uma dependência pendente, registre o bloqueio antes de começar.

## Branch e PR

```bash
git switch main
git pull --ff-only
git switch -c feat/NUMERO-resumo
# editar e verificar a tarefa
git status
git add caminho/do/arquivo
git commit -m "feat: descreve a entrega"
git push -u origin feat/NUMERO-resumo
```

Para documentação, use `docs/NUMERO-resumo` e uma mensagem `docs: ...`. Substitua NUMERO pelo número real da issue. Abra PR para `main`, descreva a mudança e use `Closes #NUMERO` quando o merge concluir a tarefa.

Um colega revisa e registra o que conferiu; o responsável técnico valida a integração. Não alterar diretamente a `main` durante o trabalho das aulas.

## Duas entregas por aula

- **A:** solução individual em `exercicios/seu-nome/aula-XX/`, com resultado observado e explicação.
- **B:** contribuição ao código, documentação ou relatórios do comparador. O projeto usa uma implementação por função.

Concluir A não conclui B. Para integrar B, verificar a mudança junto das etapas anteriores, responder à revisão e atualizar a documentação correspondente.

## Revisão útil

Confira o exemplo da issue, execute o que foi entregue e faça uma pergunta sobre uma decisão. O autor deve explicar as linhas principais e demonstrar uma variação. Registre o resultado no PR; não use apenas “ok”.

## Pedir ajuda

Informe objetivo, comando/erro, o que tentou e sua dúvida específica. Avise se ficou bloqueado após cerca de 30 minutos de tentativa ou se o prazo combinado ficou inviável.

## Arquivos

Não enviar `.venv`, credenciais, contatos pessoais, CSV real, dados derivados ou modelos gerados. Use os exemplos fictícios em `data/exemplos/` para praticar. Não mudar a licença existente.
