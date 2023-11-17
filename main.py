import bazaarcore as bzr


def Into():
    print("Stuff in () is what to put in if you do not know what")
    print()
    threshold_percent = int(input("threshold percentage (10)> "))
    max_buy = int(input("max buy price (8)> "))
    min_buy = int(input("min buy price (3)> "))
    sell_entr = int(input("sell entries (5)> "))
    min_sell_vol = int(input("min sell volume (1000)> "))
    min_buy_volume = int(input("min buy volume (1000)> "))
    
    return threshold_percent, max_buy, min_buy, sell_entr, min_sell_vol, min_buy_volume



##threshold_percent = 10
##max_buy_price_threshold = 8
##min_buy_price_threshold = 3
##min_sell_summary_entries = 5
##min_sell_volume_threshold = 1000  # Set your desired minimum sell volume threshold
##min_buy_volume_threshold = 1000   # Set your desired minimum buy volume threshold

first_in = False
loop = True 
while loop == True:
    if not first_in:
        bzr.GetKey()
        threshold_percent, max_buy, min_buy, sell_entr, min_sell_vol, min_buy_volume = Into()
        data = bzr.getItems(threshold_percent, max_buy, min_buy, sell_entr, min_sell_vol, min_buy_volume)
        bzr.ShowData(data)
        first_in = True
    print()
    print("A> Refresh")
    print("B> Change Values")
    print("C> Change API key")
    print("Q> Quit")
    choice = input("> ")
    if choice.lower == 'a':
        bzr.Refresh()
        data = bzr.getItems(threshold_percent, max_buy, min_buy, sell_entr, min_sell_vol, min_buy_volume)
    if choice.lower == 'b':
        threshold_percent, max_buy, min_buy, sell_entr, min_sell_vol, min_buy_volume = Into()
        data = bzr.getItems(threshold_percent, max_buy, min_buy, sell_entr, min_sell_vol, min_buy_volume)
    if choice.lower == 'c':
        bzr.ChangeKey()
    if choice.lower == 'q':
        loop = False
    else:
        bzr.ShowData(data)

    
    




