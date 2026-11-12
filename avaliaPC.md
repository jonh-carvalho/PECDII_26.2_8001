# Rubrica de avaliação do projeto — AP1 e AP2

## Finalidade e organização das notas

Esta rubrica organiza a avaliação do projeto em duas notas independentes, ambas calculadas em uma escala de **0 a 100 pontos**:

- **AP1 — Iniciação e Elaboração:** avalia a compreensão do problema, a definição do escopo e a qualidade dos artefatos de análise e projeto.
- **AP2 — Construção e entrega:** avalia principalmente a aplicação implementada. Construção corresponde a **60% da AP2**; os demais critérios avaliam Transição, documentação MkDocs e gestão do trabalho no GitHub.

Cada AP corresponde a uma avaliação completa, com máximo de 100 pontos. Esta rubrica não define como AP1 e AP2 compõem a média final da disciplina nem substitui as regras da Avaliação Continuada (AC).

A avaliação deve considerar evidências verificáveis nos documentos, nas issues e no Project, no site publicado, no código, nos testes e na demonstração. O fechamento de uma issue ou a existência de um artefato, por si só, não comprovam qualidade ou conclusão.

## Escala de desempenho e cálculo

Cada critério recebe um nível de 0 a 4:

| Nível | Desempenho | Descritor |
|---:|---|---|
| 0 | Não apresentado | Não há evidência verificável ou a entrega não atende ao objetivo. |
| 1 | Inicial | Há evidência parcial, com lacunas importantes ou sem validação. |
| 2 | Em desenvolvimento | Atende ao essencial, mas faltam partes, rastreabilidade ou refinamento. |
| 3 | Adequado | Entrega completa e coerente, com problemas menores que não impedem seu uso. |
| 4 | Consistente | Entrega completa, correta, validada, rastreável e integrada às demais partes. |

**Pontuação do critério = (nível obtido ÷ 4) × peso do critério.** A nota da AP é a soma dos pontos dos seus critérios. Um nível em branco indica que o critério ainda não foi avaliado. Se um critério não se aplicar ao escopo aprovado, registrar a justificativa e obter validação docente; não atribuir nota máxima automaticamente.

## Distribuição das notas

| Avaliação | Bloco | Peso na avaliação | Pontuação máxima |
|---|---|---:|---:|
| AP1 | Iniciação | 40% | 40 |
| AP1 | Elaboração | 60% | 60 |
|  | **Total AP1** | **100%** | **100** |
| AP2 | Construção da aplicação | 60% | 60 |
| AP2 | Transição | 15% | 15 |
| AP2 | Site de documentação MkDocs | 15% | 15 |
| AP2 | GitHub Issues e Project | 10% | 10 |
|  | **Total AP2** | **100%** | **100** |

# AP1 — Iniciação e Elaboração (100 pontos)

## Iniciação — 40 pontos

