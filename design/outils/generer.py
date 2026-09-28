#!/usr/bin/env python3
"""
Générateur des maquettes RENTAL CAR (thème clair, rendu « Access »).

  cd design/outils && npm install && python3 generer.py

Produit :
  design/maquettes/*.html        maquettes (ouvrables dans un navigateur)
  design/maquettes/png/*.png     captures des maquettes
  design/assets/*.png            icônes à importer dans Access
  design/COTES.md                positions et tailles des contrôles, en cm
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

BLEU, BLEU_F, GRIS, GRIS_F, ROUGE = "#2563EB", "#1D4ED8", "#6B7280", "#4B5563", "#DC2626"
MARINE, NAV_TXT = "#1E3A8A", "#AFC3F0"
NOM_APPLI = "RENTAL GABON CAR"
VERT, VIOLET = "#16A34A", "#7C3AED"
W, H = 1568, 784            # zone du formulaire (sans la barre de titre)
CW, CH = W - 220, H - 56    # zone de contenu (sous-formulaire) : 1348 x 728
DONNEES = json.loads((ICI / "donnees.json").read_text())
CLIENTS = {c["CIN"]: c for c in DONNEES["Client"]}


# --------------------------------------------------------------------------
def e(s):
    return html.escape(str(s))


def acc(nom, typ):
    return f'data-acc="{e(nom)}" data-type="{e(typ)}"'


def svg(name, color, size=18, stroke=1.75):
    raw = (SVG_DIR / f"{name}.svg").read_text()
    inner = re.search(r"<svg[^>]*>(.*)</svg>", raw, re.S).group(1)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
            f'stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round" style="display:block">{inner}</svg>')


def fdate(iso):
    y, m, d = iso[:10].split("-")
    return f"{d}/{m}/{y}"


def fcfa(n):
    return f"{n:,}".replace(",", " ")


# --------------------------------------------------------------------------
# Fenêtre Windows
# --------------------------------------------------------------------------
ICONE_FORM = ('<svg class="ico" viewBox="0 0 14 14"><rect x=".5" y="1.5" width="13" height="11" fill="#fff" stroke="#6B6B6B"/>'
              '<rect x=".5" y="1.5" width="13" height="3" fill="#A4373A"/><rect x="2.5" y="6.5" width="4" height="1.5" fill="#6B6B6B"/>'
              '<rect x="7.5" y="6.5" width="4" height="1.5" fill="#6B6B6B"/><rect x="2.5" y="9.5" width="4" height="1.5" fill="#6B6B6B"/>'
              '<rect x="7.5" y="9.5" width="4" height="1.5" fill="#6B6B6B"/></svg>')


def fenetre(titre_fen, largeur, hauteur, corps, boutons=("min", "max", "fermer")):
    ctrl = ""
    glyphes = {
        "min": '<svg width="10" height="10"><path d="M0 5.5h10" stroke="#000" stroke-width="1"/></svg>',
        "max": '<svg width="10" height="10"><rect x="2.5" y=".5" width="7" height="7" fill="none" stroke="#000"/><path d="M.5 2.5v7h7" fill="none" stroke="#000"/></svg>',
        "fermer": '<svg width="10" height="10"><path d="M0 0l10 10M10 0L0 10" stroke="#000" stroke-width="1"/></svg>',
    }
    for i, b in enumerate(reversed(boutons)):
        ctrl += f'<div class="ctrl" style="right:{i * 46}px">{glyphes[b]}</div>'
    return f"""<div class="fenetre" id="fenetre" style="width:{largeur}px">
<div class="barre-titre">{ICONE_FORM}<span class="txt">{e(titre_fen)}</span>{ctrl}</div>
<div class="ecran" id="ecran" style="width:{largeur}px;height:{hauteur}px">
{corps}
</div></div>"""


def page(titre, corps):
    return f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>{e(titre)} · {NOM_APPLI}</title>
<link rel="stylesheet" href="style.css"></head>
<body>{corps}</body></html>"""


# --------------------------------------------------------------------------
# Formulaire Menu
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


