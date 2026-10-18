"""États (impressions) du projet AURION : 8 pages A4 + ETATS.md (sections et contrôles en cm).

Usage (après generer.py bleu-royal-noir) : LD_LIBRARY_PATH=/tmp/al/lib python3 outils/etats.py
Sorties : design/styles/bleu-royal-noir/etats/*.html, etats/png/*.png, ETATS.md, etats.json
"""
import datetime as dt
import json
import subprocess
import unicodedata
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

import generer as g

ICI = Path(__file__).resolve().parent
DOS = ICI.parent / "styles" / "bleu-royal-noir"
OUT = DOS / "etats"
FONTS = (ICI.parent / "maquettes" / "fonts").as_uri()
AUJ = dt.date(2026, 9, 28)
EDITE = "Édité le lundi 28 septembre 2026 à 20:06"
NOM = "AURION"

ROYAL, OR, OR_CLAIR, NOIR = "#002366", "#C9A24B", "#E3C77A", "#000000"
TXT, GRIS, LIGNE, ZEBRE, GROUPE = "#1F2937", "#6B7690", "#E1E6EF", "#F4F6FA", "#EDF1F9"
M = 38                                   # marges de 1 cm
CM = 37.795

CSS = f"""
@font-face {{ font-family: UI; font-weight: 400; src: local("Segoe UI"), url({FONTS}/open-sans-latin-400-normal.woff2); }}
@font-face {{ font-family: UI; font-weight: 600; src: local("Segoe UI Semibold"), url({FONTS}/open-sans-latin-600-normal.woff2); }}
@font-face {{ font-family: Futur; font-weight: 300; src: local("Bahnschrift Light"), url({FONTS}/barlow-semi-condensed-latin-300-normal.woff2); }}
@font-face {{ font-family: Futur; font-weight: 400; src: local("Bahnschrift"), url({FONTS}/barlow-semi-condensed-latin-400-normal.woff2); }}
@font-face {{ font-family: Futur; font-weight: 600; src: local("Bahnschrift SemiBold"), url({FONTS}/barlow-semi-condensed-latin-600-normal.woff2); }}
html, body {{ margin: 0; background: #FFFFFF; }}
#page {{ position: relative; background: #FFFFFF; overflow: hidden; font-family: UI, "Segoe UI", sans-serif; color: {TXT}; }}
.a {{ position: absolute; white-space: nowrap; overflow: hidden; box-sizing: border-box; }}
.fu {{ font-family: Futur, Bahnschrift, sans-serif; }}
"""


def fc(n):
    return g.fcfa(n)


def d(iso):
    return g.fdate(iso)


def jour(iso):
    return dt.date.fromisoformat(iso[:10])


