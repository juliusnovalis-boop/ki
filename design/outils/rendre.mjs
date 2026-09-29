// Rendu des maquettes et des images PNG avec Chromium sans interface.
// Utilisé par generer.py : node rendre.mjs jobs.json
// Dépendances (hors dépôt) : npm i puppeteer-core @sparticuz/chromium
//   ou définir CHROME_PATH vers un Chrome/Chromium installé.
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import puppeteer from "puppeteer-core";

const jobs = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));

let executablePath = process.env.CHROME_PATH;
let args = ["--no-sandbox", "--allow-file-access-from-files", "--font-render-hinting=none"];
if (!executablePath) {
  const chromiumModule = await import("@sparticuz/chromium");
  const chromium = chromiumModule.default;
  executablePath = await chromium.executablePath();
  args = [...chromium.args, ...args];

  // The bundled browser uses NSS/NSPR on Linux. On Debian-based workspaces,
  // unpack the compatibility libraries shipped with @sparticuz/chromium.
  if (process.platform === "linux") {
    const here = path.dirname(fileURLToPath(import.meta.url));
    const compatLib = path.join(os.tmpdir(), "al2023", "lib");
    const bundledLibs = path.join(here, "node_modules", "@sparticuz", "chromium", "bin", "al2023.tar.br");
    if (!fs.existsSync(path.join(compatLib, "libnspr4.so")) && fs.existsSync(bundledLibs)) {
      await chromiumModule.inflate(bundledLibs);
    }
    if (fs.existsSync(path.join(compatLib, "libnspr4.so"))) {
      process.env.LD_LIBRARY_PATH = [compatLib, process.env.LD_LIBRARY_PATH].filter(Boolean).join(path.delimiter);
    }
  }
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
      const dans = cr && contenu.contains(el);
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
