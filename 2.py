def coke_machine():
    total_inserted = 0
    due =50
    accepted_coin = [25, 5 ,10]
    
    while total_inserted < due:
        coin =int(input("insert coins 25,5,10:"))
        if coin in accepted_coin:
            total_inserted += coin
            print (f"amount due{ due-total_inserted} cents")
            change = total_inserted -due
            if change >0 : 
                print(f"change owed{change}")
            else:
                print("no change")
coke_machine()