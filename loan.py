house_price = 1000000

good_credit = 800

scoreList = {}
scoreList["AJFPM1792H"] = 830
scoreList["ALYPG592H"] = 790


user = input(" PAN CARD NUMBER : ")


if(scoreList.__contains__(user) and scoreList[user] >= good_credit):
    dp = 20
else:
    dp = 10

discount = round((dp*house_price)/100)
print(f"you availed ${discount}  Discount ")
