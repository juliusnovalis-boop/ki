"""Les 4 designs « camarades » : chacun a sa propre navigation, sa disposition et son écran de connexion.

  a  Éditorial  (noir et blanc)     barre de navigation horizontale, grand bandeau photo, titres à empattements
  b  Rail       (rose et blanc)     rail d'icônes à gauche, panneau photo vertical à droite, formulaire en haut
  c  Latéral    (vert jade et blanc) menu photo à droite, pas d'en-tête, libellés au-dessus des champs
  d  Cockpit    (argenté et noir)   photo plein écran, onglets en pastilles, indicateurs empilés

Le module est branché par generer.py (variable g = module generer) : il réutilise ses briques
(carte, champ, liste, nav_enreg, boutons_crud, svg…) et le thème courant g.T.
"""
g = None  # module generer, fixé par generer.main()

# --------------------------------------------------------------------------
# Photos de chaque page : (photo source, position paysage, position verticale)
# --------------------------------------------------------------------------
PHOTOS = {
    "tableau": ("tableau-flotte.jpg", "center 68%", "64% center"),
    "reservations": ("reservations-cles.jpg", "center 50%", "42% center"),
    "clients": ("clients-accueil.jpg", "center 28%", "52% center"),
    "voitures": ("voitures-showroom.jpg", "center 66%", "58% center"),
    "marques": ("marques-calandres.jpg", "center 46%", "50% center"),
    "carburants": ("carburants-pompe.jpg", "center 46%", "62% center"),
    "modeles": ("modeles-interieur.jpg", "center 55%", "50% center"),
}
TEXTES = {  # (titre, sous-titre) des pages
    "tableau": ("Bonjour, admin", "Voici l'activité de {nom} au 28 septembre 2026."),
    "reservations": ("Réservations", "25 réservations · 8 en cours aujourd'hui"),
    "clients": ("Clients", "200 clients enregistrés"),
    "voitures": ("Voitures", "60 véhicules de prestige · 5 marques · 3 types de carburant"),
    "marques": ("Marques", "5 marques de prestige · 60 modèles"),
    "carburants": ("Carburants", "3 types de carburant"),
    "modeles": ("Modèles", "60 modèles répartis sur 5 marques"),
}
CHIFFRES = {  # grand chiffre affiché sur la photo (design b)
    "tableau": ("8", "voitures en location aujourd'hui"),
    "clients": ("200", "clients enregistrés"),
    "voitures": ("60", "véhicules de prestige"),
    "marques": ("5", "marques de prestige"),
    "carburants": ("3", "types de carburant"),
    "modeles": ("60", "modèles au catalogue"),
}
TITRES_MENU = {"tableau": "Tableau de bord", "reservations": "Réservations", "clients": "Clients", "voitures": "Voitures",
               "marques": "Marques", "carburants": "Carburants", "modeles": "Modèles"}


def e(s):
    return g.e(s)


def acc(n, t):
    return g.acc(n, t)


def T(k):
    return g.T[k]


def photo_url(nom):
    return f"{g.ASSET_URL}/photos/{nom}"


def img(nom, x, y, w, h, acc_nom="Image_Fond"):
    return (f'<img class="abs" src="{photo_url(nom)}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px" '
            f'{acc(acc_nom, "Image (" + nom + ")")}>')


def lbl(x, y, texte, style="", nom=None, typ="Étiquette"):
    a = acc(nom, typ) if nom else ""
    return f'<div class="abs" style="left:{x}px;top:{y}px;white-space:nowrap;{style}" {a}>{texte}</div>'


def avatar(x, y, d=32):
    return (f'<div class="avatar" style="left:{x}px;top:{y}px;width:{d}px;height:{d}px" {acc("Btn_Avatar", "Bouton (ellipse)")}>AD</div>')


def champ_haut(nom, lib, val, x, y, w, kind="texte", droite=False, total=False):
    """Libellé au-dessus du champ (design c)."""
    h = g.champ(nom, "", val, x, y + 20, 0, w, kind, droite, total)
    return f'<div class="etiq-haut" style="left:{x}px;top:{y}px">{e(lib)}</div>' + h


def contenu(x, y, w, h, corps, fond=True):
    st = "" if fond else "background:transparent;"
    return f'<div class="contenu" id="contenu" {acc("Sous_Formulaire", "Sous-formulaire")} style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;right:auto;bottom:auto;{st}">{corps}</div>'


# --------------------------------------------------------------------------
# Données des écrans
# --------------------------------------------------------------------------
def donnees_tableau():
    import datetime as dt
    ca, top = g.stats()
    auj = dt.date(2026, 9, 28)
    res = []
    for r in g.DONNEES["Reservation"]:
        d0, d1 = dt.date.fromisoformat(r["DateDebut"][:10]), dt.date.fromisoformat(r["DateFin"][:10])
        if d0 <= auj <= d1:
            c = g.CLIENTS[r["Client"]]
            res.append([r["Voiture"], g.modele_de(r["Voiture"])[0], g.fdate(r["DateDebut"]), g.fdate(r["DateFin"]), c["Prénom"], c["Nom"]])
    kpis = [("CA", "Chiffre d'affaires", g.fcfa(ca), "FCFA", "sur 25 réservations", "wallet"),
            ("Voitures", "Voitures", "60", "", "8 en location aujourd'hui", "car-front"),
            ("Clients", "Clients", "200", "", f"Meilleur client : {top[0][0]} {top[0][1]}", "users")]
    return kpis, res, top


COLS_RES = [("Matricule", 100), ("Modèle", 200), ("Date de début", 100), ("Date de fin", 100), ("Prénom", 100), ("Nom", 100)]
COLS_TOP = [("Prénom", 120), ("Nom", 120), ("CA (FCFA)", 150, "num")]
COLS_CARB = [("Type", 120), ("Voitures", 90, "num"), ("Part", 90, "num")]
COLS_LISTE_RES = [("Code", 50, "num"), ("Date de début", 100), ("Date de fin", 100), ("Prénom", 110), ("Nom", 120),
                  ("Matricule", 110), ("Modèle", 220), ("Marque", 110)]


def cartes_listes(x1, y1, w1, h1, x2, y2, w2, h2, x3, y3, w3, h3, res, top):
    """Les 3 cartes de listes du tableau de bord, positionnées librement."""
    l1 = g.liste("Liste_Voitures_Reservees", COLS_RES, res, 20, 64, w1 - 40, h1 - 84)
    p1 = g.carte("Carte_Reservees", "Voitures actuellement réservées", x1, y1, w1, h1, l1, actions=["Imprimer"],
                 info="8 en cours", icone="clipboard-list")
    l2 = g.liste("Liste_Top5", COLS_TOP, [[a, b, g.fcfa(c)] for a, b, c in top], 20, 64, w2 - 40, h2 - 84)
    p2 = g.carte("Carte_Top5", "5 meilleurs clients", x2, y2, w2, h2, l2, icone="trophy")
    l3 = g.liste("Liste_Carburants", COLS_CARB, g.flotte_carburant(), 20, 64, w3 - 40, h3 - 84)
    p3 = g.carte("Carte_Carburants", "Flotte par carburant", x3, y3, w3, h3, l3, icone="fuel")
    return p1 + p2 + p3


