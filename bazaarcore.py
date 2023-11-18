import requests
import os
import pickle

# Code below this line of code are the properity of Aroteo aka JP1Q, if you want to copy this work credit the original creator in your work!

def SaveKeyToFile(key):
    with open('api_key.pkl', 'wb') as file:
        pickle.dump(key, file)

def LoadKeyFromFile():
    try:
        with open('api_key.pkl', 'rb') as file:
            return pickle.load(file)
    except (pickle.PickleError, FileNotFoundError, EOFError):
        return None

def GetKey():
    global key

    existing_key = LoadKeyFromFile()

    if existing_key:
        key = existing_key
        print("API key loaded from pickle file.")
    else:
        key = input("Please insert your API key > ")
        SaveKeyToFile(key)
        print("API key saved to pickle file.")

def ChangeKey():
    global key
    choice = input("show current key? (y/N) > ")
    if choice.lower == "y":
        print("Current API key:", key)
    confirmation = input("Do you want to change the API key? (yes/no) > ").lower()

    if confirmation == 'yes':
        new_key = input("Please insert your new API key > ")
        SaveKeyToFile(new_key)
        key = new_key
        print("API key changed and saved to pickle file.")
    else:
        print("API key unchanged.")



data = requests.get(

    url = "https://api.hypixel.net/v2/skyblock/bazaar",
    params = {

        "key": "1927adbe-31cb-43d4-8e02-477c23af4f61"

    }

).json()

def Refresh():
    data = requests.get(

    url = "https://api.hypixel.net/v2/skyblock/bazaar",
    params = {

        "key": "1927adbe-31cb-43d4-8e02-477c23af4f61"

    }

    ).json()




def getItems(threshold_percent, max_buy_price_threshold, min_buy_price_threshold, min_sell_summary_entries, min_sell_volume_threshold, min_buy_volume_threshold):
# Set your desired thresholds
##threshold_percent = 10
##max_buy_price_threshold = 8
##min_buy_price_threshold = 3
##min_sell_summary_entries = 5
##min_sell_volume_threshold = 1000  # Set your desired minimum sell volume threshold
##min_buy_volume_threshold = 1000   # Set your desired minimum buy volume threshold

# Create a list to store product information
    product_info_list = []
    i = 0
    for product_id, product_data in data["products"].items():
        sell_summary = product_data["sell_summary"]
        buy_summary = product_data["buy_summary"]
        quick_status = product_data.get("quick_status", {})

        # Get the priciest sell price and cheapest buy price if sell_summary is not empty
        if sell_summary:
            priciest_sell_price = sell_summary[0]["pricePerUnit"]
        else:
            priciest_sell_price = 0

        # Get the cheapest buy price if buy_summary is not empty
        if buy_summary:
            cheapest_buy_price = buy_summary[0]["pricePerUnit"]
        else:
            cheapest_buy_price = 0

        # Get the sell and buy volumes from quick_status
        sell_volume = quick_status.get("sellVolume", 0)
        buy_volume = quick_status.get("buyVolume", 0)

        # Check if the priciest sell price is not zero, the buy price is below the max buy price threshold,
        # the buy price is above the min buy price threshold, the sell summary has enough entries,
        # and the sell and buy volumes are above the respective thresholds
        if (
            priciest_sell_price != 0
            and max_buy_price_threshold > cheapest_buy_price > min_buy_price_threshold
            and len(sell_summary) >= min_sell_summary_entries
            and sell_volume >= min_sell_volume_threshold
            and buy_volume >= min_buy_volume_threshold
        ):
            percentage_difference = ((cheapest_buy_price - priciest_sell_price) / priciest_sell_price) * 100    
            # Create a dictionary to store product information
            product_info = {
                "product_id": product_id,
                "priciest_sell_price": priciest_sell_price,
                "cheapest_buy_price": cheapest_buy_price,
                "percentage_difference": percentage_difference,
                "sell_volume": sell_volume,
                "buy_volume": buy_volume,
            }   
            # Append the dictionary to the list
            product_info_list.append(product_info)
        i+=1
        

    # Sort the list of dictionaries by the combination of percentage difference, sell volume, and buy volume
    product_info_list.sort(key=lambda x: (x["percentage_difference"], x["sell_volume"], x["buy_volume"]), reverse=True)
    return product_info_list






# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[95m"   # Pinkish Red
GREEN = "\033[38;5;213m"  # Light Pink (or you can choose a specific shade)
YELLOW = "\033[93m"
BLUE = "\033[38;5;141m"
CYAN = "\033[96m"




def ShowData(product_info_list):
    os.system('cls' if os.name == 'nt' else 'clear')

    # Define the number of columns for display
    num_columns = 4

    for index, product_info in enumerate(product_info_list):
        # Calculate the row and column indices
        row = index // num_columns
        col = index % num_columns

        # Calculate the padding for the index column
        index_padding = 5

        # Define colors based on conditions (you can customize these)
        sell_volume_color = GREEN if product_info['sell_volume'] > 1000 else RESET
        buy_volume_color = GREEN if product_info['buy_volume'] > 1000 else RESET
        percentage_difference_color = RED if product_info['percentage_difference'] > 10 else RESET

        # Print the item information in color
        print(
            f"{index}".ljust(index_padding) +
            f"Product ID: {BOLD}{product_info['product_id']}{RESET}, "
            f"Priciest Sell Price: {BLUE}{product_info['priciest_sell_price']:.2f}{RESET}, "
            f"Cheapest Buy Price: {BLUE}{product_info['cheapest_buy_price']:.2f}{RESET}, "
            f"Percentage Difference: {percentage_difference_color}{product_info['percentage_difference']:.2f}%{RESET}, "
            f"Sell Volume: {sell_volume_color}{product_info['sell_volume']}{RESET}, "
            f"Buy Volume: {buy_volume_color}{product_info['buy_volume']}{RESET}"
        )

        # Add code to print additional item information if needed
        print()

# Example usage:
# ShowData(product_info_list)
