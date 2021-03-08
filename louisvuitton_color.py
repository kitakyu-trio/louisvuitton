color_list = ["ECARLATE","SCARLET","ROUGE","RED","MARINE","MAGNOLIA","NOIR","ROSE","PINK","GALET","DUNE","POUDRE","POWDER","CARAMEL","BLACK","POPPY","COQUELICOT","BLEU","BLUE","BORDEAUX","GRIS","GREY","NERO","VERT","LAGON"]

def VuittonColor(color):
    correct_color = ""

    for name in color_list:
        if name in color:
            correct_color = color

    return correct_color