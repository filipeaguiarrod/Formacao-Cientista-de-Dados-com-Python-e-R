Pessoas = ['João','Pedro','Maria','João','Pedrão','Eduardo']

def remove_duplicates(List):
    List2 = []
    for n in List:
        if n not in List2:
            List2.append(n)
    return(List2)