def donnees_resa():
    r1 = g.DONNEES["Reservation"][0]
    mo, ma = g.modele_de(r1["Voiture"])
    return {"r": r1, "mod": mo, "mar": ma, "duree": f"{g.duree(r1)} jour(s)", "montant": g.fcfa(g.montant(r1)),
            "jours": g.duree(r1)}


def liste_resa(x, y, w, h):
    l = g.liste("Liste_Reservations", COLS_LISTE_RES, g.lignes_reservations(), 20, 62, w - 40, h - 80, total=25)
    return g.carte("Carte_Liste", "Liste des réservations", x, y, w, h, l, actions=["Imprimer"], info="25 réservations", icone="list")


ACTIONS4 = ["Ajouter", "Actualiser", "Rechercher", "Imprimer"]


# ==========================================================================
# DESIGN A : ÉDITORIAL (noir et blanc)
# ==========================================================================
A_HERO = 150


def a_coquille(actif, corps):
    nav, x = "", 300
    for cle, lib, _ in g.MENU:
        w = int(len(lib) * 9.2) + 30
        on = cle == actif
        nav += (f'<div class="nav-h{" actif" if on else ""}" style="left:{x}px;width:{w}px" '
                f'{acc("BoutonNavigation_" + cle, "Bouton de navigation")}>{e(lib)}</div>')
        x += w
    tete = f"""
<div class="barre-a" {acc("Entete", "Rectangle")}>
  <div class="logo-a" {acc("Logo", "Image + étiquette")}>{g.svg("car-front", "#FFFFFF", 22, 1.8)}{g.NOM_APPLI}</div>
  {nav}
  <div class="abs date-a" style="right:120px;top:24px" {acc("Date_Heure", "Zone de texte")}>lundi 28 septembre 2026 · 20:06</div>
  <div class="avatar avatar-a" style="right:64px;top:16px" {acc("Btn_Avatar", "Bouton (ellipse)")}>AD</div>
  <div class="abs" style="right:24px;top:22px" {acc("Btn_Quitter", "Bouton")}>{g.svg("power", "#FFFFFF", 20)}</div>
</div>"""
    return g.fenetre(g.NOM_APPLI, g.W, g.H, tete + contenu(0, 64, g.W, g.H - 64, corps))


