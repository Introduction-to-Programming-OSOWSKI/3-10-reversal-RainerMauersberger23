def reversal(w):
    newWord = ""
    for i in range (0, len(w)):
        newWord = newWord + w[len(w) - 1 - i]
   
    return newWord




print (reversal("lightsaber"))
