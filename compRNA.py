def enterStrand():
   while True:
      mRNA = input("Enter RNA Strand\n").upper()
      if confirmStrand(mRNA):
         return mRNA
      else:
         print("Invalid Strand, Try Again")
         
def confirmStrand(mRNA):
   for base in mRNA:
      if base not in "AUGC":
         return False
   return True

def computeComp(mRNA):
   cmRNA = "3'- "
   for base in mRNA:
      if base == "A":
         cmRNA += "U"
      if base == "U":
         cmRNA += "A"
      if base == "G":
         cmRNA += "C"
      if base == "C":
         cmRNA += "G"
   cmRNA += " - 5'"
   return cmRNA
         
def main():
   print("Compute Complementary - RNA")
   mRNA = enterStrand()
   cmRNA = computeComp(mRNA)
   print(f"Here is your sequence: \n{cmRNA}")
   