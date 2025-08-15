# First things first, define a weight variable and set it equal to any number. (in lb)
weight = 8.4
flat_charge = 20.0
print("Weight", weight)

# Ground Shipping
if weight <= 2 :
  s = weight * 1.50 + flat_charge
elif weight > 2 and weight <= 6 :
  s = weight * 3 + flat_charge
elif weight > 6 and weight <= 10 :
  s = weight * 4 + flat_charge
elif weight > 10 :
  s = weight * 4.75 + flat_charge

# A package that weighs 8.4 pounds should cost $53.60 to ship with normal ground shipping:
# 8.4 * 4 + 20.0 = 53.60
# change weight to 8.4 and try
print("Ground Shipping (according to ur weight):", s)

# Ground Shipping Premium
prem = 125.00
print("Premium Ground Shipping:", prem)

# Drone Shipping Flat Charge
flat_charge = 0.00

# Drone Shipping
if weight <= 2 :
  s = 4.50
elif weight > 2 and weight <= 6 :
  s = 9.00
elif weight > 6 and weight <= 10 :
  s = 12.00
elif weight > 10 :
  s = 14.25
print("------")
# A package that weighs 1.5 pounds should cost $6.75 to ship by drone:
# 1.5 * 4.50 + 0 = 6.75 (if weight = 1.5)
weight = 1.5
print("Weight", weight)
print("Drone Shipping:", s)
