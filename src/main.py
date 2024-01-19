# color-scheme-framework-via-ChatGPT by Brett Fraley

# Most code will probably live here in main.py, we'll see where it goes.

class ColorScheme:
    def __init__(self, primary, secondary, accent_1, accent_2, accent_3):
        self.primary = primary
        self.secondary = secondary
        self.accent_1 = accent_1
        self.accent_2 = accent_2
        self.accent_3 = accent_3

testSampleScheme = [
    ['#3498db', '#2ecc71', '#f39c12', '#e74c3c', '#95a5a6']
]

# Consume list of color schemes, producing list of color scheme objects
# Note: need to make ColorScheme more flexible, and not use scheme[index]
# explicitly for assignment.

def initColorSchemes(schemes):
    colorSchemeObjects = []

    for scheme in schemes:
        schemeObj = ColorScheme(
            scheme[0],
            scheme[1],
            scheme[2],
            scheme[3],
            scheme[4]
        )

        print(schemeObj.primary)
        colorSchemeObjects.append(schemeObj)
    
    return colorSchemeObjects

test = initColorSchemes(testSampleScheme)[0]

# CSS
# Note: this could be made rather generic and modular

def writeStyleRule(className, rule, val):
    return f".{className} " + f"{{ {rule} : {val} }}" # .primary { background-color: blue }

def testWriteStyleRule():
    css = writeStyleRule('primary', 'background-color', test.primary)
    return css

assert testWriteStyleRule() == '.primary { background-color : #3498db }'


# What should really be done is a translation of data
# so that schemes already exist as objects in an imported file

sampleFullSchemes = [
    ['#3498db', '#2ecc71',  '#f39c12', '#e74c3c', '#95a5a6' ],

    ['#27ae60', '#34495e',  '#e67e22', '#c0392b', '#3498db' ],

    ['#1abc9c', '#2c3e50',  '#f39c12', '#e74c3c', '#3498db' ],

    ['#9b59b6', '#16a085',  '#e67e22', '#c0392b', '#2c3e50' ],

    ['#3498db', '#2ecc71',  '#f39c12', '#e74c3c', '#1abc9c' ],

    ['#27ae60', '#34495e',  '#e67e22', '#c0392b', '#9b59b6' ],

    ['#1abc9c', '#2c3e50',  '#f39c12', '#e74c3c', '#27ae60' ],

    ['#3498db', '#2ecc71',  '#f39c12', '#e74c3c', '#8e44ad' ],

    ['#27ae60', '#34495e',  '#e67e22', '#c0392b', '#9b59b6' ],

    ['#1abc9c', '#2c3e50',  '#f39c12', '#e74c3c', '#3498db' ],

    ['#9b59b6', '#16a085',  '#e67e22', '#c0392b', '#27ae60' ],

    ['#3498db', '#2ecc71',  '#f39c12', '#e74c3c', '#1abc9c' ],

    ['#27ae60', '#34495e',  '#e67e22', '#c0392b', '#9b59b6' ],

    ['#1abc9c', '#2c3e50',  '#f39c12', '#e74c3c', '#27ae60' ],

    ['#3498db', '#2ecc71',  '#f39c12', '#e74c3c', '#8e44ad' ],

    ['#27ae60', '#34495e',  '#e67e22', '#c0392b', '#3498db' ],

    ['#1abc9c', '#2c3e50',  '#f39c12', '#e74c3c', '#9b59b6' ],

    ['#9b59b6', '#16a085',  '#e67e22', '#c0392b', '#27ae60' ],

    ['#3498db', '#2ecc71',  '#f39c12', '#e74c3c', '#1abc9c' ],

    ['#27ae60', '#34495e',  '#e67e22', '#c0392b', '#9b59b6' ],
]

schemeTypes = [
    'primary',
    'secondary',
    'accent_1'
    'accent_2',
    'accent_3'
]

htmlFile = [
    """<html>',
       <style>
            .color-block {
                width: 100px;
                height: 100px;
            }
       </style>
    """
]

colorSchemes = initColorSchemes(sampleFullSchemes)

testLines = []

for colorScheme in sampleFullSchemes:

    for i in range(len(colorScheme) -1 ):
        # style = writeStyleRule( { schemeTypes[i] }, 'background-color', { colorScheme[i] })

        style = f"background-color: {colorScheme[i]}"
        line = f"<div class='color-block' style = '{style}'></div>\n"
        testLines.append(line)

f = open("test-schemes.html", "a")
f.writelines(testLines)
f.close()

# #open and read the file after the appending:
# f = open("demofile3.txt", "r")
# print(f.read()) 