class Etat:
    def __init__(self, cle, nom_acc, titre, paysage=False, bouton="", source="", tri="", filtre=""):
        self.cle, self.nom_acc, self.titre = cle, nom_acc, titre
        self.W, self.H = (1123, 794) if paysage else (794, 1123)
        self.CW = self.W - 2 * M
        self.paysage = paysage
        self.bouton, self.source, self.tri, self.filtre = bouton, source, tri, filtre
        self.html = []
        self.sections = []        # (nom, hauteur px, description)
        self.ctrls = []           # (section, nom, type, x, y, w, h, contenu)
        self.y = M
        self.pages = 1

    # -- éléments
    def el(self, sec, nom, typ, x, y, w, h, contenu="", style="", note="", noter=True):
        """x, y : position sur la page ; noté dans ETATS.md relativement au haut de sa section."""
        self.html.append(f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{style}">{contenu}</div>')
        if noter and nom:
            nom = unicodedata.normalize("NFKD", nom).encode("ascii", "ignore").decode()
            self.ctrls.append((sec[0], nom, typ, x - M, y - sec[1], w, h, note))

    def img(self, sec, nom, src, x, y, w, h):
        self.html.append(f'<img class="a" src="{src}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">')
        self.ctrls.append((sec[0], nom, "Image", x - M, y - sec[1], w, h, src.replace("../", "")))

    def section(self, nom, h, desc=""):
        s = (nom, self.y)
        self.sections.append((nom, h, desc))
        self.y += h
        return s

    # -- blocs communs
    def bandeau(self, sous=EDITE, titre2=None):
        s = self.section("En-tête d'état", 0)
        self.el(s, "Rect_Bandeau", "Rectangle", M, M, self.CW, 86, style=f"background:{NOIR}", note="fond noir #000000")
        self.img(s, "Logo", "../assets/marque/aurion-menu.png", M + 20, M + 21, 181, 44)
        self.el(s, "Lbl_Titre", "Étiquette", M + self.CW - 470, M + 18, 450, 28, self.titre.upper(),
                "text-align:right;font:600 22px/28px Futur,Bahnschrift;letter-spacing:3px;color:#FFFFFF", "Bahnschrift SemiBold 16 pt, blanc")
        self.el(s, "Txt_Edition", "Zone de texte", M + self.CW - 470, M + 50, 450, 20, titre2 or sous,
                f"text-align:right;font:400 13.33px/20px Futur,Bahnschrift;letter-spacing:.5px;color:{OR_CLAIR}",
                "=\"Édité le \" & Format(Maintenant();\"dddd d mmmm yyyy à hh:nn\")" if not titre2 else
                "=\"N° R-\" & Format([IdReservation];\"0000\") & \" · Édité le \" & Format(Maintenant();\"dddd d mmmm yyyy à hh:nn\")")
        self.el(s, "Trait_Or", "Trait", M, M + 86, self.CW, 2, style=f"background:{OR}", note="doré #C9A24B, 1,5 pt")
        return s

    def chips(self, s, y, items):
        n = len(items)
        gap = 12
        w = (self.CW - gap * (n - 1)) / n
        for i, (lib, val) in enumerate(items):
            x = round(M + i * (w + gap))
            ww = round(w)
            self.el(s, f"Rect_Indicateur{i + 1}", "Rectangle", x, y, ww, 58, style="border:1px solid #D9DFEA", note="bordure #D9DFEA")
            self.el(s, None, "", x + 14, y - 1, 30, 2, style=f"background:{OR}", noter=False)
            self.el(s, f"Lbl_Indicateur{i + 1}", "Étiquette", x + 14, y + 9, ww - 28, 14, lib.upper(),
                    f"font:600 10.67px/14px Futur,Bahnschrift;letter-spacing:1.6px;color:{GRIS}", "Bahnschrift SemiBold 8 pt")
            self.el(s, f"Txt_Indicateur{i + 1}", "Zone de texte", x + 14, y + 25, ww - 28, 26, val,
                    f"font:600 20px/26px Futur,Bahnschrift;color:{ROYAL}", "Bahnschrift SemiBold 15 pt, #002366")

    def colonnes(self, cols):
        tot = sum(c[1] for c in cols)
        out, x = [], M
        for i, c in enumerate(cols):
            w = round(c[1] * self.CW / tot) if i < len(cols) - 1 else M + self.CW - x
            out.append((c[0], x, w, c[2] if len(c) > 2 else "g"))
            x += w
        return out

    def entete_colonnes(self, cols, nom_sec="En-tête de page", base=None):
        if base is None:
            s = self.section(nom_sec, 28, "répété en haut de chaque page")
        else:
            s = (nom_sec, base)
            self.y += 28
        self.el(s, "Rect_EnteteColonnes", "Rectangle", M, s[1], self.CW, 26, style=f"background:{ROYAL}", note="#002366")
        for lib, x, w, al in cols:
            ta = {"d": "right", "c": "center"}.get(al, "left")
            self.el(s, "Lbl_" + lib.split(" (")[0].replace(" ", "").replace("/", "").replace("°", "o").replace("'", ""), "Étiquette",
                    x, s[1], w, 26, lib.upper(),
                    f"padding:0 8px;text-align:{ta};font:600 11.33px/26px Futur,Bahnschrift;letter-spacing:1.3px;color:#FFFFFF",
                    "Bahnschrift SemiBold 8,5 pt, blanc", noter=True)
        return s

    def ligne(self, cols, vals, k, noms, h=22, premiere=False):
        y = self.y
        sec = ("Détail", y)
        if premiere:
            self.sections.append(("Détail", h, f"`Couleur fond` blanc, `Autre couleur fond` {ZEBRE} (lignes alternées), trait bas {LIGNE}"))
        fond = ZEBRE if k % 2 else "#FFFFFF"
        self.el(sec, None, "", M, y, self.CW, h, style=f"background:{fond};border-bottom:1px solid {LIGNE}", noter=False)
        for (lib, x, w, al), v, n in zip(cols, vals, noms):
            ta = {"d": "right", "c": "center"}.get(al, "left")
            barre = isinstance(v, tuple)
            if barre:   # (largeur relative, texte) : barre de répartition
                frac, txt = v
                self.el(sec, n, "Rectangle (barre)", x + 8, y + 7, round((w - 70) * frac), h - 14, style=f"background:{ROYAL}",
                        note="largeur calculée en VBA (Format)", noter=premiere)
                self.el(sec, None, "", x + 8 + round((w - 70) * frac) + 8, y, 60, h, txt,
                        f"font:600 12px/{h}px Futur,Bahnschrift;color:{ROYAL}", noter=False)
                continue
            self.el(sec, n, "Zone de texte", x, y, w, h, g.e(v), f"padding:0 8px;text-align:{ta};font-size:12px;line-height:{h}px",
                    "Segoe UI 9 pt", noter=premiere)
        self.y += h

    def groupe(self, titre, info, premiere=False, h=30):
        y = self.y + 6
        sec = ("En-tête de groupe", y - 6)
        if premiere:
            self.sections.append(("En-tête de groupe", h + 6, "un par valeur du regroupement"))
        self.el(sec, "Rect_Groupe", "Rectangle", M, y, self.CW, h - 4, style=f"background:{GROUPE}", note=GROUPE, noter=premiere)
        self.el(sec, "Rect_GroupeOr", "Rectangle", M, y, 4, h - 4, style=f"background:{OR}", note="doré", noter=premiere)
        self.el(sec, "Txt_Groupe", "Zone de texte", M + 16, y, 400, h - 4, g.e(titre),
                f"font:600 15px/{h - 4}px Futur,Bahnschrift;letter-spacing:1.5px;color:{ROYAL}", "Bahnschrift SemiBold 11 pt, #002366", noter=premiere)
        self.el(sec, "Txt_GroupeNombre", "Zone de texte", M + self.CW - 260, y, 244, h - 4, g.e(info),
                f"text-align:right;font:400 13.33px/{h - 4}px Futur,Bahnschrift;color:{GRIS}", "=Compte(*) & \" …\"", noter=premiere)
        self.y += h + 6

    def pied_page(self, page=1):
        y = self.H - M - 30
        s = ("Pied de page", y)
        self.sections.append(("Pied de page", 30, "en bas de chaque page"))
        self.el(s, "Trait_Pied", "Trait", M, y + 4, self.CW, 1, style=f"background:{OR}", note="doré")
        self.el(s, "Lbl_Societe", "Étiquette", M, y + 10, 420, 18, f"{NOM} · Location de prestige · Libreville",
                f"font:400 12px/18px Futur,Bahnschrift;letter-spacing:1px;color:{GRIS}", "Bahnschrift 9 pt")
        self.el(s, "Txt_Page", "Zone de texte", M + self.CW - 200, y + 10, 200, 18, f"Page {page} sur {self.pages}",
                f"text-align:right;font:600 12px/18px Futur,Bahnschrift;color:{ROYAL}", "=\"Page \" & [Page] & \" sur \" & [Pages]")

    def total(self, gauche, lib, val, h=56):
        y = self.y + 14
        s = ("Pied d'état", y - 14)
        self.sections.append(("Pied d'état", h + 14, "à la fin de l'état"))
        self.el(s, "Txt_Nombre", "Zone de texte", M, y, 400, h, g.e(gauche),
                f"font:400 14.67px/{h}px Futur,Bahnschrift;color:{GRIS}", "=Compte(*) & \" …\"")
        self.el(s, "Rect_Total", "Rectangle", M + self.CW - 330, y, 330, h, style=f"background:{ROYAL}", note="#002366")
        self.el(s, "Lbl_Total", "Étiquette", M + self.CW - 314, y + 8, 300, 14, lib.upper(),
                "font:600 10.67px/14px Futur,Bahnschrift;letter-spacing:1.8px;color:#C9D5EE", "Bahnschrift SemiBold 8 pt")
        self.el(s, "Txt_Total", "Zone de texte", M + self.CW - 314, y + 22, 300, 30, val,
                f"font:600 24px/30px Futur,Bahnschrift;color:{OR_CLAIR}", "=Somme([Montant]) · Bahnschrift SemiBold 18 pt, #E3C77A")
        self.y += h + 14

    def page_html(self):
        return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
                f'<div id="page" style="width:{self.W}px;height:{self.H}px">{"".join(self.html)}</div></body></html>')