| Critério | Peso | Evidências esperadas |
|---|---:|---|
| Problema, usuários, objetivos e escopo | 16 | Documento de visão e pesquisa explicam o problema, usuários e stakeholders, objetivos e limites. O recorte do MVP é compatível com o cenário Backend GAAP: API para apoiar serviços, agenda, presença e relatórios de treino. Funcionalidades não definidas ou fora de escopo são registradas como decisões a validar, não assumidas. Referências: [issues #2](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/2) e [#3](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/3). |
| Pesquisa, riscos e planejamento inicial | 13 | Pesquisa do domínio e de soluções relacionadas sustenta as decisões; riscos, hipóteses e dependências são identificados; há planejamento inicial coerente com o tempo e o escopo do projeto. |
| Protótipo e preparação do projeto | 11 | Protótipo de baixa fidelidade está ligado aos objetivos; repositório, ambiente, estrutura de documentação e site inicial estão preparados. Referências: [issues #1](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/1), [#7](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/7) e [#9](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/9). |

**Foco da Iniciação:** estabelecer uma visão clara e viável, com problema, público e escopo capazes de orientar os requisitos e as decisões posteriores.

## Elaboração — 60 pontos

| Critério | Peso | Evidências esperadas |
|---|---:|---|
| Requisitos funcionais e não funcionais | 21 | Requisitos relevantes, compreensíveis, verificáveis e priorizados; critérios de aceitação para requisitos prioritários; regras e dúvidas do domínio explicitadas. Referência: [issue #4](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/4). |
| Casos de uso e fluxos | 12 | Atores, pré-condições, fluxos principais, alternativos e exceções descrevem os objetivos dos usuários e são consistentes com os requisitos. Referência: [issue #5](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/5). |
| Modelo conceitual e arquitetura | 18 | Classes, responsabilidades, atributos e relacionamentos representam o domínio; arquitetura e tecnologias são justificadas e coerentes com os requisitos. Riscos técnicos relevantes são identificados. Referência: [issue #6](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/6). |
| Rastreabilidade e coerência dos artefatos | 9 | Visão, requisitos, casos de uso, modelos e protótipos não se contradizem; mudanças e decisões são refletidas nos documentos e relacionadas às tarefas correspondentes. |

**Foco da Elaboração:** definir uma base consistente de requisitos e arquitetura, suficiente para orientar a Construção sem presumir regras que ainda precisam ser validadas.

## Consolidação da AP1

| Bloco | Pontuação máxima | Pontos obtidos |
|---|---:|---:|
| Iniciação | 40 |  |
| Elaboração | 60 |  |
| **Nota AP1** | **100** |  |

# AP2 — Construção e entrega (100 pontos)

## Construção da aplicação — 60 pontos

**A Construção é o componente de maior peso da AP2 (60%).** A prioridade é verificar se a equipe transformou os requisitos em uma aplicação funcional, integrada e testada. Código escrito, endpoints listados ou telas isoladas não substituem a demonstração dos fluxos.

| Critério | Peso | Evidências esperadas |
|---|---:|---|
| Funcionalidades centrais e regras de negócio | 18 | Fluxos prioritários do MVP são executáveis; regras são aplicadas pela API e persistidas corretamente. A demonstração comprova o comportamento do sistema. Referências: [issues #10](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/10) e [#15](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/15). |
| API, dados e integração | 12 | Endpoints, validações, respostas e persistência são consistentes com os requisitos; integração ou consumo da API é demonstrável e trata entradas inválidas e erros. Referência: [issue #13](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/13). |
| Autenticação e autorização | 8 | Autenticação funciona conforme o escopo; operações e dados são protegidos por perfil; fluxos não autorizados são recusados. Segredos, senhas e tokens não são expostos indevidamente. Referência: [issue #12](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/12). |
| Testes e qualidade técnica | 9 | Testes cobrem regras e fluxos críticos; os resultados podem ser repetidos; defeitos relevantes são tratados; código e estrutura permitem manutenção. |
| Documentação técnica da API | 5 | Swagger/OpenAPI descreve a API implementada, incluindo operações, parâmetros, respostas, erros e autenticação. Referência: [issue #11](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/11). |
| Coerência com os artefatos e execução reproduzível | 8 | Aplicação, requisitos, modelos e documentação representam a mesma versão; instruções e dependências permitem configurar e iniciar o projeto sem passos omitidos. Divergências de escopo são justificadas e rastreadas. |
| **Total Construção** | **60** |  |

## Transição — 15 pontos

| Critério | Peso | Evidências esperadas |
|---|---:|---|
| Testes finais de aceitação | 5 | Cenários de ponta a ponta são executados com os perfis e fluxos prioritários. Resultados, falhas e responsável pela validação são registrados; regras e permissões são verificadas. |
| Preparação do ambiente, implantação e release | 4 | Aplicativo é instalado e iniciado em ambiente-alvo reproduzível; configuração, migrações e dependências estão documentadas; uma versão identificável é disponibilizada e validada. |
| Defeitos finais e estabilidade | 2 | Defeitos encontrados na aceitação são registrados, priorizados, corrigidos ou explicitamente aceitos como pendências conhecidas. Há validação de regressão após as correções. |
| Orientação de usuários e entrega | 2 | Tutorial de instalação e uso é adequado ao público; a equipe demonstra os fluxos e comunica limitações e procedimentos básicos de operação. Referência: [issue #14](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/14). |
| Encerramento e retrospectiva | 2 | Entregas, pendências, riscos conhecidos, decisões e próximos passos estão registrados; issues e Project refletem o estado final verificado. |
| **Total Transição** | **15** |  |

**Foco da Transição:** entregar uma versão utilizável e validada, preparar usuários e ambiente e explicitar pendências. A fase não se considera concluída apenas porque o código foi implementado ou a apresentação foi realizada.

## Site de documentação MkDocs — 15 pontos

| Critério | Peso | Evidências esperadas |
|---|---:|---|
| Cobertura e orientação de uso | 6 | Navegação permite encontrar visão, requisitos, modelos e documentação técnica. Tutorial explica como obter, configurar, executar e usar a aplicação, com pré-requisitos e exemplos coerentes. Referência: [issue #14](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/14). |
| Atualização e consistência | 4 | Páginas e diagramas correspondem ao produto entregue e às decisões mais recentes; funcionalidades não implementadas são identificadas como pendentes ou futuras. |
| Build, publicação e acessibilidade | 5 | `mkdocs build` conclui sem erros impeditivos; site publicado está acessível; navegação, imagens, diagramas e links relevantes funcionam. Referência: [issue #16](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/16). |
| **Total MkDocs** | **15** |  |

## GitHub Issues e Project — 10 pontos

| Critério | Peso | Evidências esperadas |
|---|---:|---|
| Qualidade e rastreabilidade das Issues | 4 | Issues descrevem objetivo, contexto, fase RUP/UP, critérios de aceitação e responsável; bugs, documentação, testes e funcionalidades podem ser distinguidos; evidências de conclusão são vinculadas. Referência: [issues do projeto](https://github.com/jonh-carvalho/PBE_26.2_8002/issues), incluindo [#16](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/16). |
| Uso efetivo do GitHub Project | 3 | Itens estão associados às issues; fase, prioridade, responsável e status refletem o trabalho real; bloqueios e mudanças de prioridade ficam visíveis; o quadro é revisado até o encerramento. |
| Colaboração e fluxo de revisão | 3 | Commits e Pull Requests têm relação verificável com as issues; revisões e contribuições são identificáveis; integração e fechamento das tarefas correspondem às mudanças efetivamente entregues. A contribuição individual considera qualidade, responsabilidade e colaboração, não somente volume de commits. |
| **Total GitHub** | **10** |  |

**Foco da gestão:** avaliar a qualidade e a atualização do fluxo de trabalho, não a mera existência de issues, Project ou commits.

## Consolidação da AP2

| Bloco | Peso na AP2 | Pontuação máxima | Pontos obtidos |
|---|---:|---:|---:|
| Construção da aplicação | 60% | 60 |  |
| Transição | 15% | 15 |  |
| Site de documentação MkDocs | 15% | 15 |  |
| GitHub Issues e Project | 10% | 10 |  |
| **Nota AP2** | **100%** | **100** |  |

## Orientações de aplicação

- Registrar nível (0–4), pontuação calculada e uma evidência verificável para cada critério: issue, página MkDocs, Pull Request, commit, teste, release ou demonstração.
- Em cada critério, registrar o que foi atendido, a principal lacuna e o próximo passo esperado.
- Verificar o conteúdo e os critérios de aceite das issues, seguindo os vínculos até as entregas. Issue fechada, milestone concluído ou cartão em “Concluído” não substituem a validação do artefato.
- Executar a aplicação e os testes em ambiente reproduzível; avaliar o site e seu build; não inferir que algo funciona apenas por estar descrito.
- Considerar as apresentações da [AP1 (#8)](https://github.com/jonh-carvalho/PBE_26.2_8002/issues/8) e da AP2, mas pontuar as evidências do projeto, não somente a apresentação.
- Quando o cenário ou os documentos não definirem uma regra do domínio, avaliar se a equipe explicitou e validou a decisão; não presumir um comportamento específico.

## Referências do contexto

- [Cenário Backend GAAP](docs/Iniciacao/cenario.md)
- [Avaliações da disciplina](docs/Disciplina/avaliacoes.md)
- [Roteiro RUP/UP e uso do GitHub](docs/Disciplina/Roteiros/Iniciacao/04_RUPgithub.md)
- Fases do RUP/UP: [Iniciação](docs/Iniciacao/index.md), [Elaboração](docs/Elaboracao/index.md), [Construção](docs/Construcao/index.md) e [Transição](docs/Transicao/index.md)
- [Transição: atividades e produto esperado](docs/Disciplina/Roteiros/Transicao/index.md)
- [Uso do GitHub Projects](docs/Construcao/github_projects.md)
- [Issues do projeto PBE_26.2_8002](https://github.com/jonh-carvalho/PBE_26.2_8002/issues)