def coquille(actif, titre, contenu):
    nav = ""
    for i, (cle, lib, ico) in enumerate(MENU):
        y = 76 + i * 44
        on = cle == actif
        nav += (f'<div class="nav{" actif" if on else ""}" style="top:{y}px" {acc("BoutonNavigation_" + cle, "Bouton de navigation")}>'
                f'{svg(ico, MARINE if on else NAV_TXT, 18)}{e(lib)}</div>')
    corps = f"""
<div class="menu" {acc("Menu_Fond", "Rectangle")}>
  <div class="logo" {acc("Logo", "Image + étiquette")}>{svg("car-front", "#FFFFFF", 24, 1.8)}{NOM_APPLI}</div>
  {nav}
</div>
<div class="entete" {acc("Entete", "Rectangle")}>
  <div class="titre" {acc("Titre_Page", "Étiquette")}>{e(titre)}</div>
  <div class="date" style="right:72px" {acc("Date_Heure", "Zone de texte")}>{svg("calendar-range", GRIS, 15)}28/09/2026 20:06</div>
  <div class="btn-ico abs" style="right:24px;top:12px;width:32px;height:32px" {acc("Btn_Quitter", "Bouton")}>{svg("power", MARINE, 16)}</div>
</div>
<div class="contenu" id="contenu">
{contenu}
</div>"""
    return fenetre(NOM_APPLI, W, H, corps)


# --------------------------------------------------------------------------
# Briques
# --------------------------------------------------------------------------
ACTIONS = {"Ajouter": "plus", "Actualiser": "refresh-cw", "Rechercher": "search", "Imprimer": "printer"}


def carte(nom, titre, x, y, w, h, interieur="", actions=(), info=None):
    act = ""
    if actions:
        act = '<div class="actions">' + "".join(
            f'<div class="btn-ico" title="{a}" {acc("Btn_" + a, "Bouton")}>{svg(ACTIONS[a], BLEU, 16)}</div>' for a in actions) + "</div>"
    inf = f'<div class="info" style="left:{28 + int(len(titre) * 8.6)}px">{e(info)}</div>' if info else ""
    return (f'<div class="carte" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px" {acc(nom, "Rectangle")}>'
            f'<div class="bande"></div><div class="titre-c">{e(titre)}</div>{inf}{act}<div class="trait"></div>{interieur}</div>')


def fleche_bas():
    return ('<svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="#4B5563" stroke-width="2.5" '
            'stroke-linecap="round" stroke-linejoin="round" style="display:block"><path d="m6 9 6 6 6-6"/></svg>')


def champ(nom, lib, val, x, y, lw, w, kind="texte", droite=False, total=False):
    cls = "champ" + (" lecture" if kind == "lecture" else "") + (" droite" if droite else "") + (" total" if total else "")
    extra = ""
    if kind == "liste":
        cls += " liste-der"
        extra = f'<span class="fleche">{fleche_bas()}</span>'
    typ = {"texte": "Zone de texte", "lecture": "Zone de texte (verrouillée)", "liste": "Zone de liste déroulante"}[kind]
    out = f'<div class="etiq" style="left:{x}px;top:{y}px">{e(lib)}</div>' if lib else ""
    return out + f'<div class="{cls}" style="left:{x + lw}px;top:{y}px;width:{w}px" {acc(nom, typ)}>{e(val)}{extra}</div>'


def nav_enreg(x, y, texte):
    ico = [("Premier", "chevron-first"), ("Precedent", "chevron-left"), ("Suivant", "chevron-right"), ("Dernier", "chevron-last")]
    out = ""
    pos = [x, x + 34, x + 178, x + 212]
    for (n, i), px in zip(ico, pos):
        out += f'<div class="btn-nav" style="left:{px}px;top:{y}px" {acc("Btn_" + n, "Bouton")}>{svg(i, BLEU, 16)}</div>'
    out += f'<div class="compteur" style="left:{x + 68}px;top:{y}px;width:106px" {acc("Txt_Compteur", "Zone de texte")}>{e(texte)}</div>'
    return out


def boutons_crud(x, y, w=120):
    return (f'<div class="btn primaire" style="left:{x}px;top:{y}px;width:{w}px" {acc("Btn_Enregistrer", "Bouton")}>Enregistrer</div>'
            f'<div class="btn danger" style="left:{x + w + 10}px;top:{y}px;width:{w}px" {acc("Btn_Supprimer", "Bouton")}>Supprimer</div>')


