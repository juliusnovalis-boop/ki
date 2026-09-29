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
        y = 110 + i * 44
        on = cle == actif
        nav += (f'<div class="nav{" actif" if on else ""}" style="top:{y}px" {acc("BoutonNavigation_" + cle, "Bouton de navigation")}>'
                f'{svg(ico, MARINE if on else NAV_TXT, 18)}{e(lib)}</div>')
    corps = f"""
<div class="menu" {acc("Menu_Fond", "Image (menu-fond.jpg)")}>
  <img class="abs" src="../assets/photos/menu-fond.jpg" style="left:0;top:0;width:220px;height:{H}px">
  <div class="logo" {acc("Logo", "Image + étiquette")}>{svg("car-front", "#FFFFFF", 24, 1.8)}{NOM_APPLI}</div>
  <div class="rubrique" style="top:84px">Menu principal</div>
  {nav}
  <div class="slogan" {acc("Slogan", "Étiquette")}>Location de véhicules<br>à Libreville</div>
</div>
<div class="entete" {acc("Entete", "Rectangle")}>
  <div class="date" style="left:24px" {acc("Date_Heure", "Zone de texte")}>{svg("calendar-range", GRIS, 15)}lundi 28 septembre 2026 · 20:06</div>
  <div class="avatar" style="right:196px;top:12px" {acc("Btn_Avatar", "Bouton (ellipse)")}>AD</div>
  <div class="utilisateur" style="right:72px;top:11px" {acc("Utilisateur", "Étiquettes")}><b>admin</b><span>Administrateur</span></div>
  <div class="btn-ico abs" style="right:24px;top:12px;width:32px;height:32px" {acc("Btn_Quitter", "Bouton")}>{svg("power", MARINE, 16)}</div>
</div>
<div class="contenu" id="contenu">
{contenu}
</div>"""
    return fenetre(NOM_APPLI, W, H, corps)


BANDEAUX = {  # clé : (photo source, position de l'image, hauteur)
    "tableau": ("tableau-flotte.jpg", "center 62%", 128),
    "reservations": ("reservations-cles.jpg", "center 45%", 92),
    "clients": ("clients-accueil.jpg", "center 12%", 92),
    "voitures": ("tableau-flotte.jpg", "center 68%", 92),
    "marques": ("voitures-showroom.jpg", "center 72%", 92),
    "carburants": ("carburants-pompe.jpg", "center 40%", 92),
    "modeles": ("modeles-interieur.jpg", "center 55%", 92),
}
BW = CW - 48  # largeur des bandeaux : 1300 px


def bandeau(cle, titre, sous_titre):
    h = BANDEAUX[cle][2]
    ty = (h - 58) // 2
    return (f'<div class="bandeau" style="left:24px;top:24px;width:{BW}px;height:{h}px;'
            f'background-image:url(../assets/photos/bandeau-{cle}.jpg)" {acc("Bandeau", "Image (bandeau-" + cle + ".jpg)")}>'
            f'<div class="b-titre" style="top:{ty}px" {acc("Bandeau_Titre", "Étiquette")}>{e(titre)}</div>'
            f'<div class="b-sous" style="top:{ty + 34}px" {acc("Bandeau_SousTitre", "Étiquette")}>{e(sous_titre)}</div></div>')


# --------------------------------------------------------------------------
# Briques
# --------------------------------------------------------------------------
ACTIONS = {"Ajouter": "plus", "Actualiser": "refresh-cw", "Rechercher": "search", "Imprimer": "printer"}


def carte(nom, titre, x, y, w, h, interieur="", actions=(), info=None, icone=None):
    act = ""
    if actions:
        act = '<div class="actions">' + "".join(
            f'<div class="btn-ico" title="{a}" {acc("Btn_" + a, "Bouton")}>{svg(ACTIONS[a], BLEU, 16)}</div>' for a in actions) + "</div>"
    tx = 48 if icone else 20
    ico = f'<div class="abs" style="left:20px;top:16px">{svg(icone, BLEU, 18)}</div>' if icone else ""
    inf = f'<div class="info" style="left:{tx + 10 + int(len(titre) * 8.6)}px">{e(info)}</div>' if info else ""
    return (f'<div class="carte" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px" {acc(nom, "Rectangle")}>'
            f'<div class="bande"></div>{ico}<div class="titre-c" style="left:{tx}px">{e(titre)}</div>{inf}{act}'
            f'<div class="trait"></div>{interieur}</div>')


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


