import os
import shutil

src_dir = "content/mechatronika/subs"
tmp_dir = "content/mechatronika/subs_tmp"

if not os.path.exists(tmp_dir):
    os.makedirs(tmp_dir)

# move all files to tmp_dir
for i in range(1, 27):
    if os.path.exists(f"{src_dir}/{i}.tex"):
        shutil.move(f"{src_dir}/{i}.tex", f"{tmp_dir}/{i}.tex")

def get_body(filename):
    with open(f"{tmp_dir}/{filename}") as f:
        lines = f.readlines()
    # skip subsection line
    body = []
    for line in lines:
        if line.startswith("\\subsection{"):
            continue
        body.append(line)
    return "".join(body).strip()

def write_file(num, title, body):
    with open(f"{src_dir}/{num}.tex", "w") as f:
        f.write(f"\\subsection{{{title}}}\n\n{body}\n")

# Mappings
titles = {
    1: "Hasonlítsa össze a vezérlést és a szabályozást: a hatáslánc jellege, zavarjelekkel szembeni ellenállás, a mért mennyiség fajtája, reakció idő, illetve az irányításhoz felhasznált eszközök költsége szerint, valamint szemléltesse a hatásláncokat blokkdiagram segítségével!",
    2: "Ismertesse az alábbi fogalmakat: rendszer, bemenet, kimenet, lineáris/nem lineáris rendszer, statikus/dinamikus rendszer, időinvariáns/idővariáns rendszer. Válaszában térjen ki a kauzalitás és az autonómia fogalmaira is!",
    3: "Hasonlítsa össze a diszkrét idejű rendszerek leírására szolgáló matematikai modellek típusait (állapottér modell, ARMA modell, impulzusátviteli függvény)!",
    4: "Ismertesse a diszkrét idejű konvolúció szerepét, összefüggését! Egy valós példán keresztül mutassa be a rendszer átmeneti függvényének származtatását a súlyfüggvénye ismeretében!",
    5: "Adott két diszkrét idejű átviteli függvény. Vezesse le az eredő átviteli függvény összefüggését, ha a két átviteli függvény sorba, párhuzamosan, illetve visszacsatolva (pozitív és negatív) kapcsolódik egymáshoz. Mutassa be, a hatásvázlat átalakításának szabályait (elágazási pont áthelyezése tag mögé és tag elé, illetve összegzési pont áthelyezése tag mögé és tag elé)!",
    6: "A lineáris időinvariáns (LTI) rendszerek diszkrét idejű állapottér modelljének felhasználásával, előretartó Euler módszer segítésével vezesse le a folytonos idejű lineáris időinvariáns (LTI) rendszerek állapottér modellt!",
    7: "A z transzformáció összefüggését felhasználva ismertesse a Laplace transzformáció definícióját!",
    8: "Igazolja a Dirac impulzus, az egységugrás, valamint az exponenciális függvények Laplace transzformáltjait!",
    9: "Ismertesse az egytárolós arányos tag súly és átmeneti függvényeit! Válaszában térjen ki az időállandó fogalmára!",
    10: "Ismertesse az kéttárolós arányos tag súly és átmeneti függvényeit! Válaszában térjen ki a minőségi jellemzőkre!",
    11: "Mutassa be a lineáris időinvariáns (LTI) rendszerek esetén folytonos idejű állapottér modell rendszermátrixának sajátértékei és a rendszer átviteli függvényének pólusai közötti összefüggést!",
    12: "Ismertesse a frekvencia-átviteli függvény fogalmát, illetve annak megjelenítési módjait (Bode diagram)!",
    13: "Vezesse le a Fourier sorfejtés komplex alakját!",
    14: "A Fourier sorfejtés miként általánosítható nem periodikus (lecsengő) függvényekre? Ismertesse a Fourier transzformáció származtatását!",
    15: "Ismertesse a következő fogalmakat: extenzív és intenzív fizikai mennyiségek, átmenő és keresztváltozók, energiatárolók és disszipatív elemek, csatolt kétpólus elem (transzformátor és girátor)!",
    16: "Adja meg az villamos rendszer (kapcsolt elektromechanikai), haladó és forgómozgású mechanikai rendszerek és az áramlástechnikai (pneumatikus és hidraulikai) rendszerek koncentrált paraméterű leírása esetén az átmenő és keresztváltozó típusát, valamint az energiatárolókat (amennyiben léteznek) és disszipatív elemeket.",
    17: "Mutassa be, milyen módszerekkel határozható meg a kereszt, illetve átmenő változók értékei különféle források figyelembevétele esetén! Ismertesse az egyes módszerek alkalmazásának lépéseit egy példa segítségével!",
    18: "Egy adott, tanult példa (egyenáramú motor) kapcsán ismertesse a struktúra gráf és az impedancia hálózat felrajzolásának lépéseit. Válaszában térjen ki az egy oldalra redukálás módszerére a rendszerek közötti átjárásokat biztosító fizikai összefüggések alapján!",
    19: "Egy adott, tanult példa (fogaskerékhajtómű, fogaskerék-fogasléc) kapcsán ismertesse a struktúra gráf és az impedancia hálózat felrajzolásának lépéseit. Válaszában térjen ki az egy oldalra redukálás módszerére a rendszerek közötti átjárásokat biztosító fizikai összefüggések alapján!",
    20: "Egy adott, tanult példa (hidraulikus és pneumatikus munkahenger) kapcsán ismertesse a struktúra gráf és az impedancia hálózat felrajzolásának lépéseit. Válaszában térjen ki az egy oldalra redukálás módszerére a rendszerek közötti átjárásokat biztosító fizikai összefüggések alapján!"
}

# New 1
write_file(1, titles[1], get_body("1.tex"))
# New 2
write_file(2, titles[2], get_body("2.tex"))
# New 3 (merge 4, 5, 6)
body3 = "\\textbf{Állapottér modell:}\n" + get_body("4.tex") + "\n\n\\textbf{ARMA modell:}\n" + get_body("5.tex") + "\n\n\\textbf{Impulzusátviteli függvény:}\n" + get_body("6.tex")
write_file(3, titles[3], body3)

mappings = {
    4: "7.tex",
    5: "8.tex",
    6: "9.tex",
    7: "10.tex",
    8: "11.tex",
    9: "13.tex",
    10: "14.tex",
    11: "16.tex",
    12: "17.tex",
    13: "18.tex",
    14: "19.tex",
    15: "20.tex",
    16: "21.tex",
    17: "22.tex",
    18: "23.tex",
    19: "24.tex",
    20: "25.tex"
}

for new_num, old_file in mappings.items():
    write_file(new_num, titles[new_num], get_body(old_file))

# Check mapping is correct
print("Done renaming files.")
