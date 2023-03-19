from django.test import TestCase
from django.urls import resolve, reverse
from recipes import views
from recipes.models import Category, Recipe, User


class RecipesViewsTest(TestCase):
    def test_recipes_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipes_home_view_returns_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipes_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipes_home_template_show_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here',
            response.content.decode(response.charset)
        )

    def test_recipe_home_template_loads_recipes(self):
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com',
        )
        recipe = Recipe.objects.create(
            category=category,
            author=author,
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_step='Recipe Preparation Steps',
            preparation_step_is_html=False,
            is_published=True,
        )
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode(response.charset)
        response_context_recipes = response.context['recipes']

        self.assertIn('Recipe Title', content)
        self.assertIn('10 Minutos', content)
        self.assertIn('5 Porções', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipes_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 100})
        )
        self.assertIs(view.func, views.category)

    def test_recipes_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipes_recipe_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', args=(1,)))
        self.assertIs(view.func, views.recipe)

    def test_recipes_recipe_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)
