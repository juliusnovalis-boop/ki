#!/usr/bin/env python3
"""
Générateur des maquettes « Néon sombre » de RENTAL CAR.

  python3 design/outils/generer.py

1. écrit les pages HTML des maquettes dans design/maquettes/
2. écrit les petites pages HTML servant à fabriquer les images PNG (icônes,
   fonds, cadres, logo) dans un dossier temporaire ;
3. appelle rendre.mjs (Node + Chromium sans interface) qui produit :
      design/maquettes/png/*.png   (captures des maquettes)
      design/assets/**.png         (images à importer dans Access)
      design/outils/cotes.json     (positions des contrôles en pixels)
4. écrit design/COTES.md (positions et tailles en cm pour Access).
"""
import html
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
DESIGN = ICI.parent
MAQ = DESIGN / "maquettes"
ASSETS = DESIGN / "assets"
SVG_DIR = ICI / "icones-svg"

C = dict(cyan="#00E5FF", violet="#9D5CFF", magenta="#FF2E97", vert="#2BFFA3",
         ambre="#FFC247", gris="#7F8BB0", clair="#9FB3E0", texte="#E6EDFF", fonce="#03121F")

DATE = "28/09/2026 20:06"


# --------------------------------------------------------------------------
# Icônes (Lucide, licence ISC)
# --------------------------------------------------------------------------
def svg(name, color, size=20, glow=0, stroke=2):
    raw = (SVG_DIR / f"{name}.svg").read_text()
    inner = re.search(r"<svg[^>]*>(.*)</svg>", raw, re.S).group(1)
    f = f"filter:drop-shadow(0 0 {glow}px {color});" if glow else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" '
            f'fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round" '
            f'style="display:block;{f}">{inner}</svg>')


def e(s):
    return html.escape(str(s))


def acc(nom, typ):
    """Attributs qui permettent de relever la position du contrôle."""
    return f'data-acc="{e(nom)}" data-type="{e(typ)}"'


# --------------------------------------------------------------------------
# Données (extraites de Database20.accdb)
# --------------------------------------------------------------------------
DONNEES = json.loads((ICI / "donnees.json").read_text())


def fdate(iso):
    y, m, d = iso[:10].split("-")
    return f"{d}/{m}/{y}"


def fcfa(n):
    return f"{n:,}".replace(",", " ")


# --------------------------------------------------------------------------
# Briques de mise en page
# --------------------------------------------------------------------------
MENU = [
    ("tableau", "Tableau de bord", "layout-dashboard"),
    ("reservations", "Réservations", "calendar-range"),
    ("clients", "Clients", "users"),
    ("voitures", "Voitures", "car"),
    ("marques", "Marques", "tag"),
    ("carburants", "Carburants", "fuel"),
    ("modeles", "Modèles", "layers"),
]


def page(titre, corps, rel="."):
    return f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>{e(titre)} · RENTAL CAR</title>
<link rel="stylesheet" href="{rel}/style.css"></head>
<body><div class="ecran" id="ecran">
{corps}
</div></body></html>"""


def coquille(actif, titre, fil, contenu):
    """Formulaire « Menu » : barre latérale + bandeau + zone de sous-formulaire."""
    nav = []
    for i, (cle, lib, ico) in enumerate(MENU):
        y = 128 + i * 52
        on = cle == actif
        img = f"../assets/icones/menu-{ico}-{'on' if on else 'off'}.png"
        if on:
            nav.append(f'<div class="nav-barre" style="top:{y}px" {acc("Barre_Active", "Rectangle")}></div>')
        nav.append(f'<div class="nav{" actif" if on else ""}" style="top:{y}px" {acc("BoutonNavigation_" + cle, "Bouton de navigation")}>'
                   f'<img src="{img}">{e(lib)}</div>')
    return f"""
<div class="menu" {acc("Fond_Menu", "Rectangle")}>
  <img class="abs" src="../assets/logo.png" style="left:18px;top:18px;width:188px;height:52px" {acc("Logo", "Image")}>
  <div class="rubrique" style="top:100px">NAVIGATION</div>
  {''.join(nav)}
  <div class="etat-systeme" {acc("Etat_Systeme", "Rectangle + étiquettes")}>
    <div class="l1"><span class="pt"></span>SYSTÈME EN LIGNE</div>
    <div class="l2">Database20.accdb<br>Version 2.0 · Libreville</div>
  </div>
</div>
<div class="entete" {acc("Entete", "Rectangle")}>
  <div class="titre" {acc("Titre_Page", "Étiquette")}>{e(titre)}</div>
  <div class="fil">RENTAL CAR &nbsp;/&nbsp; <b>{e(fil)}</b></div>
  <div class="date" style="left:862px;width:196px" {acc("Date_Heure", "Zone de texte")}>{svg("clock", C["cyan"], 16)}{DATE}</div>
  <div class="utilisateur" style="left:1082px" {acc("Utilisateur", "Image + étiquettes")}>
    <img src="../assets/icones/utilisateur.png" style="width:40px;height:40px">
    <div><div class="nom">admin</div><div class="role">Administrateur</div></div>
  </div>
  <div class="btn-rond" style="left:1276px;top:14px;border:1px solid {C['magenta']};background:#1A0B1E;box-shadow:0 0 12px rgba(255,46,151,.45)" {acc("Btn_Quitter", "Bouton")}>{svg("power", C["magenta"], 18)}</div>
