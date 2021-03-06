
import json

def write_data():
	batch_cooks = {
        "Bolognese":{
            "ingredients":{
                "olive_oil_ml": 15,
                "beef_mince_g": 800,
                "onions_g": 1600,
                "garlic_bulb": 1,
                "herbs_g": 15,
                "tin_chopped_tomato": 3,
                "tvp_g": 100,
                "bovrill_g": 40,
                "stock_ml": 500,
                "puree_g": 156,
                "worcester_s_ml": 15,
                "malt_vinigar_ml": 60,
                "bay_leaves": 8,
                "mushrooms_g": 600
            }
        },
        "Chilli":{
            "ingredients":{
                "olive_oil_ml": 15, 
                "beef_mince_g": 800, 
                "onions_g": 1600,
                "garlic_bulb": 1,
                "chilli_powder_g": 32,
                "paprica_g": 16,
                "smoked_paprica_g": 16,
                "cumin_ g": 32,
                "tin_chopped_tomato": 4,
                "tin_kidney_beans": 6,
                "tvp_g": 200,
                "bovrill_g": 40,
                "stock_ml": 500,
                "puree_g": 156,
                "worcester_s_ml": 15,
                "malt_vinigar_ml": 60,
                "bay_leaves": 8
            }
        },
        "Chorizo":{
            "ingredients": {
                "olive_oil_ml": 30,
                "onions_g": 640,
                "garlic_bulb": 0.5,
                "tin_chopped_tomato": 4,
                "green_pepper": 4,
                "green_olives_g": 50,
                "chorizo_g": 250,
                "herbs_g": 10,
            }
        },
        "Lamb Tagine":{
            "ingredients": {
                "olive_oil_ml": 10,
                "onions_g": 1600,
                "garlic_bulb": 1,
                "lamb_boned_g": 1900,
                "paprika_tsp": 2,
                "black_pepper_tsp": 2,
                "ras_el_hanout_tsp": 2,
                "Tumeric_tsp": 2,
                "Cinnamon_tsp": 3,
                "Cayan_perpper_tsp": 1,
                "Chicken_stock_ml": 500,
                "salt_tsp": 3,
                "Apricots_g": 200,
                "Prunes_g": 100,
                "Sultarnas_g": 200,
            }
        }
    }
	with open("batch_cooks.json", "w") as f:
		json.dump(batch_cooks, f, indent=4)

def main():
    write_data()

if __name__ == "__main__":
    main()
