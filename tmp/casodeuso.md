---
title: Caso de Uso - Gestão de Materiais
---

# Caso de Uso Descritivo

## 1. Identificação

- **Sistema:** Sistema de Gestão de Materiais
- **Caso de uso principal:** UC01 - Solicitar material
- **Objetivo:** Permitir que um funcionário solicite um material e que o sistema encaminhe a solicitação para retirada do estoque ou para compra.
- **Atores principais:** Funcionário, Responsável, Compras Centrais e Almoxarifado.
- **Atores secundários:** Fornecedor.

## 2. Pré-condições

- O funcionário identificou a necessidade de um material.
- O funcionário está autorizado a registrar solicitações.
- O sistema está disponível para registrar e acompanhar a solicitação.

## 3. Pós-condições

- O material foi retirado do estoque; ou
- Uma requisição de compra foi aprovada, transformada em pedido e enviada ao fornecedor; ou
- O pedido permanece em acompanhamento por atraso na entrega.

## 4. Fluxo principal

1. O funcionário solicita um material ao sistema.
2. O sistema verifica a disponibilidade do material em estoque.
3. Se houver material disponível, o responsável aprova a alocação do estoque.
4. O funcionário retira o material do estoque.
5. O sistema registra o atendimento da solicitação.

## 5. Fluxo alternativo: material indisponível

1. O sistema informa que o material não está disponível em estoque.
2. O funcionário cria uma requisição de compra.
3. O responsável aprova a requisição de compra.
4. Compras Centrais confere a requisição.
5. O sistema gera um pedido de compra a partir da requisição.
6. O responsável assina o pedido de compra.
7. Compras Centrais envia o pedido ao fornecedor.
8. O almoxarifado acompanha a entrega do material.
9. O fornecedor entrega o material.
10. O almoxarifado registra o recebimento e encerra o acompanhamento.

## 6. Fluxo alternativo: atraso na entrega

1. O almoxarifado aguarda a entrega do pedido.
2. Caso a entrega não ocorra em um mês, o sistema sinaliza o atraso.
3. Compras Centrais contata o fornecedor.
4. O almoxarifado continua aguardando a entrega.
5. Quando o fornecedor entregar o material, o almoxarifado registra o recebimento.

## 7. Regras de negócio

- A retirada do estoque somente pode ocorrer após a aprovação da alocação pelo responsável.
- Uma requisição de compra somente pode gerar um pedido após a aprovação do responsável e a conferência por Compras Centrais.
- O pedido de compra deve ser assinado antes de ser enviado ao fornecedor.
- O atraso deve ser tratado quando não houver entrega no prazo de um mês.

## 8. Casos de uso relacionados

### UC02 - Verificar disponibilidade em estoque

- **Ator:** Sistema.
- **Objetivo:** Determinar se a quantidade solicitada está disponível no estoque.
- **Pré-condição:** Existe uma solicitação de material registrada.
- **Fluxo principal:** O sistema consulta o estoque e informa se há material disponível.
- **Pós-condição:** A solicitação segue para retirada do estoque ou para compra.

### UC03 - Aprovar alocação do estoque

- **Ator:** Responsável.
- **Objetivo:** Autorizar a separação do material disponível.
- **Pré-condição:** O sistema confirmou que há material em estoque.
- **Fluxo principal:** O responsável analisa a solicitação e aprova a alocação.
- **Pós-condição:** O material fica autorizado para retirada.

### UC04 - Retirar material do estoque

- **Ator:** Funcionário.
- **Objetivo:** Obter o material aprovado.
- **Pré-condição:** A alocação do estoque foi aprovada.
- **Fluxo principal:** O funcionário retira o material e o sistema registra a entrega.
- **Pós-condição:** A solicitação é atendida e o estoque é atualizado.

### UC05 - Criar requisição de compra

- **Ator:** Funcionário.
- **Objetivo:** Solicitar a compra de um material indisponível.
- **Pré-condição:** O sistema confirmou que não há material em estoque.
- **Fluxo principal:** O funcionário informa o material, a quantidade e a justificativa; o sistema registra a requisição.
- **Pós-condição:** A requisição fica disponível para aprovação.

### UC06 - Aprovar requisição de compra

