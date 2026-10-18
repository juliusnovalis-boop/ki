"""Propositions de logos AURION (vectoriels, PNG transparents) + planche de choix.

Usage : LD_LIBRARY_PATH=/tmp/al/lib python3 outils/logos_aurion.py
Sortie : design/styles/bleu-royal-noir/logos-aurion/
"""
import json
import math
import subprocess
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
FONTS = (ICI.parent / "maquettes" / "fonts").as_uri()
OUT = ICI.parent / "styles" / "bleu-royal-noir" / "logos-aurion"
ROYAL, NUIT, ARGENT = "#002366", "#01040B", "#C4CAD3"

DEFS = """<defs>
<linearGradient id="or" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="120"><stop offset="0" stop-color="#F3DC94"/><stop offset=".55" stop-color="#C9A24B"/><stop offset="1" stop-color="#A3802F"/></linearGradient>
<linearGradient id="ag" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="120"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#AEB6C2"/></linearGradient>
</defs>"""

CSS = f"""
@font-face {{ font-family: Cinzel; font-weight: 600; src: url({FONTS}/cinzel-latin-600-normal.woff2); }}
@font-face {{ font-family: Cinzel; font-weight: 700; src: url({FONTS}/cinzel-latin-700-normal.woff2); }}
@font-face {{ font-family: Michroma; src: url({FONTS}/michroma-latin-400-normal.woff2); }}
@font-face {{ font-family: Futur; font-weight: 600; src: url({FONTS}/barlow-semi-condensed-latin-600-normal.woff2); }}
@font-face {{ font-family: Futur; font-weight: 400; src: url({FONTS}/barlow-semi-condensed-latin-400-normal.woff2); }}
html, body {{ margin: 0; background: transparent; }}
.logo {{ display: inline-flex; align-items: center; }}
.mot {{ line-height: 1; white-space: nowrap; }}
.sous {{ font-family: Futur; font-weight: 600; white-space: nowrap; }}
.or-txt {{ background: linear-gradient(180deg, #F3DC94, #C9A24B 55%, #A3802F); -webkit-background-clip: text; background-clip: text; color: transparent; }}
.ag-txt {{ background: linear-gradient(180deg, #FFFFFF, #AEB6C2); -webkit-background-clip: text; background-clip: text; color: transparent; }}
"""


def rayons(cx, cy, r1, r2, angles, coul, ep):
    out = ""
    for a in angles:
        t = math.radians(a)
        out += (f'<line x1="{cx + r1 * math.cos(t):.1f}" y1="{cy - r1 * math.sin(t):.1f}" x2="{cx + r2 * math.cos(t):.1f}" '
                f'y2="{cy - r2 * math.sin(t):.1f}" stroke="{coul}" stroke-width="{ep}" stroke-linecap="round"/>')
    return out


def hexagone(cx, cy, r):
    return " ".join(f"{cx + r * math.cos(math.radians(-90 + k * 60)):.1f},{cy + r * math.sin(math.radians(-90 + k * 60)):.1f}" for k in range(6))


