
aantalminuten = input("hoeveel minuten?:")
aantalminuten = int(aantalminuten)
speelhal = 745
vrgamen = ( 39 / 5 ) * aantalminuten


aantalmensen = input("hoeveel mensen?:")
aantalmensen = int(aantalmensen)

speelhaltotaal = speelhal * aantalmensen 

print(speelhaltotaal , "cent")


vrtotaal = vrgamen * aantalmensen 
print(vrtotaal, "cent")

totaalprijs = vrtotaal + speelhaltotaal

print("‘Dit geweldige dagje-uit met",aantalmensen,"mensen in de Speelhal met" ,aantalminuten," minuten VR kost je maar" ,totaalprijs ,"cent’")