def liste(nom, cols, lignes, x, y, w, h, total=None):
    """Zone de liste façon Access. cols = [(titre, largeur, 'num'?)]"""
    vis = (h - 2 - 21) // 20
    n = total or len(lignes)
    dispo = w - 2 - (17 if n > vis else 0)
    tw = sum(c[1] for c in cols)
    if tw < dispo:  # on répartit la place restante sur toutes les colonnes
        k = dispo / tw
        cols = [(c[0], int(c[1] * k)) + tuple(c[2:]) for c in cols]
        cols[-1] = (cols[-1][0], cols[-1][1] + dispo - sum(c[1] for c in cols)) + tuple(cols[-1][2:])
        tw = dispo
    colg = "".join(f'<col style="width:{c[1]}px">' for c in cols)
    th = "".join(f'<th class="{c[2] if len(c) > 2 else ""}">{e(c[0])}</th>' for c in cols)
    trs = "".join("<tr>" + "".join(f'<td class="{cols[i][2] if len(cols[i]) > 2 else ""}">{e(v)}</td>'
                                   for i, v in enumerate(l)) + "</tr>" for l in lignes)
    defil = ""
    if n > vis:
        piste = h - 2 - 34
        ph = max(20, int(piste * vis / n))
        tri_h = '<svg width="7" height="4"><path d="M0 4L3.5 0L7 4z" fill="#606060"/></svg>'
        tri_b = '<svg width="7" height="4"><path d="M0 0L3.5 4L7 0z" fill="#606060"/></svg>'
        defil = (f'<div class="defil"><div class="fl" style="top:0">{tri_h}</div>'
                 f'<div class="pouce" style="top:19px;height:{ph}px"></div>'
                 f'<div class="fl" style="bottom:0">{tri_b}</div></div>')
    return (f'<div class="liste" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px" {acc(nom, "Zone de liste")}>'
            f'<table style="width:{tw}px"><colgroup>{colg}</colgroup><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>{defil}</div>')


# --------------------------------------------------------------------------
# Données communes
# --------------------------------------------------------------------------
MODELE_RES = {1: ("Audi Q6", "Audi"), 2: ("Audi A6", "Audi"), 3: ("Audi A7", "Audi"), 4: ("Audi Q3", "Audi"),
              5: ("BMW X1", "BMW"), 6: ("BMW X5", "BMW"), 7: ("Audi Q4", "Audi")}


def lignes_reservations():
    out = []
    for r in DONNEES["Reservation"][:7]:
        c = CLIENTS[r["Client"]]
        mo, ma = MODELE_RES[r["IdReservation"]]
        out.append([r["IdReservation"], fdate(r["DateDebut"]), fdate(r["DateFin"]), c["Prénom"], c["Nom"], r["Voiture"], mo, ma])
    return out


