
# Read data file and return sequences
def readfile(filename):
    f = open(filename,"r")
    # First line is the forward plasmid sequence
    plasmid = f.readline().rstrip()
    # Second line is the restriction site for cutting the plasmid
    RE = f.readline().rstrip()
    # Third line is the forward gfp sequence
    gfp = f.readline().rstrip()
    # Two left and right restriction sites for cutting gfp
    REgfp = f.readline().rstrip().split(" ")
    return plasmid, RE, gfp, REgfp
# Function to find complement of dna sequence
def complement(s):
    s=s.upper()
    newstr = ""
    for i in s:
        if(i=="A"):
            newstr +="T"
        elif (i=="T"):
            newstr +="A"
        elif(i=="G"):
            newstr+="C"
        elif(i=="C"):
            newstr+="G"
    return newstr
# Function to cut dna sequence at RE site on forward strand
def findRE(dna,re):
    cutidx = dna.find(re)+1
    return dna[:cutidx], dna[cutidx:]
# Function to cut dna sequence at RE site on complementary strand
def findCompRE(dna,re):
    cutidx = dna.find(re)+5
    return dna[:cutidx], dna[cutidx:]

if __name__ == '__main__':
    # Input  file name
    filename = str(input())
    # Read file and return sequences
    plasmid, RE, gfp, REgfp = readfile(filename)
    # Create complementary sequences of plasmid,  gfp, RE, REgfp
    compPlasmid = complement(plasmid)
    compRE = complement(RE)
    compGFP = complement(gfp)
    comp_leftREgfp = complement(REgfp[0])
    comp_rightREgfp = complement(REgfp[1])
    # Cut the plasmid at RE
    cutPlasmid = findRE(plasmid,RE)
    # Cut the compPlasmid at compRE
    comp_cutPlasmid = findCompRE(compPlasmid,compRE)
    # Cut the gfp strand at REgfp[0] and REgfp[1]
    leftCutGFP = findRE(gfp,REgfp[0])[1]
    rightCutGFP = findRE(leftCutGFP, REgfp[1])[0]
    # Cut the compGFP at comp_leftREgfp and comp_rightREgfp
    leftCutCompGFP = findCompRE(compGFP,comp_leftREgfp)[1]
    rightCutCompGFP = findCompRE(leftCutCompGFP, comp_rightREgfp)[0]
    # Ligate left of cutPlasmid to rightCutGFP and right of cutPlasmid
    firststrand = cutPlasmid[0] + rightCutGFP + cutPlasmid[1]
    # Repeat for complementary strand
    secondstrand = comp_cutPlasmid[0] + rightCutCompGFP + comp_cutPlasmid[1]
    print(firststrand)
    print(secondstrand)



