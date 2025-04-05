#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<format>
using namespace std;
string enterStrand();
string computeComp(string);
bool confirmStrand(string);
int main() {
   cout << "Compute Complementary - DNA\n";
   string DNA = enterStrand();
   string cDNA = computeComp(DNA);
   cout << "Here is your sequence: \n" << DNA << "\n";
}
bool confirmStrand(string DNA) {
   string dnaBases = "TACG";
   for(char i: DNA) {
      if (find(dnaBases.begin(),dnaBases.end(),i) == dnaBases.end())
      return false;
   };
   return true;
}
string enterStrand() {
   string DNA;
   while(true) {
      cout << "Enter DNA Strand\n";
      cin >> DNA;
      if (confirmStrand(DNA) == true) {
         return DNA;
      } else {
         cout << "Invalid Strand, Try Again\n";
      }
   }
}
string computeComp(string DNA) {
   return "Done";
}