def gc_content(dna):
    G = dna.count("G")
    C = dna.count("C")
    total = len(dna)
    GC_content = ((G+C)/total)*100
    return GC_content

def dna_count(dna):
        return{
             "A": dna.count("A"),
             "T": dna.count("T"),
             "G": dna.count("G"),
             "C": dna.count("C")
             }

dna_input = input("Enter DNA sequence: ")
dna = dna_input.replace(" ","")
dna = dna.upper()
if(dna == ""):
    print("The DNA sequence can't be empty.")
else:
    # validating the DNA sequence
    for letter in dna:
        if(letter not in "ATGC"):
            print("Invalid DNA sequence.\nOnly A,T,G and C are allowed.")
            print(f"Invalid character found: {letter}")
            break
    else:
        # counting the length of the DNA
        length = len(dna)
        print(f"Length: {length}")
        print()

        # counting the A,T,G,C content
        counts = dna_count(dna)
        print(f"A: {counts["A"]}")
        print(f"T: {counts["T"]}")
        print(f"G: {counts["G"]}")
        print(f"C: {counts["C"]}")
        print()

        # calculating GC content
        gc = gc_content(dna)
        print(f"GC content: {round(gc,2)}%")
        print()
        print("Valid DNA sequence: Yes")