def flux(et, items, cols, noms, entete_h=28, ligne_h=22, groupe_h=36, pied_etat_h=0):
    """Place les éléments sur la page 1 et calcule le nombre de pages."""
    bas = et.H - M - 30 - 8
    y = et.y
    pages, rendus = 1, []
    for it in items:
        h = groupe_h if it[0] == "g" else ligne_h
        if y + h > bas:
            pages += 1
            y = M + entete_h
        if pages == 1:
            rendus.append(it)
        y += h
    if y + pied_etat_h > bas:
        pages += 1
    et.pages = pages
    k = 0
    vu_g = vu_l = False
    for it in rendus:
        if it[0] == "g":
            et.groupe(it[1], it[2], premiere=not vu_g)
            vu_g = True
            k = 0
        else:
            et.ligne(cols, it[1], k, noms, ligne_h, premiere=not vu_l)
            vu_l = True
            k += 1
    return pages == 1 or (len(rendus) == len(items) and y + pied_etat_h <= bas)


# ------------------------------------------------------------------ données
RES = g.DONNEES["Reservation"]
CA = sum(g.montant(r) for r in RES)
EN_COURS = [r for r in RES if jour(r["DateDebut"]) <= AUJ <= jour(r["DateFin"])]


def etat_bon():
    r = RES[0]
    c = g.CLIENTS[r["Client"]]
    v = g.VOITURES[r["Voiture"]]
    mo, ma = g.modele_de(r["Voiture"])
    et = Etat("01-bon-de-reservation", "Etat_BonReservation", "Bon de réservation",
              bouton="Réservations › carte 03 Réservation › Imprimer",
              source="Requête : Reservation + Client + Voiture + Modele + Marque + Carburant",
              filtre="`DoCmd.OpenReport \"Etat_BonReservation\", acViewPreview, , \"IdReservation=\" & Me.Txt_Code`")
    s = et.bandeau(titre2=f"N° R-{r['IdReservation']:04d} · {EDITE}")
    y = M + 106
    et.el(s, "Lbl_Intro", "Étiquette", M, y, et.CW, 20, "Merci de votre confiance. Voici le récapitulatif de votre location.",
          f"font-size:13.33px;line-height:20px;color:{GRIS}", "Segoe UI 10 pt")
    y += 34
    bw = (et.CW - 18) // 2
    blocs = [("CLIENT", "Client", [("Nom", f"{c['Prénom']} {c['Nom']}"), ("Code client", c["CIN"]), ("N° de permis", c["NumPermis"]),
                                     ("Téléphone", c["Téléphone"]), ("Email", c["Email"]), ("Adresse", c["Adresse"])]),
             ("VÉHICULE", "Vehicule", [("Modèle", mo), ("Marque", ma), ("Matricule", r["Voiture"]), ("Carburant", g.CARBURANTS[v["Carburant"]]),
                                       ("Puissance", f"{fc(v['Puissance'])} ch"), ("Année · couleur", f"{v['Annee']} · {v['Couleur']}")])]
    for i, (tt, n, lignes) in enumerate(blocs):
        x = M + i * (bw + 18)
        et.el(s, f"Rect_{n}", "Rectangle", x, y, bw, 196, style="border:1px solid #D9DFEA", note="bordure #D9DFEA")
        et.el(s, None, "", x + 16, y - 1, 30, 2, style=f"background:{OR}", noter=False)
        et.el(s, f"Lbl_{n}", "Étiquette", x + 16, y + 12, 200, 18, tt, f"font:600 13.33px/18px Futur,Bahnschrift;letter-spacing:2.5px;color:{ROYAL}",
              "Bahnschrift SemiBold 10 pt, #002366")
        for k, (lib, val) in enumerate(lignes):
            yy = y + 42 + k * 24
            et.el(s, f"Lbl_{n}_{lib.split()[0]}" if k == 0 else None, "Étiquette", x + 16, yy, 110, 20, lib,
                  f"font-size:12px;line-height:20px;color:{GRIS}", "Segoe UI 9 pt, gris", noter=k == 0)
            et.el(s, f"Txt_{n}_{lib.split()[0]}" if k == 0 else None, "Zone de texte", x + 130, yy, bw - 146, 20, g.e(val),
                  f"font-size:13.33px;line-height:20px;font-weight:{600 if k == 0 else 400}", "Segoe UI 10 pt", noter=k == 0)
    y += 222
    cols = et.colonnes([("Désignation", 300), ("Du", 90, "c"), ("Au", 90, "c"), ("Jours", 60, "d"), ("Prix / jour", 120, "d"), ("Montant", 140, "d")])
    et.y = y
    et.sections[0] = ("En-tête d'état", y + 28 - M, "bandeau, client, véhicule et titres des colonnes")
    et.entete_colonnes(cols, "En-tête d'état", base=M)
    et.ligne(cols, [f"Location {mo} ({r['Voiture']})", d(r["DateDebut"]), d(r["DateFin"]), g.duree(r), fc(v["CoutParJour"]),
                    fc(g.montant(r))], 0, ["Txt_Designation", "Txt_DateDebut", "Txt_DateFin", "Txt_Jours", "Txt_PrixJour", "Txt_Montant"],
             h=34, premiere=True)
    # barre de progression de la location
    y = et.y + 22
    s2 = ("Pied d'état", y)
    et.sections.append(("Pied d'état", 330, "total, période, conditions et signatures"))
    et.el(s2, "Lbl_Periode", "Étiquette", M, y, 340, 16, "PÉRIODE DE LOCATION",
          f"font:600 10.67px/16px Futur,Bahnschrift;letter-spacing:1.8px;color:{GRIS}")
    et.el(s2, "Txt_Periode", "Zone de texte", M, y + 18, 360, 26, f"{g.duree(r)} jours · du {d(r['DateDebut'])} au {d(r['DateFin'])}",
          f"font:600 18.67px/26px Futur,Bahnschrift;color:{ROYAL}", "Bahnschrift SemiBold 14 pt")
    et.el(s2, "Rect_Total", "Rectangle", M + et.CW - 330, y - 4, 330, 64, style=f"background:{ROYAL}", note="#002366")
    et.el(s2, "Lbl_Total", "Étiquette", M + et.CW - 312, y + 6, 300, 14, "TOTAL À PAYER",
          "font:600 10.67px/14px Futur,Bahnschrift;letter-spacing:1.8px;color:#C9D5EE")
    et.el(s2, "Txt_Total", "Zone de texte", M + et.CW - 312, y + 22, 300, 34, f"{fc(g.montant(r))} FCFA",
          f"font:600 28px/34px Futur,Bahnschrift;color:{OR_CLAIR}", "=[Montant] · Bahnschrift SemiBold 21 pt, #E3C77A")
    y += 96
    et.el(s2, "Lbl_Conditions", "Étiquette", M, y, 300, 16, "CONDITIONS", f"font:600 10.67px/16px Futur,Bahnschrift;letter-spacing:1.8px;color:{GRIS}")
    cond = ("Le véhicule est remis propre et avec le plein ; il doit être restitué dans le même état à la date de fin indiquée ci-dessus. "
            "Toute journée entamée au-delà de cette date est facturée au prix par jour. Le client présente un permis de conduire valide "
            "et reconnaît avoir pris connaissance des conditions générales de location d'AURION.")
    et.el(s2, "Txt_Conditions", "Zone de texte", M, y + 20, et.CW, 54, cond,
          f"white-space:normal;font-size:12px;line-height:18px;color:{TXT}", "Segoe UI 9 pt, plusieurs lignes")
    y += 100
    for i, (lib, n) in enumerate([("Signature du client", "Client"), (f"Pour {NOM}", "Societe")]):
        x = M + i * (bw + 18)
        et.el(s2, f"Rect_Signature{n}", "Rectangle", x, y, bw, 110, style="border:1px solid #D9DFEA", note="bordure #D9DFEA")
        et.el(s2, f"Lbl_Signature{n}", "Étiquette", x + 16, y + 12, bw - 32, 16, lib.upper(),
              f"font:600 10.67px/16px Futur,Bahnschrift;letter-spacing:1.8px;color:{GRIS}")
        et.el(s2, None, "", x + 16, y + 84, bw - 32, 1, style="background:#D9DFEA", noter=False)
        et.el(s2, None, "", x + 16, y + 88, bw - 32, 16, "Date : ___ / ___ / ______" if i == 0 else "Cachet et signature",
              f"font-size:11px;line-height:16px;color:{GRIS}", noter=False)
    et.pied_page()
    return et


