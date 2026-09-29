import express from 'express';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Enable CORS for preview proxy
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
  if (req.method === 'OPTIONS') {
    return res.sendStatus(200);
  }
  next();
});

// Load database data
let dataPath = path.join(__dirname, 'design', 'server_data.json');
let dbData = {};
try {
  dbData = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
} catch (err) {
  console.error('Error reading server_data.json:', err);
}

// Static assets
app.use('/assets', express.static(path.join(__dirname, 'design', 'assets')));
app.use('/maquettes', express.static(path.join(__dirname, 'design', 'maquettes')));
app.use(express.static(path.join(__dirname, 'public')));

// API Routes
app.get('/api/data', (req, res) => {
  res.json(dbData);
});

// Fix anomaly on Reservation #11
app.post('/api/reservations/fix-anomaly', (req, res) => {
  const res11 = dbData.reservations.find(r => r.id === 11);
  if (res11) {
    // Swap dates
    const oldDebut = res11.date_debut;
    const oldFin = res11.date_fin;
    res11.date_debut = "2026-12-06";
    res11.date_fin = "2027-02-13";
    res11.date_debut_fr = "06/12/2026";
    res11.date_fin_fr = "13/02/2027";
    res11.duree_jours = 69;
    res11.montant = 69 * (res11.cout_jour || 38000);
    res11.anomalie = false;
    
    // Recalculate total CA
    let totalCA = 0;
    for (const r of dbData.reservations) {
      totalCA += r.montant;
    }
    dbData.kpis.ca_total = totalCA;
    
    // Update audit item status
    const audit1 = dbData.audit.find(a => a.id === 'AUDIT-01');
    if (audit1) {
      audit1.statut = "✅ Corrigé dans la base active (durée = +69 jours, CA ajusté)";
    }
    
    res.json({ success: true, message: "Anomalie corrigée avec succès !", reservation: res11, total_ca: totalCA });
  } else {
    res.status(404).json({ error: "Réservation n° 11 non trouvée" });
  }
});

// Update or add a reservation
app.post('/api/reservations', (req, res) => {
  const payload = req.body;
  if (!payload.id) {
    const maxId = dbData.reservations.reduce((max, r) => Math.max(max, r.id), 0);
    payload.id = maxId + 1;
    dbData.reservations.push(payload);
    dbData.kpis.reservations_total = dbData.reservations.length;
  } else {
    const idx = dbData.reservations.findIndex(r => r.id === parseInt(payload.id));
    if (idx >= 0) {
      dbData.reservations[idx] = { ...dbData.reservations[idx], ...payload };
    } else {
      dbData.reservations.push(payload);
    }
  }
  res.json({ success: true, reservation: payload });
});

// Delete reservation
app.delete('/api/reservations/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const idx = dbData.reservations.findIndex(r => r.id === id);
  if (idx >= 0) {
    dbData.reservations.splice(idx, 1);
    dbData.kpis.reservations_total = dbData.reservations.length;
    res.json({ success: true, message: `Réservation ${id} supprimée` });
  } else {
    res.status(404).json({ error: "Réservation introuvable" });
  }
});

// Save client
app.post('/api/clients', (req, res) => {
  const client = req.body;
  if (!client.CIN) {
    const nextNum = dbData.clients.length + 1;
    client.CIN = `CL-${String(nextNum).padStart(4, '0')}`;
    dbData.clients.push(client);
    dbData.kpis.clients_total = dbData.clients.length;
  } else {
    const idx = dbData.clients.findIndex(c => c.CIN === client.CIN);
    if (idx >= 0) {
      dbData.clients[idx] = { ...dbData.clients[idx], ...client };
    } else {
      dbData.clients.push(client);
      dbData.kpis.clients_total = dbData.clients.length;
    }
  }
  res.json({ success: true, client });
});

// Save vehicle
app.post('/api/voitures', (req, res) => {
  const car = req.body;
  const idx = dbData.voitures.findIndex(v => v.matricule === car.matricule);
  if (idx >= 0) {
    dbData.voitures[idx] = { ...dbData.voitures[idx], ...car };
  } else {
    dbData.voitures.push(car);
    dbData.kpis.voitures_total = dbData.voitures.length;
  }
  res.json({ success: true, voiture: car });
});

// Fallback to index.html
app.use((req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`RENTAL GABON CAR application running at http://0.0.0.0:${PORT}`);
});
