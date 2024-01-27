def calculate_slices_of_pizzas(individuals):
    large_slices = 8
    medium_slices = 6
    regular_slices = 4
    small_slices = 1

    large_pizzas = individuals // large_slices
    medium_pizzas = (individuals % large_slices) // medium_slices
    regular_pizzas = ((individuals % large_slices) % medium_slices) // regular_slices
    small_pizzas = (((individuals % large_slices) % medium_slices) % regular_slices) // small_slices

    print("Number of individuals: ",individuals)
    print("Number of Large Pizzas: ",large_pizzas)
    print("Number of Medium Pizzas: ",medium_pizzas)
    print("Number of Regular Pizzas: ",regular_pizzas)
    print("Number of Small Pizzas: ",small_pizzas)

calculate_slices_of_pizzas(100)
