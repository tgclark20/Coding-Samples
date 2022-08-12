#----------------------------------------------------------------------------
# Created By  : Timothy Clark
# Created Date: 08/12/2022
# Description: Methods requested as coding samples.
# ---------------------------------------------------------------------------
testString='''INSTRUMENT_ID = "MDIS-NAC"
FILTER_NUMBER = "2"
CENTER_FILTER_WAVELENGTH = 747.7 <NM>
BANDWIDTH = 52.6 <NM>
EXPOSURE_DURATION = 192 <MS>
EXPOSURE_TYPE = AUTO
DETECTOR_TEMPERATURE = -42.55 <DEGC>
FOCAL_PLANE_TEMPERATURE = -35.94 <DEGC>
FILTER_TEMPERATURE = "N/A"
OPTICS_TEMPERATURE = -37.36 <DEGC>'''

# Example Question 1
def questionOne(inputString, keyword):
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