def boutons_crud(x, y, w=130):
    return (f'<div class="btn primaire" style="left:{x}px;top:{y}px;width:{w}px" {acc("Btn_Enregistrer", "Bouton")}>{svg("save", "#FFFFFF", 16)}Enregistrer</div>'
            f'<div class="btn danger" style="left:{x + w + 10}px;top:{y}px;width:{w}px" {acc("Btn_Supprimer", "Bouton")}>{svg("trash-2", ROUGE, 16)}Supprimer</div>')


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
MODELE_RES = {
    1: ("Ferrari 296 GTB", "Ferrari"),
    2: ("Lamborghini Urus SE", "Lamborghini"),
    3: ("Bentley Continental GT", "Bentley"),
    4: ("Bugatti Chiron", "Bugatti"),
    5: ("Rolls-Royce Phantom", "Rolls-Royce"),
    6: ("Ferrari 296 GTS", "Ferrari"),
    7: ("Lamborghini Revuelto", "Lamborghini"),
}


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
    kpis = [("CA", "Chiffre d'affaires", "104 261 200", "FCFA", "sur 25 réservations", "wallet", "#1E40AF", "#3F5BBE"),
            ("Voitures", "Voitures", "60", "", "8 en location aujourd'hui", "car-front", "#2563EB", "#4B7FEF"),
            ("Clients", "Clients", "200", "", "Meilleur client : Cynthia Kombila", "users", "#3B82F6", "#5C97F8")]
    kw = (CW - 48 - 32) // 3
    out = bandeau("tableau", "Bonjour, admin", "Voici l'activité de RENTAL GABON CAR au 28 septembre 2026.")
    for i, (n, lib, val, unit, sub, ico, fond, pastille) in enumerate(kpis):
        x = 24 + i * (kw + 16)
        u = f"<small>{unit}</small>" if unit else ""
        out += (f'<div class="kpi" style="left:{x}px;top:168px;width:{kw}px;height:100px;background:{fond};border-color:{fond}" {acc("Carte_" + n, "Rectangle")}>'
                f'<div class="lib">{e(lib)}</div><div class="val" {acc("Txt_" + n, "Zone de texte")}>{val}{u}</div>'
                f'<div class="sub">{e(sub)}</div>'
                f'<div class="pastille" style="background:{pastille}" {acc("Pastille_" + n, "Rectangle + image")}>{svg(ico, "#FFFFFF", 24)}</div></div>')

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
               res, 20, 66, lw1 - 42, 334)
    p1 = carte("Carte_Reservees", "Voitures actuellement réservées", 24, 284, lw1, 420, l1, actions=["Imprimer"],
               info="8 en cours", icone="clipboard-list")

    lw2 = CW - 48 - 16 - lw1
    top = [("Cynthia", "Kombila", 18457500), ("Junior", "Ondo", 11097500), ("Léa", "Eyang", 10413000),
           ("Cédric", "Nkoghe", 8021250), ("Noëlle", "Mba", 7416000)]
    l2 = liste("Liste_Top5", [("Prénom", 120), ("Nom", 120), ("CA (FCFA)", 150, "num")],
               [[a, b, fcfa(c)] for a, b, c in top], 20, 64, lw2 - 40, 124)
    p2 = carte("Carte_Top5", "5 meilleurs clients", 24 + lw1 + 16, 284, lw2, 202, l2, icone="trophy")
    l3 = liste("Liste_Carburants", [("Type", 150), ("Voitures", 110, "num"), ("Part", 130, "num")],
               [["Essence", 31, "51,7 %"], ["Diesel", 23, "38,3 %"], ["Hybride", 6, "10,0 %"]], 20, 64, lw2 - 40, 124)
    p3 = carte("Carte_Carburants", "Flotte par carburant", 24 + lw1 + 16, 502, lw2, 202, l3, icone="fuel")
    return coquille("tableau", "Tableau de bord", out + p1 + p2 + p3)