# (numéro, clé, nom, description, largeur icône, svg icône, html du nom)
LOGOS = [
    ("1", "aurore", "Aurore", "Soleil doré qui se lève sur l'horizon : AURION évoque l'or (aurum) et l'aurore. Élégant et chaleureux.", 120,
     '<path d="M30 82 A30 30 0 0 1 90 82 Z" fill="url(#or)"/>' + rayons(60, 82, 39, 50, [157.5, 135, 112.5, 90, 67.5, 45, 22.5], "url(#or)", 3.5)
     + '<line x1="10" y1="82" x2="110" y2="82" stroke="url(#or)" stroke-width="3" stroke-linecap="round"/>'
     + f'<line x1="28" y1="92" x2="92" y2="92" stroke="{ARGENT}" stroke-width="2" stroke-linecap="round"/>'
     + f'<line x1="44" y1="101" x2="76" y2="101" stroke="{ARGENT}" stroke-width="2" stroke-linecap="round"/>',
     ("Cinzel", 600, 48, 12, "#FFFFFF", "", "LOCATION DE PRESTIGE", "#C9A24B")),
    ("2", "hexa", "Hexa", "Monogramme futuriste : un A sans barre dans un hexagone bleu royal cerclé d'or, la barre dorée flotte à l'intérieur.", 120,
     f'<polygon points="{hexagone(60, 60, 52)}" fill="{ROYAL}" stroke="url(#or)" stroke-width="3.5" stroke-linejoin="round"/>'
     + '<path d="M36 88 L60 34 L84 88" fill="none" stroke="#FFFFFF" stroke-width="7.5" stroke-linejoin="miter"/>'
     + '<line x1="50" y1="75" x2="70" y2="75" stroke="url(#or)" stroke-width="5"/>',
     ("Michroma", 400, 38, 11, "#FFFFFF", "", "LOCATION DE PRESTIGE", ARGENT)),
    ("3", "ecusson", "Écusson", "Blason de constructeur de luxe : écusson bleu royal, double filet d'or et A doré. Classique et haut de gamme.", 120,
     f'<path d="M60 6 L105 21 L105 58 C105 87 84 105 60 115 C36 105 15 87 15 58 L15 21 Z" fill="{ROYAL}" stroke="url(#or)" stroke-width="3.5" stroke-linejoin="round"/>'
     + '<path d="M60 15 L97 27 L97 58 C97 81 80 97 60 106 C40 97 23 81 23 58 L23 27 Z" fill="none" stroke="#C9A24B" stroke-width="1.2" opacity=".7"/>'
     + '<text x="60" y="82" text-anchor="middle" font-family="Cinzel" font-weight="700" font-size="58" fill="url(#or)">A</text>'
     + '<line x1="44" y1="93" x2="76" y2="93" stroke="#C9A24B" stroke-width="1.5"/>',
     ("Cinzel", 700, 50, 12, "or", "", "LOCATION DE PRESTIGE", ARGENT)),
    ("4", "ailes", "Ailes", "Emblème ailé comme les grandes marques automobiles : médaillon bleu royal au A blanc, ailes dorées.", 160,
     f'<circle cx="80" cy="60" r="25" fill="{ROYAL}" stroke="url(#or)" stroke-width="3"/>'
     + '<text x="80" y="70" text-anchor="middle" font-family="Cinzel" font-weight="700" font-size="28" fill="#FFFFFF">A</text>'
     + "".join(f'<line x1="{51}" y1="{y}" x2="{51 - l}" y2="{y - d}" stroke="url(#or)" stroke-width="4" stroke-linecap="round"/>'
               f'<line x1="{109}" y1="{y}" x2="{109 + l}" y2="{y - d}" stroke="url(#or)" stroke-width="4" stroke-linecap="round"/>'
               for y, l, d in [(48, 46, 12), (57, 40, 10), (66, 31, 8), (75, 21, 6)]),
     ("Cinzel", 600, 46, 12, "#FFFFFF", "", "LOCATION DE PRESTIGE", "#C9A24B")),
    ("5", "route", "Route", "Le A dessine une route qui file vers l'horizon, la ligne centrale est dorée. Dynamique et moderne.", 120,
     '<path d="M16 110 L60 12 L104 110" fill="none" stroke="url(#ag)" stroke-width="9" stroke-linejoin="miter"/>'
     + '<line x1="60" y1="102" x2="60" y2="88" stroke="url(#or)" stroke-width="6"/>'
     + '<line x1="60" y1="78" x2="60" y2="67" stroke="url(#or)" stroke-width="5"/>'
     + '<line x1="60" y1="58" x2="60" y2="50" stroke="url(#or)" stroke-width="4"/>',
     ("Michroma", 400, 38, 11, "ag", "", "LOCATION DE PRESTIGE", "#C9A24B")),
    ("6", "orbite", "Orbite", "Futuriste : anneau doré avec un point en orbite autour d'un disque bleu royal, le O du nom est doré.", 120,
     '<circle cx="60" cy="60" r="47" fill="none" stroke="url(#or)" stroke-width="3"/>'
     + f'<circle cx="60" cy="60" r="35" fill="{ROYAL}"/>'
     + '<path d="M45 79 L60 43 L75 79" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linejoin="miter"/>'
     + f'<circle cx="93.2" cy="26.8" r="7" fill="#E3C77A" stroke="{NUIT}" stroke-width="4"/>',
     ("Michroma", 400, 38, 11, "#FFFFFF", "O", "LOCATION DE PRESTIGE", ARGENT)),
]


