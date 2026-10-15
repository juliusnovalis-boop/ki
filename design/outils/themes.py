"""Palettes des styles de maquettes RENTAL GABON CAR.

Chaque style définit :
  css      : les variables de style.css (couleurs des contrôles Access)
  kpi      : (fond, pastille) des 3 indicateurs du tableau de bord
  le reste : couleurs des icônes et du voile posé sur les photos
"""

BASE_CLAIR = {
    "surface": "#FFFFFF", "champ": "#FFFFFF", "entete": "#FFFFFF", "logo": "#FFFFFF",
    "texte": "#111827", "texte2": "#1F2937", "etiq": "#4B5563", "gris": "#6B7280",
    "champ-bordure": "#C9D0DA", "lecture": "#F4F5F7", "lecture-bordure": "#DDE1E7", "lecture-txt": "#374151",
    "liste-trait": "#D9DDE3", "sep": "#EDF0F4", "accent-txt": "#FFFFFF",
    "danger": "#DC2626", "danger-bordure": "#E8A5A5",
    "defil": "#F0F0F0", "defil-trait": "#E6E6E6", "pouce": "#C2C2C2",
    "kpi-lib": "rgba(255,255,255,.82)", "kpi-val": "#FFFFFF", "bandeau-sous": "rgba(255,255,255,.85)",
    "barre-fond": "#FFFFFF", "barre-trait": "#E6E6E6", "barre-txt": "#000000",
    "nav-actif-fond": "#FFFFFF",
}


def theme(cle, nom, dossier, css, kpi, design="bleu", **py):
    c = dict(BASE_CLAIR)
    c.update(css)
    t = {"cle": cle, "design": design, "nom": nom, "dossier": dossier, "css": c, "kpi": kpi,
         "logo": c["logo"], "gris": c["gris"], "etiq": c["etiq"], "danger": c["danger"],
         "accent_txt": c["accent-txt"], "menu": c["menu"], "kpi_ico": "#FFFFFF"}
    t.update(py)
    return t


