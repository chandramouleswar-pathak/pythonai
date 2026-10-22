def calculated_take_home(lpa_in_lakhs,tax_rate=0.20):
    annual_salary=lpa_in_lakhs*100_000
    tax_amount=annual_salary*tax_rate
    take_home=annual_salary-tax_amount
    return take_home
my_take_home=calculated_take_home(60,0.25)
print("Annual take home (60lpa at the tax rate 25%)",my_take_home)
junior_take_home=calculated_take_home(12)
print("Annual take home (at default tax rate)",junior_take_home)
offers = [
    {"company": "google", "LPA":60,"tax_rate":0.25},
    {"company": "atlassian", "LPA":45,"tax_rate":0.20},
    {"company": "startup", "LPA":25,"tax_rate":0.15},
]
print("\n---PROCESSING OFFER PIPELINE ---")
for offer in offers:
    company=offer["company"]
    Lpa=offer["LPA"]
    rate=offer["tax_rate"]
    net_pay=calculated_take_home(Lpa,rate)
    print(f"Company:{company:<10}| IN_HAND:${net_pay:,.0f}")