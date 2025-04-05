import random
import compDNA
import compRNA
import transcribe
import revTranscribe
import translate
def choose():
   while True:
      try:
         choice = int(input())
      except ValueError:
         warning()
         continue
      if choice in range(0,6):
         return choice
      else:
         warning()
         
def warning():
   warnings = ["Please Enter a Choice",
               "Enter 0 to exit program",
               "Please Enter a Number"]
   print(random.choice(warnings))
      
def mainChoices():
   while True:
      print("What would you like to do?")
      print("   0. Exit Program")
      print("   1. Find Complementary to DNA Sequence")
      print("   2. Find Complementary to mRNA Sequence")
      print("   3. Transcribe DNA")
      print("   4. Translate mRNA")
      print("   5. Reverse-Transcribe mRNA")
      choice = choose()
      if choice == 0:
         print("Exiting Program...")
         break
      elif choice == 1:
         compDNA.main()
      elif choice == 2:
         compRNA.main()
      elif choice == 3:
         transcribe.main()
      elif choice == 4:
         translate.main()
      elif choice == 5:
         revTranscribe.main()
def main():
   print("Hello, welcome to Devin's Genetics Program")
   mainChoices()
main()

