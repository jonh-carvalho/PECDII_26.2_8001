# Análise do roteiro de desenvolvimento — Streaming API

## 1. Escopo e síntese

Esta análise considera os 17 materiais encontrados na pasta `Streaming`, do projeto geral e regras de negócio aos roteiros de modelagem, API REST, playlist, autenticação, filtros, consumo Web e deploy.

O conjunto aborda temas relevantes para uma formação em desenvolvimento web, especialmente modelagem relacional, API REST, autenticação, autorização, documentação e integração com cliente. No estado atual, porém, o material funciona mais como uma coleção de exemplos do que como um roteiro de desenvolvimento progressivo: os escopos variam entre arquivos, há implementações incompatíveis entre si, conteúdo duplicado e lacunas entre a ambição anunciada e o sistema realmente construído.

O ponto de escopo mais importante é distinguir:

- **Catálogo/API de conteúdo:** cadastro e consulta de metadados, usuários, playlists e URLs de mídia. É o que os exemplos Django/DRF implementam principalmente.
- **Streaming de mídia:** ingestão e armazenamento de arquivos, processamento/transcodificação, entrega de segmentos, qualidade adaptativa, controle de acesso à mídia e distribuição. É citado na visão geral, mas não é implementado nem detalhado nos roteiros.

Assim, a recomendação principal é declarar o catálogo/API como MVP pedagógico e apresentar o streaming de mídia como uma evolução arquitetural separada, que pode ser estudada por etapas. Sem essa distinção, o nome e a introdução prometem capacidades que os exercícios não entregam.

## 2. Avaliação pelos aspectos solicitados

### 2.1 Aspectos pedagógicos

**Potencial positivo**

- O domínio é familiar e permite relacionar requisitos, entidades, regras, endpoints e experiência do cliente.
- Os exemplos percorrem diversas competências: Django e DRF, ORM, relações 1:N e N:N, serialização, CRUD, filtros, autenticação, permissões, documentação OpenAPI, consumo por JavaScript e publicação.
- O diagrama de sequência de publicação oferece uma oportunidade de relacionar requisição HTTP, autenticação, validação, persistência e resposta.
- Regras como propriedade do conteúdo e da playlist podem apoiar exercícios de autorização e modelagem de casos de teste.

**Limitações didáticas**

- Falta uma sequência explícita de objetivos de aprendizagem, pré-requisitos, entregáveis e critérios de conclusão por etapa. A numeração dos arquivos não representa inteiramente a dependência entre os assuntos.
- O projeto introdutório inclui, de uma só vez, recomendações com aprendizado de máquina, ABR, CDN, transcodificação, OAuth, DRM, pagamentos, comentários, moderação, assinaturas, deployment e escala. Isso aumenta a carga cognitiva e mistura fundamentos de API com problemas de sistemas de mídia em produção.
- A complexidade cresce sem uma delimitação explícita entre obrigatório, extensão e conteúdo apenas contextual. Regras como premium, download, notificações e moderação não aparecem implementadas nos exemplos.
- Alguns exemplos podem ensinar práticas contraditórias com o restante do próprio material: permissões amplas, dependências incorretas, campos divergentes e regras de negócio descritas sem teste automatizado.
- Não há uma estratégia de validação transversal, como testes de modelo, serializer, API, autorização, integração e migração, nem uma definição clara do que deve ser demonstrado ao final.
- A repetição de conceitos em diferentes arquivos sem referência a uma fonte canônica dificulta a manutenção e pode fazer o estudante tratar versões incompatíveis como alternativas equivalentes.

**Recomendação pedagógica:** estruturar cada etapa em torno de um resultado verificável — modelo e migração, endpoint e contrato, regra de autorização, teste, documentação — e usar extensões opcionais somente após o fluxo essencial estar funcional.

### 2.2 Aspectos evolutivos

O domínio permite uma evolução didática natural, desde que o projeto seja dividido por capacidades e que cada incremento preserve as decisões anteriores:

