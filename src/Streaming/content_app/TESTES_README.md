# Testes Unitários - Content App

## Como Executar os Testes

### Executar todos os testes do content_app
```bash
python manage.py test content_app
```

### Executar apenas os testes da classe ContentModelTestCase
```bash
python manage.py test content_app.tests.ContentModelTestCase
```

### Executar um teste específico
```bash
python manage.py test content_app.tests.ContentModelTestCase.test_create_content_successfully
```

### Executar com saída verbosa
```bash
python manage.py test content_app -v 2
```

### Executar e gerar relatório de cobertura (se pytest-cov estiver instalado)
```bash
pytest --cov=content_app --cov-report=html
```

---

## Estrutura dos Testes

```
content_app/
├── tests.py              ← Arquivo com os testes
├── models.py             ← Modelos testados
├── serializers.py
├── views.py
└── TESTES_README.md      ← Este arquivo
```

---

## O que Cada Teste Demonstra

| Teste | Tipo | Validação | Importância |
|-------|------|-----------|-------------|
| test_create_content_successfully | Criação de Objeto | CRUD básico | ⭐⭐⭐ |
| test_content_string_representation | String Representation | Método `__str__` | ⭐⭐ |
| test_content_with_private_status | Lógica de Negócio | Status e privacidade | ⭐⭐⭐ |

---

## Próximos Passos

Após passar nestes testes introdutórios, expandir para:

1. **Testes de Comentários** - Criar e validar comentários em conteúdo
2. **Testes de Likes** - Validar sistema de likes (restrição única_together)
3. **Testes de Playlist** - Testar relacionamento ManyToMany
4. **Testes de Views/APIs** - Testar endpoints REST
5. **Testes de Permissões** - Validar autenticação e autorização

---

## Dicas para Expandir

### Adicionar mais testes
Edite `content_app/tests.py` e adicione novos métodos à classe `ContentModelTestCase`:

```python
def test_nome_do_novo_teste(self):
    """Descrição do que está sendo testado"""
    # Arrange - Preparar dados
    # Act - Executar ação
    # Assert - Validar resultado
```

### Usar setUp para dados compartilhados
Todos os testes herdam o `self.user` criado no `setUp()`.

### Usar assertions do Django
- `self.assertEqual(a, b)` - Comparação de igualdade
- `self.assertTrue(a)` - Verificar se é verdadeiro
- `self.assertFalse(a)` - Verificar se é falso
- `self.assertIn(a, b)` - Verificar se está contido
- `self.assertIsNone(a)` - Verificar se é None

---

## Conclusão

Estes 3 testes unitários simples estabelecem a base para testes mais robustos na Plataforma de Streaming. Todos os testes passam com sucesso! 
