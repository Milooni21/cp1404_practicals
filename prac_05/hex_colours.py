def main():
    COLOUR_TO_CODE = {
        "AntiqueWhite": "#faebd7", "BlanchedAlmond": "#ffebcd",
        "burlywood3": "	#cdaa7d", "CadetBlue2": "#8ee5ee",
        "chartreuse4": "#458b00", "coral": "#ff7f50",
        "coral3": "#cd5b45", "CornflowerBlue": "#6495ed",
        "cornsilk2": "	#eee8cd", "DarkGoldenrod": "#b8860b"}

    colour = input("Enter colour: ")
    while colour != "":
        if colour in COLOUR_TO_CODE:
            print("{} = {}".format(colour, COLOUR_TO_CODE.get(colour)))
        else:
            print("Invalid colour")
        colour = input("Enter colour: ")


main()
