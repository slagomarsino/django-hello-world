from rest_framework import serializers

from recipe.models import Ingredient, Recipe

from .ingredient import IngredientSerializer


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes objects"""
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all(),
    )

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'ingredients', 'time_minutes', 'price',
                  'link', 'image')
        read_only_fields = ('id', )


class RecipeDetailSerializer(RecipeSerializer):
    """Serialize a recipe detail"""
    ingredients = IngredientSerializer(many=True, read_only=True)
    ingredients_count = serializers.SerializerMethodField()

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ('ingredients_count', )

    def get_ingredients_count(self, obj):
        return obj.ingredients.count()


class RecipeImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to recipe"""
    class Meta:
        model = Recipe
        fields = ('id', 'image')
        read_only_fields = ('id', )