- **Ator:** Responsável.
- **Objetivo:** Autorizar o prosseguimento da compra.
- **Pré-condição:** Existe uma requisição registrada.
- **Fluxo principal:** O responsável analisa a requisição e aprova sua continuidade.
- **Pós-condição:** A requisição é encaminhada para Compras Centrais.

### UC07 - Conferir requisição de compra

- **Ator:** Compras Centrais.
- **Objetivo:** Verificar se a requisição contém informações suficientes para gerar um pedido.
- **Pré-condição:** A requisição foi aprovada pelo responsável.
- **Fluxo principal:** Compras Centrais confere os dados e valida a requisição.
- **Pós-condição:** A requisição validada pode gerar um pedido de compra.

### UC08 - Gerar pedido de compra

- **Ator:** Sistema.
- **Objetivo:** Criar um pedido de compra com base na requisição conferida.
- **Pré-condição:** A requisição foi aprovada e conferida.
- **Fluxo principal:** O sistema cria o pedido e associa a ele os dados da requisição.
- **Pós-condição:** O pedido fica disponível para assinatura.

### UC09 - Assinar pedido de compra

- **Ator:** Responsável.
- **Objetivo:** Autorizar formalmente o envio do pedido ao fornecedor.
- **Pré-condição:** Existe um pedido gerado pelo sistema.
- **Fluxo principal:** O responsável revisa e assina o pedido.
- **Pós-condição:** O pedido fica autorizado para envio.

### UC10 - Enviar pedido ao fornecedor

- **Ator principal:** Compras Centrais.
- **Ator secundário:** Fornecedor.
- **Objetivo:** Encaminhar o pedido de compra ao fornecedor.
- **Pré-condição:** O pedido foi assinado.
- **Fluxo principal:** Compras Centrais envia o pedido e o fornecedor confirma o recebimento.
- **Pós-condição:** O pedido fica aguardando entrega.

### UC11 - Acompanhar entrega

- **Ator:** Almoxarifado.
- **Objetivo:** Monitorar o recebimento do material comprado.
- **Pré-condição:** O pedido foi enviado ao fornecedor.
- **Fluxo principal:** O almoxarifado aguarda a entrega e registra o recebimento do material.
- **Fluxo alternativo:** Se não houver entrega em um mês, o caso UC12 é acionado.
- **Pós-condição:** O material é recebido ou o pedido é marcado como atrasado.

### UC12 - Contatar fornecedor sobre atraso

- **Ator principal:** Compras Centrais.
- **Ator secundário:** Fornecedor.
- **Objetivo:** Solicitar uma posição sobre um pedido que não foi entregue no prazo.
- **Pré-condição:** O pedido está em acompanhamento e não foi entregue em um mês.
- **Fluxo principal:** Compras Centrais contata o fornecedor, solicita a previsão de entrega e atualiza o acompanhamento.
- **Pós-condição:** O pedido continua aguardando a entrega com uma nova previsão ou orientação registrada.

## 9. Matriz de rastreabilidade com o diagrama

| Relação no diagrama | Interpretação |
| --- | --- |
| UC01 `<<include>>` UC02 | Toda solicitação consulta a disponibilidade do estoque. |
| UC03 `<<extend>>` UC01 | A aprovação da alocação ocorre quando há material disponível. |
| UC04 `<<include>>` UC03 | A retirada depende da aprovação da alocação. |
| UC05 `<<extend>>` UC01 | A requisição de compra ocorre quando o material está indisponível. |
| UC06 `<<include>>` UC05 | A requisição precisa ser aprovada antes de continuar. |
| UC07 `<<include>>` UC06 | A requisição aprovada precisa ser conferida. |
| UC08 `<<include>>` UC07 | A conferência permite gerar o pedido de compra. |
| UC09 `<<include>>` UC08 | O pedido gerado precisa ser assinado. |
| UC10 `<<include>>` UC09 | O pedido assinado pode ser enviado ao fornecedor. |
| UC11 `<<include>>` UC10 | Todo pedido enviado precisa ser acompanhado até a entrega. |
| UC12 `<<extend>>` UC11 | O contato com o fornecedor ocorre somente em caso de atraso. |
