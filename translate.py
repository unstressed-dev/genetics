import textwrap
codonTable = [
   [
      #U
      ["Phe","Phe","Leu","Leu"],#U
      ["Ser","Ser","Ser","Ser"],#C
      ["Tyr","Tyr","STOP","STOP"],#A
      ["Cys","STOP","Cys","Trp"],#G
   ],
   [
      #C
      ["Leu","Leu","Leu","Leu"],#U
      ["Pro","Pro","Pro","Pro"],#C
      ["His","His","Gln","Gln"],#A
      ["Arg","Arg","Arg","Arg"],#G
   ],
   [  
      #A
      ["Ile","Ile","Ile","Met"],#U
      ["Thr","Thr","Thr","Thr"],#C
      ["Asn","Asn","Lys","Lys"],#A
      ["Ser","Ser","Arg","Arg"],#G
   ],
   [
      #G
      ["Val","Val","Val","Val"],#U
      ["Ala","Ala","Ala","Ala"],#C
      ["Asp","Asp","Glu","Glu"],#A
      ["Gly","Gly","Gly","Gly"],#G
   ]
]

codonKey = {"U":0,"C":1,"A":2,"G":3}

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

def translate(mRNA):
   #split to codons
   mRNA = mRNA[:len(mRNA)-len(mRNA)%3]
   codons = textwrap.wrap(mRNA, 3)
   #translate to proteins
   Protein = "N - "
   start = False
   for codon in codons:
      if start == False:
         if codonTable[codonKey[codon[0]]][codonKey[codon[1]]][codonKey[codon[2]]] == "Met":
            Protein += codonTable[codonKey[codon[0]]][codonKey[codon[1]]][codonKey[codon[2]]] + " "
            start = True
         else:
            continue
      elif codonTable[codonKey[codon[0]]][codonKey[codon[1]]][codonKey[codon[2]]] == "STOP":
         break
      else:
         Protein += codonTable[codonKey[codon[0]]][codonKey[codon[1]]][codonKey[codon[2]]] + " "
   Protein += " - C"
   return Protein 
         
          
          
      
      
def main():
   print("Translate mRNA")
   mRNA = enterStrand()
   ProteinSequence = translate(mRNA)
   print(ProteinSequence)