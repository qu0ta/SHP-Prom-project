from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import News


class TestHomeView(TestCase):

    def test_get_request(self):
        # Тестируем GET-запрос
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_post_request_without_news_search(self):
        # Тестируем POST-запрос без параметра news_search
        response = self.client.post(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_post_request_with_news_search(self):
        # Тестируем POST-запрос с параметром news_search
        data = {'news_search': 'test'}
        response = self.client.post(reverse('home'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/all_news.html')

    def test_authenticated_user(self):
        # Тестируем аутентифицированного пользователя
        user = User.objects.create_user('testuser', 'testuser@example.com', 'testpassword')
        self.client.force_login(user)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')
        self.assertEqual(response.context['username'], 'testuser')

    def test_anonymous_user(self):
        # Тестируем анонимного пользователя
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')
        self.assertEqual(response.context['username'], 'AnonymousUser')

    def test_context(self):
        # Тестируем контекст
        response = self.client.get(reverse('home'))
        self.assertEqual(response.context['page_title'], 'Главная')
        self.assertIn('news', response.context)

    def test_check_auth_to_context(self):
        # Тестируем функцию check_auth_to_context
        user = User.objects.create_user('testuser', 'testuser@example.com', 'testpassword')
        self.client.force_login(user)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.context['username'], 'testuser')
        self.client.logout()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.context['username'], 'AnonymousUser')


class TestAboutView(TestCase):
    def test_get_request(self):
        # Тестируем GET-запрос
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/about.html')

    def test_post_request_without_news_search(self):
        # Тестируем POST-запрос без параметра news_search
        response = self.client.post(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/about.html')

    def test_post_request_with_news_search(self):
        # Тестируем POST-запрос с параметром news_search
        data = {'news_search': 'test'}
        response = self.client.post(reverse('about'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/all_news.html')

    def test_context(self):
        # Тестируем контекст
        response = self.client.get(reverse('about'))
        self.assertEqual(response.context['page_title'], 'О нас')


class TestAllNewsView(TestCase):
    def test_get_request(self):
        # Авторизуем пользователя
        user = User.objects.create_user('testuaaser', 'testuszer@example.com', 'testpzassword')
        self.client.force_login(user)

        # Тестируем GET-запрос
        response = self.client.get(reverse('all_news'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/all_news.html')

    def test_post_request_without_news_search(self):
        # Авторизуем пользователя
        user = User.objects.create_user('tes123tuser', 'testus321er@example.com', 'testp123assword')
        self.client.force_login(user)

        # Тестируем POST-запрос без параметра news_search
        response = self.client.post(reverse('all_news'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/all_news.html')

    def test_post_request_with_news_search(self):
        # Авторизуем пользователя
        user = User.objects.create_user('testasdasdasdasduser', 'testusaer@example.com', '1233estpassword')
        self.client.force_login(user)

        # Тестируем POST-запрос с параметром news_search
        data = {'news_search': 'test'}
        response = self.client.post(reverse('all_news'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/all_news.html')

    def test_context(self):
        # Авторизуем пользователя
        user = User.objects.create_user('testuasdser', 'testu123ser@example.com', 'testpasasdsword')
        self.client.force_login(user)

        # Тестируем контекст
        response = self.client.get(reverse('all_news'))
        self.assertEqual(response.context['page_title'], 'Все новости')
        self.assertIn('news', response.context)


class TestOneNewsView(TestCase):
    def test_get_request(self):
        # Авторизуем пользователя
        user = User.objects.create_user('tes1tuser', 'testusasder@example.com', 'testpassw3112ord')
        self.client.force_login(user)

        # Тестируем GET-запрос
        news_id = 1
        response = self.client.get(reverse('one_news', args=[news_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/one_news.html')

    def test_post_request_with_news_search(self):
        # Авторизуем пользователя
        user = User.objects.create_user('testuseaqwe123r', 'testu123ser@example.com', 'testp12312assword')
        self.client.force_login(user)

        # Тестируем POST-запрос с параметром news_search
        news_id = 1
        data = {'news_search': 'test'}
        response = self.client.post(reverse('one_news', args=[news_id]), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/all_news.html')

    def test_post_request_with_comment(self):
        # Авторизуем пользователя
        user = User.objects.create_user('teasdstuser', 'testusddser@example.com', 'testpasddaassword')
        self.client.force_login(user)

        # Тестируем POST-запрос с комментарием
        news_id = 1
        data = {'text': 'test comment'}
        response = self.client.post(reverse('one_news', args=[news_id]), data=data)
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        # Авторизуем пользователя
        user = User.objects.create_user('teszzzxczxcxzctuser', 'tesccczxcztuser@example.com', 'testzxpassword')
        self.client.force_login(user)

        # Тестируем контекст
        news_id = 1
        response = self.client.get(reverse('one_news', args=[news_id]))
        self.assertIn(response.context['page_title'], ["Заголовок новости", 'Такой новости нет'])
        self.assertIn('form', response.context)
        self.assertIn('comments', response.context)
        self.assertIn('user', response.context)


class TestRegistrationView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = '/registration/'

    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/registration.html')

    def test_post_request_with_valid_data(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'birthdate': '1990-01-01',
            'email': 'test@example.com',

            'fullname': 'Test User',
            'about': 'Test about'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_post_request_with_invalid_data(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'invalid_email',
            'birthdate': '1990-01-01',
            'fullname': 'Test User',
            'about': 'Test about'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/registration.html')
    def test_post_request_with_news_search(self):
        data = {
            'news_search': 'test'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/all_news.html')

    def test_post_request_with_news_search_and_valid_data(self):
        data = {
            'news_search': 'test',
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com',
            'birthdate': '1990-01-01',
            'fullname': 'Test User',
            'about': 'Test about'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/all_news.html')



class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = '/login/'
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/login.html')

    def test_post_request_with_empty_form(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/login.html')

    def test_post_request_with_invalid_credentials(self):
        data = {'username': 'wronguser', 'password': 'wrongpassword'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/login.html')
    def test_post_request_with_valid_credentials(self):
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_post_request_with_news_search(self):
        data = {'news_search': 'test'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/all_news.html')

    def test_post_request_with_news_search_and_valid_credentials(self):
        data = {'news_search': 'test', 'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/all_news.html')


class ProfileViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = '/profile/'
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_get_request(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/profile.html')

    def test_get_request_without_login(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_post_request_with_news_search(self):
        self.client.force_login(self.user)
        data = {'news_search': 'test'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/all_news.html')

    def test_post_request_without_news_search(self):
        self.client.force_login(self.user)
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/profile.html')

    def test_context(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.context['page_title'], 'Профиль')


class LogoutViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = '/logout/'
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_logout(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertFalse(self.client.session.get('_auth_user_id'))

    def test_logout_without_login(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_logout_post_request(self):
        self.client.force_login(self.user)
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertFalse(self.client.session.get('_auth_user_id'))