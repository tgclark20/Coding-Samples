#----------------------------------------------------------------------------
# Created By  : Timothy Clark
# Created Date: 08/12/2022
# Description: Methods requested as coding samples.
# ---------------------------------------------------------------------------
import Constants

encodings= Constants.encodings
tempEncodings=Constants.tempEncodings
timeEncodings=Constants.timeEncodings
measurementEncodings=Constants.measurmentEncodings
standardConversions=Constants.standardConversions


# Example Question 1
def questionOne(inputString, keyword):
    
    inputString= inputString.replace(' = ',' ')

    inputDict = dict((x.strip(), y.strip())  
        for x, y in (element.split(' ')  
            for element in inputString.split('\n'))) 

    return inputDict[keyword]


# Example Question 2
def questionTwo(inputString, keyword):
    
    inputString= inputString.replace(' = ',' ')
    inputDict =dict()
    
    for element in inputString.split('\n'):
        values = element.split()
        if len(values)==2:
            inputDict[values[0]]= {'value' : values[1]}
        else:
            inputDict[values[0]]={'value': values[1], 'unit': values[2]}
    
    return inputDict[keyword].get('value')


#Example Question 3
def questionThree(inputString, unit ,keyword):
    inputString= inputString.replace(' = ',' ')
    inputDict =dict()
    
    for element in inputString.split('\n'):
        values = element.split()
        if len(values)==2:
            inputDict[values[0]]= {'value' : values[1]}
        else:
            inputDict[values[0]]={'value': values[1], 'unit': values[2]}

    selectedValue=float(inputDict[keyword].get('value'))
    selectedUnit=inputDict[keyword].get('unit')
    unitExpanded=encodings[selectedUnit]

    if unitExpanded in measurementEncodings and unit in measurementEncodings:
       return (selectedValue*standardConversions[unitExpanded])/(standardConversions[unit])

    elif unitExpanded in timeEncodings and unit in timeEncodings:
       return (selectedValue*standardConversions[unitExpanded])/(standardConversions[unit])
    
    elif unitExpanded in tempEncodings and unit in tempEncodings:
        if unit == unitExpanded:
            return selectedValue
        elif unit == 'Celcius':
            return round(((5.0/9.0)*(selectedValue-32)),2)
        elif unit == 'Fahrenheit':
            return round((((9.0/5.0)*(selectedValue))+32),2)
        else:
            return "an Exception has Occurred"
    else:
        return "***Unit mismatch***"


#Example Question 4
def questionFour(inputStrings, filter, keyword):
    inputDict =dict()
    selectedValues=[]
    for index,inputString in enumerate(inputStrings):
        inputString= inputString.replace(' = ',' ')
        tempDict=dict()
        for element in inputString.split('\n'):
            values = element.split()
            tempDict[values[0]]=values[1]
        inputDict[index]=tempDict


    for i,j in inputDict.items():
        try:
            float(j[keyword])
            selectedValues.append(float(j[keyword]))
        except:
            continue

    if filter=='Minimum':
        return min(selectedValues)
    if filter=='Maximum':
        return max(selectedValues)



