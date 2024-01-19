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