</div>
<img class="ligne-neon" src="../assets/ligne-neon.png" {acc("Ligne_Neon", "Image")}>
<div class="contenu" id="contenu">
{contenu}
</div>"""


def panneau(nom, titre, x, y, w, h, interieur="", actions=(), accent=C["cyan"], sous_titre=None):
    act = ""
    if actions:
        act = '<div class="actions">' + "".join(
            f'<div class="btn-icone" {acc("Btn_" + a, "Bouton (ovale)")}>{svg(ICONES_ACTION[a], C["clair"], 16)}</div>'
            for a in actions) + "</div>"
    st = ""
    if sous_titre:
        st = f'<div class="sous-titre" style="left:{32 + len(titre) * 11 + 14}px">{e(sous_titre)}</div>'
    return f"""<div class="panneau" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px" {acc(nom, "Rectangle")}>
  <div class="tete"></div><div class="accent" style="background:{accent}"></div>
  <div class="titre-p">{e(titre)}</div>{st}{act}
  {interieur}
</div>"""


ICONES_ACTION = {"Ajouter": "plus", "Actualiser": "refresh-cw", "Rechercher": "search", "Imprimer": "printer"}


def champ(nom, lib, val, x, y, lw, w, kind="texte", droite=False):
    cls = "champ"
    if kind == "lecture":
        cls += " lecture"
    if droite:
        cls += " droite"
    extra = ""
    if kind == "liste":
        cls += " liste-der"
        extra = f'<span class="fleche">{svg_down()}</span>'
    typ = {"texte": "Zone de texte", "lecture": "Zone de texte (verrouillée)", "liste": "Zone de liste déroulante"}[kind]
    out = ""
    if lib:
        out += f'<div class="etiq" style="left:{x}px;top:{y}px;width:{lw}px">{e(lib)}</div>'
    out += f'<div class="{cls}" style="left:{x + (lw + 14 if lib else 0)}px;top:{y}px;width:{w}px" {acc(nom, typ)}>{e(val)}{extra}</div>'
    return out


def svg_down():
    return ('<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#7F8BB0" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round" style="display:block"><path d="m6 9 6 6 6-6"/></svg>')


def nav_enreg(x, y, texte="1 / 25"):
    ico = ["chevron-first", "chevron-left", "chevron-right", "chevron-last"]
    noms = ["Premier", "Precedent", "Suivant", "Dernier"]
    out = ""
    for i in range(2):
        out += f'<div class="btn-nav" style="left:{x + i * 46}px;top:{y}px" {acc("Btn_" + noms[i], "Bouton")}>{svg(ico[i], C["cyan"], 18)}</div>'
    out += f'<div class="compteur" style="left:{x + 92}px;top:{y}px;width:92px" {acc("Compteur", "Zone de texte")}>{e(texte)}</div>'
    for i in range(2, 4):
        out += f'<div class="btn-nav" style="left:{x + 184 + (i - 2) * 46}px;top:{y}px" {acc("Btn_" + noms[i], "Bouton")}>{svg(ico[i], C["cyan"], 18)}</div>'
    return out


def boutons_crud(x, y, w=150, gap=16):
    return (f'<div class="btn primaire" style="left:{x}px;top:{y}px;width:{w}px" {acc("Btn_Enregistrer", "Bouton")}>{svg("save", C["fonce"], 17)}Enregistrer</div>'
            f'<div class="btn danger" style="left:{x + w + gap}px;top:{y}px;width:{w}px" {acc("Btn_Supprimer", "Bouton")}>{svg("trash-2", C["magenta"], 17)}Supprimer</div>')


def liste(nom, cols, lignes, x, y, w, h, defil=True):
    """cols = [(titre, largeur_px, classe)]"""
    colg = "".join(f'<col style="width:{c[1]}px">' for c in cols)
    th = "".join(f'<th class="{c[2] if len(c) > 2 else ""}">{e(c[0])}</th>' for c in cols)
    trs = ""
    for l in lignes:
        trs += "<tr>" + "".join(
            f'<td class="{cols[i][2] if len(cols[i]) > 2 else ""}">{e(v)}</td>' for i, v in enumerate(l)) + "</tr>"
    nb_vis = max(1, (h - 36) // 27)
    d = ""
    if defil and len(lignes) > nb_vis:
        hh = max(30, int((h - 44) * nb_vis / len(lignes)))
        d = f'<div class="defil" style="height:{hh}px"></div>'
    return (f'<div class="liste" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px" {acc(nom, "Zone de liste")}>'
            f'<table><colgroup>{colg}</colgroup><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>{d}</div>')


# --------------------------------------------------------------------------
# Écrans
# --------------------------------------------------------------------------
CLIENTS = {c["CIN"]: c for c in DONNEES["Client"]}
RES = DONNEES["Reservation"]


def ecran_tableau():
    kpis = [
        ("CA", "Chiffre d'affaires", "104 261 200", "FCFA", "Total des locations", "cyan", "wallet"),
        ("Voitures", "Voitures", "60", "", "Véhicules dans la flotte", "violet", "car-front"),
        ("Clients", "Clients", "200", "", "Clients enregistrés", "magenta", "users"),
        ("Reservations", "Réservations", "25", "", "8 en cours aujourd'hui", "vert", "calendar-check"),
    ]
    out = ""
    for i, (n, lib, val, unit, sub, col, ico) in enumerate(kpis):
        x = 32 + i * (302 + 24)
        u = f"<small style='color:{C[col]}'>{unit}</small>" if unit else ""
        out += (f'<div class="kpi" style="left:{x}px;top:28px;background-image:url(../assets/cadres/kpi-{col}.png)" {acc("Carte_" + n, "Image (cadre) + étiquettes")}>'
                f'<div class="lib" style="color:{C[col]}">{e(lib)}</div><div class="val" {acc("Txt_" + n, "Zone de texte")}>{val}{u}</div>'
                f'<div class="sub">{e(sub)}</div><img src="../assets/icones/kpi-{ico}-{col}.png"></div>')

    # Voitures actuellement réservées (au 28/09/2026)
    import datetime as dt
    auj = dt.date(2026, 9, 28)
    lignes = []
    for r in RES:
        d0 = dt.date.fromisoformat(r["DateDebut"][:10])
        d1 = dt.date.fromisoformat(r["DateFin"][:10])
        if d0 <= auj <= d1:
            c = CLIENTS[r["Client"]]
            lignes.append([r["Voiture"], f'{c["Prénom"]} {c["Nom"]}', fdate(r["DateDebut"]), fdate(r["DateFin"]), f"{(d1 - auj).days} j"])
    l1 = liste("Liste_Voitures_Reservees",
               [("Matricule", 130, "mono"), ("Client", 220), ("Début", 130), ("Fin", 130), ("Restant", 150, "num cyan")],
               lignes, 20, 68, 780, 260, defil=False)
    p1 = panneau("Panneau_Reservees", "Voitures actuellement réservées", 32, 180, 820, 348, l1, actions=["Imprimer"],
                 sous_titre="8 EN COURS")

    top = [("01", "Cynthia", "Kombila", 18457500), ("02", "Junior", "Ondo", 11097500), ("03", "Léa", "Eyang", 10413000),
           ("04", "Cédric", "Nkoghe", 8021250), ("05", "Noëlle", "Mba", 7416000)]
    l2 = liste("Liste_Top5", [("#", 44, "cyan"), ("Prénom", 104), ("Nom", 104), ("CA (FCFA)", 148, "num")],
               [[a, b, c, fcfa(d)] for a, b, c, d in top], 20, 68, 400, 176, defil=False)
    stats = (f'<div class="stat" style="left:20px;top:262px;width:192px;height:70px" {acc("Stat_Duree", "Rectangle + zone de texte")}>'
             f'<div class="l">Durée moyenne</div><div class="v" style="color:{C["ambre"]}">69<small>jours</small></div></div>'
             f'<div class="stat" style="left:228px;top:262px;width:192px;height:70px" {acc("Stat_Occupation", "Rectangle + zone de texte")}>'
             f'<div class="l">Taux d’occupation</div><div class="v" style="color:{C["vert"]}">13,3<small>%</small></div></div>')
    p2 = panneau("Panneau_Top5", "5 meilleurs clients", 872, 180, 440, 348, l2 + stats, accent=C["violet"])

    # bandeau d'activité en bas
    act = (f'<div class="panneau" style="left:32px;top:548px;width:1280px;height:140px" {acc("Panneau_Flotte", "Rectangle")}>'
           f'<div class="tete"></div><div class="accent" style="background:{C["magenta"]}"></div><div class="titre-p">Flotte par marque</div>')
    marques = [("Audi", 12), ("BMW", 12), ("Ford", 12), ("Nissan", 12), ("Mercedes", 12)]
    for i, (m, n) in enumerate(marques):
        x = 24 + i * 250
        act += (f'<div class="stat" style="left:{x}px;top:66px;width:232px;height:58px">'
                f'<div class="l" style="top:10px">{m}</div><div class="v" style="top:26px;font-size:22px;color:{C["texte"]}">{n}<small>modèles</small></div>'
                f'<img src="../assets/icones/mini-tag.png" style="position:absolute;right:14px;top:15px;width:28px;height:28px"></div>')
    act += "</div>"
    return coquille("tableau", "Tableau de bord", "VUE D'ENSEMBLE", out + p1 + p2 + act)


def ecran_reservations():
    cli = (champ("Cbo_Client", "Client", "Jean Mboumba", 20, 68, 110, 440, "liste")
           + champ("Txt_Telephone", "Téléphone", "(+241) 62 54 85 85", 20, 112, 110, 440, "lecture")
           + champ("Txt_Email", "Email", "jean.mboumba1@example.com", 20, 156, 110, 440, "lecture"))
    p1 = panneau("Panneau_Client", "Informations client", 24, 20, 640, 208, cli, sous_titre="CL-0001")
    voi = (champ("Cbo_Voiture", "Voiture", "AB-3988-AA", 20, 68, 110, 440, "liste")
           + champ("Txt_Modele", "Modèle", "Audi Q6", 20, 112, 110, 440, "lecture")
           + champ("Txt_Marque", "Marque", "Audi", 20, 156, 110, 440, "lecture"))
    p2 = panneau("Panneau_Voiture", "Informations voiture", 680, 20, 640, 208, voi, accent=C["violet"])

    res = (champ("Txt_Code", "Code", "1", 20, 72, 60, 90, droite=True)
           + champ("Txt_DateDebut", "Date de début", "23/09/2026", 200, 72, 110, 140, droite=True)
           + champ("Txt_DateFin", "Date de fin", "24/10/2026", 474, 72, 94, 140, droite=True)
           + f'<div class="btn contour" style="left:736px;top:69px;width:92px" {acc("Btn_OK", "Bouton")}>{svg("check", C["cyan"], 17)}OK</div>'
           + nav_enreg(20, 124, "1 / 25")
           + boutons_crud(344, 121, w=150, gap=14)
           + '<div class="sep-v" style="left:856px;top:53px;height:130px"></div>'
           + f'<div class="etiq" style="left:872px;top:66px;width:90px">Durée</div>'
           + f'<div class="champ lecture droite" style="left:976px;top:66px;width:290px" {acc("Txt_Duree", "Zone de texte (calculée)")}>31 jour(s)</div>'
           + f'<div class="etiq" style="left:872px;top:118px;width:90px;line-height:42px;height:42px">Montant</div>'
           + f'<div class="champ fort" style="left:976px;top:118px;width:290px" {acc("Txt_Montant", "Zone de texte (calculée)")}>1 023 000 FCFA</div>')
    p3 = panneau("Panneau_Reservation", "Informations réservation", 24, 244, 1296, 184, res,
                 actions=["Ajouter", "Actualiser", "Rechercher", "Imprimer"])

    connus = {1: ("Audi Q6", "Audi"), 2: ("Audi A6", "Audi"), 3: ("Audi A7", "Audi"), 4: ("Audi Q3", "Audi"),
              5: ("BMW X1", "BMW"), 6: ("BMW X5", "BMW"), 7: ("Audi Q4", "Audi")}
    lignes = []
    for r in RES[:7]:  # 7 premières (modèle/marque relevés sur votre capture)
        c = CLIENTS[r["Client"]]
        mo, ma = connus[r["IdReservation"]]
        lignes.append([r["IdReservation"], fdate(r["DateDebut"]), fdate(r["DateFin"]), c["Prénom"], c["Nom"], r["Voiture"], mo, ma])
    l = liste("Liste_Reservations", [("Code", 80, "cyan"), ("Début", 140), ("Fin", 140), ("Prénom", 160), ("Nom", 170),
                                     ("Matricule", 170, "mono"), ("Modèle", 170), ("Marque", 226)],
              lignes, 20, 64, 1256, 168, defil=True)
    p4 = panneau("Panneau_Liste", "Liste des réservations", 24, 444, 1296, 252, l, actions=["Imprimer"],
                 accent=C["magenta"], sous_titre="25 ENREGISTREMENTS")
    return coquille("reservations", "Réservations", "GESTION DES RÉSERVATIONS", p1 + p2 + p3 + p4)


def ecran_formulaire(cle, titre, fil, titre_form, champs, titre_liste, cols, lignes, largeur_form=560, hauteur=None,
                     sous_titre_liste=None, accent_liste=C["violet"], compteur="1 / 1", y0=24):
    """Écran type : fiche à gauche, liste à droite."""
    lw = 150
    iw = largeur_form - 40 - lw - 14
    inner = ""
    y = 80
    for (n, lib, val, kind, *opt) in champs:
        w = opt[0] if opt else iw
        inner += champ(n, lib, val, 20, y, lw, w, kind, droite=False)
        y += 52
    y += 8
    inner += nav_enreg((largeur_form - 276) // 2, y, compteur)
    y += 58
    inner += f'<div class="sep-h" style="left:0;top:{y}px;width:{largeur_form - 2}px"></div>'
    y += 16
    inner += boutons_crud((largeur_form - 316) // 2, y)
    h = hauteur or (y + 40 + 24)
    if y0 is None:  # centré verticalement
        y0 = (716 - h) // 2
    p1 = panneau("Panneau_Fiche", titre_form, 24, y0, largeur_form, h, inner,
                 actions=["Ajouter", "Actualiser", "Rechercher", "Imprimer"])
    lx = 24 + largeur_form + 16
    lwid = 1344 - 24 - lx
    l = liste("Liste_" + cle.capitalize(), cols, lignes, 20, 68, lwid - 42, h - 88)
    p2 = panneau("Panneau_Liste", titre_liste, lx, y0, lwid, h, l, actions=["Imprimer"], accent=accent_liste,
                 sous_titre=sous_titre_liste)
    return coquille(cle, titre, fil, p1 + p2)


def ecran_clients():
    c = CLIENTS["CL-0001"]
    champs = [("Txt_CIN", "Code client", c["CIN"], "texte", 200), ("Txt_Permis", "N° de permis", c["NumPermis"], "texte", 220),
              ("Txt_Prenom", "Prénom", c["Prénom"], "texte"), ("Txt_Nom", "Nom", c["Nom"], "texte"),
              ("Cbo_Sexe", "Sexe", c["Sexe"], "liste", 100), ("Txt_Adresse", "Adresse", c["Adresse"], "texte"),
              ("Txt_Telephone", "Téléphone", c["Téléphone"], "texte"), ("Txt_Email", "Email", c["Email"], "texte")]
    lignes = [[x["CIN"], x["NumPermis"], x["Prénom"], x["Nom"], x["Sexe"], x["Adresse"]] for x in DONNEES["Client"][:21]]
    cols = [("Code", 90, "mono cyan"), ("Permis", 140, "mono"), ("Prénom", 100), ("Nom", 110), ("Sexe", 56), ("Adresse", 200)]
    return ecran_formulaire("clients", "Clients", "GESTION DES CLIENTS", "Fiche client", champs, "Liste des clients", cols,
                            lignes, largeur_form=540, hauteur=672, sous_titre_liste="200 CLIENTS", compteur="1 / 200")


def ecran_voitures():
    champs = [("Txt_Matricule", "Matricule", "AB-2344-AA", "texte", 200), ("Txt_Annee", "Année du modèle", "2026", "texte", 120),
              ("Txt_Couleur", "Couleur", "Gris", "texte"), ("Txt_Puissance", "Puissance", "15 CV", "texte", 120),
              ("Txt_CoutJour", "Coût par jour", "95 000 FCFA", "texte", 200), ("Cbo_Modele", "Modèle", "Audi Q5", "liste"),
              ("Cbo_Carburant", "Carburant", "Diesel", "liste"), ("Cbo_Marque", "Marque", "Audi", "liste")]
    v = [("AB-2344-AA", "2026", "Gris", "15CV", "95 000"), ("LB-8235-AA", "2024", "Bleu", "11CV", "42 000"),
         ("RT-7002-AA", "2025", "Blanc", "13CV", "46 000"), ("CD-2481-AA", "2022", "Bleu", "7CV", "27 500"),
         ("DF-1111-AA", "2022", "Noir", "7CV", "27 500"), ("EF-4262-AA", "2025", "Gris", "13CV", "60 000"),
         ("FG-2892-AA", "2025", "Jaune", "13CV", "48 000"), ("FJ-4673-AA", "2023", "Argent", "9CV", "65 000"),
         ("GA-5495-AA", "2024", "Rouge", "11CV", "40 000"), ("KL-8098-AA", "2023", "Gris", "9CV", "33 000"),
         ("MN-6728-AA", "2023", "Jaune", "9CV", "35 000"), ("QS-6865-AA", "2024", "Noir", "11CV", "40 000")]
    cols = [("Matricule", 130, "mono cyan"), ("Année", 90), ("Couleur", 120), ("Puissance", 110), ("Coût / jour (FCFA)", 170, "num")]
    return ecran_formulaire("voitures", "Voitures", "GESTION DE LA FLOTTE", "Fiche voiture", champs, "Liste des voitures", cols,
                            [list(x) for x in v], largeur_form=540, hauteur=672, sous_titre_liste="60 VÉHICULES",
                            compteur="1 / 60")


def ecran_marques():
    champs = [("Txt_IdMarque", "Identifiant", "1", "texte", 120), ("Txt_Marque", "Marque", "Audi", "texte")]
    lignes = [[m["IdMarque"], m["Marque"], "12"] for m in DONNEES["Marque"]]
    cols = [("ID", 80, "cyan"), ("Marque", 300), ("Modèles", 120, "num")]
    return ecran_formulaire("marques", "Marques", "RÉFÉRENTIEL DES MARQUES", "Fiche marque", champs, "Liste des marques",
                            cols, lignes, largeur_form=560, sous_titre_liste="5 MARQUES", compteur="1 / 5",
                            y0=None)


def ecran_carburants():
    champs = [("Txt_IdType", "Identifiant", "1", "texte", 120), ("Txt_Type", "Type", "Diesel", "texte")]
    lignes = [[c["IdType"], c["Type"]] for c in DONNEES["Carburant"]]
    cols = [("ID", 80, "cyan"), ("Type de carburant", 400)]
    return ecran_formulaire("carburants", "Carburants", "RÉFÉRENTIEL DES CARBURANTS", "Fiche carburant", champs,
                            "Types de carburant", cols, lignes, largeur_form=560, sous_titre_liste="3 TYPES",
                            compteur="1 / 3", y0=None)


def ecran_modeles():
    marques = {m["IdMarque"]: m["Marque"] for m in DONNEES["Marque"]}
    champs = [("Txt_IdModele", "Identifiant", "1", "texte", 120), ("Txt_Modele", "Modèle", "Audi Q5", "texte"),
              ("Cbo_Marque", "Marque", "Audi", "liste")]
    lignes = [[m["IdModele"], m["Modele"], marques[m["Marque"]]] for m in DONNEES["Modele"][:16]]
    cols = [("ID", 80, "cyan"), ("Modèle", 260), ("Marque", 200)]
    return ecran_formulaire("modeles", "Modèles", "RÉFÉRENTIEL DES MODÈLES", "Fiche modèle", champs, "Liste des modèles",
                            cols, lignes, largeur_form=560, sous_titre_liste="60 MODÈLES", compteur="1 / 60",
                            y0=None)


def ecran_login():
    x, y, w, h = 574, 120, 420, 544
    corps = f"""
