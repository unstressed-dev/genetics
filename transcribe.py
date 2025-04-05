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

def transcribe(DNA):
   mRNA = "5'- "
   for base in DNA:
      if base == "A":
         mRNA += "U"
      if base == "T":
         mRNA += "A"
      if base == "G":
         mRNA += "C"
      if base == "C":
         mRNA += "G"
   mRNA += " - 3'"
   return mRNA
         
def main():
   print("Transcribe DNA")
   DNA = enterStrand()
   mRNA = transcribe(DNA)
   print(f"Here is your sequence: \n{mRNA}")
   