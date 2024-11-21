import string
#### Fonction secondaire
def ispalindrome(s):
    """
    Vérifie que la chaine de caractères en argument est un palindrome
    Args :
        s : chaine de caractères
    Returns :
        ispalindrome(s) : True or False
    >>> ispalindrome(kayak)
    True
    >>> ispalindrome(Le lapin est mignon)
    False
    """
    table = str.maketrans("éèêëàâäîïôùûç","eeeeaaaiiouuc")
    table_ponc = str.maketrans("","",string.punctuation)
    chaine_sans_espace = s.replace(" ","",-1).lower()
    chaine = chaine_sans_espace.translate(table).translate(table_ponc)
    si = chaine[::-1]
    if chaine==si:
        return True   
    return False

#### Fonction principale
def main():
    # vos appels à la fonction secondaire ici
    print("Le petit cheval est content",ispalindrome("Le petit cheval est content"))
    print("J'ai acheté, il me semble, un canapé."
        ,ispalindrome("J'ai acheté, il me semble, un canapé."))
    print("helicoptere",ispalindrome("helicoptere"))
    help(ispalindrome)
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