# --------------------------------------------------------------------------
# Écrans
# --------------------------------------------------------------------------
def ecran_tableau():
    kpis = [("CA", "Chiffre d'affaires", "104 261 200", "FCFA", "wallet", "#1E40AF", "#3F5BBE"),
            ("Voitures", "Voitures", "60", "", "car-front", "#2563EB", "#4B7FEF"),
            ("Clients", "Clients", "200", "", "users", "#3B82F6", "#5C97F8")]
    kw = (CW - 48 - 32) // 3
    out = ""
    for i, (n, lib, val, unit, ico, fond, pastille) in enumerate(kpis):
        x = 24 + i * (kw + 16)
        u = f"<small>{unit}</small>" if unit else ""
        out += (f'<div class="kpi" style="left:{x}px;top:24px;width:{kw}px;height:96px;background:{fond};border-color:{fond}" {acc("Carte_" + n, "Rectangle")}>'
                f'<div class="lib">{e(lib)}</div><div class="val" {acc("Txt_" + n, "Zone de texte")}>{val}{u}</div>'
                f'<div class="pastille" style="background:{pastille}" {acc("Pastille_" + n, "Rectangle + image")}>{svg(ico, "#FFFFFF", 24)}</div></div>')

    # réservations en cours au 28/09/2026 (DateDebut <= aujourd'hui <= DateFin)
    import datetime as dt
    auj = dt.date(2026, 9, 28)
    res = []
    for r in DONNEES["Reservation"]:
        d0, d1 = dt.date.fromisoformat(r["DateDebut"][:10]), dt.date.fromisoformat(r["DateFin"][:10])
        if d0 <= auj <= d1:
            c = CLIENTS[r["Client"]]
            res.append([r["Voiture"], fdate(r["DateDebut"]), fdate(r["DateFin"]), c["Prénom"], c["Nom"]])
    lw1 = 836
    l1 = liste("Liste_Voitures_Reservees",
               [("Matricule", 130), ("Date de début", 140), ("Date de fin", 140), ("Prénom", 180), ("Nom", 180)],
               res, 20, 66, lw1 - 42, 186)
    p1 = carte("Carte_Reservees", "Voitures actuellement réservées", 24, 136, lw1, 272, l1, actions=["Imprimer"])

    top = [("Cynthia", "Kombila", 18457500), ("Junior", "Ondo", 11097500), ("Léa", "Eyang", 10413000),
           ("Cédric", "Nkoghe", 8021250), ("Noëlle", "Mba", 7416000)]
    lw2 = CW - 48 - 16 - lw1
    l2 = liste("Liste_Top5", [("Prénom", 130), ("Nom", 130), ("CA (FCFA)", lw2 - 42 - 262, "num")],
               [[a, b, fcfa(c)] for a, b, c in top], 20, 66, lw2 - 40, 186)
    p2 = carte("Carte_Top5", "5 meilleurs clients", 24 + lw1 + 16, 136, lw2, 272, l2)

    l3 = liste("Liste_Dernieres", [("Code", 60, "num"), ("Date de début", 130), ("Date de fin", 130), ("Prénom", 150), ("Nom", 160),
                                   ("Matricule", 140), ("Modèle", 150), ("Marque", 120)],
               lignes_reservations(), 20, 66, CW - 48 - 40, 186, total=25)
    p3 = carte("Carte_Dernieres", "Réservations", 24, 424, CW - 48, 272, l3, actions=["Imprimer"], info="25 au total")
    return coquille("tableau", "Tableau de bord", out + p1 + p2 + p3)


def ecran_reservations():
    lw, iw = 104, 480
    cw = (CW - 48 - 16) // 2
    cli = (champ("Cbo_Client", "Client", "Jean Mboumba", 20, 68, lw, iw, "liste")
           + champ("Txt_Telephone", "Téléphone", "(+241) 62 54 85 85", 20, 106, lw, iw, "lecture")
           + champ("Txt_Email", "Email", "jean.mboumba1@example.com", 20, 144, lw, iw, "lecture"))
    p1 = carte("Carte_Client", "Client", 24, 24, cw, 192, cli)
    voi = (champ("Cbo_Voiture", "Voiture", "AB-3988-AA", 20, 68, lw, iw, "liste")
           + champ("Txt_Modele", "Modèle", "Audi Q6", 20, 106, lw, iw, "lecture")
           + champ("Txt_Marque", "Marque", "Audi", 20, 144, lw, iw, "lecture"))
    p2 = carte("Carte_Voiture", "Voiture", 24 + cw + 16, 24, cw, 192, voi)

    res = (champ("Txt_Code", "Code", "1", 20, 68, 104, 80, droite=True)
           + champ("Txt_DateDebut", "Date de début", "23/09/2026", 20, 106, 104, 120, droite=True)
           + champ("Txt_DateFin", "Date de fin", "24/10/2026", 272, 106, 90, 120, droite=True)
           + f'<div class="btn secondaire" style="left:494px;top:104px;width:60px" {acc("Btn_OK", "Bouton")}>OK</div>'
           + nav_enreg(124, 150, "1 sur 25")
           + '<div class="sep-v" style="left:640px;top:51px;height:139px"></div>'
           + champ("Txt_Duree", "Durée", "31 jour(s)", 664, 68, 90, 200, "lecture", droite=True)
           + champ("Txt_Montant", "Montant", "1 023 000 FCFA", 664, 106, 90, 200, "lecture", droite=True, total=True)
           + boutons_crud(CW - 48 - 20 - 250, 148))
    p3 = carte("Carte_Reservation", "Réservation", 24, 232, CW - 48, 196, res, actions=["Ajouter", "Actualiser", "Rechercher", "Imprimer"])

    l = liste("Liste_Reservations", [("Code", 60, "num"), ("Date de début", 130), ("Date de fin", 130), ("Prénom", 150), ("Nom", 160),
                                     ("Matricule", 140), ("Modèle", 150), ("Marque", 120)],
              lignes_reservations(), 20, 66, CW - 48 - 40, 186, total=25)
    p4 = carte("Carte_Liste", "Liste des réservations", 24, 444, CW - 48, 272, l, actions=["Imprimer"], info="25 réservations")
    return coquille("reservations", "Réservations", p1 + p2 + p3 + p4)


