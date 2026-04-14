print("=== UPA RISK CLASIFFIER ===")
temperature = float(input("Temperature: "))
systolic_blood_pressure = int(input("Systolic Blood Pressure: "))


while True:
  pain_level = int(input("Pain Level [0 - 10]:"))
  if  pain_level <= 10  and pain_level >= 0:
    break;
  print(f"The Pain level shoud be [0 - 10]")

#classifier

if temperature > 39.5 or systolic_blood_pressure > 180 or pain_level >= 9:
  risk = "Red"
  recomendation = "This is an emergency"
elif temperature > 38.5 or systolic_blood_pressure > 160 or pain_level >= 7:
  risk = "Orange"
  recomendation = "You can wait a bit until you get attention"
elif temperature > 37.5 or systolic_blood_pressure > 140 or pain_level >= 4:
  risk = "yellow"
  recomendation = "You can wait more time for attention"
else:
  risk = "green"
  recomendation = "This is not an emergency"

print(f"The Risk is: {risk}\nRecomendation: {recomendation}")
