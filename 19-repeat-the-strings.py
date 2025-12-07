# Function to join given strings
def combo_string(a, b):

    aLength = len(a)
    bLength = len(b)

    short = a
    longer = b

    if aLength > bLength:
        short = b
        longer = a

    return short + longer + short

print(combo_string("Hi", "There"))