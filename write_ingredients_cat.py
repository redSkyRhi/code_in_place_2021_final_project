
import json

def write_data():
	ingredients_cat = {
        "olive_oil_ml": "condiments",
        "beef_mince_g": "meat",
        "onions_g": "veg",
        "garlic_bulb": "veg",
        "herbs_g": "herb_spice",
        "tin_chopped_tomato": "store_cupboard",
        "tvp_g": "store_cupboard",
        "bovrill_g": "condiments",
        "stock_ml": "home_made",
        "puree_g": "store_cupboard",
        "worcester_s_ml": "condiments",
        "malt_vinigar_ml": "condiments",
        "bay_leaves": "herb_spice",
        "mushrooms_g": "veg",
        "chilli_powder_g": "herb_spice",
        "paprica_g": "herb_spice",
        "smoked_paprica_g": "herb_spice",
        "cumin_ g": "herb_spice",
        "tin_kidney_beans": "store_cupboard",
        "green_pepper": "veg",
        "green_olives_g": "store_cupboard",
        "chorizo_g": "meat",
        "lamb_boned_g": "meat",
        "paprika_tsp": "herb_spice",
        "black_pepper_tsp": "herb_spice",
        "ras_el_hanout_tsp": "herb_spice",
        "Tumeric_tsp": "herb_spice",
        "Cinnamon_tsp": "herb_spice",
        "Cayan_perpper_tsp": "herb_spice",
        "Chicken_stock_ml": "home_made",
        "salt_tsp": "herb_spice",
        "Apricots_g": "store_cupboard",
        "Prunes_g": "store_cupboard",
        "Sultarnas_g": "store_cupboard",
    }

	with open("ingredients_cat.json", "w") as f:
		json.dump(ingredients_cat, f, indent=4)

def main():
    write_data()

if __name__ == "__main__":
    main()
