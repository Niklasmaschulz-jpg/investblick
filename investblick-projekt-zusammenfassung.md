# InvestBlick – Projekt-Zusammenfassung

Kompletter Überblick über alle Entscheidungen, Funktionen und Bausteine. Zum Nachschlagen.

---

## 1. Was ist InvestBlick?
Ein kostenloses, werbefreies **Info- und Bildungs-Tool** für Einsteiger: Sparpläne durchrechnen, Dividenden/Aktien/ETFs verstehen, Live-Charts ansehen. **Keine Anlageberatung** – überall klar gekennzeichnet.

- **Live-Adresse:** https://investblick-nms.netlify.app
- **Hosting:** Netlify (kostenlos, per Ordner-Upload / „Deploys")
- **Technik:** eine einzige `index.html` (alles in einer Datei), plus Hilfsdateien
- **Betreiber (Impressum):** Niklas Schulz, Waldstr. 28, 24939 Flensburg, Niklas.ma.schulz@gmail.com

---

## 2. Funktionen der App (alle Tabs)
- **Start:** Übersicht + „Erste Schritte"-Onboarding.
- **ETFs / Aktien:** getrennte Listen (strikt getrennt), mit Ø Rendite, Dividende, Schwankung, Risikoklasse; **Stern-Favoriten** + Filter (Alle / Dividende ≥3 % / Defensiv / ★ Favoriten). ~111 Werte inkl. Themen-ETFs (AI & Big Data, Halbleiter, Cyber, Cloud …).
- **Sparplan-Rechner:** Sparrate + Laufzeit → Endwert, Gewinn, Dividende, Risiko, Wahrscheinlichkeiten. Extras: **dynamische Sparrate** (jährlich erhöhen), **Tagesgeld-Vergleich**, **Monte-Carlo-Simulation** (500 Zufallsverläufe), **„Nach Steuern & Kosten"** (Abgeltungssteuer + TER, vereinfacht).
- **Mein Portfolio:** mehrere Werte kombinieren, speichern/laden.
- **Beispiele:** fertige Misch-Portfolios in **4 Sicherheitsstufen** + Mix-Kategorie (riskant & sicher kombiniert); Sparbetrag eingeben → Ergebnis je Karte.
- **Ziel-Rechner:** Zielbetrag → nötige Monatsrate.
- **Entnahmeplan:** wie lange reicht das Vermögen / 4-%-Regel.
- **Vergleich:** zwei Werte nebeneinander mit gemeinsamem Chart.
- **Live-Charts:** Top-Mover + große Märkte (via TradingView).
- **Aktien-Suche:** praktisch jeder Wert weltweit, mit Autovervollständigung.
- **Ratgeber & FAQ:** Einsteiger-Fragen + Artikel.
- **Hilfe-Assistent:** Chat-Button unten rechts, **39 vorbereitete Fragen/Antworten** (Grundlagen, ETFs, Aktien, Risiko, Steuern, Bedienung) + Stichwortsuche.
- **Teilen/Export:** Ergebnis-Link kopieren, **als Bild speichern**, **als PDF speichern**.
- **Umschalter:** Hell/Dunkel, **Historisch ↔ Experten-Prognose** (Datenbasis).

---

## 3. Wichtige Produkt-/Design-Entscheidungen
- **Statistik statt „Vorhersage":** Ergebnisse als **≈ Schätzung mit Spanne**, keine punktgenauen Versprechen.
- **Rendite berechnet das System** (nicht der Nutzer): historischer Durchschnitt bzw. Experten-CMA (J.P. Morgan, Vanguard, BlackRock, Morningstar 2026). US ~6 %, Welt ~7 %, EM ~8,5 %, Anleihen ~4,3 %.
- **Risikoklasse 1–7** nach EU-Standard (aus Schwankung).
- **Menü aufgeräumt:** Gruppen-Dropdowns „Rechner ▾" / „Entdecken ▾".
- **Design:** Apple-/Lean-Look, **einfarbige Icons statt Emojis**.
- **Barrierefreiheit:** Tastaturbedienung, Fokus-Markierung, vorlesbare Tooltips, „Bewegung reduzieren", Barrierefreiheitserklärung (BFSG).
- **Eingabe-Absicherung:** keine negativen/absurden Werte.

---

## 4. Rechtliches (in App und Handbüchern)
- **Zustimmungs-Gate** beim ersten Besuch („keine Anlageberatung" akzeptieren).
- **Cookie-Hinweis**; TradingView-Charts laden **erst nach Zustimmung** (DSGVO-Fix).
- **Impressum** (§ 5 DDG, mit Adresse), **Datenschutzerklärung**, **Haftungsausschluss**, **Über/Kontakt**.
- Überall Hinweis „keine Anlageberatung, ohne Gewähr".
- **Hinweis:** Vorlagen; für echten Dauerbetrieb im Zweifel rechtlich prüfen lassen.

---

## 5. Analyse & Admin
- **Besucherzählung:** GoatCounter (cookielos, DSGVO-freundlich). **Code: `investblicknms`** → Dashboard: https://investblicknms.goatcounter.com
- **Versteckter Admin-Bereich:** Logo 5× klicken oder Adresse mit `#admin`; **Zugangscode: `nms`** (im Datei-Code änderbar; nur Sichtschutz, keine echte Sicherheit). Zeigt lokale Nutzungszahlen + Gesamt-Aufrufe (GoatCounter).

---

## 6. Die zwei Handbücher (eigene Unterseiten)
Ausführliche, durchsuchbare Einsteiger-Handbücher mit Themen-Navigation, Zustimmungs-Gate und komplettem Rechts-Teil:
- **ETF-Handbuch:** Ordner `investblicknmsetf/` (26 Kapitel).
- **Aktien-Handbuch:** Ordner `investblicknmsaktien/` (21 Kapitel).
- Auf der Startseite von InvestBlick verlinkt (2 Karten + Footer); gegenseitig verlinkt.
- Live-Adressen nach Upload: `…netlify.app/investblicknmsetf/` und `…/investblicknmsaktien/`.
- **Steuerfakten geprüft:** Abgeltungssteuer 25 % + Soli ≈ 26,375 %, Teilfreistellung 30 % bei Aktien-ETFs, Sparerpauschbetrag 1.000 €, Vorabpauschale (Basiszins 2025: 2,53 %).

---

## 7. Veröffentlichung & SEO
- **Upload:** ganzen `investblick`-Ordner (inkl. Unterordner) bei Netlify unter „Deploys" reinziehen; danach Strg+F5.
- **Startdatei muss `index.html` heißen.**
- **Google Search Console:** bestätigt (HTML-Datei `googledf03ecc33f6455a5.html`), **Sitemap** eingereicht (`sitemap.xml`, enthält auch die beiden Handbücher), `robots.txt` + strukturierte Daten (JSON-LD) vorhanden.
- **Teilen-Vorschau (Open Graph)** + Favicon vorhanden.
- **PWA:** installierbar, Grundansicht offline.

---

## 8. Marketing / Social Media / Videos
- **Social-Media-Plan** erstellt (`social-media-plan-investblick.md`): TikTok/Reels/Shorts, 3–4 Videos/Woche, 4-Wochen-Kalender, Hooks, Hashtags.
- **TikTok-Skripte** (`tiktok-skripte-investblick.md`): 5 fertige Skripte.
- **Logo** in mehreren Varianten (Icon, Schriftzug, transparent) + **HeyGen-Hintergrund** (9:16).
- **Video-Workflow (faceless):** Skript → Stimme bei **ElevenLabs** (deine geklonte Stimme) → Bild via **eigener Screen-Aufnahme** oder **Kling** → Zusammenbau in **ffmpeg** (durch mich) oder **CapCut** (durch dich, gratis, ohne Wasserzeichen).
- **Video 1 ist FERTIG:** `video-1-fertig.mp4` (deine Stimme + Screen-Clip, endet auf ≈101.722 €). Direkt hochladbar.
- **Kling:** Gratis-Warteschlange war blockiert (Upsell) → aktuell nicht genutzt; Empfehlung: eigene Screen-Clips bevorzugen. HeyGen im Gratis-Plan = Wasserzeichen (nur mit Abo weg).

---

## 9. Dateien im `investblick`-Ordner
**Website:** `index.html`, `manifest.webmanifest`, `sw.js`, `sitemap.xml`, `robots.txt`, `googledf03ecc33f6455a5.html`, Bilder (`icon-192/512`, `apple-touch-icon`, `share-preview`).
**Handbücher:** `investblicknmsetf/index.html`, `investblicknmsaktien/index.html`.
**Marketing/Assets (nicht Teil der Website nötig):** Logos, `heygen-hintergrund.png`, komprimierte Screen-Clips, `video-1-fertig.mp4`.

---

## 10. Wichtige Zugänge / Merkzettel
| Was | Wert |
|---|---|
| Live-Seite | investblick-nms.netlify.app |
| Admin-Code | `nms` (Logo 5× klicken oder `#admin`) |
| GoatCounter-Code | `investblicknms` |
| GoatCounter-Dashboard | investblicknms.goatcounter.com |
| Google-Bestätigungsdatei | googledf03ecc33f6455a5.html |

---

## 11. Offene Punkte / mögliche nächste Schritte
- Impressum/Datenschutz vor Dauerbetrieb **fachlich prüfen** lassen.
- **Eigene Domain** (z. B. investblick.de, ~10 €/Jahr) später auf Netlify legen – dann alle Adressen (Sitemap, OG, GoatCounter, Handbuch-Links) umstellen.
- **Manueller Handy-/Screenreader-Test** der Live-Seite.
- Optional: echte KI (statt Regel-Assistent), Cloud-Konten, englische Version, Affiliate/Abo/Werbung (mit Kennzeichnung + Datenschutz).
- **Monetarisierung:** braucht zuerst Reichweite; TikTok Creator Rewards ab 10.000 Followern + 100.000 Views/30 Tage.

---

*Alle Berechnungen sind statistische Schätzungen. Keine Anlageberatung. Angaben ohne Gewähr, Stand 2025/2026.*