def ecran_reservations():
    lw, iw = 104, 470
    cw = (CW - 48 - 16) // 2
    b = bandeau("reservations", "Réservations", "25 réservations · 8 en cours aujourd'hui")
    cli = (champ("Cbo_Client", "Client", "Jean Mboumba", 20, 64, lw, iw, "liste")
           + champ("Txt_Telephone", "Téléphone", "(+241) 62 54 85 85", 20, 100, lw, iw, "lecture")
           + champ("Txt_Email", "Email", "jean.mboumba1@example.com", 20, 136, lw, iw, "lecture"))
    p1 = carte("Carte_Client", "Client", 24, 132, cw, 180, cli, icone="user")
    voi = (champ("Cbo_Voiture", "Voiture", "AB-3988-AA", 20, 64, lw, iw, "liste")
           + champ("Txt_Modele", "Modèle", "Ferrari 296 GTB", 20, 100, lw, iw, "lecture")
           + champ("Txt_Marque", "Marque", "Ferrari", 20, 136, lw, iw, "lecture"))
    p2 = carte("Carte_Voiture", "Voiture", 24 + cw + 16, 132, cw, 180, voi, icone="car")

    res = (champ("Txt_Code", "Code", "1", 20, 64, 104, 80, droite=True)
           + champ("Txt_DateDebut", "Date de début", "23/09/2026", 20, 100, 104, 120, droite=True)
           + champ("Txt_DateFin", "Date de fin", "24/10/2026", 272, 100, 90, 120, droite=True)
           + f'<div class="btn secondaire" style="left:494px;top:98px;width:60px" {acc("Btn_OK", "Bouton")}>OK</div>'
           + nav_enreg(124, 138, "1 sur 25")
           + '<div class="sep-v" style="left:640px;top:51px;height:127px"></div>'
           + champ("Txt_Duree", "Durée", "31 jour(s)", 664, 64, 90, 200, "lecture", droite=True)
           + champ("Txt_Montant", "Montant", "1 023 000 FCFA", 664, 100, 90, 200, "lecture", droite=True, total=True)
           + boutons_crud(CW - 48 - 20 - 270, 136))
    p3 = carte("Carte_Reservation", "Réservation", 24, 328, CW - 48, 180, res,
               actions=["Ajouter", "Actualiser", "Rechercher", "Imprimer"], icone="calendar-range")

    l = liste("Liste_Reservations", [("Code", 60, "num"), ("Date de début", 130), ("Date de fin", 130), ("Prénom", 150), ("Nom", 160),
                                     ("Matricule", 140), ("Modèle", 150), ("Marque", 120)],
              lignes_reservations(), 20, 62, CW - 48 - 40, 104, total=25)
    p4 = carte("Carte_Liste", "Liste des réservations", 24, 524, CW - 48, 180, l, actions=["Imprimer"],
               info="25 réservations", icone="list")
    return coquille("reservations", "Réservations", b + p1 + p2 + p3 + p4)


def ecran_fiche(cle, titre, sous_titre, titre_fiche, icone, champs, titre_liste, cols, lignes, total, compteur, info,
                fiche_w=520, grande_liste=True):
    y0 = 132
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
    inner += boutons_crud(fiche_w - 20 - 270, y)
    h = y + 32 + 18
    p1 = carte("Carte_Fiche", titre_fiche, 24, y0, fiche_w, h, inner,
               actions=["Ajouter", "Actualiser", "Rechercher", "Imprimer"], icone=icone)
    lx = 24 + fiche_w + 16
    lw_ = CW - 24 - lx
    lh = (704 - y0) if grande_liste else max(h, 300)
    l = liste("Liste_" + cle.capitalize(), cols, lignes, 20, 66, lw_ - 40, lh - 86, total=total)
    p2 = carte("Carte_Liste", titre_liste, lx, y0, lw_, lh, l, actions=["Imprimer"], info=info, icone="list")
    return coquille(cle, titre, bandeau(cle, titre, sous_titre) + p1 + p2)