1. **Fundação:** definir vocabulário e escopo; criar projeto, app, ambiente, modelo inicial e migrações.
2. **Catálogo:** implementar cadastro e leitura de conteúdo com validação, estados de publicação e testes.
3. **Propriedade e acesso:** estabelecer quem pode criar, listar, consultar, atualizar e excluir cada recurso; proteger dados privados por objeto e por queryset.
4. **Organização:** acrescentar playlists e a relação N:N. Se for necessário ordenar conteúdo ou guardar a data de inclusão, substituir a relação implícita por uma entidade intermediária explícita.
5. **Descoberta:** adicionar filtros, busca, paginação e contrato OpenAPI; testar a combinação de filtros e os limites de consulta.
6. **Cliente Web:** consumir a API com estados de carregamento, erro e autenticação, sem confiar em identificadores de usuário enviados pelo navegador.
7. **Operação:** preparar configuração por ambiente, banco persistente, migrações, armazenamento seguro de segredos, deploy e observabilidade básica.
8. **Evolução de mídia:** estudar separadamente upload/ingestão, armazenamento de objetos, transcodificação, HLS/DASH, CDN e autorização de acesso à mídia.
9. **Extensões de produto:** avaliar comentários, curtidas, assinaturas, recomendações e moderação como módulos independentes, cada um com requisitos, modelo, riscos e testes próprios.

Essa progressão evita colocar serviços de produção — por exemplo, CDN, DRM e recomendação — antes de a turma compreender o contrato da API e as regras de propriedade. Também torna possível avaliar cada incremento sem pressupor que todos os grupos implementem uma plataforma comercial completa.

### 2.3 Complexidade

| Tema | Complexidade didática | Importância técnica | Observação |
|---|---|---|---|
| CRUD, serializers e rotas REST | Baixa a média | Alta | Núcleo adequado para o primeiro incremento; precisa de validação e testes. |
| Modelagem de usuário e conteúdo | Média | Alta | Exige consistência entre campos, relações, regras e migrações. |
| Regras de negócio e integridade | Média | Alta | Regras devem ser verificadas na API e protegidas por constraints quando aplicável. |
| Relação N:N e playlist | Média | Alta | Torna-se mais complexa com ordem, duplicidade, visibilidade e permissões. |
| Autenticação e autorização | Média a alta | Muito alta | Autenticar identidade não basta; é necessário limitar ações e dados por propriedade e perfil. |
| Busca, filtros e paginação | Média | Alta | Devem ter entradas validadas, limites e comportamento documentado. |
| Frontend integrado e CORS | Média | Média a alta | Útil após o contrato da API estar estável; envolve origem, credenciais e tratamento de erros. |
| Deploy e persistência | Alta | Muito alta | Exige configuração segura, banco persistente, migrações, logs e tratamento de arquivos estáticos. |
| Upload, processamento e streaming real | Muito alta | Muito alta | Envolve arquivos grandes, armazenamento, filas, transcodificação, entrega e custos. |
| Assinaturas, pagamentos, DRM e recomendações | Muito alta | Alta, mas fora do núcleo didático | São módulos independentes, sujeitos a integração externa, requisitos de negócio e conformidade. |

O projeto completo de streaming é de alta ou muito alta complexidade. O recorte de catálogo/API é adequado a uma sequência de disciplinas ou projeto incremental, mas não deve herdar automaticamente todos os requisitos de uma plataforma comercial.

### 2.4 Importância técnica

As competências de maior valor formativo neste roteiro são:

1. **Integridade e modelagem:** chaves estrangeiras, unicidade, cardinalidades, estados e comportamento de exclusão.
2. **Contratos HTTP:** semântica de métodos e códigos de resposta, validação consistente e documentação OpenAPI alinhada à implementação.
3. **Autenticação e autorização:** separar identificação do usuário de autorização por recurso; filtrar resultados privados e impedir alterações por usuários que não são proprietários.
4. **Proteção de dados e configuração:** não expor segredos, restringir origens e hosts, usar HTTPS em produção e evitar confiar em dados de identidade enviados pelo cliente.
5. **Qualidade e testes:** cobrir regras de negócio, permissões e fluxos de erro automatizadamente.
6. **Operação confiável:** banco e armazenamento persistentes, migrações reproduzíveis, logs e instruções de deploy.
7. **Arquitetura de mídia:** importante para streaming real, mas distinta do CRUD da API; requer decisões próprias de armazenamento, transcodificação e distribuição.

## 3. Coerência e problemas técnicos observados

Os exemplos devem ser harmonizados antes de serem usados como uma sequência executável. Os pontos abaixo são inconsistências observáveis entre os roteiros, não uma auditoria de uma aplicação implantada.

