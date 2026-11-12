# Rubrica de avaliação do projeto

## Finalidade e formato das notas

Esta rubrica organiza a avaliação do projeto em duas notas independentes, cada uma calculada em uma escala de 0 a 100 pontos:

- **AP1 — Iniciação e Elaboração:** avalia a definição do problema, a documentação e o planejamento do sistema.
- **AP2 — Construção e evidências de apoio:** avalia principalmente a implementação da aplicação, além da documentação MkDocs e da gestão do trabalho no GitHub.

A fase de **Transição não faz parte desta rubrica**. Os critérios correspondentes à entrega e implantação final foram retirados. Cada AP tem sua própria pontuação máxima de 100; esta rubrica não determina como essas notas compõem a média final da disciplina.

Os critérios estão alinhados aos roteiros RUP/UP e às issues do repositório [PBE_26.2_8002](https://github.com/jonh-carvalho/PBE_26.2_8002/issues). Os pesos abaixo são uma proposta de distribuição para cada nota.

## Escala de desempenho

Cada critério recebe um nível de 0 a 4:

| Nível | Desempenho | Descritor |
|---:|---|---|
| 0 | Não apresentado | Não há evidência verificável, ou a entrega não atende ao objetivo do critério. |
| 1 | Inicial | Há evidência parcial, mas com lacunas importantes, inconsistências ou sem validação. |
| 2 | Em desenvolvimento | Atende ao essencial, porém faltam partes, rastreabilidade ou refinamento. |
| 3 | Adequado | Entrega completa e coerente, com pequenos problemas que não impedem seu uso ou compreensão. |
| 4 | Consistente | Entrega completa, correta, rastreável, validada e integrada às demais partes do projeto. |

**Cálculo por critério:**

`pontuação do critério = (nível obtido ÷ 4) × peso do critério`

Um nível em branco significa que o critério ainda não foi avaliado. Quando um critério não for aplicável ao escopo aprovado, a equipe deve registrar a justificativa em uma issue e obter validação docente; não se deve atribuir nota máxima automaticamente.

## AP1 — Iniciação e Elaboração (100 pontos)

### Iniciação — 40 pontos

| Critério | Peso | Evidências esperadas |
|---|---:|---|
| Problema, público, objetivos e escopo | 16 | Contexto e problema delimitados; público e stakeholders identificados; objetivos, limites e visão do produto coerentes. Referências: [issue #2](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/2), [issue #3](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/3). |
| Pesquisa, riscos e planejamento inicial | 13 | Pesquisa do domínio e de soluções relacionadas, com justificativas; riscos e ações identificados; plano compreensível e compatível com o semestre. |
| Protótipo e preparação do trabalho | 11 | Protótipo de baixa fidelidade ligado aos objetivos; repositório, ambiente, estrutura de documentação e site inicial configurados. Referências: [issue #1](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/1), [issue #7](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/7). |

**Foco da fase:** estabelecer uma visão clara e viável, capaz de orientar os requisitos e permitir avaliar se o produto proposto responde ao problema.

### Elaboração — 60 pontos

| Critério | Peso | Evidências esperadas |
|---|---:|---|
| Requisitos funcionais e não funcionais | 21 | Requisitos relevantes, compreensíveis, verificáveis e priorizados; critérios de aceitação; relação explícita com o problema e o escopo. Referência: [issue #4](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/4). |
| Casos de uso e fluxos | 12 | Atores, pré-condições, fluxos principais e alternativos descritos; cobertura dos objetivos do usuário e consistência com os requisitos. Referência: [issue #5](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/5). |
| Modelo conceitual e arquitetura | 18 | Classes, responsabilidades, atributos e relacionamentos coerentes com os requisitos; decisões arquiteturais e tecnologias justificadas; riscos técnicos críticos tratados. Referência: [issue #6](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/6). |
| Rastreabilidade e coerência dos artefatos | 9 | Visão, requisitos, casos de uso, modelos e protótipos não se contradizem; mudanças são atualizadas nos documentos e ligadas às tarefas correspondentes. |

**Foco da fase:** os artefatos devem orientar a implementação. Diagramas e protótipos precisam representar o sistema proposto, e não apenas cumprir formalmente um formato.

### Consolidação da nota AP1

| Bloco | Pontuação máxima |
|---|---:|
| Iniciação | 40 |
| Elaboração | 60 |
| **Total AP1** | **100** |

**Evidências para apresentação:** documentos de visão e pesquisa, levantamento de requisitos, casos de uso, diagramas, protótipo, repositório e issues relacionadas. As issues [#1](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/1) a [#9](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/9) servem como referências de acompanhamento da AP1; a avaliação deve considerar o conteúdo e a qualidade real das entregas, não apenas o estado das issues.

## AP2 — Construção e evidências de apoio (100 pontos)

A Construção representa **70% da AP2**, valorizando a implementação funcional, as regras de negócio, a integração e a qualidade técnica. A documentação MkDocs e a gestão do trabalho complementam a avaliação com 15 pontos cada.

### Construção da aplicação — 70 pontos

| Critério | Peso | Evidências esperadas |
|---|---:|---|
| Funcionalidades centrais e regras de negócio | 24 | Fluxos principais implementados e demonstráveis; regras de negócio tratadas no sistema; persistência e respostas compatíveis com os requisitos. Referências: lógica central na [issue #15](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/15) e classes de análise na [issue #10](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/10). |
| API e integração | 12 | Endpoints implementados e consistentes com os contratos; integração ou consumo demonstrado; tratamento adequado de entradas, erros e respostas. Referência: [issue #13](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/13). |
| Autenticação e controle de acesso | 10 | Autenticação funcional conforme o escopo; rotas protegidas e permissões verificadas; credenciais e tokens não expostos indevidamente. Referência: [issue #12](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/12). |
| Documentação técnica da API | 6 | Swagger/OpenAPI disponível e alinhado à versão implementada; operações, parâmetros, respostas e autenticação explicados. Referência: [issue #11](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/11). |
| Testes e qualidade técnica | 12 | Testes relevantes para regras e fluxos críticos; execução demonstrável; defeitos tratados; organização e legibilidade do código permitem manutenção. |
| Coerência entre implementação e especificação | 6 | Comportamento da aplicação corresponde aos requisitos e modelos atualizados; divergências estão registradas e justificadas. |

**Foco da fase:** avaliar o sistema em funcionamento por meio de cenários reais. A demonstração deve comprovar os fluxos implementados, não apenas exibir código ou telas isoladas.

### Site de documentação MkDocs — 15 pontos

| Critério | Peso | Evidências esperadas |
|---|---:|---|
| Cobertura, organização e documentação de uso | 5 | Navegação coerente; páginas e artefatos relevantes acessíveis; tutorial explica como obter, configurar, executar e usar a aplicação. Referência: [issue #14](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/14). |
| Atualização e rastreabilidade | 5 | Site reflete a implementação e os documentos da AP1; documentação, diagramas, API e aplicação descrevem a mesma versão; links para issues e entregas facilitam a conferência. Referência: [issue #16](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/16). |
| Publicação e funcionamento | 5 | Site publicado e acessível; navegação, imagens, diagramas e links funcionam; build do MkDocs executa sem erros relevantes. |

### Gestão e colaboração no GitHub — 15 pontos

| Critério | Peso | Evidências esperadas |
|---|---:|---|
| Qualidade das Issues | 5 | Tarefas compreensíveis, com objetivo, contexto, fase, critérios de aceitação e links para entregas; etiquetas ajudam a localizar documentação, desenvolvimento, testes e defeitos. |
| Uso do GitHub Project | 5 | Project representa o fluxo real; itens associados às issues; estados atualizados; marcos distinguem Iniciação, Elaboração e Construção; bloqueios e mudanças de prioridade ficam visíveis. |
| Colaboração e contribuição verificável | 5 | Commits e Pull Requests identificáveis e relacionados a issues; mudanças revisadas e discutidas; contribuição individual demonstrável por qualidade, responsabilidade e colaboração, não pelo volume bruto de commits. |

**Foco da gestão:** não se avalia positivamente uma issue apenas por estar fechada, nem um Project apenas por existir. Consideram-se o conteúdo, os critérios de conclusão, a rastreabilidade com as entregas e a atualização coerente do fluxo.

### Consolidação da nota AP2

| Bloco | Pontuação máxima |
|---|---:|
| Construção da aplicação | 70 |
| Site de documentação MkDocs | 15 |
| Gestão e colaboração no GitHub | 15 |
| **Total AP2** | **100** |

**Evidências para apresentação:** aplicação executável, funcionalidades e regras demonstradas, testes, documentação de API, tutorial de uso, site MkDocs atualizado, Issues e Project coerentes. As issues [#10](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/10) a [#16](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/16) apoiam a verificação, sem substituir a validação das entregas.

## Orientações de avaliação

- Registrar nível (0–4), pontuação calculada e uma evidência verificável para cada critério: issue, página MkDocs, Pull Request, commit, teste ou demonstração.
- Em cada comentário, indicar o que foi atendido, a principal lacuna e o próximo passo esperado.
- Verificar o histórico e os critérios de aceite das issues, seguindo os links até a entrega; o estado da issue, isoladamente, não comprova qualidade.
- Considerar autoria e conteúdo das mudanças, tarefas assumidas, revisões e colaboração na análise individual. Não usar apenas a contagem de commits como medida de contribuição.
- Ausências e pontualidade seguem as regras da disciplina e não devem ser inferidas apenas pelo histórico do GitHub.

## Registro das notas

### AP1 — Iniciação e Elaboração

| Bloco | Pontuação obtida | Evidências e observações |
|---|---:|---|
| Iniciação (40) |  |  |
| Elaboração (60) |  |  |
| **Nota AP1 (100)** |  |  |

### AP2 — Construção e evidências de apoio

| Bloco | Pontuação obtida | Evidências e observações |
|---|---:|---|
| Construção da aplicação (70) |  |  |
| Site de documentação MkDocs (15) |  |  |
| Gestão e colaboração no GitHub (15) |  |  |
| **Nota AP2 (100)** |  |  |

## Referências do contexto

- [Avaliações da disciplina](../docs/Disciplina/avaliacoes.md)
- [Roteiro RUP/UP e uso do GitHub](../docs/Disciplina/Roteiros/Iniciacao/04_RUPgithub.md)
- Fases do RUP/UP: [Iniciação](../docs/Iniciacao/index.md), [Elaboração](../docs/Elaboracao/index.md) e [Construção](../docs/Construcao/index.md)
- [Issues do projeto PBE_26.2_8002](https://github.com/jonh-carvalho/PBE_26.2_8002/issues)