def ecran_clients():
    c = CLIENTS["CL-0001"]
    champs = [("Txt_CIN", "Code client", c["CIN"], "texte", 140), ("Txt_Permis", "N° de permis", c["NumPermis"], "texte", 180),
              ("Txt_Prenom", "Prénom", c["Prénom"], "texte"), ("Txt_Nom", "Nom", c["Nom"], "texte"),
              ("Cbo_Sexe", "Sexe", c["Sexe"], "liste", 80), ("Txt_Adresse", "Adresse", c["Adresse"], "texte"),
              ("Txt_Telephone", "Téléphone", c["Téléphone"], "texte"), ("Txt_Email", "Email", c["Email"], "texte")]
    lignes = [[x["CIN"], x["NumPermis"], x["Prénom"], x["Nom"], x["Sexe"], x["Adresse"], x["Téléphone"]] for x in DONNEES["Client"][:30]]
    cols = [("Code client", 76), ("N° de permis", 112), ("Prénom", 86), ("Nom", 96), ("Sexe", 36), ("Adresse", 160), ("Téléphone", 139)]
    return ecran_fiche("clients", "Clients", "200 clients enregistrés", "Fiche client", "user", champs, "Liste des clients",
                       cols, lignes, 200, "1 sur 200", "200 clients")


def ecran_voitures():
    champs = [("Txt_Matricule", "Matricule", "AB-2344-AA", "texte", 140), ("Txt_Annee", "Année", "2025", "texte", 80),
              ("Txt_Couleur", "Couleur", "Rouge rubis", "texte"), ("Txt_Puissance", "Puissance", "612 CV", "texte", 80),
              ("Txt_CoutJour", "Coût par jour", "95 000 FCFA", "texte", 140), ("Cbo_Modele", "Modèle", "Ferrari Roma", "liste"),
              ("Cbo_Carburant", "Carburant", "Essence", "liste"), ("Cbo_Marque", "Marque", "Ferrari", "liste")]
    voitures = [
        ("AB-2344-AA", "Ferrari Roma", "Ferrari", "2025", "Rouge", "612 CV", "95 000"),
        ("LB-8235-AA", "Lamborghini Urus SE", "Lamborghini", "2025", "Noir", "800 CV", "42 000"),
        ("RT-7002-AA", "Bentley Continental GT", "Bentley", "2024", "Blanc", "550 CV", "46 000"),
        ("CD-2481-AA", "Bugatti Chiron", "Bugatti", "2022", "Bleu nuit", "1 500 CV", "27 500"),
        ("DF-1111-AA", "Rolls-Royce Phantom", "Rolls-Royce", "2023", "Noir", "563 CV", "27 500"),
        ("EF-4262-AA", "Ferrari 296 GTB", "Ferrari", "2025", "Gris", "830 CV", "60 000"),
        ("FG-2892-AA", "Lamborghini Revuelto", "Lamborghini", "2025", "Jaune", "1 001 CV", "48 000"),
        ("FJ-4673-AA", "Bentley Continental GTC", "Bentley", "2023", "Argent", "550 CV", "65 000"),
        ("GA-5495-AA", "Bugatti Chiron Sport", "Bugatti", "2024", "Rouge", "1 500 CV", "40 000"),
        ("KL-8098-AA", "Rolls-Royce Ghost", "Rolls-Royce", "2023", "Gris", "563 CV", "33 000"),
        ("MN-6728-AA", "Ferrari 296 GTS", "Ferrari", "2024", "Jaune", "830 CV", "35 000"),
        ("QS-6865-AA", "Lamborghini Temerario", "Lamborghini", "2024", "Noir", "920 CV", "40 000"),
    ]
    cols = [("Matricule", 98), ("Modèle", 200), ("Marque", 85), ("Année", 56),
            ("Couleur", 68), ("Puissance", 75), ("Coût/jour", 110, "num")]
    return ecran_fiche("voitures", "Voitures", "60 véhicules · 5 marques haut de gamme · 3 carburants", "Fiche voiture", "car",
                       champs, "Parc de véhicules", cols, [list(x) for x in voitures], 60, "1 sur 60", "60 véhicules")


