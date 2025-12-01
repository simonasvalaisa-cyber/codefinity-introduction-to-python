seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

overstock_risk = seasonal and current_stock >= high_stock_threshold
print ("Is the item is seasonal and its current stock exeeds the high stock threshold?", overstock_risk )

discount_eligible = not selling_well and not on_sale
print ("Is the item discount eligible?", discount_eligible)

make_discount = overstock_risk or discount_eligible
print ("Should the item be discounted?", make_discount)