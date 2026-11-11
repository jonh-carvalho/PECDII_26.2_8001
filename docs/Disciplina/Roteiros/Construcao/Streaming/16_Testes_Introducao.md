# 16 - **Testes Introdutórios - Streaming Platform**

## Objetivo

Estabelecer uma base sólida de testes para a Plataforma de Streaming, cobrindo casos simples de testes unitários, de integração e de API, garantindo a qualidade e confiabilidade do código antes do deploy.

---

## 1. **Tipos de Testes a Implementar**

### 1.1 Testes Unitários
- **Propósito**: Testar funções e métodos isolados
- **Escopo**: Lógica de negócio (validações, transformações de dados, cálculos)
- **Exemplos**:
  - Validação de email de usuário
  - Cálculo de duração de vídeo
  - Geração de tokens de autenticação

### 1.2 Testes de Integração
- **Propósito**: Testar interação entre componentes
- **Escopo**: Models com banco de dados, views com models
- **Exemplos**:
  - Criar usuário e verificar persistência no BD
  - Adicionar conteúdo à playlist e validar associação

### 1.3 Testes de API (REST)
- **Propósito**: Testar endpoints HTTP
- **Escopo**: Requisições, respostas, status codes, validações
- **Exemplos**:
  - GET /api/videos/ (listar vídeos)
  - POST /api/users/ (criar usuário)
  - PUT /api/playlists/{id}/ (atualizar playlist)

---

## 2. **Configuração Inicial**

### 2.1 Instalar Dependências de Teste

```bash
# Ferramentas de teste
pip install pytest pytest-django pytest-cov

# Mocking e fixtures
pip install factory-boy faker

# Cliente HTTP para testes de API
pip install requests pytest-httpx
```

### 2.2 Configurar pytest.ini

Criar arquivo `pytest.ini` na raiz do projeto:

```ini
[pytest]
DJANGO_SETTINGS_MODULE = streaming_platform.settings
python_files = tests.py test_*.py *_tests.py
python_classes = Test*
python_functions = test_*
addopts = --cov=. --cov-report=html --cov-report=term-missing
testpaths = tests
```

### 2.3 Estrutura de Pastas para Testes

```
streaming_platform/
├── content_app/
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_models.py
│   │   ├── test_views.py
│   │   ├── test_api.py
│   │   └── factories.py
│   └── ...
└── tests/
    ├── __init__.py
    └── conftest.py  # Fixtures compartilhadas
```

---

## 3. **Roteiro de Testes por Etapas**

### 🔵 **Etapa 1: Testes Unitários (Models)**

**Objetivo**: Validar a lógica de modelos

**Casos de Teste Simples**:

```python
# tests/test_models.py
import pytest
from content_app.models import User, Video, Playlist

@pytest.mark.django_db
class TestUserModel:
    def test_create_user(self):
        """Criar um usuário com dados válidos"""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        assert user.username == 'testuser'
        assert user.is_active is True

    def test_user_string_representation(self):
        """Verificar representação em string do usuário"""
        user = User.objects.create_user(
            username='joao',
            email='joao@example.com'
        )
        assert str(user) == 'joao'

@pytest.mark.django_db
class TestVideoModel:
    def test_create_video(self):
        """Criar um vídeo com dados válidos"""
        user = User.objects.create_user(
            username='creator',
            email='creator@example.com'
        )
        video = Video.objects.create(
            title='Tutorial Python',
            description='Aprenda Python do zero',
            uploader=user,
            duration=3600
        )
        assert video.title == 'Tutorial Python'
        assert video.duration == 3600

    def test_video_publish_status(self):
        """Verificar status de publicação de vídeo"""
        user = User.objects.create_user(username='creator')
        video = Video.objects.create(
            title='Vídeo Privado',
            uploader=user,
            is_published=False
        )
        assert video.is_published is False
```

**Comando para executar**:
```bash
pytest content_app/tests/test_models.py -v
```

---

### 🟢 **Etapa 2: Testes de Integração (Views e BD)**

**Objetivo**: Validar fluxos que envolvem múltiplos componentes

**Casos de Teste**:

```python
# tests/test_views.py
import pytest
from django.test import Client
from content_app.models import User, Video

@pytest.mark.django_db
class TestVideoListView:
    def setup_method(self):
        """Preparar dados para cada teste"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='creator',
            email='creator@example.com',
            password='pass123'
        )

    def test_list_videos_empty(self):
        """Listar vídeos quando nenhum existe"""
        response = self.client.get('/api/videos/')
        assert response.status_code == 200
        data = response.json()
        assert len(data['results']) == 0

    def test_list_videos_with_content(self):
        """Listar vídeos após adicionar conteúdo"""
        # Criar vídeos
        for i in range(3):
            Video.objects.create(
                title=f'Vídeo {i+1}',
                uploader=self.user,
                is_published=True
            )
        
        response = self.client.get('/api/videos/')
        assert response.status_code == 200
        data = response.json()
        assert len(data['results']) == 3

@pytest.mark.django_db
class TestPlaylistInteraction:
    def test_add_video_to_playlist(self):
        """Adicionar um vídeo a uma playlist"""
        user = User.objects.create_user(username='user1')
        video = Video.objects.create(
            title='Video 1',
            uploader=user
        )
        playlist = Playlist.objects.create(
            title='Minha Playlist',
            owner=user
        )
        
        playlist.videos.add(video)
        
        assert playlist.videos.count() == 1
        assert video in playlist.videos.all()
```