def ecran_marques():
    champs = [("Txt_IdMarque", "Identifiant", "1", "texte", 80), ("Txt_Marque", "Marque", "Ferrari", "texte")]
    lignes = [[m["IdMarque"], m["Marque"]] for m in DONNEES["Marque"]]
    return ecran_fiche("marques", "Marques", "5 marques premium · 60 modèles", "Fiche marque", "tag", champs, "Marques du parc premium",
                       [("Identifiant", 90), ("Marque", 200)], lignes, None, "1 sur 5", "5 marques", grande_liste=False)


def ecran_carburants():
    champs = [("Txt_IdType", "Identifiant", "1", "texte", 80), ("Txt_Type", "Type", "Diesel", "texte")]
    lignes = [[c["IdType"], c["Type"]] for c in DONNEES["Carburant"]]
    return ecran_fiche("carburants", "Carburants", "3 types de carburant", "Fiche carburant", "fuel", champs,
                       "Types de carburant", [("Identifiant", 90), ("Type", 200)], lignes, None, "1 sur 3", "3 types",
                       grande_liste=False)


def ecran_modeles():
    marques = {m["IdMarque"]: m["Marque"] for m in DONNEES["Marque"]}
    premier = DONNEES["Modele"][0]
    champs = [("Txt_IdModele", "Identifiant", str(premier["IdModele"]), "texte", 80),
              ("Txt_Modele", "Modèle", premier["Modele"], "texte"),
              ("Cbo_Marque", "Marque", marques[premier["Marque"]], "liste")]
    lignes = [[m["IdModele"], m["Modele"], marques[m["Marque"]]] for m in DONNEES["Modele"][:30]]
    return ecran_fiche("modeles", "Modèles", "60 modèles haut de gamme répartis sur 5 marques", "Fiche modèle", "layers", champs,
                       "Catalogue premium", [("Identifiant", 90), ("Modèle", 180), ("Marque", 140)], lignes, 60,
                       "1 sur 60", "60 modèles")


