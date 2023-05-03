from .test_recipes_base import RecipesTestBase


class RecipeModelTest(RecipesTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_the_test(self):
        recipe = self.recipe
        ...
