# Tool 1 : resilient e-commerce order processor with exception handling and batch analytics

def parse_and_bill_order(raw_order_string):
    try:
        splited_value = raw_order_string.split(":")
        if len(splited_value) != 4:
            raise IndexError
        
        price = float(splited_value[2])
        quantity = int(splited_value[3]) 

        if price <= 0 or quantity <= 0:
            raise ValueError  
    
    except (IndexError, ValueError):
        return None

    else:
        name = splited_value[0].strip().title()
        category = splited_value[1].strip().upper()

        subtotal = price * quantity
        if quantity >= 5:
            subtotal *= 0.90

        fee = 0
        if category == "ELECTRONICS":
            fee += 15.00
        elif category != "FOOD":
            fee += 5.00

        final_total = subtotal + fee
        total_revenue = {}
        total_revenue["name"] = name
        total_revenue["category"] = category
        total_revenue["final total"] = final_total 

        return total_revenue

def process_batch_pipeline(raw_orders_list):
    total_revenue = 0.0
    failed_orders_count = 0
    valid_orders = []

    top_item_name = ""
    top_item_amount = -1.0

    for list_string in raw_orders_list:
        cleared_string = parse_and_bill_order(list_string)
        
        if cleared_string is None:
            failed_orders_count += 1
            continue

        valid_orders.append(cleared_string)
        total_revenue += cleared_string["final total"]

        if cleared_string["final total"] > top_item_amount:
            top_item_amount = cleared_string["final total"]
            top_item_name = cleared_string["name"]

    if not valid_orders:
        return f"CRITICAL: Batch Failed! 0 valid orders | Rejected: {failed_orders_count}"

    return f"Total Revenue: ${total_revenue:,.2f} | Processed: {len(valid_orders)} | Failed: {failed_orders_count} | Top Earner: {top_item_name} (${top_item_amount:,.2f})"        


raw_data = [
    "  macbook pro : electronics : 1200.00 : 2 ",  
    "apple : food : 2.50 : 10 ",                   
    "corrupt_string_without_colons",               
    "desk chair : furniture : 150.00 : 1 ",        
    "gaming mouse : electronics : twenty : 2 ",    
    "t-shirt : clothing : -20.00 : 3 ",            
    "notebook : stationery : 5.00 : 6 "           
]

print(process_batch_pipeline(raw_data))