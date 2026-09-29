/**
 * RENTAL GABON CAR - Script Principal de la Suite
 * Gère l'interactivité, le comparateur glissant, les données de la base et la navigation.
 */

// Application State
let appData = null;
let currentResIndex = 0;
let currentCliIndex = 0;
let currentVoiIndex = 0;

// Formatters
const fcfa = (n) => {
  return new Intl.NumberFormat('fr-FR').format(Math.round(n)) + ' FCFA';
};

const formatDate = (isoStr) => {
  if (!isoStr) return '';
  const parts = isoStr.split('T')[0].split(' ')[0].split('-');
  if (parts.length === 3) {
    return `${parts[2]}/${parts[1]}/${parts[0]}`;
  }
  return isoStr;
};

// Toast notification
function showToast(msg, duration = 3000) {
  const toast = document.getElementById('toast');
  if (!toast) return;
  toast.textContent = msg;
  toast.style.display = 'block';
  setTimeout(() => {
    toast.style.display = 'none';
  }, duration);
}

// Live Libreville Clock (UTC+1)
function initClock() {
  const clockEl = document.getElementById('suite-clock');
  const dateDisplay = document.getElementById('content-date-display');
  
  function update() {
    const now = new Date();
    // Gabon is UTC+1 (WAT)
    const options = {
      timeZone: 'Africa/Libreville',
      weekday: 'long',
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit'
    };
    const dateStr = now.toLocaleDateString('fr-FR', options);
    if (clockEl) {
      clockEl.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg><span>Libreville : ${now.toLocaleTimeString('fr-FR', { timeZone: 'Africa/Libreville' })}</span>`;
    }
    if (dateDisplay) {
      dateDisplay.textContent = dateStr;
    }
  }
  update();
  setInterval(update, 1000);
}

// =============================================================================
// MAIN INITIALIZATION
// =============================================================================
async function initApp() {
  initClock();
  setupSuiteTabs();
  setupAppSidebar();
  setupSlider();
  setupGallery();
  setupGuide();
  setupDbExplorer();
  setupAssetsView();

  try {
    const res = await fetch('/api/data');
    appData = await res.json();
    renderAll();
  } catch (err) {
    console.error('Failed to load initial data:', err);
    showToast('Erreur lors du chargement des données.');
  }
}

// Suite Top Navigation Switcher
function setupSuiteTabs() {
  const tabBtns = document.querySelectorAll('.suite-tab-btn');
  const views = document.querySelectorAll('.suite-view');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const targetView = btn.dataset.view;
      views.forEach(v => {
        v.classList.remove('active');
        if (v.id === `view-${targetView}`) {
          v.classList.add('active');
        }
      });
    });
  });
}

// App Sidebar Navigation Switcher (Mode 1)
function setupAppSidebar() {
  const navItems = document.querySelectorAll('.sidebar-nav .nav-item');
  const screens = document.querySelectorAll('.screen-view');

  navItems.forEach(item => {
    item.addEventListener('click', () => {
      navItems.forEach(i => i.classList.remove('active'));
      item.classList.add('active');

      const targetScreen = item.dataset.screen;
      screens.forEach(s => {
        s.classList.remove('active');
        if (s.id === `screen-${targetScreen}`) {
          s.classList.add('active');
        }
      });
    });
  });

  const btnQuickLogin = document.getElementById('btn-quick-login');
  if (btnQuickLogin) {
    btnQuickLogin.addEventListener('click', () => {
      navItems.forEach(i => i.classList.remove('active'));
      document.querySelector('[data-screen="login"]').classList.add('active');
      screens.forEach(s => s.classList.remove('active'));
      document.getElementById('screen-login').classList.add('active');
    });
  }
}

// =============================================================================
// DATA RENDERING
// =============================================================================
function renderAll() {
  if (!appData) return;

  renderDashboard();
  renderReservations();
  renderClients();
  renderVoitures();
  renderMarques();
  renderCarburants();
  renderModeles();
  renderAuditCards();
  renderRawTable('Client');
  renderCotesSection('Tableau de bord');
}

// -----------------------------------------------------------------------------
// 1. Dashboard Render
// -----------------------------------------------------------------------------
function renderDashboard() {
  const kpis = appData.kpis;
  document.getElementById('kpi-ca-val').innerHTML = `${new Intl.NumberFormat('fr-FR').format(kpis.ca_total)} <small>FCFA</small>`;
  document.getElementById('kpi-voi-val').textContent = kpis.voitures_total;
  document.getElementById('kpi-cli-val').textContent = kpis.clients_total;

  const activeReservations = appData.reservations.filter(r => r.en_cours);
  document.getElementById('kpi-voi-sub').textContent = `${activeReservations.length} en location aujourd'hui`;
  document.getElementById('dash-active-count').textContent = `${activeReservations.length} en cours au 28/09/2026`;

  // Active rentals table
  const tbody = document.getElementById('tbody-dash-active');
  tbody.innerHTML = '';
  activeReservations.forEach(r => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><strong>${r.voiture_matricule}</strong></td>
      <td>${r.voiture_modele}</td>
      <td>${r.date_debut_fr}</td>
      <td>${r.date_fin_fr}</td>
      <td>${r.client_prenom}</td>
      <td>${r.client_nom}</td>
      <td>
        <button class="btn-primary" style="padding: 3px 8px; font-size: 11px;" onclick="jumpToReservation(${r.id})">
          Voir fiche
        </button>
      </td>
    `;
    tbody.appendChild(tr);
  });

  // Top 5 clients
  const topTbody = document.getElementById('tbody-top5-clients');
  topTbody.innerHTML = '';
  const medals = ['🥇', '🥈', '🥉', '4.', '5.'];
  kpis.top_clients.forEach((c, idx) => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${medals[idx] || idx+1}</td>
      <td><strong>${c.prenom}</strong></td>
      <td>${c.nom}</td>
      <td class="num" style="font-weight: 700; color: #1E40AF;">${new Intl.NumberFormat('fr-FR').format(c.ca)}</td>
    `;
    topTbody.appendChild(tr);
  });

  // Flotte par carburant
  const carbBox = document.getElementById('container-carburants-progress');
  carbBox.innerHTML = '';
  kpis.flotte_carburants.forEach(item => {
    const wrap = document.createElement('div');
    wrap.className = 'progress-wrap';
    wrap.innerHTML = `
      <div class="progress-header">
        <span><strong>${item.type}</strong> (${item.voitures} véhicules)</span>
        <span style="font-weight: 700; color: #2563EB;">${item.part}</span>
      </div>
      <div class="progress-bar-bg">
        <div class="progress-bar-fill" style="width: ${item.pct}%;"></div>
      </div>
    `;
    carbBox.appendChild(wrap);
  });
}

// -----------------------------------------------------------------------------
// 2. Reservations Module
// -----------------------------------------------------------------------------
function renderReservations() {
  const reservations = appData.reservations;
  document.getElementById('badge-res-count').textContent = reservations.length;
  document.getElementById('lbl-res-table-count').textContent = `${reservations.length} réservations`;

  // Populate client dropdown
  const cboCli = document.getElementById('form-res-client');
  cboCli.innerHTML = '';
  appData.clients.forEach(c => {
    const opt = document.createElement('option');
    opt.value = c.CIN;
    opt.textContent = `${c.Prénom} ${c.Nom} (${c.CIN})`;
    cboCli.appendChild(opt);
  });

  // Populate vehicle dropdown
  const cboVoi = document.getElementById('form-res-voiture');
  cboVoi.innerHTML = '';
  appData.voitures.forEach(v => {
    const opt = document.createElement('option');
    opt.value = v.matricule;
    opt.textContent = `${v.matricule} - ${v.modele} (${v.marque})`;
    cboVoi.appendChild(opt);
  });

  // Check for Res #11 anomaly
  const res11 = reservations.find(r => r.id === 11);
  const alert11 = document.getElementById('alert-res-11');
  if (res11 && res11.anomalie) {
    alert11.style.display = 'flex';
  } else {
    alert11.style.display = 'none';
  }

  // Load current reservation into form
  loadReservationToForm(currentResIndex);
  renderReservationsTable(reservations);
  setupReservationEvents();
}

function loadReservationToForm(index) {
  const reservations = appData.reservations;
  if (!reservations || reservations.length === 0) return;
  
  if (index < 0) index = 0;
  if (index >= reservations.length) index = reservations.length - 1;
  currentResIndex = index;

  const r = reservations[index];
  document.getElementById('form-res-code').value = r.id;
  document.getElementById('form-res-client').value = r.client_cin;
  document.getElementById('form-res-tel').value = r.client_tel || '';
  document.getElementById('form-res-email').value = r.client_email || '';

  document.getElementById('form-res-voiture').value = r.voiture_matricule;
  document.getElementById('form-res-modele').value = r.voiture_modele;
  document.getElementById('form-res-marque').value = r.voiture_marque;

  document.getElementById('form-res-datedebut').value = r.date_debut;
  document.getElementById('form-res-datefin').value = r.date_fin;

  const durationStr = r.duree_jours < 0 ? `${r.duree_jours} jour(s) ⚠️ Inversion!` : `${r.duree_jours} jour(s)`;
  document.getElementById('form-res-duree').value = durationStr;
  document.getElementById('form-res-montant').value = fcfa(r.montant);

  document.getElementById('lbl-res-counter').textContent = `${index + 1} sur ${reservations.length}`;

  // Highlight row in table
  const rows = document.querySelectorAll('#tbody-reservations tr');
  rows.forEach(row => {
    row.classList.remove('selected');
    if (parseInt(row.dataset.id) === r.id) {
      row.classList.add('selected');
    }
  });
}

function renderReservationsTable(list) {
  const tbody = document.getElementById('tbody-reservations');
  tbody.innerHTML = '';

  list.forEach(r => {
    const tr = document.createElement('tr');
    tr.dataset.id = r.id;
    if (r.id === appData.reservations[currentResIndex]?.id) {
      tr.classList.add('selected');
    }

    let statusBadge = '<span class="status-pill info">Terminée</span>';
    if (r.anomalie) {
      statusBadge = '<span class="status-pill danger">⚠️ Date négative</span>';
    } else if (r.en_cours) {
      statusBadge = '<span class="status-pill success">En cours</span>';
    } else {
      const d0 = new Date(r.date_debut);
      const now = new Date('2026-09-28');
      if (d0 > now) {
        statusBadge = '<span class="status-pill warning">À venir</span>';
      }
    }

    tr.innerHTML = `
      <td><strong>${r.id}</strong></td>
      <td>${r.date_debut_fr}</td>
      <td>${r.date_fin_fr}</td>
      <td>${r.client_nom_complet}</td>
      <td>${r.voiture_matricule}</td>
      <td>${r.voiture_modele}</td>
      <td>${r.voiture_marque}</td>
      <td>${r.duree_jours} j</td>
      <td class="num">${new Intl.NumberFormat('fr-FR').format(r.montant)}</td>
      <td>${statusBadge}</td>
    `;

    tr.addEventListener('click', () => {
      const idx = appData.reservations.findIndex(item => item.id === r.id);
      if (idx >= 0) loadReservationToForm(idx);
    });

    tbody.appendChild(tr);
  });
}

function setupReservationEvents() {
  // Navigation buttons
  document.getElementById('btn-res-first').onclick = () => loadReservationToForm(0);
  document.getElementById('btn-res-prev').onclick = () => loadReservationToForm(currentResIndex - 1);
  document.getElementById('btn-res-next').onclick = () => loadReservationToForm(currentResIndex + 1);
  document.getElementById('btn-res-last').onclick = () => loadReservationToForm(appData.reservations.length - 1);

  // Client dropdown change
  document.getElementById('form-res-client').onchange = (e) => {
    const cli = appData.clients.find(c => c.CIN === e.target.value);
    if (cli) {
      document.getElementById('form-res-tel').value = cli.Téléphone || '';
      document.getElementById('form-res-email').value = cli.Email || '';
    }
  };

  // Voiture dropdown change
  document.getElementById('form-res-voiture').onchange = (e) => {
    const v = appData.voitures.find(item => item.matricule === e.target.value);
    if (v) {
      document.getElementById('form-res-modele').value = v.modele;
      document.getElementById('form-res-marque').value = v.marque;
      recalculateResAmount();
    }
  };

  // Date changes
  document.getElementById('form-res-datedebut').onchange = recalculateResAmount;
  document.getElementById('form-res-datefin').onchange = recalculateResAmount;

  // Fix anomaly button
  document.getElementById('btn-fix-res-11').onclick = async () => {
    try {
      const res = await fetch('/api/reservations/fix-anomaly', { method: 'POST' });
      const data = await res.json();
      if (data.success) {
        showToast('Réservation n° 11 corrigée ! Dates et CA réajustés.');
        const fresh = await fetch('/api/data');
        appData = await fresh.json();
        renderAll();
      }
    } catch (e) {
      showToast('Erreur lors de la correction');
    }
  };

  // Save Reservation
  document.getElementById('btn-res-save').onclick = async () => {
    const code = document.getElementById('form-res-code').value;
    const clientCin = document.getElementById('form-res-client').value;
    const plate = document.getElementById('form-res-voiture').value;
    const debut = document.getElementById('form-res-datedebut').value;
    const fin = document.getElementById('form-res-datefin').value;

    const cli = appData.clients.find(c => c.CIN === clientCin);
    const voi = appData.voitures.find(v => v.matricule === plate);

    const d0 = new Date(debut);
    const d1 = new Date(fin);
    const days = Math.round((d1 - d0) / (1000 * 60 * 60 * 24));
    const cj = voi ? voi.cout_jour : 40000;
    const montant = days > 0 ? days * cj : 0;

    const payload = {
      id: code ? parseInt(code) : undefined,
      client_cin: clientCin,
      client_nom_complet: cli ? `${cli.Prénom} ${cli.Nom}` : 'Client',
      client_prenom: cli ? cli.Prénom : '',
      client_nom: cli ? cli.Nom : '',
      client_tel: cli ? cli.Téléphone : '',
      client_email: cli ? cli.Email : '',
      voiture_matricule: plate,
      voiture_modele: voi ? voi.modele : '',
      voiture_marque: voi ? voi.marque : '',
      cout_jour: cj,
      date_debut: debut,
      date_fin: fin,
      date_debut_fr: formatDate(debut),
      date_fin_fr: formatDate(fin),
      duree_jours: days,
      montant: montant,
      en_cours: (d0 <= new Date('2026-09-28') && d1 >= new Date('2026-09-28')),
      anomalie: (days < 0)
    };

    try {
      const res = await fetch('/api/reservations', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const data = await res.json();
      if (data.success) {
        showToast('Réservation enregistrée avec succès !');
        const fresh = await fetch('/api/data');
        appData = await fresh.json();
        renderAll();
      }
    } catch (e) {
      showToast('Erreur lors de la sauvegarde');
    }
  };

  // Delete Reservation
  document.getElementById('btn-res-del').onclick = async () => {
    const code = document.getElementById('form-res-code').value;
    if (!code) return;
    if (confirm(`Voulez-vous vraiment supprimer la réservation n° ${code} ?`)) {
      try {
        const res = await fetch(`/api/reservations/${code}`, { method: 'DELETE' });
        const data = await res.json();
        if (data.success) {
          showToast(`Réservation ${code} supprimée.`);
          const fresh = await fetch('/api/data');
          appData = await fresh.json();
          currentResIndex = Math.max(0, currentResIndex - 1);
          renderAll();
        }
      } catch (e) {
        showToast('Erreur lors de la suppression');
      }
    }
  };

  // New Reservation Button
  document.getElementById('btn-res-new').onclick = () => {
    document.getElementById('form-res-code').value = '';
    document.getElementById('form-res-datedebut').value = '2026-10-01';
    document.getElementById('form-res-datefin').value = '2026-10-08';
    recalculateResAmount();
    showToast('Formulaire prêt pour une nouvelle réservation.');
  };

  // Search & Filter
  const searchInput = document.getElementById('search-reservations');
  const statusFilter = document.getElementById('filter-res-status');

  const filterTable = () => {
    const q = searchInput.value.toLowerCase();
    const st = statusFilter.value;
    const now = new Date('2026-09-28');

    const filtered = appData.reservations.filter(r => {
      const matchSearch = r.client_nom_complet.toLowerCase().includes(q) ||
                          r.voiture_matricule.toLowerCase().includes(q) ||
                          r.voiture_modele.toLowerCase().includes(q) ||
                          String(r.id).includes(q);
      if (!matchSearch) return false;

      if (st === 'all') return true;
      if (st === 'active') return r.en_cours;
      if (st === 'anomaly') return r.anomalie;
      if (st === 'past') return (new Date(r.date_fin) < now && !r.anomalie);
      if (st === 'future') return (new Date(r.date_debut) > now);
      return true;
    });

    renderReservationsTable(filtered);
  };

  searchInput.oninput = filterTable;
  statusFilter.onchange = filterTable;
}

function recalculateResAmount() {
  const debut = document.getElementById('form-res-datedebut').value;
  const fin = document.getElementById('form-res-datefin').value;
  const plate = document.getElementById('form-res-voiture').value;

  if (!debut || !fin) return;

  const d0 = new Date(debut);
  const d1 = new Date(fin);
  const diffDays = Math.round((d1 - d0) / (1000 * 60 * 60 * 24));

  const voi = appData.voitures.find(v => v.matricule === plate);
  const rate = voi ? voi.cout_jour : 40000;

  if (diffDays < 0) {
    document.getElementById('form-res-duree').value = `${diffDays} jour(s) ⚠️ Date fin < Date début`;
    document.getElementById('form-res-montant').value = '0 FCFA (Invalide)';
  } else {
    document.getElementById('form-res-duree').value = `${diffDays} jour(s)`;
    document.getElementById('form-res-montant').value = fcfa(diffDays * rate);
  }
}

// -----------------------------------------------------------------------------
// 3. Clients Module
// -----------------------------------------------------------------------------
function renderClients() {
  const clients = appData.clients;
  document.getElementById('badge-cli-count').textContent = clients.length;
  document.getElementById('lbl-cli-list-info').textContent = `${clients.length} clients`;

  loadClientToForm(currentCliIndex);
  renderClientsTable(clients);
  setupClientEvents();
}

function loadClientToForm(index) {
  const clients = appData.clients;
  if (!clients || clients.length === 0) return;

  if (index < 0) index = 0;
  if (index >= clients.length) index = clients.length - 1;
  currentCliIndex = index;

  const c = clients[index];
  document.getElementById('form-cli-cin').value = c.CIN;
  document.getElementById('form-cli-permis').value = c.NumPermis || '';
  document.getElementById('form-cli-prenom').value = c.Prénom || '';
  document.getElementById('form-cli-nom').value = c.Nom || '';
  document.getElementById('form-cli-sexe').value = c.Sexe || 'M';
  document.getElementById('form-cli-adresse').value = c.Adresse || '';
  document.getElementById('form-cli-tel').value = c.Téléphone || '';
  document.getElementById('form-cli-email').value = c.Email || '';

  document.getElementById('lbl-cli-counter').textContent = `${index + 1} sur ${clients.length}`;

  const rows = document.querySelectorAll('#tbody-clients tr');
  rows.forEach(r => {
    r.classList.remove('selected');
    if (r.dataset.cin === c.CIN) r.classList.add('selected');
  });
}

function renderClientsTable(list) {
  const tbody = document.getElementById('tbody-clients');
  tbody.innerHTML = '';

  list.slice(0, 100).forEach(c => {
    const tr = document.createElement('tr');
    tr.dataset.cin = c.CIN;
    if (c.CIN === appData.clients[currentCliIndex]?.CIN) {
      tr.classList.add('selected');
    }

    tr.innerHTML = `
      <td><strong>${c.CIN}</strong></td>
      <td>${c.NumPermis || ''}</td>
      <td>${c.Prénom}</td>
      <td>${c.Nom}</td>
      <td>${c.Sexe}</td>
      <td>${c.Adresse}</td>
      <td>${c.Téléphone}</td>
    `;

    tr.addEventListener('click', () => {
      const idx = appData.clients.findIndex(item => item.CIN === c.CIN);
      if (idx >= 0) loadClientToForm(idx);
    });

    tbody.appendChild(tr);
  });
}

function setupClientEvents() {
  document.getElementById('btn-cli-first').onclick = () => loadClientToForm(0);
  document.getElementById('btn-cli-prev').onclick = () => loadClientToForm(currentCliIndex - 1);
  document.getElementById('btn-cli-next').onclick = () => loadClientToForm(currentCliIndex + 1);
  document.getElementById('btn-cli-last').onclick = () => loadClientToForm(appData.clients.length - 1);

  document.getElementById('search-clients').oninput = (e) => {
    const q = e.target.value.toLowerCase();
    const filtered = appData.clients.filter(c => {
      return (c.Prénom && c.Prénom.toLowerCase().includes(q)) ||
             (c.Nom && c.Nom.toLowerCase().includes(q)) ||
             (c.CIN && c.CIN.toLowerCase().includes(q)) ||
             (c.Adresse && c.Adresse.toLowerCase().includes(q)) ||
             (c.Téléphone && c.Téléphone.toLowerCase().includes(q));
    });
    renderClientsTable(filtered);
  };

  // Client history modal / alert
  document.getElementById('btn-cli-view-res').onclick = () => {
    const cin = document.getElementById('form-cli-cin').value;
    const clientRes = appData.reservations.filter(r => r.client_cin === cin);
    if (clientRes.length === 0) {
      alert(`Aucune réservation enregistrée pour le client ${cin}.`);
    } else {
      let totalSpent = 0;
      let details = clientRes.map(r => {
        totalSpent += r.montant;
        return `• Réservation #${r.id} (${r.voiture_matricule} - ${r.voiture_modele}) du ${r.date_debut_fr} au ${r.date_fin_fr} : ${new Intl.NumberFormat('fr-FR').format(r.montant)} FCFA`;
      }).join('\n');
      alert(`Historique de locations pour ${cin} (${clientRes.length} réservation(s)) :\n\n${details}\n\nTotal généré : ${fcfa(totalSpent)}`);
    }
  };

  // Save client
  document.getElementById('btn-cli-save').onclick = async () => {
    const client = {
      CIN: document.getElementById('form-cli-cin').value,
      NumPermis: document.getElementById('form-cli-permis').value,
      Prénom: document.getElementById('form-cli-prenom').value,
      Nom: document.getElementById('form-cli-nom').value,
      Sexe: document.getElementById('form-cli-sexe').value,
      Adresse: document.getElementById('form-cli-adresse').value,
      Téléphone: document.getElementById('form-cli-tel').value,
      Email: document.getElementById('form-cli-email').value,
    };

    try {
      const res = await fetch('/api/clients', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(client)
      });
      const data = await res.json();
      if (data.success) {
        showToast('Client enregistré avec succès !');
        const fresh = await fetch('/api/data');
        appData = await fresh.json();
        renderAll();
      }
    } catch (e) {
      showToast('Erreur lors de la sauvegarde du client');
    }
  };
}

// -----------------------------------------------------------------------------
// 4. Voitures Module
// -----------------------------------------------------------------------------
function renderVoitures() {
  const voitures = appData.voitures;
  document.getElementById('badge-voi-count').textContent = voitures.length;
  document.getElementById('lbl-voi-list-info').textContent = `${voitures.length} véhicules`;

  loadVoitureToForm(currentVoiIndex);
  renderVoituresTable(voitures);
  setupVoitureEvents();
}

function loadVoitureToForm(index) {
  const voitures = appData.voitures;
  if (!voitures || voitures.length === 0) return;

  if (index < 0) index = 0;
  if (index >= voitures.length) index = voitures.length - 1;
  currentVoiIndex = index;

  const v = voitures[index];
  document.getElementById('form-voi-matricule').value = v.matricule;
  document.getElementById('form-voi-annee').value = v.annee;
  document.getElementById('form-voi-puissance').value = v.puissance;
  document.getElementById('form-voi-couleur').value = v.couleur;
  document.getElementById('form-voi-coutjour').value = fcfa(v.cout_jour);
  document.getElementById('form-voi-modele').value = v.modele;
  document.getElementById('form-voi-marque').value = v.marque;
  document.getElementById('form-voi-carburant').value = v.carburant;

  document.getElementById('lbl-voi-counter').textContent = `${index + 1} sur ${voitures.length}`;

  const rows = document.querySelectorAll('#tbody-voitures tr');
  rows.forEach(r => {
    r.classList.remove('selected');
    if (r.dataset.matricule === v.matricule) r.classList.add('selected');
  });
}

function renderVoituresTable(list) {
  const tbody = document.getElementById('tbody-voitures');
  tbody.innerHTML = '';

  list.forEach(v => {
    const tr = document.createElement('tr');
    tr.dataset.matricule = v.matricule;
    if (v.matricule === appData.voitures[currentVoiIndex]?.matricule) {
      tr.classList.add('selected');
    }

    let statusPill = '<span class="status-pill success">Disponible</span>';
    if (v.statut === 'En location') {
      statusPill = '<span class="status-pill warning">En location</span>';
    } else if (v.statut === 'En entretien') {
      statusPill = '<span class="status-pill danger">Entretien</span>';
    }

    tr.innerHTML = `
      <td><strong>${v.matricule}</strong></td>
      <td>${v.modele}</td>
      <td>${v.marque}</td>
      <td>${v.carburant}</td>
      <td>${v.annee}</td>
      <td>${v.couleur}</td>
      <td>${v.puissance}</td>
      <td class="num">${new Intl.NumberFormat('fr-FR').format(v.cout_jour)}</td>
      <td>${statusPill}</td>
    `;

    tr.addEventListener('click', () => {
      const idx = appData.voitures.findIndex(item => item.matricule === v.matricule);
      if (idx >= 0) loadVoitureToForm(idx);
    });

    tbody.appendChild(tr);
  });
}

function setupVoitureEvents() {
  document.getElementById('btn-voi-first').onclick = () => loadVoitureToForm(0);
  document.getElementById('btn-voi-prev').onclick = () => loadVoitureToForm(currentVoiIndex - 1);
  document.getElementById('btn-voi-next').onclick = () => loadVoitureToForm(currentVoiIndex + 1);
  document.getElementById('btn-voi-last').onclick = () => loadVoitureToForm(appData.voitures.length - 1);

  const searchInput = document.getElementById('search-voitures');
  const carbFilter = document.getElementById('filter-voi-carb');

  const filterCars = () => {
    const q = searchInput.value.toLowerCase();
    const c = carbFilter.value;
    const filtered = appData.voitures.filter(v => {
      const matchSearch = v.matricule.toLowerCase().includes(q) ||
                          v.modele.toLowerCase().includes(q) ||
                          v.marque.toLowerCase().includes(q) ||
                          v.couleur.toLowerCase().includes(q);
      if (!matchSearch) return false;
      if (c !== 'all' && v.carburant !== c) return false;
      return true;
    });
    renderVoituresTable(filtered);
  };

  searchInput.oninput = filterCars;
  carbFilter.onchange = filterCars;
}

// -----------------------------------------------------------------------------
// 5. Marques, Carburants, Modèles
// -----------------------------------------------------------------------------
function renderMarques() {
  const tbody = document.getElementById('tbody-marques');
  tbody.innerHTML = '';
  appData.marques.forEach(m => {
    const count = appData.modeles.filter(mod => mod.IdMarque === m.IdMarque).length;
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><strong>${m.IdMarque}</strong></td>
      <td><strong>${m.Marque}</strong></td>
      <td>${count} modèles catalogués</td>
    `;
    tbody.appendChild(tr);
  });
}

function renderCarburants() {
  const tbody = document.getElementById('tbody-carburants');
  tbody.innerHTML = '';
  appData.kpis.flotte_carburants.forEach((c, idx) => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><strong>${idx + 1}</strong></td>
      <td><strong>${c.type}</strong></td>
      <td>${c.voitures} véhicules</td>
      <td style="color: #2563EB; font-weight: 700;">${c.part}</td>
    `;
    tbody.appendChild(tr);
  });
}

function renderModeles() {
  const tbody = document.getElementById('tbody-modeles');
  tbody.innerHTML = '';
  appData.modeles.forEach(m => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${m.IdModele}</td>
      <td><strong>${m.Modele}</strong></td>
      <td>${m.Marque}</td>
    `;
    tbody.appendChild(tr);
  });

  document.getElementById('search-modeles').oninput = (e) => {
    const q = e.target.value.toLowerCase();
    const rows = tbody.querySelectorAll('tr');
    rows.forEach(r => {
      r.style.display = r.textContent.toLowerCase().includes(q) ? '' : 'none';
    });
  };
}

// Jump from Dashboard to specific reservation
window.jumpToReservation = function(id) {
  document.querySelector('[data-view="app"]').click();
  document.querySelector('[data-screen="reservations"]').click();
  const idx = appData.reservations.findIndex(r => r.id === id);
  if (idx >= 0) {
    loadReservationToForm(idx);
  }
};

// =============================================================================
// COMPARATOR (Mode 2)
// =============================================================================
function setupSlider() {
  const sliderBox = document.getElementById('slider-box');
  const divider = document.getElementById('slider-divider');
  const afterWrap = document.getElementById('slider-after-wrap');
  const imgAfter = document.getElementById('slider-img-after');
  
  let isDragging = false;

  function setSliderPos(x) {
    const rect = sliderBox.getBoundingClientRect();
    let pos = (x - rect.left) / rect.width;
    if (pos < 0.05) pos = 0.05;
    if (pos > 0.95) pos = 0.95;

    const pct = pos * 100;
    divider.style.left = `${pct}%`;
    afterWrap.style.width = `${pct}%`;
    imgAfter.style.width = `${rect.width}px`;
  }

  window.addEventListener('resize', () => {
    if (sliderBox) {
      const rect = sliderBox.getBoundingClientRect();
      imgAfter.style.width = `${rect.width}px`;
    }
  });

  divider.addEventListener('mousedown', () => isDragging = true);
  window.addEventListener('mouseup', () => isDragging = false);
  window.addEventListener('mousemove', (e) => {
    if (isDragging) setSliderPos(e.clientX);
  });

  // Touch support
  divider.addEventListener('touchstart', () => isDragging = true);
  window.addEventListener('touchend', () => isDragging = false);
  window.addEventListener('touchmove', (e) => {
    if (isDragging && e.touches[0]) setSliderPos(e.touches[0].clientX);
  });

  // Mode toggles
  const btnSlider = document.getElementById('btn-mode-slider');
  const btnSplit = document.getElementById('btn-mode-split');
  const sliderWrap = document.getElementById('slider-wrapper');
  const sideBySide = document.getElementById('side-by-side-box');

  btnSlider.onclick = () => {
    btnSlider.classList.add('active');
    btnSplit.classList.remove('active');
    sliderWrap.style.display = 'block';
    sideBySide.style.display = 'none';
  };

  btnSplit.onclick = () => {
    btnSplit.classList.add('active');
    btnSlider.classList.remove('active');
    sliderWrap.style.display = 'none';
    sideBySide.style.display = 'grid';
  };
}

// =============================================================================
// GALLERY (Mode 3)
// =============================================================================
function setupGallery() {
  const thumbs = document.querySelectorAll('.gallery-thumb');
  const mainImg = document.getElementById('gallery-main-img');
  const mainTitle = document.getElementById('gallery-cur-title');
  const mainDesc = document.getElementById('gallery-cur-desc');
  const rawBtn = document.getElementById('btn-open-raw-html');

  thumbs.forEach(thumb => {
    thumb.addEventListener('click', () => {
      thumbs.forEach(t => t.classList.remove('active'));
      thumb.classList.add('active');

      const img = thumb.dataset.img;
      const html = thumb.dataset.html;
      const title = thumb.dataset.title;
      const desc = thumb.dataset.desc;

      mainImg.src = img;
      mainTitle.textContent = title;
      mainDesc.textContent = desc;
      rawBtn.href = html;
    });
  });
}

// =============================================================================
// GUIDE & COTES (Mode 4)
// =============================================================================
function setupGuide() {
  const palette = [
    { name: 'Bleu Marine (Menu & Titres)', hex: '#1E3A8A' },
    { name: 'Bleu Primaire (Boutons Enregistrer)', hex: '#2563EB' },
    { name: 'Bleu Survol (Navigation)', hex: '#264796' },
    { name: 'Fond Contenu (Sous-formulaire)', hex: '#EEF2F9' },
    { name: 'Titre des Cartes (Fond)', hex: '#F2F6FD' },
    { name: 'Bordures Cartes & Traits', hex: '#D3DDEE' },
    { name: 'Fond Montant Total FCFA', hex: '#EAF1FD' },
    { name: 'Texte Montant & Titres', hex: '#1E40AF' },
    { name: 'Rouge Supprimer / Danger', hex: '#DC2626' },
    { name: 'Bordure Supprimer', hex: '#E8A5A5' },
    { name: 'Texte Principal Sombre', hex: '#111827' },
    { name: 'Texte Secondaire / Étiquettes', hex: '#4B5563' }
  ];

  const box = document.getElementById('palette-swatches-box');
  box.innerHTML = '';
  palette.forEach(p => {
    const card = document.createElement('div');
    card.className = 'palette-card';
    card.innerHTML = `
      <div class="palette-swatch" style="background: ${p.hex};"></div>
      <div class="palette-name">${p.name}</div>
      <div class="palette-hex">${p.hex}</div>
    `;
    card.onclick = () => {
      navigator.clipboard.writeText(p.hex);
      showToast(`Code couleur ${p.hex} copié dans le presse-papiers !`);
    };
    box.appendChild(card);
  });
}

function renderCotesSection(sectionName) {
  if (!appData || !appData.cotes) return;

  const select = document.getElementById('cotes-section-select');
  if (select.children.length === 0) {
    Object.keys(appData.cotes).forEach(s => {
      const opt = document.createElement('option');
      opt.value = s;
      opt.textContent = s;
      if (s === sectionName) opt.selected = true;
      select.appendChild(opt);
    });

    select.onchange = (e) => renderCotesSection(e.target.value);
  }

  const controls = appData.cotes[sectionName] || [];
  const tbody = document.getElementById('tbody-cotes');
  tbody.innerHTML = '';

  controls.forEach(ctrl => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td class="ctrl-name">${ctrl.name}</td>
      <td class="ctrl-type">${ctrl.type}</td>
      <td class="ctrl-cm">${ctrl.left} cm</td>
      <td class="ctrl-cm">${ctrl.top} cm</td>
      <td class="ctrl-cm">${ctrl.width} cm</td>
      <td class="ctrl-cm">${ctrl.height} cm</td>
    `;
    tbody.appendChild(tr);
  });

  const searchInput = document.getElementById('cotes-search-input');
  searchInput.oninput = (e) => {
    const q = e.target.value.toLowerCase();
    const rows = tbody.querySelectorAll('tr');
    rows.forEach(r => {
      r.style.display = r.textContent.toLowerCase().includes(q) ? '' : 'none';
    });
  };
}