def logo_html(L, s=1.0, icone_seule=False):
    num, cle, nom, desc, iw, svg, (police, poids, taille, esp, coul, o_or, sous, coul_sous) = L
    ic = f'<svg width="{iw * s:.0f}" height="{120 * s:.0f}" viewBox="0 0 {iw} 120" xmlns="http://www.w3.org/2000/svg">{DEFS}{svg}</svg>'
    if icone_seule:
        return f'<div class="logo" id="a" style="padding:{6 * s:.0f}px">{ic}</div>'
    cls = {"or": "or-txt", "ag": "ag-txt"}.get(coul, "")
    style_c = "" if cls else f"color:{coul};"
    mot = "AURION" if not o_or else "AURI<span style='color:#E3C77A'>O</span>N"
    texte = (f'<div><div class="mot {cls}" style="font-family:{police};font-weight:{poids};font-size:{taille * s:.1f}px;'
             f'letter-spacing:{esp * s:.1f}px;{style_c}">{mot}</div>'
             f'<div class="sous" style="margin-top:{10 * s:.0f}px;font-size:{12.5 * s:.1f}px;letter-spacing:{5.2 * s:.1f}px;color:{coul_sous}">{sous}</div></div>')
    return f'<div class="logo" id="a" style="gap:{22 * s:.0f}px;padding:{6 * s:.0f}px {4 * s:.0f}px {6 * s:.0f}px {6 * s:.0f}px">{ic}{texte}</div>'


def page(corps, fond="transparent"):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS} body{{background:{fond}}}</style></head><body>{corps}</body></html>'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp(prefix="aurion-"))
    jobs = []

    def job(nom, html, w, h, transparent=True, sel="#a"):
        p = tmp / f"{nom}.html"
        p.write_text(html)
        jobs.append({"html": p.as_uri(), "out": str(OUT / nom), "w": w, "h": h, "transparent": transparent, "sel": sel})

    for L in LOGOS:
        base = f"logo-{L[0]}-{L[1]}"
        job(f"{base}-horizontal.png", page(logo_html(L, 2)), 1400, 400)
        job(f"{base}-icone.png", page(logo_html(L, 2, True)), 600, 400)
    # planche de choix : 6 cartes sur le fond de l'application
    cartes = ""
    sans_id = ' id="a"'
    for L in LOGOS:
        cartes += (f'<div class="carte"><div class="tete"><span class="n">{L[0]}</span>{L[2].upper()}</div>'
                   f'<div class="zone">{logo_html(L, 0.9).replace(sans_id, "")}</div>'
                   f'<div class="ic">{logo_html(L, 0.42, True).replace(sans_id, "")}</div>'
                   f'<div class="desc">{L[3]}</div></div>')
    planche = (f'<div id="a" class="planche"><div class="titre">AURION · PROPOSITIONS DE LOGO</div>'
               f'<div class="st">Bleu royal #002366 · or · argent · blanc — choisissez un numéro</div><div class="grille">{cartes}</div></div>')
    css_pl = """
.planche { width: 1568px; padding: 34px 40px 40px; box-sizing: border-box; background: #01040B; }
.titre { font-family: Futur; font-weight: 600; font-size: 15px; letter-spacing: 5px; color: #C9A24B; }
.st { font-family: Futur; font-weight: 400; font-size: 15px; color: #8A96AD; margin: 6px 0 24px; }
.grille { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.carte { position: relative; height: 250px; background: #06112A; border: 1px solid #13284F; }
.tete { position: absolute; left: 22px; top: 16px; font-family: Futur; font-weight: 600; font-size: 14px; letter-spacing: 2.5px; color: #FFFFFF; }
.tete .n { color: #C9A24B; margin-right: 12px; font-size: 18px; }
.zone { position: absolute; left: 22px; top: 62px; }
.ic { position: absolute; right: 24px; top: 14px; padding: 6px; border: 1px solid #13284F; background: #01040B; }
.desc { position: absolute; left: 22px; right: 22px; bottom: 16px; font-family: Futur; font-size: 14.5px; color: #A9B4C8; }
"""
    p = tmp / "planche.html"
    p.write_text(page(planche).replace("</style>", css_pl + "</style>"))
    jobs.append({"html": p.as_uri(), "out": str(OUT / "planche-logos.png"), "w": 1568, "h": 900, "transparent": False, "sel": "#a"})
    jf = tmp / "jobs.json"
    jf.write_text(json.dumps({"assets": jobs, "ecrans": [], "cotes": str(tmp / "c.json")}))
    r = subprocess.run(["node", str(ICI / "rendre.mjs"), str(jf)], cwd=ICI)
    raise SystemExit(r.returncode)


if __name__ == "__main__":
    main()