### 3.1 Escopo e nomenclatura

- [00_Projeto_Streaming.md](./00_Projeto_Streaming.md) apresenta uma plataforma completa com ABR, CDN, transcodificação, recomendações, pagamentos, DRM e múltiplos clientes. Os exemplos posteriores concentram-se em CRUD de metadados e URLs, sem implementar o transporte ou o processamento de áudio/vídeo.
- A lista de arquivos tem ordenação irregular: `04_Diagrama_Sequencia.md` vem antes do exercício de playlist; o arquivo `1117_Carga de Dados.md` tem nome e título interno que não correspondem; há conceitos de relacionamentos novamente em `11_Associações.md`.
- [01_Regras_Negocio.md](./01_Regras_Negocio.md) contém marcadores de conflito de merge (`<<<<<<<`, `=======`, `>>>>>>>`) e repete regras em seções resumidas e detalhadas. Isso prejudica leitura e reduz a confiabilidade do material como fonte de requisitos.
- [14_Regras_Negocio.md](./14_Regras_Negocio.md) repete validações já descritas e introduz variações de nomes (`creator` e `owner`) sem estabelecer qual versão prevalece.

### 3.2 Modelos e regras de negócio

- [02_Modelagem.md](./02_Modelagem.md) propõe muitas entidades desde o início — comentários, curtidas, assinatura e histórico — sem priorização nem cobertura equivalente nos exercícios de implementação.
- A modelagem combina um campo `role` no usuário com uma tabela `Role`, e contadores `likes`/`views` com entidades de curtida/histórico. É necessário decidir se os contadores são derivados, mantidos como agregados ou removidos do escopo inicial.
- O Django já oferece um modelo de usuário e mecanismos de hash de senha. A atividade deve explicitar quando estender ou substituir o modelo padrão, evitando ensinar a armazenar diretamente senha ou hash em um modelo paralelo sem necessidade.
- A unicidade de título por criador aparece como regra, mas deve ser consistente no modelo, serializer e banco. Validação somente na aplicação não substitui uma constraint de unicidade no banco quando a regra precisa resistir a operações concorrentes.
- Regras como miniatura obrigatória, privacidade, duplicidade em playlist, número máximo de playlists, moderação, downloads e premium são apresentadas sem critérios de aceitação ou sem exemplo de implementação/teste correspondente.
- Há escolhas de exclusão potencialmente consequentes — por exemplo, apagar usuário e conteúdos associados — que deveriam ser discutidas e justificadas, não tratadas apenas como configuração técnica.

### 3.3 API e controle de acesso

- [03_Rest.md](./03_Rest.md) expõe um `ModelViewSet` com `IsAuthenticatedOrReadOnly`. Essa permissão permite que usuários autenticados cheguem às ações de alteração; não demonstra, por si só, autorização de que apenas o criador possa modificar ou excluir seu conteúdo.
- A consulta apresentada usa um queryset geral e serialização de todos os campos. Sem regras de visibilidade e filtragem, conteúdo privado ou campos internos podem ser expostos; os exemplos devem ensinar permissões por objeto e querysets limitados ao usuário/contexto.
- O campo que identifica o criador é chamado `creator` em alguns exemplos e `owner` em outros. O [14_Regras_Negocio.md](./14_Regras_Negocio.md) filtra por `owner`, apesar de o modelo REST inicial definir `creator`.
- [05_Playlist_NxN.md](./05_Playlist_NxN.md) filtra playlists por usuário, mas não apresenta uma política de permissão completa para todos os métodos. A adição de conteúdos também precisa validar visibilidade e acesso, e documentar o que acontece com conteúdo removido ou tornado privado.
- O serializer de playlist usa uma relação N:N sem posição. Isso não implementa a regra de reordenar itens; para ordenar e registrar atributos do vínculo, o exercício deve introduzir um modelo intermediário, com constraints e operações explícitas.
- [13_Filtros.md](./13_Filtros.md) ignora silenciosamente um tipo inválido de conteúdo, podendo aparentar que o filtro foi aplicado. É preferível definir e documentar uma resposta clara para parâmetros inválidos, além de limitar consultas e adicionar paginação quando apropriado.

### 3.4 Autenticação, CORS e cliente Web