// =============================================================================
// DATABASE EXPLORER & AUDIT (Mode 5)
// =============================================================================
function setupDbExplorer() {
  const tabBtns = document.querySelectorAll('.table-tabs-bar .table-tab-btn');
  tabBtns.forEach(btn => {
    btn.onclick = () => {
      tabBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderRawTable(btn.dataset.table);
    };
  });
}

function renderAuditCards() {
  const container = document.getElementById('audit-cards-container');
  container.innerHTML = '';
  appData.audit.forEach(item => {
    const borderClass = item.gravite === 'Haute' ? '' : (item.gravite === 'Moyenne' ? 'warning-border' : 'info-border');
    const card = document.createElement('div');
    card.className = `audit-item-card ${borderClass}`;
    card.innerHTML = `
      <div class="audit-header">
        <h4>${item.id} · ${item.titre}</h4>
        <span class="status-pill ${item.gravite === 'Haute' ? 'danger' : 'warning'}">Gravité ${item.gravite}</span>
      </div>
      <div class="audit-desc"><strong>Impact :</strong> ${item.impact}</div>
      <div class="audit-desc">${item.detail}</div>
      <div class="audit-code-box">Solution SQL : ${item.solution_sql}</div>
      <div class="audit-status" style="color: ${item.statut.includes('✅') ? '#4ADE80' : '#FBBF24'};">
        ${item.statut}
      </div>
    `;
    container.appendChild(card);
  });
}

