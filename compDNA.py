def enterStrand():
   while True:
      DNA = input("Enter DNA Strand\n").upper()
      if confirmStrand(DNA):
         return DNA
      else:
         print("Invalid Strand, Try Again")
         
def confirmStrand(DNA):
   for base in DNA:
      if base not in "ATGC":
         return False
   return True

def computeComp(DNA):
   cDNA = "3'- "
   for base in DNA:
      if base == "A":
         cDNA += "T"
      if base == "T":
         cDNA += "A"
      if base == "G":
         cDNA += "C"
      if base == "C":
         cDNA += "G"
   cDNA += " - 5'"
   return cDNA
         
def main():
   print("Compute Complementary - DNA")
   DNA = enterStrand()
   cDNA = computeComp(DNA)
   print(f"Here is your sequence: \n{cDNA}")
   