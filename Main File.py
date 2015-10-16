#This program was written by David Sun
#/r/ggggg is a subreddit consisting of only G's
#Supposedly, it's written all in morse code using uppercase and lowercase G's
#This program will be able to take the text and output a correct answer
#Not necessarily everything will be written in morse code though

#Edit - This program can now convert things into G's too

#FIXED: Errors - Random invalid inputs at a long conversions of g's -> letters


#Objective: Create a list of morse Code using G's and g's
#Note: Python string comparison is case sensitive

#Import for space splitting - Unsure if it works
import re
#re.split(u'\s|\u200b',stringtosplit)
#this will split by spaces
#setting this to a new variable will create a new list

#Variables for all the values of morse code
#Note: Changing the G's will result in an entirely different encryption
G_AMorse = ['gG','A']
G_BMorse = ['Gggg','B']
G_CMorse = ['GgGg','C']
G_DMorse = ['Ggg','D']
G_EMorse = ['g','E']
G_FMorse = ['ggGg','F']
G_GMorse = ['GGg','G']
G_HMorse = ['gggg','H']
G_IMorse = ['gg','I']
G_JMorse = ['gGGG','J']
G_KMorse = ['GgG','K']
G_LMorse = ['gGgg','L']
G_MMorse = ['GG','M']
G_NMorse = ['Gg','N']
G_OMorse = ['GGG','O']
G_PMorse = ['gGGg','P']
G_QMorse = ['GGgG','Q']
G_RMorse = ['gGg','R']
G_SMorse = ['ggg','S']
G_TMorse = ['G','T']
G_UMorse = ['ggG','U']
G_VMorse = ['gggG','V']
G_WMorse = ['gGG','W']
G_XMorse = ['GggG','X']
G_YMorse = ['GgGG','Y']
G_ZMorse = ['GGgg','Z']
G_1Morse = ['gGGGG','1']
G_2Morse = ['ggGGG','2']
G_3Morse = ['gggGG','3']
G_4Morse = ['ggggG','4']
G_5Morse = ['ggggg','5']
G_6Morse = ['Ggggg','6']
G_7Morse = ['GGggg','7']
G_8Morse = ['GGGgg','8']
G_9Morse = ['GGGGg','9']
G_0Morse = ['GGGGG','0']
#Error Exception
G_Error1Morse = ['/',' ']
G_Error2Morse = ['', '']
#Punctuation Exception
G_Punct1Morse = ['!', '!']
G_Punct2Morse = ['?', '?']
G_Punct3Morse = ['"' , '"']
G_Punct4Morse = ["'" , "'"]
G_Punct5Morse = ['_','_']
G_Punct6Morse = ['.','.']


#List of all the variables
#Nested List
GList =[G_AMorse, G_BMorse, G_CMorse, G_DMorse, G_EMorse, G_FMorse, G_GMorse,
       G_HMorse, G_IMorse, G_JMorse, G_KMorse, G_LMorse, G_MMorse, G_NMorse,
       G_OMorse, G_PMorse, G_QMorse, G_RMorse, G_SMorse, G_TMorse, G_UMorse,
       G_VMorse, G_WMorse, G_XMorse, G_YMorse, G_ZMorse, G_1Morse, G_2Morse,
       G_3Morse, G_4Morse, G_5Morse, G_6Morse, G_7Morse, G_8Morse, G_9Morse,
       G_0Morse, G_Error1Morse, G_Error2Morse, G_Punct1Morse, G_Punct2Morse,
       G_Punct3Morse, G_Punct4Morse, G_Punct5Morse, G_Punct6Morse]

#String Testing
#x = 'some string'

#Some List Testing
def GReturn():
    return GList

#Return G's and g's
def GListReturnG():
    for x in range(len(GList)):
        for i in range (0,1):
            print (GList[x][i])
            
#Return Letters
def GListReturnLetter():
    for x in range(len(GList)):
        for i in range (1,2):
            #return GList[x][i]
            print (GList[x][i])
        
#return testing
#print(GListReturnLetter())

#Random Testing
def GTesting():
    for x in range(len(GList)):
        for i in range (0,1):
            if (GList[x][i] == G_DMorse[0]):
                print(G_DMorse)
#Main Testing
#Finds the character when morse code is inputted
def GCharFind(strInput):
    for x in range(len(GList)):
        #This is not needed
        #for i in range (0,1):
            #since this was done with a string, theres an issue here
        if (GList[x][0] == strInput):
            return(GList[x][1])
        #Unsure if this is needed, but I don't believe so
        elif (strInput == ' '):
            return ' '
    return ' Invalid Letter '

#Find the Morse Code when character is inputted
#Error is probably in strInput -> charInput
#Error fixed
def CharToGFind(charInput):
    for x in range(len(GList)):
        #this is technically redundant
        #This is also not needed
        #for i in range (1,2):
        if (GList[x][1].lower() == charInput.lower() ):
            return(GList[x][0])
        elif (charInput == ' '):
            #return ' '
            pass
            #This doesn't actually catch the error
            #elif (charInput == ' /'):
                #return ' '
        #elif (charInput == '.'):
            #return '.'
    return ' Invalid Input '

#Main Clases
#Method to change G to Letters
def MainGtoLetters():
    stringOutput = ''
    gStrInput = input('Enter a G Morse Code: ')
    #Actually this variable below is a list
    newSplitString = re.split(u'\s|\u200b',gStrInput)
    #print (newSplitString)
    #ouput testing
    #print(gStrInput)
    #print(gStrInput[0])
    for x in range(len(newSplitString)):
        #print(gStrInput[x])
        stringOutput += GCharFind(newSplitString[x])
    print(stringOutput)

#Method to change Letters to G
def MainLetterstoG():
    stringOutput = ''
    gStrInput = input("Enter something to be made into G's: ")
    #unsure if new List is needed
    newSplitString = re.split(u'\s|\u200b',gStrInput)
    #print (newSplitString)
    for x in range(len(newSplitString)):
        #with luck, i will become all the variables in list[x]
        #error in this line
        #for i in range (newSplitString[x]):
            #print (i)
        #for z in range(len(newSplitString[x])):
        for y in newSplitString[x]:
            stringOutput = stringOutput + CharToGFind(y) + ' '
        stringOutput += '/ '
    stringOutput = stringOutput[:-2]
    print(stringOutput)

def MainLoop():
    rerun = True
    while (rerun == True):
        runagainInput = ''
        runDecision = ''
        #I should probably ask them again if the input is incorrect, but lazy
        #Will fix later
        runDecision = input("Do you want to go from G to Letters or Letters to G: ")
        if (runDecision.lower() == 'g to letters'):
            MainGtoLetters()
        elif (runDecision.lower() == 'letters to g'):
            MainLetterstoG()
        else:
            print("Invalid Input")
        runagainInput = input('Do you want to run it again? : ')
        if(runagainInput.lower() == 'no' or runagainInput.lower() == 'n' or
           runagainInput.lower() == 'break'):
            rerun = False

MainLoop()





