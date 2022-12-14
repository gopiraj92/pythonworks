from mobileapp.models import mobiles as mob

# number of mobiles
# print("Number of mobiles is", len(mob))

# print 5g mobile names
# print([mo.get("name") for mo in mob if mo.get("band")=="5g"])

# costly mobile
# costly_mobile = max(mob, key=lambda mo:mo.get("price"))
# print("Costly mobile is", costly_mobile)

# cheapest mobile
# cheap_mobile = min(mob, key=lambda mo:mo.get("price"))
# print("Cheapest mobile is", cheap_mobile)

# print AMOLED display mobile names
# AMOLED_display = [mo.get("name") for mo in mob if mo.get("display")=="AMOLED"]
# print(AMOLED_display)

# sort mobiles based on price
