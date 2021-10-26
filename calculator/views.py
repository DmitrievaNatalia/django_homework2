from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def get_recipes(request, name):
    recipe = DATA.get(name)
    count_person = request.GET.get('servings', '1')
    for ingredient, amount in recipe.items():
        amount = amount * int(count_person)
        recipe.update({ingredient: amount})
    context = {
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)