def a_hero(cle, h=A_HERO):
    titre, sous = TEXTES[cle]
    sous = sous.replace("{nom}", g.NOM_APPLI)
    return (img(f"a-bandeau-{cle}.jpg", 0, 0, g.W, h, "Bandeau")
            + lbl(48, h // 2 - 40, e(titre), "font-family:'Titre',Georgia,serif;font-size:37.33px;color:#FFFFFF", "Bandeau_Titre")
            + lbl(50, h // 2 + 14, e(sous).upper(), "font-size:12px;letter-spacing:2px;color:#D4D4D4", "Bandeau_SousTitre"))


def a_tableau():
    kpis, res, top = donnees_tableau()
    out = a_hero("tableau")
    cw = (g.W - 64) // 3
    band = ""
    for i, (n, lib, val, unit, sub, ico) in enumerate(kpis):
        x = i * cw
        u = f'<small>{unit}</small>' if unit else ""
        band += (f'<div class="abs" style="left:{x + 32}px;top:18px">{g.svg(ico, "#111111", 18)}</div>'
                 + lbl(x + 58, 18, e(lib).upper(), "font-size:12px;letter-spacing:1.5px;color:#6E6E6E")
                 + f'<div class="val-a" style="left:{x + 32}px;top:40px" {acc("Txt_" + n, "Zone de texte")}>{val}{u}</div>'
                 + lbl(x + 32, 86, e(sub), "font-size:13.33px;color:#6E6E6E"))
        if i:
            band += f'<div class="abs" style="left:{x}px;top:20px;width:1px;height:76px;background:#DADADA"></div>'
    out += f'<div class="carte kpi-a" style="left:32px;top:{A_HERO + 24}px;width:{g.W - 64}px;height:116px" {acc("Bande_Indicateurs", "Rectangle")}>{band}</div>'
    y = A_HERO + 156
    out += cartes_listes(32, y, 920, 396, 968, y, 568, 212, 968, y + 228, 568, 168, res, top)
    return a_coquille("tableau", out)


def a_fiche(cle, titre_fiche, icone, champs, titre_liste, cols, lignes, total, compteur, info, grande_liste=True):
    y0 = A_HERO + 24
    fx, fw = 968, 568
    lw, iw = 130, fw - 40 - 130
    inner, y = "", 70
    for (n, lib, val, kind, *opt) in champs:
        inner += g.champ(n, lib, val, 20, y, lw, opt[0] if opt else iw, kind)
        y += 40
    y += 8
    inner += g.nav_enreg(20 + lw, y, compteur)
    y += 46
    inner += f'<div class="sep-h" style="left:0;top:{y}px;width:{fw - 2}px"></div>'
    y += 16
    inner += g.boutons_crud(fw - 20 - 270, y)
    h = y + 50
    fiche = g.carte("Carte_Fiche", titre_fiche, fx, y0, fw, h, inner, actions=ACTIONS4, icone=icone)
    lh = (g.H - 64 - 24 - y0) if grande_liste else max(h, 300)
    l = g.liste("Liste_" + cle.capitalize(), cols, lignes, 20, 66, 920 - 40, lh - 86, total=total)
    lst = g.carte("Carte_Liste", titre_liste, 32, y0, 920, lh, l, actions=["Imprimer"], info=info, icone="list")
    return a_coquille(cle, a_hero(cle) + lst + fiche)


def a_reservations():
    d = donnees_resa()
    y0 = A_HERO + 24
    lw, iw = 100, 488 - 40 - 100
    cli = (g.champ("Cbo_Client", "Client", "Jean Mboumba", 20, 64, lw, iw, "liste")
           + g.champ("Txt_Telephone", "Téléphone", "(+241) 62 54 85 85", 20, 100, lw, iw, "lecture")
           + g.champ("Txt_Email", "Email", "jean.mboumba1@example.com", 20, 136, lw, iw, "lecture"))
    voi = (g.champ("Cbo_Voiture", "Voiture", d["r"]["Voiture"], 20, 64, lw, iw, "liste")
           + g.champ("Txt_Modele", "Modèle", d["mod"], 20, 100, lw, iw, "lecture")
           + g.champ("Txt_Marque", "Marque", d["mar"], 20, 136, lw, iw, "lecture"))
    out = (g.carte("Carte_Client", "Client", 32, y0, 488, 176, cli, icone="user")
           + g.carte("Carte_Voiture", "Voiture", 536, y0, 488, 176, voi, icone="car"))
    out += (f'<div class="carte panneau-a" style="left:1040px;top:{y0}px;width:496px;height:176px" {acc("Carte_Montant", "Rectangle")}>'
            + lbl(28, 22, "MONTANT DE LA RÉSERVATION", "font-size:12px;letter-spacing:2px;color:#BDBDBD")
            + f'<div class="val-a" style="left:28px;top:48px;color:#FFFFFF" {acc("Txt_Montant", "Zone de texte")}>{d["montant"]}<small style="color:#BDBDBD">FCFA</small></div>'
            + lbl(28, 108, f'<span {acc("Txt_Duree", "Zone de texte")}>{e(d["duree"])}</span> · {e(d["mod"])}', "font-size:14.67px;color:#E5E5E5")
            + lbl(28, 136, "du 23/09/2026 au 24/10/2026", "font-size:13.33px;color:#9E9E9E") + '</div>')
    y1 = y0 + 192
    row = (g.champ("Txt_Code", "Code", "1", 20, 64, 50, 60, droite=True)
           + g.champ("Txt_DateDebut", "Date de début", "23/09/2026", 150, 64, 104, 120, droite=True)
           + g.champ("Txt_DateFin", "Date de fin", "24/10/2026", 398, 64, 90, 120, droite=True)
           + f'<div class="btn secondaire" style="left:620px;top:62px;width:60px" {acc("Btn_OK", "Bouton")}>OK</div>'
           + g.nav_enreg(712, 64, "1 sur 25")
           + g.boutons_crud(1504 - 20 - 270, 62))
    out += g.carte("Carte_Reservation", "Réservation", 32, y1, 1504, 112, row, actions=ACTIONS4, icone="calendar-range")
    y2 = y1 + 128
    out += liste_resa(32, y2, 1504, g.H - 64 - 24 - y2)
    return a_coquille("reservations", a_hero("reservations") + out)


def a_login():
    lw, lh = 880, 500
    c = f"""
{img("a-connexion.jpg", 0, 0, lw, lh, "Login_Photo")}
{lbl(40, 36, g.svg("car-front", "#FFFFFF", 26, 1.8) + g.NOM_APPLI, "display:flex;align-items:center;gap:10px;font-size:16px;font-weight:600;letter-spacing:3px;color:#FFFFFF", "Logo", "Image + étiquette")}
{lbl(40, 360, "Location de véhicules<br>de prestige à Libreville", "font-family:'Titre',Georgia,serif;font-size:29.33px;line-height:38px;color:#FFFFFF;white-space:normal;width:400px", "Login_Slogan")}
{lbl(40, 450, "© 2026 " + g.NOM_APPLI, "font-size:12px;letter-spacing:1px;color:#BDBDBD", "Login_Copyright")}
<div class="abs" style="left:500px;top:44px;width:340px;height:412px;background:#FFFFFF;border-top:4px solid #0D0D0D" {acc("Login_Carte", "Rectangle")}></div>
{lbl(532, 84, "Connexion", "font-family:'Titre',Georgia,serif;font-size:32px;color:#0D0D0D", "Lbl_Titre")}
{lbl(534, 132, "ESPACE RÉSERVÉ AU PERSONNEL", "font-size:11px;letter-spacing:2px;color:#6E6E6E")}
<div class="etiq" style="left:532px;top:176px">Nom d'utilisateur</div>
<div class="champ" style="left:532px;top:204px;width:276px;height:34px;line-height:32px" {acc("Txt_Utilisateur", "Zone de texte")}>admin</div>
<div class="etiq" style="left:532px;top:248px">Mot de passe</div>
<div class="champ" style="left:532px;top:276px;width:276px;height:34px;line-height:32px;letter-spacing:2px" {acc("Txt_MotDePasse", "Zone de texte")}>********</div>
<div class="btn primaire" style="left:532px;top:338px;width:276px;height:40px;border-radius:0;letter-spacing:2px" {acc("Btn_Connexion", "Bouton")}>SE CONNECTER</div>
{lbl(532, 398, "Mot de passe oublié ? Contactez l'administrateur.", "font-size:12px;color:#6E6E6E;width:276px;white-space:normal;text-align:center")}
"""
    return g.fenetre(g.NOM_APPLI + " - Connexion", lw, lh, c, boutons=("fermer",))


# ==========================================================================
# DESIGN B : RAIL D'ICÔNES (rose et blanc)
# ==========================================================================
B_RAIL, B_TETE, B_PAN = 104, 72, 320
B_CX = B_CW = B_CH = None  # remplis par b_init()


def b_init():
    global B_CX, B_CW, B_CH
    B_CX, B_CW, B_CH = B_RAIL, g.W - B_RAIL - B_PAN, g.H - B_TETE


def b_coquille(actif, corps, panneau):
    b_init()
    nav = ""
    for i, (cle, lib, ico) in enumerate(g.MENU):
        on = cle == actif
        y = 96 + i * 72
        nav += (f'<div class="rail-item{" actif" if on else ""}" style="top:{y}px" {acc("BoutonNavigation_" + cle, "Bouton de navigation")}>'
                f'<div class="ri">{g.svg(ico, T("nav_ico_actif") if on else T("nav_ico"), 22)}</div><div class="rl">{e(lib if cle != "tableau" else "Tableau")}</div></div>')
    titre = TITRES_MENU[actif]
    c = f"""
<div class="rail" {acc("Menu_Fond", "Rectangle")}>
  <div class="rail-logo" {acc("Logo", "Image")}>{g.svg("car-front", T("menu"), 26, 1.8)}</div>
  {nav}
  <div class="abs" style="left:38px;bottom:28px" {acc("Btn_Quitter", "Bouton")}>{g.svg("power", T("nav_ico"), 26)}</div>
</div>
<div class="tete-b" {acc("Entete", "Rectangle")}>
  {lbl(24, 10, e(titre), "font-size:22.67px;font-weight:600;color:var(--titre)", "Lbl_Titre_Page")}
  {lbl(24, 44, g.NOM_APPLI + " · lundi 28 septembre 2026 · 20:06", "font-size:12px;color:var(--gris)", "Date_Heure", "Zone de texte")}
  {avatar(g.W - B_RAIL - 196, 18, 36)}
  <div class="utilisateur" style="left:{g.W - B_RAIL - 150}px;top:19px" {acc("Utilisateur", "Étiquettes")}><b>admin</b><span>Administrateur</span></div>
</div>
{panneau}
{contenu(B_CX, B_TETE, B_CW, B_CH, corps)}"""
    return g.fenetre(g.NOM_APPLI, g.W, g.H, c)


def b_panneau(cle, grand=None, unite="", texte="", lignes=()):
    x = g.W - B_PAN
    out = img(f"b-panneau-{cle}.jpg", x, B_TETE, B_PAN, g.H - B_TETE, "Panneau_Photo")
    if grand is None:
        grand, texte = CHIFFRES[cle]
    y = g.H - 200 - 26 * len(lignes)
    taille = 52 if len(str(grand)) <= 4 else 32
    out += lbl(x + 28, y, f'{e(grand)}<small style="font-size:16px;font-weight:400;margin-left:6px">{e(unite)}</small>' if unite else e(grand),
               f"font-size:{taille}px;font-weight:600;color:#FFFFFF;line-height:56px", "Panneau_Chiffre", "Zone de texte")
    out += lbl(x + 30, y + 62, e(texte), "font-size:16px;color:rgba(255,255,255,.9)", "Panneau_Texte")
    for i, l in enumerate(lignes):
        out += lbl(x + 30, y + 96 + i * 26, l, "font-size:13.33px;color:rgba(255,255,255,.8)")
    out += lbl(x + 30, g.H - 52, g.NOM_APPLI + " · Libreville", "font-size:12px;letter-spacing:1px;color:rgba(255,255,255,.7)")
    return out


def b_tableau():
    b_init()
    kpis, res, top = donnees_tableau()
    w = (B_CW - 48 - 32) // 3
    out = ""
    for i, (n, lib, val, unit, sub, ico) in enumerate(kpis):
        x = 24 + i * (w + 16)
        u = f'<small style="font-size:14px;font-weight:400;margin-left:4px;color:var(--gris)">{unit}</small>' if unit else ""
        out += (f'<div class="carte" style="left:{x}px;top:24px;width:{w}px;height:100px" {acc("Carte_" + n, "Rectangle")}>'
                f'<div class="pastille-ronde" style="left:20px;top:26px;background:{T("kpi")[i][0]}" {acc("Pastille_" + n, "Bouton (ellipse) + image")}>{g.svg(ico, "#FFFFFF", 22)}</div>'
                + lbl(88, 16, e(lib), "font-size:13.33px;color:var(--gris)")
                + f'<div class="abs" style="left:88px;top:36px;font-size:24px;font-weight:600;color:var(--titre);white-space:nowrap" {acc("Txt_" + n, "Zone de texte")}>{val}{u}</div>'
                + lbl(88, 70, e(sub), "font-size:12px;color:var(--gris)") + '</div>')
    bw = (B_CW - 48 - 16) // 2
    out += cartes_listes(24, 140, B_CW - 48, 290, 24, 446, bw, B_CH - 24 - 446, 24 + bw + 16, 446, bw, B_CH - 24 - 446, res, top)
    pan = b_panneau("tableau", "Bonjour, admin", "", "Bienvenue sur votre espace.",
                    ["8 voitures en location aujourd'hui", "25 réservations enregistrées"])
    return b_coquille("tableau", out, pan)


def b_fiche(cle, titre_fiche, icone, champs, titre_liste, cols, lignes, total, compteur, info, grande_liste=True):
    b_init()
    fw = B_CW - 48
    lw, iw = 120, 380
    inner = ""
    for i, (n, lib, val, kind, *opt) in enumerate(champs):
        col, row = i % 2, i // 2
        inner += g.champ(n, lib, val, 20 + col * 540, 66 + row * 40, lw, opt[0] if opt else iw, kind)
    rows = (len(champs) + 1) // 2
    y = 66 + rows * 40 + 10
    inner += g.nav_enreg(20 + lw, y, compteur) + g.boutons_crud(fw - 20 - 270, y - 2)
    h = y + 30 + 22
    out = g.carte("Carte_Fiche", titre_fiche, 24, 24, fw, h, inner, actions=ACTIONS4, icone=icone)
    ly = 24 + h + 16
    lh = B_CH - 24 - ly
    l = g.liste("Liste_" + cle.capitalize(), cols, lignes, 20, 66, fw - 40, lh - 86, total=total)
    out += g.carte("Carte_Liste", titre_liste, 24, ly, fw, lh, l, actions=["Imprimer"], info=info, icone="list")
    return b_coquille(cle, out, b_panneau(cle))


def b_reservations():
    b_init()
    d = donnees_resa()
    fw = B_CW - 48
    res = (g.champ("Txt_Code", "Code", "1", 20, 64, 60, 70, droite=True)
           + g.champ("Txt_DateDebut", "Date de début", "23/09/2026", 180, 64, 104, 120, droite=True)
           + g.champ("Txt_DateFin", "Date de fin", "24/10/2026", 430, 64, 90, 120, droite=True)
           + f'<div class="btn secondaire" style="left:656px;top:62px;width:60px" {acc("Btn_OK", "Bouton")}>OK</div>'
           + g.nav_enreg(80, 108, "1 sur 25") + g.boutons_crud(fw - 20 - 270, 106))
    out = g.carte("Carte_Reservation", "Réservation n° 1", 24, 24, fw, 156, res, actions=ACTIONS4, icone="calendar-range")
    cw = (fw - 16) // 2
    lw, iw = 100, cw - 40 - 100
    cli = (g.champ("Cbo_Client", "Client", "Jean Mboumba", 20, 64, lw, iw, "liste")
           + g.champ("Txt_Telephone", "Téléphone", "(+241) 62 54 85 85", 20, 100, lw, iw, "lecture")
           + g.champ("Txt_Email", "Email", "jean.mboumba1@example.com", 20, 136, lw, iw, "lecture"))
    voi = (g.champ("Cbo_Voiture", "Voiture", d["r"]["Voiture"], 20, 64, lw, iw, "liste")
           + g.champ("Txt_Modele", "Modèle", d["mod"], 20, 100, lw, iw, "lecture")
           + g.champ("Txt_Marque", "Marque", d["mar"], 20, 136, lw, iw, "lecture"))
    out += g.carte("Carte_Client", "Client", 24, 196, cw, 178, cli, icone="user")
    out += g.carte("Carte_Voiture", "Voiture", 24 + cw + 16, 196, cw, 178, voi, icone="car")
    out += liste_resa(24, 390, fw, B_CH - 24 - 390)
    pan = b_panneau("reservations", d["montant"], "FCFA", "Montant de la réservation",
                    [f'Durée : <span {acc("Txt_Duree", "Zone de texte")}>{e(d["duree"])}</span>', e(d["mod"])])
    return b_coquille("reservations", out, pan)


def b_login():
    lw, lh = 480, 620
    c = f"""
<div class="abs" style="left:0;top:0;width:{lw}px;height:{lh}px;background:var(--surface)" {acc("Login_Fond", "Section Détail")}></div>
{img("b-connexion.jpg", 0, 0, lw, 220, "Login_Photo")}
<div class="rail-logo" style="left:{lw // 2 - 36}px;top:184px;width:72px;height:72px;border-radius:18px;box-shadow:0 0 0 6px #FFFFFF" {acc("Logo", "Bouton arrondi + image")}>{g.svg("car-front", T("menu"), 34, 1.8)}</div>
{lbl(0, 276, g.NOM_APPLI, f"width:{lw}px;text-align:center;font-size:18.67px;font-weight:600;letter-spacing:1px;color:var(--titre)", "Lbl_Titre")}
{lbl(0, 308, "Location de véhicules de prestige à Libreville", f"width:{lw}px;text-align:center;font-size:13.33px;color:var(--gris)")}
<div class="etiq" style="left:60px;top:348px">Nom d'utilisateur</div>
<div class="champ" style="left:60px;top:376px;width:360px;height:36px;line-height:34px" {acc("Txt_Utilisateur", "Zone de texte")}>admin</div>
<div class="etiq" style="left:60px;top:420px">Mot de passe</div>
<div class="champ" style="left:60px;top:448px;width:360px;height:36px;line-height:34px;letter-spacing:2px" {acc("Txt_MotDePasse", "Zone de texte")}>********</div>
<div class="btn primaire" style="left:60px;top:508px;width:360px;height:40px;border-radius:20px" {acc("Btn_Connexion", "Bouton (forme arrondie)")}>Se connecter</div>
{lbl(0, 568, "Mot de passe oublié ? Contactez l'administrateur.", f"width:{lw}px;text-align:center;font-size:12px;color:var(--gris)")}
"""
    return g.fenetre(g.NOM_APPLI + " - Connexion", lw, lh, c, boutons=("fermer",))


# ==========================================================================
# DESIGN C : MENU PHOTO À DROITE (vert jade et blanc)
# ==========================================================================
C_MENU = 260


def c_coquille(actif, corps):
    cw = g.W - C_MENU
    x0 = cw
    nav = ""
    for i, (cle, lib, ico) in enumerate(g.MENU):
        on = cle == actif
        nav += (f'<div class="nav nav-c{" actif" if on else ""}" style="left:{x0 + 16}px;top:{120 + i * 46}px;width:{C_MENU - 32}px" '
                f'{acc("BoutonNavigation_" + cle, "Bouton de navigation")}>{g.svg(ico, T("nav_ico_actif") if on else "#FFFFFF", 18)}{e(lib)}</div>')
    c = f"""
{img(f"c-menu-{actif}.jpg", x0, 0, C_MENU, g.H, "Menu_Fond")}
<div class="abs" style="left:{x0 + 24}px;top:28px;display:flex;align-items:center;gap:10px;font-size:15px;font-weight:600;letter-spacing:.5px;color:#FFFFFF" {acc("Logo", "Image + étiquette")}>{g.svg("car-front", "#FFFFFF", 26, 1.8)}{g.NOM_APPLI}</div>
{lbl(x0 + 26, 64, "Location de prestige · Libreville", "font-size:12px;color:rgba(255,255,255,.75)")}
{lbl(x0 + 28, 98, "NAVIGATION", "font-size:11px;letter-spacing:1.5px;color:rgba(255,255,255,.6)")}
{nav}
<div class="abs" style="left:{x0 + 16}px;top:{g.H - 80}px;width:{C_MENU - 32}px;height:60px;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.25)" {acc("Carte_Utilisateur", "Rectangle")}></div>
<div class="avatar" style="left:{x0 + 28}px;top:{g.H - 66}px;background:#FFFFFF;color:var(--titre)" {acc("Btn_Avatar", "Bouton (ellipse)")}>AD</div>
<div class="utilisateur" style="left:{x0 + 72}px;top:{g.H - 67}px" {acc("Utilisateur", "Étiquettes")}><b style="color:#FFFFFF">admin</b><span style="color:rgba(255,255,255,.75)">Administrateur</span></div>
<div class="abs" style="left:{x0 + C_MENU - 52}px;top:{g.H - 60}px" {acc("Btn_Quitter", "Bouton")}>{g.svg("power", "#FFFFFF", 20)}</div>
{contenu(0, 0, cw, g.H, corps)}"""
    return g.fenetre(g.NOM_APPLI, g.W, g.H, c)


def c_titre(cle):
    titre, sous = TEXTES[cle]
    sous = sous.replace("{nom}", g.NOM_APPLI)
    cw = g.W - C_MENU
    return (lbl(32, 24, e(titre), "font-size:29.33px;font-weight:600;color:var(--titre)", "Lbl_Titre_Page")
            + lbl(34, 68, e(sous), "font-size:14.67px;color:var(--gris)", "Lbl_SousTitre")
            + f'<div class="abs date-c" style="right:32px;top:34px" {acc("Date_Heure", "Zone de texte")}>{g.svg("calendar-range", T("icone"), 16)}lundi 28 septembre 2026 · 20:06</div>'
            + f'<div class="abs" style="left:32px;top:{100}px;width:{cw - 64}px;height:1px;background:var(--carte-bordure)"></div>')


def c_tableau():
    kpis, res, top = donnees_tableau()
    cw = g.W - C_MENU
    w = (cw - 64 - 48) // 3
    out = c_titre("tableau")
    for i, (n, lib, val, unit, sub, ico) in enumerate(kpis):
        x = 32 + i * (w + 24)
        fond = T("kpi")[i][0]
        u = f'<small style="font-size:16px;font-weight:400;margin-left:4px;opacity:.85">{unit}</small>' if unit else ""
        out += (f'<div class="kpi" style="left:{x}px;top:120px;width:{w}px;height:110px;background:{fond}" {acc("Carte_" + n, "Rectangle")}>'
                f'<div class="abs" style="right:20px;top:18px;opacity:.85">{g.svg(ico, "#FFFFFF", 30)}</div>'
                + lbl(22, 16, e(lib).upper(), "font-size:12px;letter-spacing:1.2px;color:rgba(255,255,255,.85)")
                + f'<div class="abs" style="left:22px;top:38px;font-size:30px;font-weight:600;color:#FFFFFF;white-space:nowrap" {acc("Txt_" + n, "Zone de texte")}>{val}{u}</div>'
                + f'<div class="abs" style="left:22px;top:80px;width:{w - 44}px;height:1px;background:rgba(255,255,255,.35)"></div>'
                + lbl(22, 86, e(sub), "font-size:12px;color:rgba(255,255,255,.9)") + '</div>')
    lw1 = 760
    rx, rw = 32 + lw1 + 24, cw - 64 - lw1 - 24
    out += cartes_listes(32, 250, lw1, g.H - 24 - 250, rx, 250, rw, 240, rx, 506, rw, g.H - 24 - 506, res, top)
    return c_coquille("tableau", out)


def c_fiche(cle, titre_fiche, icone, champs, titre_liste, cols, lignes, total, compteur, info, grande_liste=True):
    cw = g.W - C_MENU
    fw = 440
    inner, y = "", 64
    for (n, lib, val, kind, *opt) in champs:
        inner += champ_haut(n, lib, val, 20, y, min(opt[0] + 60, fw - 40) if opt else fw - 40, kind)
        y += 58
    y += 6
    inner += g.nav_enreg(20, y, compteur)
    y += 44
    inner += g.boutons_crud(20, y, (fw - 50) // 2)
    h = y + 32 + 20
    out = c_titre(cle) + g.carte("Carte_Fiche", titre_fiche, 32, 120, fw, h, inner, actions=ACTIONS4, icone=icone)
    lx = 32 + fw + 24
    lw = cw - 32 - lx
    lh = (g.H - 24 - 120) if grande_liste else max(h, 360)
    l = g.liste("Liste_" + cle.capitalize(), cols, lignes, 20, 66, lw - 40, lh - 86, total=total)
    out += g.carte("Carte_Liste", titre_liste, lx, 120, lw, lh, l, actions=["Imprimer"], info=info, icone="list")
    return c_coquille(cle, out)


def c_reservations():
    d = donnees_resa()
    cw = g.W - C_MENU
    w3 = (cw - 64 - 32) // 3
    fw = w3 - 40
    cli = (champ_haut("Cbo_Client", "Client", "Jean Mboumba", 20, 64, fw, "liste")
           + champ_haut("Txt_Telephone", "Téléphone", "(+241) 62 54 85 85", 20, 122, fw, "lecture")
           + champ_haut("Txt_Email", "Email", "jean.mboumba1@example.com", 20, 180, fw, "lecture"))
    voi = (champ_haut("Cbo_Voiture", "Voiture", d["r"]["Voiture"], 20, 64, fw, "liste")
           + champ_haut("Txt_Modele", "Modèle", d["mod"], 20, 122, fw, "lecture")
           + champ_haut("Txt_Marque", "Marque", d["mar"], 20, 180, fw, "lecture"))
    hw = (fw - 16) // 2
    res = (champ_haut("Txt_Code", "Code", "1", 20, 64, 70, droite=True)
           + champ_haut("Txt_DateDebut", "Date de début", "23/09/2026", 106, 64, (fw - 86 - 76) // 2 + 0, droite=True)
           + champ_haut("Txt_DateFin", "Date de fin", "24/10/2026", 106 + (fw - 86 - 76) // 2 + 12, 64, (fw - 86 - 76) // 2, droite=True)
           + f'<div class="btn secondaire" style="left:{20 + fw - 60}px;top:84px;width:60px;height:30px" {acc("Btn_OK", "Bouton")}>OK</div>'
           + champ_haut("Txt_Duree", "Durée", d["duree"], 20, 122, hw, "lecture", droite=True)
           + champ_haut("Txt_Montant", "Montant", d["montant"] + " FCFA", 20 + hw + 16, 122, hw, "lecture", droite=True, total=True)
           + g.nav_enreg(20, 190, "1 sur 25"))
    h = 250
    out = c_titre("reservations")
    out += g.carte("Carte_Client", "Client", 32, 120, w3, h, cli, icone="user")
    out += g.carte("Carte_Voiture", "Voiture", 32 + w3 + 16, 120, w3, h, voi, icone="car")
    out += g.carte("Carte_Reservation", "Réservation", 32 + 2 * (w3 + 16), 120, w3, h, res, actions=["Ajouter", "Rechercher"],
                   icone="calendar-range")
    out += g.boutons_crud(cw - 32 - 270, 120 + h + 14)
    y = 120 + h + 62
    out += liste_resa(32, y, cw - 64, g.H - 24 - y)
    return c_coquille("reservations", out)


def c_login():
    lw, lh = 880, 520
    c = f"""
<div class="abs" style="left:0;top:0;width:{lw}px;height:{lh}px;background:var(--surface)" {acc("Login_Fond", "Section Détail")}></div>
{img("c-connexion.jpg", 0, 0, lw, 300, "Login_Photo")}
{lbl(40, 34, g.svg("car-front", "#FFFFFF", 28, 1.8) + g.NOM_APPLI, "display:flex;align-items:center;gap:10px;font-size:18.67px;font-weight:600;color:#FFFFFF", "Logo", "Image + étiquette")}
{lbl(40, 196, "Bienvenue", "font-size:32px;font-weight:600;color:#FFFFFF", "Lbl_Titre")}
{lbl(42, 244, "Location de véhicules de prestige à Libreville", "font-size:14.67px;color:rgba(255,255,255,.9)")}
<div class="etiq-haut" style="left:40px;top:336px">Nom d'utilisateur</div>
<div class="champ" style="left:40px;top:358px;width:260px;height:36px;line-height:34px" {acc("Txt_Utilisateur", "Zone de texte")}>admin</div>
<div class="etiq-haut" style="left:320px;top:336px">Mot de passe</div>
<div class="champ" style="left:320px;top:358px;width:260px;height:36px;line-height:34px;letter-spacing:2px" {acc("Txt_MotDePasse", "Zone de texte")}>********</div>
<div class="btn primaire" style="left:600px;top:358px;width:240px;height:36px" {acc("Btn_Connexion", "Bouton")}>Se connecter</div>
<div class="abs" style="left:40px;top:430px;width:800px;height:1px;background:var(--carte-bordure)"></div>
{lbl(40, 448, "Mot de passe oublié ? Contactez l'administrateur.", "font-size:12px;color:var(--gris)")}
{lbl(840 - 160, 448, "© 2026 " + g.NOM_APPLI, "font-size:12px;color:var(--gris);width:160px;text-align:right")}
"""
    return g.fenetre(g.NOM_APPLI + " - Connexion", lw, lh, c, boutons=("fermer",))


# ==========================================================================
# DESIGN D : COCKPIT (argenté et noir)
# ==========================================================================
D_TETE = 72


def d_coquille(actif, corps):
    items = []
    for cle, lib, ico in g.MENU:
        items.append((cle, lib, ico, int(len(lib) * 7.9) + 52))
    tot = sum(i[3] for i in items) + 6 * (len(items) - 1)
    x = (g.W - tot) // 2 + 20
    nav = ""
    for cle, lib, ico, w in items:
        on = cle == actif
        nav += (f'<div class="pill{" actif" if on else ""}" style="left:{x}px;width:{w}px" {acc("BoutonNavigation_" + cle, "Bouton de navigation")}>'
                f'{g.svg(ico, T("nav_ico_actif") if on else "#B8BCC2", 16)}{e(lib)}</div>')
        x += w + 6
    c = f"""
{img(f"d-fond-{actif}.jpg", 0, 0, g.W, g.H, "Image_Fond")}
<div class="abs" style="left:32px;top:22px;display:flex;align-items:center;gap:10px;font-size:15px;font-weight:600;letter-spacing:2px;color:#E8EAED" {acc("Logo", "Image + étiquette")}>{g.svg("car-front", "#E8EAED", 26, 1.8)}{g.NOM_APPLI}</div>
{nav}
{avatar(g.W - 104, 20, 32)}
<div class="abs" style="left:{g.W - 56}px;top:26px" {acc("Btn_Quitter", "Bouton")}>{g.svg("power", "#C9CDD2", 20)}</div>
<div class="abs" style="left:32px;top:{D_TETE - 1}px;width:{g.W - 64}px;height:1px;background:rgba(201,205,210,.25)"></div>
{contenu(0, D_TETE, g.W, g.H - D_TETE, corps, fond=False)}"""
    return g.fenetre(g.NOM_APPLI, g.W, g.H, c)


def d_titre(cle):
    titre, sous = TEXTES[cle]
    sous = sous.replace("{nom}", g.NOM_APPLI)
    return (lbl(32, 18, e(titre), "font-size:29.33px;font-weight:600;color:#FFFFFF", "Lbl_Titre_Page")
            + lbl(34, 60, e(sous), "font-size:13.33px;letter-spacing:.5px;color:#AEB3B9", "Lbl_SousTitre")
            + f'<div class="abs" style="right:32px;top:32px;font-size:13.33px;color:#AEB3B9" {acc("Date_Heure", "Zone de texte")}>lundi 28 septembre 2026 · 20:06</div>')


D_Y0 = 104


def d_tableau():
    kpis, res, top = donnees_tableau()
    out = d_titre("tableau")
    for i, (n, lib, val, unit, sub, ico) in enumerate(kpis):
        y = D_Y0 + i * 136
        fond, past = T("kpi")[i]
        u = f'<small>{unit}</small>' if unit else ""
        out += (f'<div class="kpi" style="left:32px;top:{y}px;width:360px;height:120px;background:{fond}" {acc("Carte_" + n, "Rectangle")}>'
                + lbl(22, 16, e(lib).upper(), "font-size:12px;letter-spacing:1.5px;color:rgba(0,0,0,.6)")
                + f'<div class="val" style="left:22px;top:38px" {acc("Txt_" + n, "Zone de texte")}>{val}{u}</div>'
                + lbl(22, 86, e(sub), "font-size:12px;color:rgba(0,0,0,.62)")
                + f'<div class="pastille-ronde" style="left:292px;top:20px;width:48px;height:48px;background:{past}" {acc("Pastille_" + n, "Bouton (ellipse) + image")}>{g.svg(ico, "#0B0C0E", 22)}</div></div>')
    bas = g.H - D_TETE - 24
    yc = D_Y0 + 3 * 136
    out += cartes_listes(408, D_Y0, g.W - 440, 330, 408, D_Y0 + 346, g.W - 440, bas - D_Y0 - 346, 32, yc, 360, bas - yc, res, top)
    return d_coquille("tableau", out)


def d_fiche(cle, titre_fiche, icone, champs, titre_liste, cols, lignes, total, compteur, info, grande_liste=True):
    fw = g.W - 64
    lh = 300
    l = g.liste("Liste_" + cle.capitalize(), cols, lignes, 20, 66, fw - 40, lh - 86, total=total)
    out = d_titre(cle) + g.carte("Carte_Liste", titre_liste, 32, D_Y0, fw, lh, l, actions=["Imprimer"], info=info, icone="list")
    lw, iw = 120, 340
    inner = ""
    for i, (n, lib, val, kind, *opt) in enumerate(champs):
        col, row = i % 3, i // 3
        inner += g.champ(n, lib, val, 20 + col * 500, 66 + row * 40, lw, opt[0] if opt else iw, kind)
    rows = (len(champs) + 2) // 3
    y = 66 + rows * 40 + 12
    inner += f'<div class="sep-h" style="left:0;top:{y - 6}px;width:{fw - 2}px"></div>'
    inner += g.nav_enreg(20 + lw, y + 8, compteur) + g.boutons_crud(fw - 20 - 270, y + 6)
    h = y + 8 + 30 + 22
    out += g.carte("Carte_Fiche", titre_fiche, 32, D_Y0 + lh + 16, fw, h, inner, actions=ACTIONS4, icone=icone)
    return d_coquille(cle, out)


def d_reservations():
    d = donnees_resa()
    bas = g.H - D_TETE - 24
    lw_ = 420
    res = (g.champ("Txt_Code", "Code", "1", 20, 64, 120, 80, droite=True)
           + g.champ("Txt_DateDebut", "Date de début", "23/09/2026", 20, 102, 120, 140, droite=True)
           + g.champ("Txt_DateFin", "Date de fin", "24/10/2026", 20, 140, 120, 140, droite=True)
           + f'<div class="btn secondaire" style="left:300px;top:138px;width:80px" {acc("Btn_OK", "Bouton")}>OK</div>'
           + g.nav_enreg(140, 184, "1 sur 25")
           + f'<div class="sep-h" style="left:0;top:228px;width:{lw_ - 2}px"></div>'
           + g.boutons_crud(20, 244, 185))
    out = d_titre("reservations") + g.carte("Carte_Reservation", "Réservation", 32, D_Y0, lw_, 296, res, actions=ACTIONS4,
                                            icone="calendar-range")
    fond, past = T("kpi")[0]
    y2 = D_Y0 + 312
    out += (f'<div class="kpi" style="left:32px;top:{y2}px;width:{lw_}px;height:{bas - y2}px;background:{fond}" {acc("Carte_Montant", "Rectangle")}>'
            + lbl(22, 18, "MONTANT DE LA RÉSERVATION", "font-size:12px;letter-spacing:1.5px;color:rgba(0,0,0,.6)")
            + f'<div class="val" style="left:22px;top:44px;font-size:34px" {acc("Txt_Montant", "Zone de texte")}>{d["montant"]}<small>FCFA</small></div>'
            + lbl(22, 100, f'Durée : <b {acc("Txt_Duree", "Zone de texte")}>{e(d["duree"])}</b> · {e(d["mod"])}', "font-size:13.33px;color:rgba(0,0,0,.7)")
            + f'<div class="abs" style="left:22px;top:136px;width:{lw_ - 44}px;height:1px;background:rgba(0,0,0,.18)"></div>'
            + lbl(22, 152, "Du 23/09/2026 au 24/10/2026", "font-size:13.33px;color:rgba(0,0,0,.7)")
            + lbl(22, 178, f'Coût par jour : {g.fcfa(g.VOITURES[d["r"]["Voiture"]]["CoutParJour"])} FCFA', "font-size:13.33px;color:rgba(0,0,0,.7)")
            + lbl(22, 204, "Client : Jean Mboumba", "font-size:13.33px;color:rgba(0,0,0,.7)")
            + '</div>')
    rx = 32 + lw_ + 16
    rw = g.W - 32 - rx
    cw = (rw - 16) // 2
    lw, iw = 100, cw - 40 - 100
    cli = (g.champ("Cbo_Client", "Client", "Jean Mboumba", 20, 64, lw, iw, "liste")
           + g.champ("Txt_Telephone", "Téléphone", "(+241) 62 54 85 85", 20, 100, lw, iw, "lecture")
           + g.champ("Txt_Email", "Email", "jean.mboumba1@example.com", 20, 136, lw, iw, "lecture"))
    voi = (g.champ("Cbo_Voiture", "Voiture", d["r"]["Voiture"], 20, 64, lw, iw, "liste")
           + g.champ("Txt_Modele", "Modèle", d["mod"], 20, 100, lw, iw, "lecture")
           + g.champ("Txt_Marque", "Marque", d["mar"], 20, 136, lw, iw, "lecture"))
    out += g.carte("Carte_Client", "Client", rx, D_Y0, cw, 178, cli, icone="user")
    out += g.carte("Carte_Voiture", "Voiture", rx + cw + 16, D_Y0, cw, 178, voi, icone="car")
    y = D_Y0 + 194
    out += liste_resa(rx, y, rw, bas - y)
    return d_coquille("reservations", out)


def d_login():
    lw, lh = 880, 520
    cx = (lw - 400) // 2
    c = f"""
{img("d-connexion.jpg", 0, 0, lw, lh, "Login_Photo")}
<div class="abs" style="left:{cx}px;top:48px;width:400px;height:424px;background:#16181B;border:1px solid #3A3E44" {acc("Login_Carte", "Rectangle")}></div>
<div class="abs" style="left:{cx + 176}px;top:76px" {acc("Logo", "Image")}>{g.svg("car-front", "#C9CDD2", 48, 1.5)}</div>
{lbl(cx, 132, g.NOM_APPLI, "width:400px;text-align:center;font-size:18.67px;font-weight:600;letter-spacing:3px;color:#F1F2F4", "Lbl_Titre")}
{lbl(cx, 162, "LOCATION DE PRESTIGE · LIBREVILLE", "width:400px;text-align:center;font-size:11px;letter-spacing:2px;color:#8B9097")}
<div class="etiq" style="left:{cx + 40}px;top:200px">Nom d'utilisateur</div>
<div class="champ" style="left:{cx + 40}px;top:228px;width:320px;height:34px;line-height:32px" {acc("Txt_Utilisateur", "Zone de texte")}>admin</div>
<div class="etiq" style="left:{cx + 40}px;top:272px">Mot de passe</div>
<div class="champ" style="left:{cx + 40}px;top:300px;width:320px;height:34px;line-height:32px;letter-spacing:2px" {acc("Txt_MotDePasse", "Zone de texte")}>********</div>
<div class="btn primaire" style="left:{cx + 40}px;top:362px;width:320px;height:38px;letter-spacing:1px" {acc("Btn_Connexion", "Bouton")}>Se connecter</div>
{lbl(cx, 420, "Mot de passe oublié ? Contactez l'administrateur.", "width:400px;text-align:center;font-size:12px;color:#8B9097")}
"""
    return g.fenetre(g.NOM_APPLI + " - Connexion", lw, lh, c, boutons=("fermer",))


# ==========================================================================
# Aiguillage
# ==========================================================================
def fn(nom):
    return globals()[f"{g.T['design']}_{nom}"]


# Position (object-position) des photos propres à chaque projet : design -> page -> position
POS_PROPRES = {
    "a": {"tableau": "center 78%", "reservations": "center 50%", "clients": "center 62%", "voitures": "center 58%",
          "marques": "center 50%", "carburants": "center 72%", "modeles": "center 55%", "connexion": "40% center"},
    "b": {"tableau": "center 78%", "reservations": "center 60%", "clients": "center 55%", "voitures": "center 60%",
          "marques": "center 50%", "carburants": "center 55%", "modeles": "center 50%", "connexion": "center 60%"},
    "c": {"tableau": "center 60%", "reservations": "center 55%", "clients": "center 55%", "voitures": "center 60%",
          "marques": "15% center", "carburants": "center 55%", "modeles": "center 50%", "connexion": "center 62%"},
    "d": {"tableau": "center center", "reservations": "center center", "clients": "center center", "voitures": "center center",
          "marques": "center center", "carburants": "center center", "modeles": "center center", "connexion": "70% center"},
}


def source(cle, src, pos):
    """Photo propre au projet (photos/<dossier>/<cle>.jpg) si elle existe, sinon la photo commune."""
    dos = g.T.get("photos")
    if dos and (g.ICI / "photos" / dos / f"{cle}.jpg").exists():
        return f"{dos}/{cle}.jpg", POS_PROPRES[g.T["design"]][cle]
    return src, pos


def photos_jobs(photo, H, W):
    """Photos propres à chaque design (photo = fonction de generer.assets_jobs)."""
    d = g.T["design"]
    v = g.T["voile"]
    filtre = g.T.get("photo_filtre", "none")

    def rgba(a):
        return f"rgba({v[0]},{v[1]},{v[2]},{a})"

    if d == "a":
        for cle, (src, pos, _) in PHOTOS.items():
            photo(f"photos/a-bandeau-{cle}.jpg", W, A_HERO, *source(cle, src, pos),
                  f"linear-gradient(90deg, {rgba(.92)} 0%, {rgba(.7)} 35%, {rgba(.25)} 70%, {rgba(.1)} 100%)", filtre)
        photo("photos/a-connexion.jpg", 880, 500, *source("connexion", "login-route-cotiere.jpg", "30% center"),
              f"linear-gradient(90deg, {rgba(.55)} 0%, {rgba(.25)} 50%, {rgba(.55)} 100%), linear-gradient(0deg, {rgba(.7)} 0%, {rgba(0)} 50%)", filtre)
    elif d == "b":
        for cle, (src, _, posv) in PHOTOS.items():
            photo(f"photos/b-panneau-{cle}.jpg", B_PAN, H - B_TETE, *source(cle, src, posv),
                  f"linear-gradient(180deg, {rgba(.15)} 0%, {rgba(.25)} 40%, {rgba(.85)} 72%, {rgba(.95)} 100%)", filtre)
        photo("photos/b-connexion.jpg", 480, 220, *source("connexion", "login-route-cotiere.jpg", "center 60%"),
              f"linear-gradient(180deg, {rgba(.15)} 0%, {rgba(.55)} 100%)", filtre)
    elif d == "c":
        for cle, (src, _, posv) in PHOTOS.items():
            photo(f"photos/c-menu-{cle}.jpg", C_MENU, H, *source(cle, src, posv),
                  f"linear-gradient(180deg, {rgba(.97)} 0%, {rgba(.93)} 50%, {rgba(.55)} 68%, {rgba(.45)} 84%, {rgba(.9)} 100%)", filtre)
        photo("photos/c-connexion.jpg", 880, 300, *source("connexion", "login-route-cotiere.jpg", "center 62%"),
              f"linear-gradient(90deg, {rgba(.9)} 0%, {rgba(.55)} 45%, {rgba(.1)} 100%)", filtre)
    elif d == "d":
        for cle, (src, pos, _) in PHOTOS.items():
            photo(f"photos/d-fond-{cle}.jpg", W, H, *source(cle, src, pos),
                  f"linear-gradient(180deg, rgba(0,0,0,.88) 0%, rgba(0,0,0,.62) 12%, rgba(0,0,0,.72) 40%, rgba(0,0,0,.86) 100%)", filtre)
        photo("photos/d-connexion.jpg", 880, 520, *source("connexion", "login-route-cotiere.jpg", "70% center"),
              "radial-gradient(ellipse at center, rgba(0,0,0,.55) 0%, rgba(0,0,0,.8) 100%)", filtre)
