# names of your group mates
MemName1 = "Chryson Neil M. Valdez"
MemName2 = "Adrian Cedric O. Calindas"
MemName3 = "Sharmaine N. Gasatan"
# member age
AgeMember1 = "20"
AgeMember2 = "20"
AgeMember3 = "19"

convert1 = int(AgeMember1)
convert2 = int(AgeMember2)
convert3 = int(AgeMember3)

# member allowance

AllowanceMem1 = float(500.0)
AllowanceMem2 = float(500.0)
AllowanceMem3 = float(500.0)

# print the names of group members

print ("Team Name: Vanilla")

print ("Member 1:" , MemName1 , ", " , "his age is " , AgeMember1 , ", " , "allowance per week is " , AllowanceMem1 , ".")
print ("Member 2:" , MemName2 , ", " , "his age is " , AgeMember2 , ", " , "allowance per week is " , AllowanceMem2 , ".")
print ("Member 3:" , MemName3 , ", " , "her age is " , AgeMember3 , ", " , "allowance per week is " , AllowanceMem3 , ".")

lengthMem1 = len(MemName1)
lengthMem2 = len(MemName3)
lengthMem3 = len(MemName3)

print("Member 1 consists of", MemName1 , "characters")
print("Member 2 consists of", MemName2 , "characters")
print("Member 3 consists of", MemName3 , "characters")


sumMemb1 = (convert1 + convert2 + convert3)
print (sumMemb1)
subMemb2 = (convert1 - convert2 - convert3)
print (subMemb2)

prod1 = (convert1 * AllowanceMem1)
prod2 = (convert2 * AllowanceMem2)
prod3 = (convert3 * AllowanceMem3)

print(prod1)
print(prod2)
print(prod3)

# Comparison of members age

res1 = (convert1 - convert2)
res2 = (convert2 - convert3)
print(res1)
print(res2)

# Comparison of name length of group members

Length1 = (lengthMem1 - lengthMem2)
Length2 = (lengthMem2 - lengthMem3)

print(Length1)
print(Length2)