<img class="abs" src="../assets/fonds/fond-login.png" style="left:0;top:0;width:1568px;height:784px" {acc("Fond_Login", "Image (Image du formulaire)")}>
<div class="panneau" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:#0B1229;border-color:#23336A" {acc("Carte_Login", "Rectangle")}>
  <img class="abs" src="../assets/icones/login-cadenas.png" style="left:{w // 2 - 40}px;top:32px;width:80px;height:80px" {acc("Icone_Cadenas", "Image")}>
  <div class="abs" style="left:0;top:124px;width:{w}px;text-align:center;font:600 30px Titre;letter-spacing:4px">RENTAL CAR</div>
  <div class="abs" style="left:0;top:166px;width:{w}px;text-align:center;font:400 12px Mono;letter-spacing:3px;color:{C['cyan']}">ACCÈS SÉCURISÉ</div>
  <div class="sep-h" style="left:40px;top:200px;width:{w - 80}px"></div>
  <div class="abs" style="left:40px;top:222px;font:600 12px Titre;letter-spacing:2px;color:#8A97BC">NOM D’UTILISATEUR</div>
  <div class="champ" style="left:40px;top:244px;width:{w - 80}px;height:42px;line-height:40px;padding-left:44px" {acc("Txt_Utilisateur", "Zone de texte")}>admin</div>
  <img class="abs" src="../assets/icones/champ-user.png" style="left:50px;top:253px;width:24px;height:24px" {acc("Icone_User", "Image")}>
  <div class="abs" style="left:40px;top:304px;font:600 12px Titre;letter-spacing:2px;color:#8A97BC">MOT DE PASSE</div>
  <div class="champ" style="left:40px;top:326px;width:{w - 80}px;height:42px;line-height:40px;padding-left:44px;letter-spacing:3px" {acc("Txt_MotDePasse", "Zone de texte (Masque : Mot de passe)")}>••••••••</div>
  <img class="abs" src="../assets/icones/champ-lock.png" style="left:50px;top:335px;width:24px;height:24px" {acc("Icone_Lock", "Image")}>
  <div class="btn primaire" style="left:40px;top:398px;width:{w - 80}px;height:46px" {acc("Btn_Connexion", "Bouton")}>{svg("log-in", C["fonce"], 18)}Se connecter</div>
  <div class="abs" style="left:0;top:470px;width:{w}px;text-align:center;font:400 12px Texte;color:#56638A">Mot de passe oublié ? Contactez l’administrateur.</div>
  <div class="abs" style="left:0;top:500px;width:{w}px;text-align:center;font:400 11px Mono;color:#3E4A70;letter-spacing:1px">© 2026 RENTAL CAR · LIBREVILLE</div>
