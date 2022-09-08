
aantalminuten = input("hoeveel minuten?:")
aantalminuten = int(aantalminuten)
speelhal = float(7.45)
vrgamen = (0.39 / 5) * aantalminuten


aantalmensen = input("hoeveel mensen?:")
aantalmensen = int(aantalmensen)

speelhaltotaal = speelhal * aantalmensen 

print(speelhaltotaal , "euro")


vrtotaal = vrgamen * aantalmensen 
print(vrtotaal, "euro")

totaalprijs = vrtotaal + speelhaltotaal

print("‘Dit geweldige dagje-uit met", aantalmensen ,"mensen in de Speelhal met" , aantalminuten," minuten VR kost je maar" , totaalprijs ,"euro’")