- [12_Autentication.md](./12_Autentication.md) instrui instalar `django-rest-authtoken`; para a autenticação Token padrão do DRF, o app utilizado é `rest_framework.authtoken`, disponibilizado pelo Django REST Framework. A dependência e o procedimento devem ser corrigidos e testados.
- O exemplo de cabeçalho alterna entre `Token` e `token`; os exemplos devem usar consistentemente o esquema esperado pelo backend. A recomendação de token no JavaScript precisa discutir armazenamento, exposição e adequação do mecanismo ao tipo de cliente.
- [08_CorsOrigin.md](./08_CorsOrigin.md) mostra permitir todas as origens e permitir credenciais na mesma seção sem advertência suficiente. CORS deve ser restrito às origens necessárias, principalmente em produção, e não substitui autenticação ou autorização.
- [09_Consume_Web.md](./09_Consume_Web.md) permite preencher `creator` no formulário apesar de o backend dizer que usa o usuário autenticado. A identidade do proprietário deve ser definida no servidor.
- O cliente concatena dados da API em `innerHTML`. Conteúdo textual deve ser inserido de forma segura, sem interpretar valores não confiáveis como marcação HTML.
- O exemplo de POST não envia credenciais, apesar de a API exigir autenticação para criação. Também não define fluxo de login, estado de sessão/token ou mensagens acessíveis para erros; o exemplo de GET assume sucesso antes de verificar o status HTTP.

### 3.5 Carga de dados, documentação e deploy

- [1117_Carga de Dados.md](./1117_Carga%20de%20Dados.md) alterna entre apps e caminhos (`content`, `content_app`) e grava `owner`, enquanto o primeiro modelo define `creator`. A importação não é idempotente e captura exceções amplas, o que pode ocultar falhas e deixar carga parcial. Deve haver validação explícita, transação e relatório de erros por registro.
- [07_Swagger.md](./07_Swagger.md) usa `app.urls` no exemplo, ao passo que os demais materiais usam `content_app`; além disso, schema, serializer e permissões precisam refletir o contrato real, e não apenas gerar uma interface navegável.
- [10_Admin.md](./10_Admin.md) contém exemplos úteis de customização, mas permissões do Django Admin não substituem as permissões da API. Campos, nomes de modelo e regras devem corresponder ao projeto canônico.
- [15_Deploy.md](./15_Deploy.md) reconhece que SQLite em armazenamento efêmero pode perder dados, mas o roteiro deve orientar de forma consistente para banco persistente no ambiente de publicação. `ALLOWED_HOSTS = ['*']` é inadequado como recomendação de produção; usar hosts explícitos e configurações por ambiente. Segredos não devem ser gravados no repositório.
- O procedimento de deploy deixa migrações e coleta de estáticos dependentes de comandos manuais no shell do provedor. Deve ser definida uma sequência reproduzível e segura para build, migrações, configuração de banco, arquivos estáticos e verificação de saúde.

## 4. Recomendações priorizadas

### Prioridade 1 — tornar o roteiro executável e seguro

1. Definir o escopo do MVP como catálogo/API e declarar explicitamente o que não é streaming de mídia.
2. Escolher nomes canônicos para os apps e campos (`creator` ou `owner`), bem como uma única versão de cada modelo e regra.
3. Remover conflitos de merge, duplicações e exemplos que não correspondem ao código apresentado.
4. Corrigir autenticação e autorização: proprietário derivado da identidade autenticada no servidor, filtragem de conteúdo privado e testes para leitura, criação, edição e exclusão.
5. Garantir constraints de integridade no banco e cobrir as regras centrais com testes automatizados.
6. Restringir CORS e hosts de produção; revisar o uso de tokens e a inserção de dados no cliente Web.

### Prioridade 2 — melhorar aprendizagem e manutenção

1. Reorganizar os arquivos como módulos sequenciais, com objetivos, pré-requisitos, entregável, critérios de aceite e testes de cada etapa.
2. Manter uma fonte única para requisitos/regras e referenciar essa fonte nos roteiros de implementação.
3. Criar uma aplicação-base coerente (modelo, serializer, viewset, URLs, admin e testes) usada por todos os capítulos, evitando nomes divergentes entre snippets.
4. Separar conteúdo obrigatório de extensões e introduzir playlists, comentários, curtidas e filtros após o CRUD e as permissões estarem validados.
5. Adicionar exemplos de testes de sucesso, validação, autenticação, autorização, privacidade e integridade.
6. Definir critérios para dados de demonstração e cargas repetíveis, sem ocultar falhas de importação.