def ecran_fiche(cle, titre, titre_fiche, champs, titre_liste, cols, lignes, total, compteur, info, fiche_w=520, hauteur=None,
                hauteur_liste=None):
    lw = 130
    iw = fiche_w - 40 - lw
    inner = ""
    y = 70
    for (n, lib, val, kind, *opt) in champs:
        inner += champ(n, lib, val, 20, y, lw, opt[0] if opt else iw, kind)
        y += 40
    y += 8
    inner += nav_enreg(20 + lw, y, compteur)
    y += 46
    inner += f'<div class="sep-h" style="left:0;top:{y}px;width:{fiche_w - 2}px"></div>'
    y += 16
    inner += boutons_crud(fiche_w - 20 - 250, y)
    h = hauteur or (y + 32 + 18)
    p1 = carte("Carte_Fiche", titre_fiche, 24, 24, fiche_w, h, inner, actions=["Ajouter", "Actualiser", "Rechercher", "Imprimer"])
    lx = 24 + fiche_w + 16
    lw_ = CW - 24 - lx
    lh = hauteur_liste or (max(h, 300) if hauteur is None else h)
    l = liste("Liste_" + cle.capitalize(), cols, lignes, 20, 66, lw_ - 40, lh - 86, total=total)
    p2 = carte("Carte_Liste", titre_liste, lx, 24, lw_, lh, l, actions=["Imprimer"], info=info)
    return coquille(cle, titre, p1 + p2)


def ecran_clients():
    c = CLIENTS["CL-0001"]
    champs = [("Txt_CIN", "Code client", c["CIN"], "texte", 140), ("Txt_Permis", "N° de permis", c["NumPermis"], "texte", 180),
              ("Txt_Prenom", "Prénom", c["Prénom"], "texte"), ("Txt_Nom", "Nom", c["Nom"], "texte"),
              ("Cbo_Sexe", "Sexe", c["Sexe"], "liste", 80), ("Txt_Adresse", "Adresse", c["Adresse"], "texte"),
              ("Txt_Telephone", "Téléphone", c["Téléphone"], "texte"), ("Txt_Email", "Email", c["Email"], "texte")]
    lignes = [[x["CIN"], x["NumPermis"], x["Prénom"], x["Nom"], x["Sexe"], x["Adresse"], x["Téléphone"]] for x in DONNEES["Client"][:30]]
    cols = [("Code client", 76), ("N° de permis", 112), ("Prénom", 86), ("Nom", 96), ("Sexe", 36), ("Adresse", 160), ("Téléphone", 139)]
    return ecran_fiche("clients", "Clients", "Fiche client", champs, "Liste des clients", cols, lignes, 200, "1 sur 200",
                       "200 clients", hauteur_liste=680)


def ecran_voitures():
    champs = [("Txt_Matricule", "Matricule", "AB-2344-AA", "texte", 140), ("Txt_Annee", "Année", "2026", "texte", 80),
              ("Txt_Couleur", "Couleur", "Gris", "texte"), ("Txt_Puissance", "Puissance", "15 CV", "texte", 80),
              ("Txt_CoutJour", "Coût par jour", "95 000 FCFA", "texte", 140), ("Cbo_Modele", "Modèle", "Audi Q5", "liste"),
              ("Cbo_Carburant", "Carburant", "Diesel", "liste"), ("Cbo_Marque", "Marque", "Audi", "liste")]
    v = [("AB-2344-AA", "2026", "Gris", "15CV", "95 000"), ("LB-8235-AA", "2024", "Bleu", "11CV", "42 000"),
         ("RT-7002-AA", "2025", "Blanc", "13CV", "46 000"), ("CD-2481-AA", "2022", "Bleu", "7CV", "27 500"),
         ("DF-1111-AA", "2022", "Noir", "7CV", "27 500"), ("EF-4262-AA", "2025", "Gris", "13CV", "60 000"),
         ("FG-2892-AA", "2025", "Jaune", "13CV", "48 000"), ("FJ-4673-AA", "2023", "Argent", "9CV", "65 000"),
         ("GA-5495-AA", "2024", "Rouge", "11CV", "40 000"), ("KL-8098-AA", "2023", "Gris", "9CV", "33 000"),
         ("MN-6728-AA", "2023", "Jaune", "9CV", "35 000"), ("QS-6865-AA", "2024", "Noir", "11CV", "40 000")]
    cols = [("Matricule", 120), ("Année", 70), ("Couleur", 100), ("Puissance", 90), ("Coût par jour", 120, "num")]
    return ecran_fiche("voitures", "Voitures", "Fiche voiture", champs, "Liste des voitures", cols, [list(x) for x in v], 12,
                       "1 sur 60", "60 voitures", hauteur_liste=680)


