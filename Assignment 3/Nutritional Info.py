#Mustafa Eski
#ID: 2046388
#Reference: https://gist.github.com/Ih8Hondas/d2637c3a88fe16734398b7946f97dc86
class FoodItem: #Creating the class

    def __init__(info, name=None, fat=0.0, carbs=0.0, protein=0.0): #Constructor
        info.name = name
        info.fat = fat
        info.carbs = carbs
        info.protein = protein

    def get_calories(info, num_servings):
        calories = ((info.fat * 9) + (info.carbs * 4) + (info.protein * 4)) * num_servings
        return calories

    def print_info(info): #printing the information
        print('Nutritional information per serving of {}:'.format(info.name))
        print('   Fat: {:.2f} g'.format(info.fat))
        print('   Carbohydrates: {:.2f} g'.format(info.carbs))
        print('   Protein: {:.2f} g'.format(info.protein))


if __name__ == '__main__': #function printing the none and the food item 
    food_item1 = FoodItem()

    item_name = input()
    amount_fat = float(input())
    amount_carbs = float(input())
    amount_protein = float(input())

    food_item2 = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
    num_servings = float(input())
    food_item1.print_info()
    print("Number of calories for {:.2f} serving(s): {:.2f}\n".format(num_servings, food_item1.get_calories(num_servings)))
    food_item2.print_info()
    print("Number of calories for {:.2f} serving(s): {:.2f}".format(num_servings, food_item2.get_calories(num_servings)))

