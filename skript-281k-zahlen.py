def fv(rate_monthly, months, pmt):
    r = rate_monthly
    return pmt * (((1+r)**months - 1) / r)

r = 0.07/12
p = 200

v40 = fv(r, 480, p)
v30 = fv(r, 360, p)
print(f"200 EUR/Monat, 7% p.a.")
print(f"  40 Jahre (Start mit 25): {v40:,.0f} EUR   eingezahlt: {200*480:,} EUR")
print(f"  30 Jahre (Start mit 35): {v30:,.0f} EUR   eingezahlt: {200*360:,} EUR")
print(f"  DIFFERENZ: {v40-v30:,.0f} EUR")
print(f"  Mehr eingezahlt: nur {200*480 - 200*360:,} EUR")
print(f"  -> pro 1 EUR extra eingezahlt: {(v40-v30)/(200*120):,.2f} EUR mehr am Ende")
print()

# Was passiert in den einzelnen Dekaden? Wertzuwachs pro Jahrzehnt (40-Jahre-Fall)
print("Wertzuwachs je Jahrzehnt (40-Jahre-Sparplan):")
prev = 0
for dec in range(1,5):
    v = fv(r, dec*120, p)
    print(f"  Jahrzehnt {dec} (Jahr {(dec-1)*10+1}-{dec*10}): Depot waechst um {v-prev:,.0f} EUR  -> Stand {v:,.0f} EUR")
    prev = v
print()

# Letztes Jahrzehnt vs erste 20 Jahre
zuwachs_letztes = fv(r,480,p) - fv(r,360,p)
zuwachs_erste20 = fv(r,240,p)
print(f"  Letzte 10 Jahre bringen:  {zuwachs_letztes:,.0f} EUR")
print(f"  Erste 20 Jahre bringen:   {zuwachs_erste20:,.0f} EUR")
print(f"  -> letztes Jahrzehnt = {zuwachs_letztes/zuwachs_erste20:.2f}x der ersten 20 Jahre")
print()

# Aufholen: welche Rate braucht der Spaetstarter (30 J) fuer 525k?
needed = v40 / (((1+r)**360 - 1)/r)
print(f"Aufholen mit hoeherer Rate:")
print(f"  Spaetstarter braucht {needed:,.0f} EUR/Monat statt 200 EUR, um dasselbe zu erreichen")
print(f"  = {needed/200:.2f}x so viel, also +{needed-200:,.0f} EUR jeden Monat")
print()

# Hebel-Vergleich: +10 Jahre Zeit vs +100 EUR Rate vs +1% Rendite (jeweils ab 30-Jahre-Basis)
base = fv(r,360,200)
print(f"Hebel-Vergleich (Basis: 30 Jahre, 200 EUR, 7% = {base:,.0f} EUR):")
print(f"  +10 Jahre Zeit    -> {fv(r,480,200):,.0f} EUR  (+{fv(r,480,200)-base:,.0f})")
print(f"  +100 EUR Rate     -> {fv(r,360,300):,.0f} EUR  (+{fv(r,360,300)-base:,.0f})")
print(f"  +1% Rendite (8%)  -> {fv(0.08/12,360,200):,.0f} EUR  (+{fv(0.08/12,360,200)-base:,.0f})")
print()

# Realitaetscheck: Inflation 2% -> Kaufkraft der 525k in 40 Jahren
infl = 0.02
print(f"Realitaetscheck:")
print(f"  525.020 EUR in 40 Jahren = heutige Kaufkraft von {v40/((1+infl)**40):,.0f} EUR (bei 2% Inflation)")
print(f"  281.023 EUR Differenz    = heutige Kaufkraft von {(v40-v30)/((1+infl)**40):,.0f} EUR")