function renderRawTable(tableName) {
  const thead = document.getElementById('db-raw-thead');
  const tbody = document.getElementById('db-raw-tbody');
  thead.innerHTML = '';
  tbody.innerHTML = '';

  let list = [];
  if (tableName === 'Client') list = appData.clients;
  else if (tableName === 'Reservation') list = appData.reservations;
  else if (tableName === 'Voiture') list = appData.voitures;
  else if (tableName === 'Modele') list = appData.modeles;
  else if (tableName === 'Marque') list = appData.marques;
  else if (tableName === 'Carburant') list = appData.carburants;

  if (list.length === 0) return;

  const cols = Object.keys(list[0]);
  const trHead = document.createElement('tr');
  cols.forEach(col => {
    const th = document.createElement('th');
    th.textContent = col;
    trHead.appendChild(th);
  });
  thead.appendChild(trHead);

  list.slice(0, 50).forEach(row => {
    const tr = document.createElement('tr');
    cols.forEach(col => {
      const td = document.createElement('td');
      td.textContent = row[col] !== undefined ? row[col] : '';
      tr.appendChild(td);
    });
    tbody.appendChild(tr);
  });
}

// =============================================================================
// ASSETS & PHOTOS VIEW (Mode 6)
// =============================================================================
function setupAssetsView() {
  const photos = [
    { name: 'bandeau-tableau.jpg', title: 'Bandeau Tableau de bord', desc: 'Flotte de véhicules sous voile bleu marine (1300 × 128 px)' },
    { name: 'bandeau-reservations.jpg', title: 'Bandeau Réservations', desc: 'Remise de clés de voiture (1300 × 92 px)' },
    { name: 'bandeau-clients.jpg', title: 'Bandeau Clients', desc: 'Accueil et relation client (1300 × 92 px)' },
    { name: 'bandeau-voitures.jpg', title: 'Bandeau Voitures', desc: 'Showroom automobile (1300 × 92 px)' },
    { name: 'bandeau-marques.jpg', title: 'Bandeau Marques', desc: 'Calandres et logos constructeurs (1300 × 92 px)' },
    { name: 'bandeau-carburants.jpg', title: 'Bandeau Carburants', desc: 'Station-service et pistolet pompe (1300 × 92 px)' },
    { name: 'bandeau-modeles.jpg', title: 'Bandeau Modèles', desc: 'Habitacle et tableau de bord moderne (1300 × 92 px)' },
    { name: 'menu-fond.jpg', title: 'Fond du Menu Latéral', desc: 'Route côtière de nuit à Libreville (220 × 784 px)' },
    { name: 'login-photo.jpg', title: 'Photo de Connexion', desc: 'Front de mer de Libreville et SUV (420 × 500 px)' }
  ];

  const photosBox = document.getElementById('assets-photos-box');
  photosBox.innerHTML = '';
  photos.forEach(p => {
    const card = document.createElement('div');
    card.className = 'asset-card';
    card.innerHTML = `
      <div class="asset-img-thumb">
        <img src="/assets/photos/${p.name}" alt="${p.title}" loading="lazy">
      </div>
      <div class="asset-card-info">
        <h5>${p.title}</h5>
        <p>${p.desc}</p>
        <a href="/assets/photos/${p.name}" target="_blank" style="font-size: 11px; color: #38BDF8; text-decoration: none; display: inline-block; margin-top: 6px;">
          Télécharger le fichier original &rarr;
        </a>
      </div>
    `;
    photosBox.appendChild(card);
  });

  const icons = [
    'bouton-plus.png', 'bouton-enregistrer.png', 'bouton-supprimer.png', 'bouton-search.png',
    'bouton-refresh-cw.png', 'bouton-printer.png', 'bouton-power.png',
    'bouton-chevron-first.png', 'bouton-chevron-left.png', 'bouton-chevron-right.png', 'bouton-chevron-last.png',
    'indicateur-wallet.png', 'indicateur-car-front.png', 'indicateur-users.png', 'logo-voiture.png',
    'menu-layout-dashboard.png', 'menu-calendar-range.png', 'menu-users.png', 'menu-car.png',
    'menu-tag.png', 'menu-fuel.png', 'menu-layers.png'
  ];

  const iconsBox = document.getElementById('assets-icons-box');
  iconsBox.innerHTML = '';
  icons.forEach(ico => {
    const card = document.createElement('div');
    card.className = 'icon-card';
    card.innerHTML = `
      <div class="icon-thumb">
        <img src="/assets/${ico}" alt="${ico}">
      </div>
      <div class="icon-name">${ico}</div>
    `;
    iconsBox.appendChild(card);
  });
}

// Run when DOM is ready
document.addEventListener('DOMContentLoaded', initApp);