**Comando para executar**:
```bash
pytest content_app/tests/test_views.py -v
```

---

### 🟡 **Etapa 3: Testes de API REST**

**Objetivo**: Validar endpoints HTTP

**Casos de Teste**:

```python
# tests/test_api.py
import pytest
from django.test import Client
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from content_app.models import Video

User = get_user_model()

@pytest.mark.django_db
class TestVideoAPI:
    def setup_method(self):
        """Preparar cliente API para cada teste"""
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='creator',
            email='creator@example.com',
            password='pass123'
        )

    def test_get_videos_list(self):
        """GET /api/videos/ - Listar todos os vídeos"""
        # Criar dados
        Video.objects.create(
            title='Python Basics',
            uploader=self.user
        )
        Video.objects.create(
            title='Django Advanced',
            uploader=self.user
        )
        
        # Testar
        response = self.client.get('/api/videos/')
        
        assert response.status_code == 200
        assert response.data['count'] == 2

    def test_create_video_authenticated(self):
        """POST /api/videos/ - Criar vídeo autenticado"""
        self.client.force_authenticate(user=self.user)
        
        payload = {
            'title': 'New Video',
            'description': 'Video description',
            'file': 'video.mp4'
        }
        
        response = self.client.post('/api/videos/', payload, format='json')
        
        assert response.status_code == 201
        assert response.data['title'] == 'New Video'

    def test_create_video_unauthenticated(self):
        """POST /api/videos/ - Criar vídeo sem autenticação (deve falhar)"""
        payload = {
            'title': 'New Video',
            'description': 'Video description'
        }
        
        response = self.client.post('/api/videos/', payload, format='json')
        
        assert response.status_code == 401

    def test_get_video_detail(self):
        """GET /api/videos/{id}/ - Obter detalhes de um vídeo"""
        video = Video.objects.create(
            title='Test Video',
            uploader=self.user
        )
        
        response = self.client.get(f'/api/videos/{video.id}/')
        
        assert response.status_code == 200
        assert response.data['title'] == 'Test Video'

    def test_update_video(self):
        """PUT /api/videos/{id}/ - Atualizar vídeo (permissão)"""
        video = Video.objects.create(
            title='Original Title',
            uploader=self.user
        )
        
        self.client.force_authenticate(user=self.user)
        
        payload = {'title': 'Updated Title'}
        response = self.client.patch(f'/api/videos/{video.id}/', payload, format='json')
        
        assert response.status_code == 200
        video.refresh_from_db()
        assert video.title == 'Updated Title'

    def test_delete_video(self):
        """DELETE /api/videos/{id}/ - Deletar vídeo"""
        video = Video.objects.create(
            title='To Delete',
            uploader=self.user
        )
        
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/api/videos/{video.id}/')
        
        assert response.status_code == 204
        assert Video.objects.filter(id=video.id).exists() is False
```

**Comando para executar**:
```bash
pytest content_app/tests/test_api.py -v
```

---

## 4. **Executando os Testes**

### 4.1 Executar todos os testes
```bash
pytest
```

### 4.2 Executar com cobertura de código
```bash
pytest --cov=content_app --cov-report=html
```

### 4.3 Executar teste específico
```bash
pytest content_app/tests/test_models.py::TestUserModel::test_create_user -v
```

### 4.4 Executar com saída detalhada
```bash
pytest -v -s
```

---

## 5. **Boas Práticas**

### ✅ **Sim**
- ✓ Um teste = uma responsabilidade
- ✓ Use `setup_method()` para dados iniciais
- ✓ Nomeie testes de forma descritiva: `test_should_do_something_when_condition`
- ✓ Use fixtures para dados compartilhados
- ✓ Teste casos de sucesso E de erro
- ✓ Mockeia dependências externas

### ❌ **Não**
- ✗ Não dependa de ordem de execução dos testes
- ✗ Não use dados do banco de dados de produção
- ✗ Não escreva testes muito longos (>20 linhas)
- ✗ Não teste detalhes de implementação

---

## 6. **Cobertura de Testes - Meta**

| Componente | Meta de Cobertura |
|---|---|
| Models | 90%+ |
| Views | 80%+ |
| Serializers | 85%+ |
| API Endpoints | 85%+ |
| Lógica de Negócio | 90%+ |

---

## 7. **Próximos Passos**

1. **✓ Etapa Atual**: Testes simples e introdutórios
2. **Próximo**: Testes de autenticação e permissões
3. **Depois**: Testes de performance e carga
4. **Final**: CI/CD integration (GitHub Actions)

---

## 8. **Referências Rápidas**

- [Pytest Documentation](https://docs.pytest.org/)
- [Django Testing](https://docs.djangoproject.com/en/stable/topics/testing/)
- [Django REST Framework Testing](https://www.django-rest-framework.org/api-guide/testing/)
- [Factory Boy](https://factoryboy.readthedocs.io/)

---

## Resumo

Este roteiro fornece uma base sólida para começar a testar a Plataforma de Streaming com:
- ✓ Estrutura de organização de testes
- ✓ Exemplos práticos de testes unitários
- ✓ Exemplos de testes de integração
- ✓ Exemplos completos de testes de API
- ✓ Comandos prontos para executar
- ✓ Boas práticas essenciais

**Próximo**: Implemente os testes, comece simples e expanda gradualmente a cobertura!