def ecran_marques():
    champs = [("Txt_IdMarque", "Identifiant", "1", "texte", 80), ("Txt_Marque", "Marque", "Audi", "texte")]
    lignes = [[m["IdMarque"], m["Marque"]] for m in DONNEES["Marque"]]
    return ecran_fiche("marques", "Marques", "Fiche marque", champs, "Liste des marques", [("Identifiant", 90), ("Marque", 200)],
                       lignes, None, "1 sur 5", "5 marques")


def ecran_carburants():
    champs = [("Txt_IdType", "Identifiant", "1", "texte", 80), ("Txt_Type", "Type", "Diesel", "texte")]
    lignes = [[c["IdType"], c["Type"]] for c in DONNEES["Carburant"]]
    return ecran_fiche("carburants", "Carburants", "Fiche carburant", champs, "Types de carburant",
                       [("Identifiant", 90), ("Type", 200)], lignes, None, "1 sur 3", "3 types")


def ecran_modeles():
    marques = {m["IdMarque"]: m["Marque"] for m in DONNEES["Marque"]}
    champs = [("Txt_IdModele", "Identifiant", "1", "texte", 80), ("Txt_Modele", "Modèle", "Audi Q5", "texte"),
              ("Cbo_Marque", "Marque", "Audi", "liste")]
    lignes = [[m["IdModele"], m["Modele"], marques[m["Marque"]]] for m in DONNEES["Modele"][:30]]
    return ecran_fiche("modeles", "Modèles", "Fiche modèle", champs, "Liste des modèles",
                       [("Identifiant", 90), ("Modèle", 180), ("Marque", 140)], lignes, 60, "1 sur 60", "60 modèles",
                       hauteur_liste=680)


def ecran_login():
    lw, lh = 440, 420
    corps = f"""
<div class="abs" style="left:0;top:0;width:{lw}px;height:{lh}px;background:#FFFFFF" {acc("Login_Fond", "Section Détail")}></div>
<div class="abs" style="left:0;top:0;width:{lw}px;height:96px;background:{MARINE}" {acc("Bandeau_Bleu", "Rectangle")}></div>
<div class="abs" style="left:40px;top:34px;display:flex;align-items:center;gap:10px;font-size:18.67px;font-weight:600;color:#FFFFFF;letter-spacing:.5px" {acc("Logo", "Image + étiquette")}>{svg("car-front", "#FFFFFF", 28, 1.8)}{NOM_APPLI}</div>
<div class="abs" style="left:40px;top:124px;font-size:21.33px;font-weight:600;color:{MARINE}" {acc("Lbl_Titre", "Étiquette")}>Connexion</div>
<div class="abs" style="left:40px;top:156px;font-size:13.33px;color:#6B7280">Entrez vos identifiants pour continuer.</div>
<div class="etiq" style="left:40px;top:194px">Nom d'utilisateur</div>
<div class="champ" style="left:40px;top:222px;width:360px;height:32px;line-height:30px" {acc("Txt_Utilisateur", "Zone de texte")}>admin</div>
<div class="etiq" style="left:40px;top:262px">Mot de passe</div>
<div class="champ" style="left:40px;top:290px;width:360px;height:32px;line-height:30px;letter-spacing:2px" {acc("Txt_MotDePasse", "Zone de texte")}>********</div>
<div class="btn primaire" style="left:40px;top:350px;width:360px;height:36px" {acc("Btn_Connexion", "Bouton")}>Se connecter</div>
"""
    return fenetre(NOM_APPLI + " - Connexion", lw, lh, corps, boutons=("fermer",))


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
# Icônes PNG à importer dans Access
# --------------------------------------------------------------------------
def assets_jobs(tmp):
    jobs = []

    def add(out, taille, name, color, size, stroke=1.75):
        off = (taille - size) / 2
        corps = f'<div style="position:absolute;left:{off}px;top:{off}px">{svg(name, color, size, stroke)}</div>'
        p = tmp / (out.replace("/", "_") + ".html")
        p.write_text(f'<!doctype html><html><head><style>html,body{{margin:0;background:transparent}}'
                     f'#a{{position:relative;width:{taille}px;height:{taille}px}}</style></head><body><div id="a">{corps}</div></body></html>')
        jobs.append({"html": p.as_uri(), "out": str(ASSETS / out), "w": taille, "h": taille, "transparent": True, "sel": "#a"})

    for _, _, ico in MENU:
        add(f"menu-{ico}.png", 20, ico, NAV_TXT, 18)
        add(f"menu-{ico}-actif.png", 20, ico, MARINE, 18)
    for ico in list(ACTIONS.values()) + ["chevron-first", "chevron-left", "chevron-right", "chevron-last", "power"]:
        add(f"bouton-{ico}.png", 16, ico, MARINE if ico == "power" else BLEU, 16)
    add("date.png", 16, "calendar-range", GRIS, 15)
    add("logo-voiture.png", 28, "car-front", "#FFFFFF", 24, 1.8)
    for ico, col in [("wallet", "#FFFFFF"), ("car-front", "#FFFFFF"), ("users", "#FFFFFF")]:
        add(f"indicateur-{ico}.png", 24, ico, col, 24)
    return jobs