THEMES = [
    # ------------------------------------------------------------------ bleu (version validée)
    theme("bleu", "Bleu marine", "maquettes", {
        "fond": "#EEF2F9", "menu": "#1E3A8A", "nav-txt": "#DCE6FB", "nav-actif-txt": "#1E3A8A", "rubrique": "#8FA6DA",
        "entete-trait": "#2563EB", "titre": "#1E3A8A", "carte-bordure": "#D3DDEE", "bande": "#F2F6FD",
        "btn-bordure": "#C6D4EE", "montant": "#EAF1FD", "montant-bordure": "#C6D4EE", "montant-txt": "#1E40AF",
        "accent": "#2563EB", "liste-bordure": "#B9C9E6",
    }, kpi=[("#1E40AF", "#3F5BBE"), ("#2563EB", "#4B7FEF"), ("#3B82F6", "#5C97F8")],
        societe="RENTAL GABON CAR", photos="", design="bleu", icone="#2563EB", icone_titre="#1E3A8A", nav_ico="#AFC3F0", nav_ico_actif="#1E3A8A", voile=(30, 58, 138)),

    # ------------------------------------------------------------------ noir & blanc
    theme("noir-blanc", "Noir et blanc", "styles/noir-blanc", {
        "fond": "#F2F2F2", "menu": "#0D0D0D", "nav-txt": "#D4D4D4", "nav-actif-txt": "#0D0D0D", "rubrique": "#8A8A8A",
        "entete-trait": "#0D0D0D", "titre": "#0D0D0D", "carte-bordure": "#DADADA", "bande": "#F8F8F8",
        "btn-bordure": "#CFCFCF", "montant": "#F1F1F1", "montant-bordure": "#C9C9C9", "montant-txt": "#0D0D0D",
        "accent": "#111111", "liste-bordure": "#BDBDBD", "champ-bordure": "#C8C8C8", "lecture": "#F5F5F5",
        "lecture-bordure": "#DEDEDE", "liste-trait": "#DDDDDD", "sep": "#EEEEEE",
        "etiq": "#4A4A4A", "gris": "#6E6E6E", "texte": "#111111", "texte2": "#1C1C1C", "lecture-txt": "#333333",
    }, kpi=[("#0D0D0D", "#2A2A2A"), ("#262626", "#404040"), ("#404040", "#5A5A5A")],
        societe="ONYX CAR", photos="onyx", design="a", icone="#111111", icone_titre="#111111", nav_ico="#BDBDBD", nav_ico_actif="#0D0D0D", voile=(13, 13, 13),
        photo_filtre="grayscale(1) contrast(1.05)"),

    # ------------------------------------------------------------------ rose & blanc
    theme("rose-blanc", "Rose et blanc", "styles/rose-blanc", {
        "fond": "#FCF1F6", "menu": "#9D174D", "nav-txt": "#FCE1EE", "nav-actif-txt": "#9D174D", "rubrique": "#F39CC4",
        "entete-trait": "#DB2777", "titre": "#9D174D", "carte-bordure": "#F2D2E1", "bande": "#FEF6FA",
        "btn-bordure": "#F0C6DA", "montant": "#FDE8F2", "montant-bordure": "#F0C6DA", "montant-txt": "#9D174D",
        "accent": "#DB2777", "liste-bordure": "#EBB8CF", "sep": "#F8EAF0", "lecture": "#FAF5F7", "lecture-bordure": "#EEDFE6",
        "danger": "#B91C1C", "danger-bordure": "#E3A3A3",
    }, kpi=[("#9D174D", "#B53D6F"), ("#DB2777", "#E35491"), ("#EC4899", "#F06DAC")],
        societe="TIFFANY CAR", photos="tiffany", design="b", icone="#DB2777", icone_titre="#9D174D", nav_ico="#F6B5D3", nav_ico_actif="#9D174D", voile=(131, 24, 67)),

    # ------------------------------------------------------------------ vert jade & blanc
    theme("vert-jade-blanc", "Vert jade et blanc", "styles/vert-jade-blanc", {
        "fond": "#EDF7F3", "menu": "#064E3B", "nav-txt": "#D1F2E4", "nav-actif-txt": "#064E3B", "rubrique": "#6CC4A1",
        "entete-trait": "#00A86B", "titre": "#065F46", "carte-bordure": "#CDE7DC", "bande": "#F3FAF7",
        "btn-bordure": "#BCE0D0", "montant": "#E2F5EC", "montant-bordure": "#BCE0D0", "montant-txt": "#047857",
        "accent": "#00A86B", "liste-bordure": "#A8D6C2", "sep": "#E6F2EC", "lecture": "#F4F8F6", "lecture-bordure": "#DCE8E2",
    }, kpi=[("#065F46", "#2A7A63"), ("#00A86B", "#2DBA87"), ("#10B981", "#3CC99A")],
        societe="JADE MOTORS", photos="jade", design="c", icone="#00A86B", icone_titre="#065F46", nav_ico="#9FDCC3", nav_ico_actif="#064E3B", voile=(6, 78, 59)),

    # ------------------------------------------------------------------ argenté & noir (sombre)
    theme("argente-noir", "Argenté et noir", "styles/argente-noir", {
        "fond": "#0B0C0E", "surface": "#16181B", "champ": "#1F2226", "entete": "#121417", "logo": "#E8EAED",
        "menu": "#000000", "nav-txt": "#B8BCC2", "nav-actif-fond": "#D4D7DB", "nav-actif-txt": "#000000", "rubrique": "#7D828A",
        "entete-trait": "#AEB3B9", "titre": "#E8EAED", "carte-bordure": "#2A2D32", "bande": "#1B1D21",
        "btn-bordure": "#3A3E44", "montant": "#24272C", "montant-bordure": "#4A4F56", "montant-txt": "#F1F2F4",
        "accent": "#C9CDD2", "accent-txt": "#0B0C0E", "liste-bordure": "#3A3E44", "liste-trait": "#2C2F34",
        "texte": "#F1F2F4", "texte2": "#DADDE1", "etiq": "#A3A8AF", "gris": "#8B9097",
        "champ-bordure": "#3A3E44", "lecture": "#1A1C20", "lecture-bordure": "#2E3136", "lecture-txt": "#C3C7CC",
        "sep": "#25282C", "danger": "#F87171", "danger-bordure": "#6B2C2C",
        "defil": "#1F2226", "defil-trait": "#2E3136", "pouce": "#4A4F56",
        "kpi-lib": "rgba(0,0,0,.62)", "kpi-val": "#0B0C0E",
        "barre-fond": "#202020", "barre-trait": "#2B2B2B", "barre-txt": "#FFFFFF",
    }, kpi=[("#D9DCE0", "#BFC3C9"), ("#C2C6CC", "#A9AEB5"), ("#A9AEB5", "#91969E")],
        societe="PLATINUM DRIVE", photos="platinum", design="d", icone="#C9CDD2", icone_titre="#C9CDD2", nav_ico="#8E939A", nav_ico_actif="#000000", voile=(0, 0, 0),
        kpi_ico="#0B0C0E", photo_filtre="saturate(.35) contrast(1.05)"),
]
