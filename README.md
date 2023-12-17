# Ülesanne 1: Laius-Esmalt Otsing (Breadth-First Search, BFS) Implementatsioon 
1.Rakenda laius-esmalt otsingu algoritm (BFS) vabalt valitud 
programmeerimiskeeles. 

2.Näita, kuidas algoritm töötab, kasutades konkreetset graafi näidet. 

Vastus esitatud koodifailina laius-esmalt.py

# Ülesanne 2: Sügavus-Esmalt Otsing (Depth-First Search, DFS) Implementatsioon 
1. Rakenda sügavus-esmalt otsingu algoritm (DFS) vabalt valitud programmeerimiskeeles. 

Vastus esitatud koodifailina sõõgavus-esmalt.py

2. Analüüsi selle algoritmi aja- ja ruumikomplekssust. 

Selle algoritmi ajakomplekssus on O(V+E), kus V on sõlmede arv ja E on servade arv graafis.
Ruumikomplekksus on O(V).

# Ülesanne 3: Dijkstra Algoritmi Teoreetiline Analüüs 
1. Kirjelda Dijkstra algoritmi ja selle kasutamist lühima tee leidmiseks graafides.
   
Dijkstra leiab lühimad teed alguspunktist kõigi teiste graafide tippudeni. Samm sammult määratakse alguspunkt, mis määratakse nulliks ja teised tippude kaugused on lõpmatuseni. Valitakse prioriteetjärjekorrast sõlm, mille kaugus on hetkel kõige väiksem, vaadeldakse sõlme naabersõlmi. Kui uus tee kaalutud kaugusega naabersõlme kaudu on väiksem, kui senine teadaolev kaugus, siis uuendatakse naabersõlme kaugust ja korrratakse seda seni, kõik sõlmed on külastatud või lõpmatuseni kauged. Kui lõppeb kõikide sõlmede külastamine, on iga sõlme kaugus algussõlmest leitud.

2. Arutle, millistes olukordades on Dijkstra algoritm eriti efektiivne ja millistes olukordades see võib ebaefektiivne olla.
   
Dijkstra on efektiivne, kui graafis ei ole tihti muutuvaid kaalusid. See sobib navigeermise, marsuudiplaneermise ja võrgujuhtimise rakendustesse, kui vaja on leida lühimat aadressi. On ebaefektiivne, kui mingi kaal pole nullist suurem ehk negatiivne. Kui oleks vaja leida kõik teed, mitte punktist A punkti B lühim, siis selleks juhuks pole Dijkstra parim.

# Ülesanne 4: Bellman-Fordi Algoritmi Teoreetiline Analüüs 
1. Kirjelda Bellman-Fordi algoritmi ja selle erinevust Dijkstra algoritmist.

Bellman-Fordi algoritm on sarnane Dijkstraga, erinevus seisneb selles, et siin saab kasutada ka negatiivseid kaale ja tsükleid. Ajaliselt on Bellman keerulisem, kui Dijkstra. Samuti ajamahukam.

2. Arutle, kuidas Bellman-Fordi algoritm suudab tuvastada negatiivseid tsükleid graafides ja milline on selle praktiline tähtsus.
   
Kasutab selleks V-1 meetodit, kus V on sõlmede arv, et leida lühimat teed. Peale selle meetodi kasutamist, kui mõni tee väheneb, siis see tähendab, et graafis on negatiivne tsükkel. Praktiliselt tähendab see seda, et negatiivsed tüklid võivad tekitada probleeme kui soovitakse leida lühemat teed.

# Ülesanne 5: Graafide Värvimise Probleem 
1. Kirjelda graafide värvimise probleemi olemust ja selle tähtsust arvutiteaduses.
   
Graafide värvimise probleem seisneb selles, et iga graafi sõlm tuleb määrata kindlale värvile nii, et kaks omavahel ühendatud sõlme ei oleks sama värviga. Soovitakse leida väikseimat võimalikku värvide arvu. Arvutiteaduses aitab see kaasa optimeermisprobleemidele, erinevate tarkvarade kokkupõrgete vältimiseks jne. Värvidega sorteeritus kasvatab jõudlust ja tõhusust, efektiivsust ressursside kasutamisel.

2. Arutle, kuidas graafide värvimist saab kasutada ressursside jaotamise ja konfliktide lahendamise probleemides. 

Näiteks tööülesannete jaotamisel, olgu need tarkvaralised või reaalelus, siis saab teha sõlmed, kus iga sõlm tähistab teatud tööülesannet ja servad näitavad nende vahelist sõltuvust. See aitab töö tegemise efektiivsusele kaasa ega teki konfliktne, kes millist ülesannet täitma pidi. Graafide värvimist saaks kasutada ka näiteks sidevõrkudes, kus graafi sõlmed näitavad sidejaamu ja seadmeid ning servad seda, et need samad seadmed ei tohi kasutada sama sagedusriba, et vältida signaalide ülekostuvust või segunemist.

# Boonusülesanne (2 punkti): P vs NP Probleemi Ülevaade 
1. Kirjelda P vs NP probleemi olemust ja selle tähtsust arvutiteaduses.
   
P vs. NP probleem on üks arvutiteaduse fundamentaalsemaid küsimusi, mis käsitleb algoritmide tõhusust ja probleemide lahendamise keerukust. Probleem seisneb selles, kas iga probleem, mille lahenduse saab kiiresti kontrollida, saab ka kiiresti lahendada.

2. Arutle, miks on P vs NP probleemi lahendamine oluline ja millised võiksid olla selle lahendamise tagajärjed.
See on oluline, sest sellest sõltub efektiivsus ja asjade optimeerimine, nt mõne programmi tõhusus ja ülesannete jaotamine ning probleemide lahendamine aja ja ruumikomplekksust arvesse võttes.