def etat_liste(cle, nom_acc, titre, paysage, bouton, source, tri, chips, cols_spec, noms, items, total=None, ligne_h=22):
    et = Etat(cle, nom_acc, titre, paysage, bouton, source, tri)
    s = et.bandeau()
    et.chips(s, M + 106, chips)
    et.sections[0] = ("En-tête d'état", 106 + 58 + 18, "bandeau, logo, titre, indicateurs (page 1 seulement)")
    et.y = M + 106 + 58 + 18
    cols = et.colonnes(cols_spec)
    et.entete_colonnes(cols)
    fin = flux(et, items, cols, noms, ligne_h=ligne_h, pied_etat_h=84 if total else 0)
    if total and fin:
        et.total(*total)
    et.pied_page()
    return et


def etats():
    out = [etat_bon()]
    # Liste des réservations
    lignes = []
    for r in RES:
        c = g.CLIENTS[r["Client"]]
        mo, ma = g.modele_de(r["Voiture"])
        lignes.append(("l", [r["IdReservation"], f"{c['Prénom']} {c['Nom']}", r["Voiture"], mo, ma, d(r["DateDebut"]), d(r["DateFin"]),
                             g.duree(r), fc(g.montant(r))]))
    out.append(etat_liste(
        "02-liste-des-reservations", "Etat_Reservations", "Liste des réservations", True,
        "Réservations › carte 04 Liste des réservations › Imprimer",
        "Requête : Reservation + Client + Voiture + Modele + Marque ; Jours = [DateFin]-[DateDebut] ; Montant = [Jours]*[CoutParJour]",
        "IdReservation croissant",
        [("Réservations", "25"), ("En cours aujourd'hui", str(len(EN_COURS))), ("Jours loués", fc(sum(g.duree(r) for r in RES))),
         ("Chiffre d'affaires", f"{fc(CA)} FCFA")],
        [("N°", 50, "d"), ("Client", 170), ("Matricule", 100), ("Modèle", 210), ("Marque", 110), ("Du", 90, "c"), ("Au", 90, "c"),
         ("Jours", 60, "d"), ("Montant (FCFA)", 150, "d")],
        ["Txt_IdReservation", "Txt_Client", "Txt_Matricule", "Txt_Modele", "Txt_Marque", "Txt_DateDebut", "Txt_DateFin", "Txt_Jours", "Txt_Montant"],
        lignes, ("25 réservations", "Chiffre d'affaires total", f"{fc(CA)} FCFA"), ligne_h=20))
    # Voitures actuellement réservées
    lignes = []
    for r in sorted(EN_COURS, key=lambda r: r["DateFin"]):
        c = g.CLIENTS[r["Client"]]
        lignes.append(("l", [r["Voiture"], g.modele_de(r["Voiture"])[0], f"{c['Prénom']} {c['Nom']}", d(r["DateDebut"]), d(r["DateFin"]),
                             f"{(jour(r['DateFin']) - AUJ).days} j", fc(g.montant(r))]))
    tot = sum(g.montant(r) for r in EN_COURS)
    proch = min(EN_COURS, key=lambda r: r["DateFin"])
    out.append(etat_liste(
        "03-voitures-reservees", "Etat_VoituresReservees", "Voitures réservées", False,
        "Tableau de bord › carte 02 Voitures actuellement réservées › Imprimer",
        "Requête « Voitures réservées » (DateDebut <= Date() Et DateFin >= Date()) ; Retour dans = [DateFin]-Date()",
        "DateFin croissante (prochain retour en premier)",
        [("En location", f"{len(EN_COURS)} / 60"), ("Taux d'occupation", f"{round(len(EN_COURS) * 100 / 60)} %"),
         ("Prochain retour", d(proch["DateFin"]))],
        [("Matricule", 84), ("Modèle", 196), ("Client", 124), ("Du", 72, "c"), ("Au", 72, "c"), ("Retour dans", 66, "d"), ("Montant", 104, "d")],
        ["Txt_Matricule", "Txt_Modele", "Txt_Client", "Txt_DateDebut", "Txt_DateFin", "Txt_RetourDans", "Txt_Montant"],
        lignes, (f"{len(EN_COURS)} voitures en location", "Montant des locations en cours", f"{fc(tot)} FCFA"), ligne_h=26))
    # Clients, regroupés par initiale du nom
    cl = sorted(g.DONNEES["Client"], key=lambda c: (c["Nom"], c["Prénom"]))
    par = defaultdict(list)
    for c in cl:
        par[c["Nom"][0].upper()].append(c)
    items = []
    for lettre in sorted(par):
        items.append(("g", lettre, f"{len(par[lettre])} client(s)"))
        items += [("l", [c["CIN"], c["Nom"], c["Prénom"], c["Sexe"], c["Adresse"], c["Téléphone"], c["Email"]]) for c in par[lettre]]
    sexes = Counter(c["Sexe"] for c in cl)
    out.append(etat_liste(
        "04-liste-des-clients", "Etat_Clients", "Liste des clients", True, "Clients › carte 01 Liste des clients › Imprimer",
        "Table Client", "Regroupement sur =Gauche([Nom];1), puis tri Nom, Prénom",
        [("Clients", "200"), ("Hommes", str(sexes["M"])), ("Femmes", str(sexes["F"])),
         ("Clients ayant réservé", str(len({r["Client"] for r in RES})))],
        [("Code", 76), ("Nom", 120), ("Prénom", 110), ("Sexe", 44, "c"), ("Adresse", 200), ("Téléphone", 140), ("Email", 250)],
        ["Txt_CIN", "Txt_Nom", "Txt_Prenom", "Txt_Sexe", "Txt_Adresse", "Txt_Telephone", "Txt_Email"], items, ligne_h=20))
    # Parc automobile, regroupé par marque
    items = []
    vs = g.DONNEES["Voiture"]
    for im, mq in sorted(g.MARQUES.items()):
        lot = sorted([v for v in vs if g.modele_de(v["Matricule"])[1] == mq], key=lambda v: -v["CoutParJour"])
        items.append(("g", mq.upper(), f"{len(lot)} voitures"))
        items += [("l", [v["Matricule"], g.modele_de(v["Matricule"])[0], v["Annee"], v["Couleur"], g.CARBURANTS[v["Carburant"]],
                         f"{fc(v['Puissance'])} ch", fc(v["CoutParJour"])]) for v in lot]
    moy = sum(v["CoutParJour"] for v in vs) / len(vs)
    out.append(etat_liste(
        "05-parc-automobile", "Etat_Voitures", "Parc automobile", False, "Voitures › carte 01 Liste des voitures › Imprimer",
        "Requête : Voiture + Modele + Marque + Carburant", "Regroupement sur Marque, puis CoutParJour décroissant",
        [("Voitures", "60"), ("Marques", "5"), ("Tarif moyen / jour", fc(int(round(moy, -3)))), ("Puissance max.", f"{fc(max(v['Puissance'] for v in vs))} ch")],
        [("Matricule", 90), ("Modèle", 200), ("Année", 52, "c"), ("Couleur", 70), ("Carburant", 80), ("Puissance", 80, "d"), ("Prix / jour", 110, "d")],
        ["Txt_Matricule", "Txt_Modele", "Txt_Annee", "Txt_Couleur", "Txt_Carburant", "Txt_Puissance", "Txt_CoutParJour"], items, ligne_h=21))
    # Marques
    lignes = []
    for im, mq in sorted(g.MARQUES.items()):
        mods = [m for m in g.DONNEES["Modele"] if m["Marque"] == im]
        lot = [v for v in vs if g.modele_de(v["Matricule"])[1] == mq]
        lignes.append(("l", [im, mq, len(mods), len(lot), fc(int(round(sum(v["CoutParJour"] for v in lot) / len(lot), -3))) if lot else "–"]))
    out.append(etat_liste(
        "06-marques", "Etat_Marques", "Marques", False, "Marques › carte 01 Liste des marques › Imprimer",
        "Requête : Marque + Compte des modèles + Compte et moyenne des voitures", "IdMarque croissant",
        [("Marques", "5"), ("Modèles", "60"), ("Voitures", "60")],
        [("Identifiant", 80), ("Marque", 220), ("Modèles", 110, "d"), ("Voitures", 110, "d"), ("Tarif moyen / jour (FCFA)", 200, "d")],
        ["Txt_IdMarque", "Txt_Marque", "Txt_NbModeles", "Txt_NbVoitures", "Txt_TarifMoyen"], lignes,
        ("5 marques", "Voitures au parc", "60 voitures"), ligne_h=30))
    # Carburants
    lignes = []
    n = Counter(v["Carburant"] for v in vs)
    for it, ty in sorted(g.CARBURANTS.items()):
        lignes.append(("l", [it, ty, n[it], f"{n[it] * 100 / 60:.1f} %".replace(".", ","), (n[it] / 60, f"{n[it]}")]))
    out.append(etat_liste(
        "07-carburants", "Etat_Carburants", "Types de carburant", False, "Carburants › carte 01 Types de carburant › Imprimer",
        "Requête : Carburant + Compte des voitures", "IdType croissant",
        [("Types", "3")] + [(ty, str(n[it])) for it, ty in sorted(g.CARBURANTS.items())],
        [("Identifiant", 80), ("Type", 150), ("Voitures", 90, "d"), ("Part", 80, "d"), ("Répartition", 300)],
        ["Txt_IdType", "Txt_Type", "Txt_NbVoitures", "Txt_Part", "Rect_Barre"], lignes, ("3 types de carburant", "Voitures au parc", "60 voitures"),
        ligne_h=34))
    # Modèles, regroupés par marque
    items = []
    for im, mq in sorted(g.MARQUES.items()):
        mods = [m for m in g.DONNEES["Modele"] if m["Marque"] == im]
        items.append(("g", mq.upper(), f"{len(mods)} modèles"))
        for m in mods:
            lot = [v for v in vs if v["Modele"] == m["IdModele"]]
            items.append(("l", [m["IdModele"], m["Modele"], len(lot), fc(min(v["CoutParJour"] for v in lot)) if lot else "–"]))
    out.append(etat_liste(
        "08-modeles", "Etat_Modeles", "Modèles", False, "Modèles › carte 01 Liste des modèles › Imprimer",
        "Requête : Modele + Marque + Compte des voitures", "Regroupement sur Marque, puis IdModele",
        [("Modèles", "60"), ("Marques", "5"), ("Modèles au parc", str(len({v["Modele"] for v in vs})))],
        [("Identifiant", 90), ("Modèle", 330), ("Voitures", 110, "d"), ("Prix / jour (FCFA)", 188, "d")],
        ["Txt_IdModele", "Txt_Modele", "Txt_NbVoitures", "Txt_PrixJour"], items, ligne_h=21))
    return out


