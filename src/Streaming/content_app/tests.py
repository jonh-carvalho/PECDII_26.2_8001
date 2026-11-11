from django.test import TestCase
from django.contrib.auth.models import User
from .models import Content, Comment, Like, Playlist


class ContentModelTestCase(TestCase):
    """Testes unitários simples para o modelo Content"""

    def setUp(self):
        """Preparar dados para cada teste"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_create_content_successfully(self):
        """
        TESTE 1: Criar um conteúdo com dados válidos
        - Deve criar o objeto no banco de dados
        - Deve ter a contagem de views padrão como 0
        """
        content = Content.objects.create(
            title='Tutorial Python Básico',
            description='Aprenda Python do zero',
            file_url='https://example.com/video.mp4',
            content_type='video',
            creator=self.user
        )

        # Verificações
        self.assertEqual(content.title, 'Tutorial Python Básico')
        self.assertEqual(content.views, 0)
        self.assertEqual(content.likes, 0)
        self.assertTrue(content.is_public)
        self.assertEqual(content.status, 'published')
        self.assertEqual(content.creator.username, 'testuser')

    def test_content_string_representation(self):
        """
        TESTE 2: Verificar representação em string do conteúdo
        - Deve retornar o título como string representation
        """
        content = Content.objects.create(
            title='Django REST Framework',
            description='Build APIs with Django',
            file_url='https://example.com/tutorial.mp4',
            content_type='video',
            creator=self.user
        )

        # Verificação
        self.assertEqual(str(content), 'Django REST Framework')

    def test_content_with_private_status(self):
        """
        TESTE 3: Criar conteúdo privado
        - Deve permitir que conteúdo seja criado como privado (is_public=False)
        - Deve manter o status correto
        """
        content = Content.objects.create(
            title='Conteúdo Privado',
            description='Apenas para mim',
            file_url='https://example.com/private.mp4',
            content_type='audio',
            is_public=False,
            status='draft',
            creator=self.user
        )

        # Verificações
        self.assertFalse(content.is_public)
        self.assertEqual(content.status, 'draft')
        self.assertEqual(content.content_type, 'audio')
