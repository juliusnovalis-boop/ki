// Rendu des maquettes et des images PNG avec Chromium sans interface.
// Utilisé par generer.py : node rendre.mjs jobs.json
// Dépendances (hors dépôt) : npm i puppeteer-core @sparticuz/chromium
//   ou définir CHROME_PATH vers un Chrome/Chromium installé.
import fs from "node:fs";
import puppeteer from "puppeteer-core";

const jobs = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));

let executablePath = process.env.CHROME_PATH;
let args = ["--no-sandbox", "--allow-file-access-from-files", "--font-render-hinting=none"];
if (!executablePath) {
  const chromium = (await import("@sparticuz/chromium")).default;
  executablePath = await chromium.executablePath();
  args = [...chromium.args, ...args];
}
const browser = await puppeteer.launch({ executablePath, args, headless: true });
const page = await browser.newPage();

async function rendre(j, scale = 1) {
  await page.setViewport({ width: Math.max(j.w, 800), height: Math.max(j.h, 200), deviceScaleFactor: scale });
  await page.goto(j.html, { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready);
  const el = await page.$(j.sel);
  const opts = { path: j.out, omitBackground: j.transparent };
  if (j.out.endsWith('.jpg')) { opts.type = 'jpeg'; opts.quality = 86; opts.omitBackground = false; }
  await el.screenshot(opts);
}

// Logos : l'élément (ou les éléments) seuls, sur fond transparent, à la taille exacte de la maquette
const logos = {};
for (const j of (jobs.logos || [])) {
  await page.setViewport({ width: 1600, height: 820, deviceScaleFactor: 1 });
  await page.goto(j.html, { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready);
  const r = await page.evaluate((sels, marge) => {
    const els = sels.map((s) => document.querySelector(s)).filter(Boolean);
    if (els.length !== sels.length) return null;
    document.querySelectorAll("*").forEach((e) => (e.style.visibility = "hidden"));
    document.documentElement.style.background = "transparent";
    document.body.style.background = "transparent";
    let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
    for (const el of els) {
      el.style.visibility = "visible";
      el.querySelectorAll("*").forEach((c) => (c.style.visibility = "visible"));
      const cs = getComputedStyle(el);
      const plein = cs.backgroundColor !== "rgba(0, 0, 0, 0)" || cs.boxShadow !== "none";
      let q;
      if (plein) {
        const b = el.getBoundingClientRect();
        q = { left: b.left - marge, top: b.top - marge, right: b.right + marge, bottom: b.bottom + marge };
      } else {
        const rg = document.createRange();
        rg.selectNodeContents(el);
        q = rg.getBoundingClientRect();
      }
      x0 = Math.min(x0, q.left); y0 = Math.min(y0, q.top); x1 = Math.max(x1, q.right); y1 = Math.max(y1, q.bottom);
    }
    const ec = document.getElementById("ecran").getBoundingClientRect();
    x0 = Math.floor(x0); y0 = Math.floor(y0);
    return { x: x0, y: y0, w: Math.ceil(x1) - x0, h: Math.ceil(y1) - y0, ex: ec.left, ey: ec.top };
  }, j.sels, j.marge || 0);
  if (!r) { console.error("Logo introuvable : " + j.out); process.exit(2); }
  await page.screenshot({ path: j.out, clip: { x: r.x, y: r.y, width: r.w, height: r.h }, omitBackground: true });
  logos[j.out] = { x: Math.round(r.x - r.ex), y: Math.round(r.y - r.ey), w: r.w, h: r.h };
}
if (jobs.logos_out) fs.writeFileSync(jobs.logos_out, JSON.stringify(logos, null, 1));

for (const j of jobs.assets) await rendre(j);

const cotes = {};
for (const j of jobs.ecrans) {
  await rendre(j);
  cotes[j.cotes] = await page.evaluate(() => {
    const ecran = document.getElementById("ecran").getBoundingClientRect();
    const contenu = document.getElementById("contenu");
    const cr = contenu ? contenu.getBoundingClientRect() : null;
    return [...document.querySelectorAll("[data-acc]")].map((el) => {
      const r = el.getBoundingClientRect();
      const dans = cr && contenu.contains(el) && el !== contenu;
      const o = dans ? cr : ecran;
      return {
        nom: el.dataset.acc, type: el.dataset.type, zone: dans ? "contenu" : "ecran",
        x: Math.round(r.left - o.left), y: Math.round(r.top - o.top),
        w: Math.round(r.width), h: Math.round(r.height),
      };
    });
  });
}
fs.writeFileSync(jobs.cotes, JSON.stringify(cotes, null, 1));
await browser.close();
console.log(`OK : ${jobs.assets.length} images, ${jobs.ecrans.length} maquettes`);