def cm(px):
    return f"{px / CM:.2f}".replace(".", ",")


def ecrire_md(liste):
    L = ["# États (impressions) · AURION", "",
         "Chaque bouton **Imprimer** des formulaires ouvre un état. Les aperçus sont dans `etats/png/` (A4, prêts à reproduire).", "",
         "## Réglages communs", "",
         "* **Mise en page** : A4, marges de **1 cm** partout (*Mise en page › Marges › Personnalisées*). Portrait sauf mention « paysage ».",
         "* **Bandeau** (en-tête d'état) : Rectangle noir `#000000` sur toute la largeur, 2,28 cm de haut ; logo `assets/marque/aurion-menu.png` "
         "(4,79 × 1,16 cm) ; titre en **Bahnschrift SemiBold 16 pt** blanc, majuscules ; date d'édition dorée `#E3C77A` ; trait doré `#C9A24B` dessous.",
         "* **En-tête de page** : Rectangle bleu royal `#002366` de 0,69 cm, étiquettes blanches Bahnschrift SemiBold 8,5 pt en majuscules. "
         "Propriété de la section *Répéter la section* : **Oui**.",
         "* **Détail** : zones de texte Segoe UI 9 pt, `Couleur fond` blanc et **`Autre couleur fond` `#F4F6FA`** (lignes alternées automatiques), "
         "trait bas `#E1E6EF`. Toutes les zones de texte : `Style bordure` **Transparent**.",
         "* **En-tête de groupe** (quand l'état est regroupé) : Rectangle `#EDF1F9` avec une barre dorée de 0,11 cm à gauche, texte Bahnschrift SemiBold 11 pt `#002366`.",
         "* **Pied de page** : trait doré, « AURION · Location de prestige · Libreville » à gauche, `=\"Page \" & [Page] & \" sur \" & [Pages]` à droite.",
         "* **Pied d'état** : rectangle bleu royal `#002366` avec le total en **Bahnschrift SemiBold 18 pt doré `#E3C77A`**.", "",
         "Code des boutons Imprimer (procédure `Sur clic`) :", "", "```vba",
         "DoCmd.OpenReport \"Etat_Clients\", acViewPreview      ' remplacer par le nom de l'état", "```", "",
         "## Liste des états", "",
         "| Aperçu | Nom de l'état | Ouvert par | Orientation |", "|---|---|---|---|"]
    for et in liste:
        L.append(f"| `etats/png/{et.cle}.png` | **{et.nom_acc}** | {et.bouton} | {'Paysage' if et.paysage else 'Portrait'} |")
    for et in liste:
        L += ["", f"## {et.titre} · `{et.nom_acc}`", "",
              f"* Aperçu : `etats/png/{et.cle}.png` · {'paysage' if et.paysage else 'portrait'} · {et.pages} page(s) avec les données actuelles",
              f"* Bouton : {et.bouton}", f"* Source : {et.source}"]
        if et.tri:
            L.append(f"* Tri et regroupement (*Regrouper, trier et total*) : {et.tri}")
        if et.filtre:
            L.append(f"* Ouverture filtrée : {et.filtre}")
        L += ["", "| Section | Hauteur | Remarque |", "|---|---:|---|"]
        vus = set()
        for nom, h, desc in et.sections:
            if nom in vus or not h:
                continue
            vus.add(nom)
            L.append(f"| {nom} | {cm(h)} cm | {desc} |")
        L += ["", "| Contrôle | Type | Section | Gauche | Haut | Largeur | Hauteur | Contenu / format |", "|---|---|---|---:|---:|---:|---:|---|"]
        for sec, nom, typ, x, y, w, h, note in et.ctrls:
            L.append(f"| `{nom}` | {typ} | {sec} | {cm(x)} | {cm(y)} | {cm(w)} | {cm(h)} | {note} |")
    (DOS / "ETATS.md").write_text("\n".join(L) + "\n")


