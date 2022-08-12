#----------------------------------------------------------------------------
# Created By  : Timothy Clark
# Created Date: 08/12/2022
# Description: Methods requested as coding samples.
# ---------------------------------------------------------------------------

# Example Question 1
def questionOne(inputString, keyword):
    inputDict = dict((x.strip(), y.strip())  
        for x, y in (element.split('=')  
            for element in inputString.split('\n'))) 

    return inputDict[keyword]