# --------------------------------------------------------------------------
def cm(px):
    return f"{px / 37.795:.2f}".replace(".", ",")


def ecrire_cotes(cotes):
    L = ["# Cotes des contrôles", "",
         "Positions et tailles en **centimètres**, à saisir dans la feuille de propriétés d'Access "
         "(onglet *Format* : `Gauche`, `Haut`, `Largeur`, `Hauteur`).", "",
         "* **Menu** : mesurées depuis le coin haut-gauche du formulaire `Menu` (41,49 × 20,74 cm).",
         f"* **Autres écrans** : mesurées depuis le coin haut-gauche du **sous-formulaire** ({cm(CW)} × {cm(CH)} cm).",
         "* Les contrôles placés dans une carte sont donnés en position absolue dans le sous-formulaire.",
         "* Fichier généré par `outils/generer.py`.", ""]

    def table(items):
        out = ["| Contrôle | Type | Gauche | Haut | Largeur | Hauteur |", "|---|---|---:|---:|---:|---:|"]
        vus = set()
        for i in items:
            k = (i["nom"], i["x"], i["y"])
            if k in vus:
                continue
            vus.add(k)
            out.append(f'| `{i["nom"]}` | {i["type"]} | {cm(i["x"])} | {cm(i["y"])} | {cm(i["w"])} | {cm(i["h"])} |')
        return out + [""]

    for fic, titre, _ in ECRANS:
        items = cotes.get(fic, [])
        if fic == "01-tableau-de-bord":
            L += ["## Formulaire « Menu » (commun à tous les écrans)", ""] + table([i for i in items if i["zone"] == "ecran"])
        zone = "ecran" if fic == "00-connexion" else "contenu"
        L += [f"## {titre}", "", f"Maquette : `maquettes/png/{fic}.png`", ""] + table([i for i in items if i["zone"] == zone])
    (DESIGN / "COTES.md").write_text("\n".join(L))


def main():
    (MAQ / "png").mkdir(parents=True, exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp(prefix="rentalcar-"))
    jobs = assets_jobs(tmp)
    ecr = []
    for fic, titre, fn in ECRANS:
        (MAQ / f"{fic}.html").write_text(page(titre, fn()))
        ecr.append({"html": (MAQ / f"{fic}.html").as_uri(), "out": str(MAQ / "png" / f"{fic}.png"),
                    "w": 1600, "h": 820, "transparent": False, "sel": "#fenetre", "cotes": fic})
    jf = tmp / "jobs.json"
    cf = tmp / "cotes.json"
    jf.write_text(json.dumps({"assets": jobs, "ecrans": ecr, "cotes": str(cf)}))
    r = subprocess.run(["node", str(ICI / "rendre.mjs"), str(jf)], cwd=ICI)
    if r.returncode:
        sys.exit(r.returncode)
    ecrire_cotes(json.loads(cf.read_text()))


if __name__ == "__main__":
    main()