def main():
    (OUT / "png").mkdir(parents=True, exist_ok=True)
    for f in list(OUT.glob("*.html")) + list((OUT / "png").glob("*.png")):
        f.unlink()
    liste = etats()
    jobs = []
    for et in liste:
        p = OUT / f"{et.cle}.html"
        p.write_text(et.page_html())
        jobs.append({"html": p.as_uri(), "out": str(OUT / "png" / f"{et.cle}.png"), "w": et.W, "h": et.H, "transparent": False,
                     "sel": "#page", "scale": 2})
    tmp = Path(tempfile.mkdtemp(prefix="etats-"))
    jf = tmp / "jobs.json"
    jf.write_text(json.dumps({"assets": jobs, "ecrans": [], "cotes": str(tmp / "c.json")}))
    r = subprocess.run(["node", str(ICI / "rendre.mjs"), str(jf)], cwd=ICI)
    if r.returncode:
        raise SystemExit(r.returncode)
    ecrire_md(liste)
    (DOS / "etats.json").write_text(json.dumps([{"png": f"etats/png/{et.cle}.png", "nom": et.nom_acc, "titre": et.titre,
                                                 "bouton": et.bouton, "pages": et.pages} for et in liste], ensure_ascii=False, indent=1))
    for et in liste:
        print(f"{et.cle:28} {et.nom_acc:24} {et.pages} page(s)")


if __name__ == "__main__":
    main()