### Prioridade 3 — evoluir para streaming real

Se o objetivo curricular for ensinar transmissão de áudio/vídeo — e não apenas a API de catálogo —, planejar um módulo avançado separado para:

- armazenamento e ciclo de vida dos arquivos;
- processamento assíncrono e transcodificação;
- HLS ou DASH e geração de variantes;
- entrega por CDN e controle de acesso aos recursos;
- observabilidade, custos, limites e tratamento de falhas de processamento;
- direitos de uso e proteção apropriada ao escopo.

DRM, pagamentos, recomendações com aprendizado de máquina e distribuição comercial devem ser apresentados como estudos de arquitetura ou extensões, não como pré-requisitos implícitos do exercício básico.

## 5. Proposta de organização didática

| Etapa | Entrega verificável | Critério de conclusão |
|---|---|---|
| 1. Escopo e domínio | Requisitos priorizados, atores, regras e modelo inicial | Cada requisito essencial aponta para uma regra e entidade; funcionalidades de extensão estão separadas. |
| 2. Persistência | Modelos, constraints, migrações e dados de demonstração | Migrações reproduzíveis; integridade e unicidade verificadas por testes. |
| 3. API de catálogo | Endpoints CRUD, serializers e respostas de erro | Contrato consistente, validação documentada e testes de API. |
| 4. Autorização | Propriedade, visibilidade e perfis | Usuários só veem e alteram os recursos permitidos; testes cobrem acesso anônimo e de terceiros. |
| 5. Playlists | Relação N:N e operações para incluir, remover e ordenar | Duplicidade, ordem, privacidade e propriedade têm comportamento definido e testado. |
| 6. Descoberta e documentação | Filtros, busca, paginação e OpenAPI | Parâmetros inválidos têm resposta definida; documentação corresponde à API. |
| 7. Cliente Web | Listagem e operações autenticadas | Estados de erro/carregamento tratados, identidade não confiada ao cliente e renderização segura. |
| 8. Deploy | Aplicação publicada com banco persistente | Configuração por ambiente, segredos fora do código, migrações repetíveis e instruções reproduzíveis. |
| 9. Extensão de mídia | Protótipo de ingestão e entrega de mídia | Arquitetura e limites documentados; processamento e entrega separados da API de metadados. |

## 6. Conclusão

O roteiro tem valor pedagógico e cobre competências tecnicamente relevantes, mas precisa de consolidação antes de ser utilizado como caminho linear de implementação. Sua principal fragilidade é a distância entre a promessa de uma plataforma de streaming completa e os exemplos reais de CRUD para metadados, somada a divergências de modelo, propriedade, autenticação e permissões.

Com um MVP explícito, exemplos harmonizados, sequência gradual e testes de regras e autorização, o material pode formar uma trilha útil de desenvolvimento de API. A arquitetura de streaming propriamente dita deve ser tratada como evolução avançada e independente, para que a complexidade seja introduzida de forma consciente e compatível com os objetivos pedagógicos.

## 7. Materiais analisados

- [00_Projeto_Streaming.md](./00_Projeto_Streaming.md)
- [01_Regras_Negocio.md](./01_Regras_Negocio.md)
- [02_Modelagem.md](./02_Modelagem.md)
- [03_Rest.md](./03_Rest.md)
- [04_Diagrama_Sequencia.md](./04_Diagrama_Sequencia.md)
- [05_Playlist_NxN.md](./05_Playlist_NxN.md)
- [06_Shell.md](./06_Shell.md)
- [07_Swagger.md](./07_Swagger.md)
- [08_CorsOrigin.md](./08_CorsOrigin.md)
- [09_Consume_Web.md](./09_Consume_Web.md)
- [10_Admin.md](./10_Admin.md)
- [1117_Carga de Dados.md](./1117_Carga%20de%20Dados.md)
- [11_Associações.md](./11_Associa%C3%A7%C3%B5es.md)
- [12_Autentication.md](./12_Autentication.md)
- [13_Filtros.md](./13_Filtros.md)
- [14_Regras_Negocio.md](./14_Regras_Negocio.md)
- [15_Deploy.md](./15_Deploy.md)