def ecran_login():
    lw, lh = 880, 500
    fx = 470
    corps = f"""
<div class="abs" style="left:0;top:0;width:{lw}px;height:{lh}px;background:#FFFFFF" {acc("Login_Fond", "Section Détail")}></div>
<img class="abs" src="../assets/photos/login-photo.jpg" style="left:0;top:0;width:420px;height:{lh}px" {acc("Login_Photo", "Image (login-photo.jpg)")}>
<div class="abs" style="left:36px;top:36px;display:flex;align-items:center;gap:10px;font-size:18.67px;font-weight:600;color:#FFFFFF;letter-spacing:.5px" {acc("Logo", "Image + étiquette")}>{svg("car-front", "#FFFFFF", 28, 1.8)}{NOM_APPLI}</div>
<div class="abs" style="left:36px;top:388px;width:350px;font-size:21.33px;font-weight:600;color:#FFFFFF;line-height:28px" {acc("Login_Slogan", "Étiquette")}>Location de véhicules<br>à Libreville</div>
<div class="abs" style="left:36px;top:454px;font-size:12px;color:#C9D6F5" {acc("Login_Copyright", "Étiquette")}>© 2026 RENTAL GABON CAR</div>
<div class="abs" style="left:{fx}px;top:84px;font-size:26.67px;font-weight:600;color:{MARINE}" {acc("Lbl_Titre", "Étiquette")}>Connexion</div>
<div class="abs" style="left:{fx}px;top:126px;font-size:14.67px;color:#6B7280">Entrez vos identifiants pour accéder à l'application.</div>
<div class="etiq" style="left:{fx}px;top:172px">Nom d'utilisateur</div>
<div class="champ" style="left:{fx}px;top:200px;width:360px;height:34px;line-height:32px" {acc("Txt_Utilisateur", "Zone de texte")}>admin</div>
<div class="etiq" style="left:{fx}px;top:244px">Mot de passe</div>
<div class="champ" style="left:{fx}px;top:272px;width:360px;height:34px;line-height:32px;letter-spacing:2px" {acc("Txt_MotDePasse", "Zone de texte")}>********</div>
<div class="btn primaire" style="left:{fx}px;top:334px;width:360px;height:38px" {acc("Btn_Connexion", "Bouton")}>Se connecter</div>
<div class="abs" style="left:{fx}px;top:392px;width:360px;font-size:12px;color:#6B7280;text-align:center">Mot de passe oublié ? Contactez l'administrateur.</div>
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
        add(f"menu-{ico}.png", 18, ico, NAV_TXT, 18)
        add(f"menu-{ico}-actif.png", 18, ico, MARINE, 18)
    for ico in list(ACTIONS.values()) + ["chevron-first", "chevron-left", "chevron-right", "chevron-last", "power"]:
        add(f"bouton-{ico}.png", 16, ico, MARINE if ico == "power" else BLEU, 16)
    add("date.png", 15, "calendar-range", GRIS, 15)
    add("logo-voiture.png", 24, "car-front", "#FFFFFF", 24, 1.8)
    for ico, col in [("wallet", "#FFFFFF"), ("car-front", "#FFFFFF"), ("users", "#FFFFFF")]:
        add(f"indicateur-{ico}.png", 24, ico, col, 24)
    add("bouton-enregistrer.png", 16, "save", "#FFFFFF", 16)
    add("bouton-supprimer.png", 16, "trash-2", ROUGE, 16)
    for ico in ["user", "car", "calendar-range", "list", "trophy", "clipboard-list", "tag", "fuel", "layers"]:
        add(f"carte-{ico}.png", 18, ico, BLEU, 18)

    # Huit photos de référence fournies : recadrées à la taille exacte et teintées en bleu pour Access
    def photo(out, w, h, src, pos, voile):
        p = tmp / (out.replace("/", "_") + ".html")
        p.write_text(f'<!doctype html><html><head><style>html,body{{margin:0}}#a{{position:relative;width:{w}px;height:{h}px;'
                     f'overflow:hidden;background:{MARINE}}}#a img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;'
                     f'object-position:{pos}}}#a .v{{position:absolute;inset:0;background:{voile}}}</style></head>'
                     f'<body><div id="a"><img src="{(ICI / "photos" / src).as_uri()}"><div class="v"></div></div></body></html>')
        jobs.append({"html": p.as_uri(), "out": str(ASSETS / out), "w": w, "h": h, "transparent": False, "sel": "#a"})

    voile_b = ("linear-gradient(90deg, rgba(30,58,138,.97) 0%, rgba(30,58,138,.92) 30%, rgba(30,58,138,.55) 58%, "
               "rgba(30,58,138,.18) 100%)")
    for cle, (src, pos, h) in BANDEAUX.items():
        photo(f"photos/bandeau-{cle}.jpg", BW, h, src, pos, voile_b)
    photo("photos/menu-fond.jpg", 220, H, "menu-route.jpg", "center 70%",
          f"linear-gradient(180deg, {MARINE} 0%, {MARINE} 55%, rgba(30,58,138,.55) 70%, rgba(30,58,138,.25) 86%, rgba(30,58,138,.60) 100%)")
    photo("photos/login-photo.jpg", 420, 500, "login-route.jpg", "62% center",
          "linear-gradient(180deg, rgba(30,58,138,.88) 0%, rgba(30,58,138,.35) 38%, rgba(30,58,138,.25) 62%, rgba(30,58,138,.92) 100%)")
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
    (ASSETS / "photos").mkdir(parents=True, exist_ok=True)
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
