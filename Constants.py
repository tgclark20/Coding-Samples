#----------------------------------------------------------------------------
# Created By  : Timothy Clark
# Created Date: 08/12/2022
# Description: Constants used within the example question methods, as well
#              as within the unit tests.
# ---------------------------------------------------------------------------

encodings= {'<DEGC>': 'Celcius', '<DEGF>':'Fahrenheit', '<NM>':'Nanometers', '<MM>': 'Millimeters','<CM>':'Centimeters', '<MS>':'Milliseconds', '<S>':'Seconds','<MIN>':'Minutes'}
timeEncodings=['Milliseconds','Seconds','Minutes']
measurmentEncodings=['Nanometers','Millimeters','Centimeters']
tempEncodings=['Celcius','Fahrenheit']
standardConversions={'Nanometers':.0001,'Millimeters':.001, 'Centimeters':.01, 'Seconds':1.0, 'Minutes':60.0, 'Milliseconds':.001}

testString='''INSTRUMENT_ID = "MDIS-NAC"
FILTER_NUMBER = "2"
CENTER_FILTER_WAVELENGTH = 747.7
BANDWIDTH = 52.6
EXPOSURE_DURATION = 192
EXPOSURE_TYPE = AUTO
DETECTOR_TEMPERATURE = -42.55
FOCAL_PLANE_TEMPERATURE = -35.94
FILTER_TEMPERATURE = "N/A"
OPTICS_TEMPERATURE = -37.36'''
testStringUnit='''INSTRUMENT_ID = "MDIS-NAC"
FILTER_NUMBER = "2"
CENTER_FILTER_WAVELENGTH = 747.7 <NM>
BANDWIDTH = 52.6 <NM>
EXPOSURE_DURATION = 192 <MS>
EXPOSURE_TYPE = AUTO
DETECTOR_TEMPERATURE = -42.55 <DEGC>
FOCAL_PLANE_TEMPERATURE = -35.94 <DEGC>
FILTER_TEMPERATURE = "N/A"
OPTICS_TEMPERATURE = -37.36 <DEGC>'''
testStringMultipleA = '''INSTRUMENT_ID = "MDIS-NAC"
FILTER_NUMBER = "2"
CENTER_FILTER_WAVELENGTH = 747.7
BANDWIDTH = 52.6
EXPOSURE_DURATION = 192
DETECTOR_TEMPERATURE = -42.55
FOCAL_PLANE_TEMPERATURE = -35.94
FILTER_TEMPERATURE = "N/A"'''
testStringMultipleB = '''INSTRUMENT_ID = "MDIS-NAC"
FILTER_NUMBER = "5"
CENTER_FILTER_WAVELENGTH = 747.7
BANDWIDTH = 52.6
EXPOSURE_DURATION = 150
EXPOSURE_TYPE = AUTO
DETECTOR_TEMPERATURE = -32.20
FOCAL_PLANE_TEMPERATURE = -25.94
FILTER_TEMPERATURE = "N/A"'''
testStringMultipleC = '''INSTRUMENT_ID = "MDIS-NAC"
FILTER_NUMBER = "2"
CENTER_FILTER_WAVELENGTH = 747.7
BANDWIDTH = 52.6
EXPOSURE_DURATION = 209
DETECTOR_TEMPERATURE = -47.85
FOCAL_PLANE_TEMPERATURE = -42.34
FILTER_TEMPERATURE = "N/A"'''