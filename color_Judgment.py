color_list = ["Brown","Green","Orange","Beige","Pink","Green","Gray","Red","Aqua","Copper","Yellow","Blue","White","Black","Cream"]

def ColorJudgment(color_1,color_2):
    judged_color = ""
    for colors in color_list:
        if color_1 in colors:
            judged_color = colors
            return judged_color

    for colors in color_list:
        if color_2 in colors:
            judged_color = colors
            return judged_color

    if judged_color == "":
        judged_color = "ニュートラル"
        return judged_color