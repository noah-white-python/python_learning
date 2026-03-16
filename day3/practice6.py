shop = {
    "fruits":     [("apple", 8), ("banana", 3), ("mango", 15)],
    "vegetables": [("carrot", 5), ("spinach", 7), ("potato", 4)],
    "drinks":     [("water", 2), ("juice", 12), ("tea", 9)],
}


for name, information in shop.items():
    m = max(information, key=lambda item: item[1])
    print(f"{name} 最贵的商品：{m[0]}，价格：{m[1]}")


all_items = []
max_price = 0
for name, information in shop.items():
    all_items += information
    max_price = max(all_items, key=lambda item: item[1])
print(max_price)