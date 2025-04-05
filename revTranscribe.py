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

def revTranscribe(mRNA):
   DNA = "5'- "
   for base in mRNA:
      if base == "A":
         DNA += "T"
      if base == "U":
         DNA += "A"
      if base == "G":
         DNA += "C"
      if base == "C":
         DNA += "G"
   DNA += " - 3'"
   return DNA
         
def main():
   print("Reverse Transcribe mRNA")
   mRNA = enterStrand()
   DNA = revTranscribe(mRNA)
   print(f"Here is your sequence: \n{DNA}")
   