</div>"""
    return corps


ECRANS = [
    ("00-connexion", "Connexion", ecran_login),
    ("01-tableau-de-bord", "Tableau de bord", ecran_tableau),
    ("02-reservations", "Réservations", ecran_reservations),
    ("03-clients", "Clients", ecran_clients),
    ("04-voitures", "Voitures", ecran_voitures),
    ("05-marques", "Marques", ecran_marques),
    ("06-carburants", "Carburants", ecran_carburants),
    ("07-modeles", "Modèles", ecran_modeles),
]


# --------------------------------------------------------------------------
# Images PNG à importer dans Access
# --------------------------------------------------------------------------
def asset_page(w, h, corps, fond="transparent"):
    return f"""<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="{MAQ.as_uri()}/style.css">
<style>html,body{{margin:0;background:{fond};}} #a{{position:relative;width:{w}px;height:{h}px;overflow:hidden}}</style></head>
<body><div id="a">{corps}</div></body></html>"""


def icone_centree(name, color, box, size, glow, stroke=2, cercle=None):
    c = ""
    if cercle:
        c = (f'<div style="position:absolute;left:{(box - cercle[0]) / 2}px;top:{(box - cercle[0]) / 2}px;width:{cercle[0]}px;'
             f'height:{cercle[0]}px;border-radius:50%;background:{cercle[1]};border:1px solid {cercle[2]}"></div>')
    off = (box - size) / 2
    return c + f'<div style="position:absolute;left:{off}px;top:{off}px">{svg(name, color, size, glow, stroke)}</div>'


def assets_jobs(tmp):
    jobs = []

    def add(out, w, h, corps, fond="transparent"):
        p = tmp / (out.replace("/", "_") + ".html")
        p.write_text(asset_page(w, h, corps, fond))
        jobs.append({"html": p.as_uri(), "out": str(ASSETS / out), "w": w, "h": h, "transparent": fond == "transparent", "sel": "#a"})

    # Icônes du menu (28 x 28 px) : éteinte (gris) et allumée (cyan lumineux)
    for _, _, ico in MENU:
        add(f"icones/menu-{ico}-off.png", 28, 28, icone_centree(ico, C["gris"], 28, 20, 0))
        add(f"icones/menu-{ico}-on.png", 28, 28, icone_centree(ico, C["cyan"], 28, 20, 3))
    # Icônes des boutons d'action (20 x 20 px, sur bouton ovale 34 px)
    for a, ico in ICONES_ACTION.items():
        add(f"icones/action-{ico}.png", 20, 20, icone_centree(ico, C["clair"], 20, 16, 0))
    for ico in ["chevron-first", "chevron-left", "chevron-right", "chevron-last"]:
        add(f"icones/nav-{ico}.png", 20, 20, icone_centree(ico, C["cyan"], 20, 18, 0))
    add("icones/bouton-enregistrer.png", 20, 20, icone_centree("save", C["fonce"], 20, 17, 0))
    add("icones/bouton-supprimer.png", 20, 20, icone_centree("trash-2", C["magenta"], 20, 17, 0))
    add("icones/bouton-ok.png", 20, 20, icone_centree("check", C["cyan"], 20, 17, 0))
    add("icones/bouton-connexion.png", 20, 20, icone_centree("log-in", C["fonce"], 20, 18, 0))
    add("icones/quitter.png", 24, 24, icone_centree("power", C["magenta"], 24, 18, 0))
    add("icones/horloge.png", 18, 18, icone_centree("clock", C["cyan"], 18, 16, 0))
    add("icones/mini-tag.png", 28, 28, icone_centree("tag", C["magenta"], 28, 18, 3))
    add("icones/champ-user.png", 24, 24, icone_centree("user", C["gris"], 24, 18, 0))
    add("icones/champ-lock.png", 24, 24, icone_centree("lock", C["gris"], 24, 18, 0))
    add("icones/utilisateur.png", 40, 40, icone_centree("user", C["cyan"], 40, 20, 0,
                                                         cercle=(38, "#0A1A2E", "#0E5566")))
    add("icones/login-cadenas.png", 80, 80, icone_centree("shield-check", C["cyan"], 80, 38, 6, 1.8,
                                                          cercle=(70, "#07192A", "#0E5566")))
    # Icônes des cartes indicateurs (60 x 60 px, pastille + halo)
    fonds_pastille = {"cyan": "#062331", "violet": "#1A1238", "magenta": "#2A0C24", "vert": "#08261E"}
    for ico, col in [("wallet", "cyan"), ("car-front", "violet"), ("users", "magenta"), ("calendar-check", "vert")]:
        add(f"icones/kpi-{ico}-{col}.png", 60, 60, icone_centree(ico, C[col], 60, 28, 5, 1.8,
                                                                  cercle=(52, fonds_pastille[col], C[col] + "55")))
    # Cadres des cartes indicateurs (302 x 124 px)
    for col in ["cyan", "violet", "magenta", "vert"]:
        cc = C[col]
        coins = ""
        for (l, t, bl, bt) in [(0, 0, "left", "top"), (1, 0, "right", "top"), (0, 1, "left", "bottom"), (1, 1, "right", "bottom")]:
            coins += (f'<div style="position:absolute;{bl}:6px;{bt}:6px;width:16px;height:16px;'
                      f'border-{bl}:2px solid {cc};border-{bt}:2px solid {cc}"></div>')
        corps = (f'<div style="position:absolute;left:6px;top:6px;right:6px;bottom:6px;'
                 f'background:linear-gradient(135deg,{cc}1f 0%,#0D1530 45%,#0B1229 100%);'
                 f'border:1px solid {cc}66;box-shadow:0 0 12px {cc}40, inset 0 0 18px {cc}14"></div>'
                 f'<div style="position:absolute;left:6px;top:6px;right:6px;height:2px;background:linear-gradient(90deg,{cc},{cc}00)"></div>'
                 + coins)
        add(f"cadres/kpi-{col}.png", 302, 124, corps)
    # Logo (188 x 52 px)
    logo = (f'<div style="position:absolute;left:2px;top:6px">{svg("car-front", C["cyan"], 38, 4, 1.8)}</div>'
            f'<div style="position:absolute;left:48px;top:5px;font:700 22px Titre;letter-spacing:1.5px;white-space:nowrap;color:#fff;'
            f'text-shadow:0 0 10px {C["cyan"]}99">RENTAL<span style="color:{C["cyan"]}"> CAR</span></div>'
            f'<div style="position:absolute;left:49px;top:33px;font:400 9px Mono;letter-spacing:1.6px;white-space:nowrap;color:#6F7EA8">GESTION DE LOCATION</div>')
    add("logo.png", 188, 52, logo)
    # Ligne néon sous le bandeau (1344 x 2 px)
    add("ligne-neon.png", 1344, 2,
        f'<div style="position:absolute;inset:0;background:linear-gradient(90deg,{C["cyan"]} 0%,{C["violet"]} 45%,{C["magenta"]}66 75%,#16213F 100%)"></div>')
    # Fond de la zone de contenu (1344 x 716 px) : grille fine + halos
    grille = ("background-image:linear-gradient(#0E1733 1px,transparent 1px),linear-gradient(90deg,#0E1733 1px,transparent 1px);"
              "background-size:48px 48px;")
    fond_c = (f'<div style="position:absolute;inset:0;background:#070B18"></div>'
              f'<div style="position:absolute;inset:0;{grille}opacity:.55"></div>'
              f'<div style="position:absolute;inset:0;background:radial-gradient(ellipse 700px 420px at 92% 0%,#00E5FF14,transparent 70%),'
              f'radial-gradient(ellipse 700px 420px at 0% 100%,#9D5CFF14,transparent 70%)"></div>')
    add("fonds/fond-contenu.png", 1344, 716, fond_c, fond="#070B18")
    # Fond de l'écran de connexion (1568 x 784 px)
    route = ""
    for i in range(9):
        route += (f'<div style="position:absolute;left:{-200 + i * 40}px;top:{520 + i * 14}px;width:2400px;height:1px;'
                  f'background:linear-gradient(90deg,transparent,{C["cyan"]}{hex(40 - i * 4)[2:].zfill(2)},transparent);transform:rotate(-8deg)"></div>')
    fond_l = (f'<div style="position:absolute;inset:0;background:#050814"></div>'
              f'<div style="position:absolute;inset:0;{grille}opacity:.5"></div>'
              f'<div style="position:absolute;inset:0;background:radial-gradient(circle 420px at 50% 50%,#00E5FF1c,transparent 70%),'
              f'radial-gradient(circle 600px at 85% 10%,#9D5CFF22,transparent 70%),radial-gradient(circle 600px at 10% 95%,#FF2E9718,transparent 70%)"></div>'
              + route +
              f'<div style="position:absolute;left:60px;top:48px">{svg("car-front", C["cyan"], 34, 4, 1.8)}</div>'
              f'<div style="position:absolute;left:106px;top:50px;font:700 24px Titre;letter-spacing:3px;color:#fff">RENTAL <span style="color:{C["cyan"]}">CAR</span></div>'
              f'<div style="position:absolute;right:60px;bottom:40px;font:400 12px Mono;letter-spacing:3px;color:#3E4A70">SYSTÈME DE GESTION DE LOCATION · V2.0</div>')
    add("fonds/fond-login.png", 1568, 784, fond_l, fond="#050814")
    # Palette (aperçu)
    pal = [("Fond", "#070B18"), ("Menu", "#050913"), ("Panneau", "#0D1530"), ("Champ", "#081024"), ("Bordure", "#1F2C52"),
           ("Bordure champ", "#2A3B6B"), ("Texte", "#E6EDFF"), ("Étiquette", "#8A97BC"), ("Discret", "#56638A"),
           ("Cyan", C["cyan"]), ("Violet", C["violet"]), ("Magenta", C["magenta"]), ("Vert", C["vert"]), ("Ambre", C["ambre"])]
    blocs = ""
    for i, (n, hx) in enumerate(pal):
        x = 20 + (i % 7) * 160
        y = 20 + (i // 7) * 130
        blocs += (f'<div style="position:absolute;left:{x}px;top:{y}px;width:144px;height:64px;background:{hx};border:1px solid #2A3B6B"></div>'
                  f'<div style="position:absolute;left:{x}px;top:{y + 72}px;font:600 14px Titre;color:#E6EDFF;letter-spacing:1px">{n.upper()}</div>'
                  f'<div style="position:absolute;left:{x}px;top:{y + 92}px;font:400 13px Mono;color:#8A97BC">{hx}</div>')
    add("palette.png", 1140, 280, blocs, fond="#070B18")
    return jobs


# --------------------------------------------------------------------------
def main():
    MAQ.mkdir(parents=True, exist_ok=True)
    (MAQ / "png").mkdir(exist_ok=True)
    tmp = Path(tempfile.mkdtemp(prefix="rentalcar-"))
    jobs = assets_jobs(tmp)
    for sub in {Path(j["out"]).parent for j in jobs}:
        sub.mkdir(parents=True, exist_ok=True)
    ecr_jobs = []
    for fic, titre, fn in ECRANS:
        (MAQ / f"{fic}.html").write_text(page(titre, fn()))
        ecr_jobs.append({"html": (MAQ / f"{fic}.html").as_uri(), "out": str(MAQ / "png" / f"{fic}.png"),
                         "w": 1568, "h": 784, "transparent": False, "sel": "#ecran", "cotes": fic})
    jf = tmp / "jobs.json"
    jf.write_text(json.dumps({"assets": jobs, "ecrans": ecr_jobs, "cotes": str(ICI / "cotes.json")}))
    r = subprocess.run(["node", str(ICI / "rendre.mjs"), str(jf)], cwd=os.environ.get("RENDER_CWD", ICI))
    if r.returncode:
        sys.exit(r.returncode)
    ecrire_cotes()


def cm(px):
    return f"{px / 37.795:.2f}".replace(".", ",")


def ecrire_cotes():
    cotes = json.loads((ICI / "cotes.json").read_text())
    L = ["# Cotes des contrôles (en cm, pour la feuille de propriétés d'Access)", "",
         "Généré automatiquement par `design/outils/generer.py` à partir des maquettes.", "",
         "* Les positions sont en **centimètres** (96 ppp : 1 cm = 37,8 px), comme dans la feuille de propriétés "
         "(onglet *Format* : `Gauche`, `Haut`, `Largeur`, `Hauteur`).",
         "* **Menu** : positions mesurées depuis le coin haut-gauche du formulaire `Menu`.",
         "* **Autres écrans** : positions mesurées depuis le coin haut-gauche du **sous-formulaire** "
         "(la zone de contenu, 35,56 × 18,94 cm).",
         "* Les contrôles placés *dans* un panneau sont indiqués avec leur position absolue dans le sous-formulaire "
         "(plus pratique dans Access, qui n'a pas de conteneur).", ""]
    for fic, titre, _ in ECRANS:
        items = cotes.get(fic, [])
        if fic == "01-tableau-de-bord":
            menu = [i for i in items if i["zone"] == "ecran"]
            L += ["## Formulaire « Menu » (commun à tous les écrans)", "",
                  "| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |", "|---|---|---:|---:|---:|---:|"]
            vus = set()
            for i in menu:
                if i["nom"] in vus:
                    continue
                vus.add(i["nom"])
                L.append(f'| `{i["nom"]}` | {i["type"]} | {cm(i["x"])} | {cm(i["y"])} | {cm(i["w"])} | {cm(i["h"])} |')
            L.append("")
        zone = "ecran" if fic == "00-connexion" else "contenu"
        sel = [i for i in items if i["zone"] == zone]
        L += [f"## {titre} ({'formulaire Login' if zone == 'ecran' else 'sous-formulaire'})", "",
              f"Maquette : `maquettes/png/{fic}.png`", "",
              "| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |", "|---|---|---:|---:|---:|---:|"]
        vus = set()
        for i in sel:
            k = (i["nom"], i["x"], i["y"])
            if k in vus:
                continue
            vus.add(k)
            L.append(f'| `{i["nom"]}` | {i["type"]} | {cm(i["x"])} | {cm(i["y"])} | {cm(i["w"])} | {cm(i["h"])} |')
        L.append("")
    (DESIGN / "COTES.md").write_text("\n".join(L))


if __name__ == "__main__":
    main()
