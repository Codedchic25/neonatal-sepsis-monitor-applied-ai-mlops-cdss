# 🩺 Sepsis Monitor AI – Interview Defense Manual

## 📂 Section 1 – Project Overview

### 1. Tell me about your project?
**Answer**
Sepsis Monitor AI este un sistem neonatal de suport decizional clinic (CDSS) bazat pe o arhitectură securizată de tip **Defense-in-Depth**. Acesta decuplează complet logica medicală deterministă de stratul non-determinist de Inteligență Artificială (LLM sandboxed). Platforma monitorizează telemetria fiziologică în timp real printr-un dashboard Streamlit, rulează calcule farmaceutice precise, generează rapoarte clinice bilingve și validează securitatea prompt-urilor prin teste automate MLOps.

---

### 2. Why did you build this project?
**Answer**
Scopul a fost să demonstrez cum se pot integra în siguranță modelele LLM în medii medicale cu risc critic, eliminând complet riscul de halucinație sau manipulare a instrucțiunilor. Proiectul îmi consolidează tranziția de la background-ul clinic direct către ingineria software și AI, aplicând bune practici de backend (SQLAlchemy, Alembic), securitate cibernetică (Promptfoo) și automatizare CI/CD (GitHub Actions).

---

### 3. What problem does the project solve?
**Answer**
Rezolvă problema vulnerabilității sistemelor AI clasice în medicină prin implementarea unui control determinist: algoritmul Python dictează diagnosticul, stadiile AKI și dozele, iar AI-ul este limitat strict la analiză contextuală, traducere și comunicare structurată, fără dreptul de a modifica datele clinice brute.

---

### 4. Who are the intended users?
**Answer**
Platforma simulează fluxul operațional complet dintr-o unitate de terapie intensivă neonatală (NICU). Implementează o arhitectură ierarhică de **Role-Based Access Control (RBAC)** ce restricționează accesul la interfață pentru 5 profiluri profesionale: Șef de Secție (acces total + suite MLOps), Medic Specialist, Medic de Gardă, Medic Rezident și Asistent Șef NICU.

---

### 5. Why is neonatal sepsis important?
**Answer**
Sepsisul neonatal este o urgență medicală majoră și o cauză principală de mortalitate infantilă globală. Identificarea timpurie a instabilității fiziologice și corelarea cineticii biomarkerilor (CRP și PCT) în primele ore sunt critice pentru supraviețuirea nou-născutului.

---

## 🏗 Section 2 – Architecture

### 6. Describe the system architecture.
**Answer**
Aplicația implementează o arhitectură hibridă, decuplată, optimizată pentru **Fail-Safe Locality**. Aceasta integrează un strat de prezentare Streamlit, un framework de telemetrie operațională, motoare de reguli deterministe în Python, un wrapper AI izolat (Groq/Llama-3.1) și o infrastructură tranzacțională ce folosește SQLAlchemy ORM și Alembic pentru persistența datelor într-un fișier local SQLite (PostgreSQL-ready).

---

### 7. Why did you choose a modular architecture?
**Answer**
Pentru a asigura **Separation of Concerns** (Separarea Responsabilităților). Împărțirea codului în module independente (`src/brain`, `src/services`, `src/database`) permite testarea izolată a fiecărei componente, previne contaminarea contextului și asigură scalabilitatea ulterioară fără a afecta nucleul determinist al aplicației.

---

### 8. What are the main architectural layers?
**Answer**
- **Presentation Layer:** Interfața reactivă Streamlit UI.
- **Business Logic Layer:** Serviciile Python de procesare a telemetriei și simularea AKI (Acute Kidney Injury).
- **AI Services Layer:** Orchestrarea prompt-urilor și parsarea contractelor structurate XML.
- **Persistence Layer:** Modelele declarative SQLAlchemy și baza de date SQLite.
- **Validation & Testing Layer:** Suitele automate de testare Pytest și Promptfoo regression gates.

---

### 9. What is Separation of Concerns?
**Answer**
Este principiul architectural conform căruia fiecare componentă are o singură responsabilitate bine definită. UI-ul se ocupă doar de prezentare, serviciile backend rulează logica medicală, iar modelele bazei de date gestionează persistența, facilitând o mentenanță curată.

---

### 10. Why is modularity important?
**Answer**
Modularitatea permite dezvoltarea independentă a componentelor și izolarea erorilor. Dacă API-ul extern de LLM devine indisponibil, nucleul determinist, calculele de dozaj și alertele locale continuă să funcționeze intact, asigurând reziliența sistemului.

---

## 🖥 Section 3 – Streamlit Dashboard

### 11. Why did you choose Streamlit?
**Answer**
Streamlit a permis dezvoltarea rapidă a unei interfețe medicaler reactive și complet interactive utilizând exclusiv cod nativ Python, eliminând complexitatea managementului de stări din framework-urile frontend tradiționale.

---

### 12. What are Streamlit's advantages?
**Answer**
- Prototipare ultra-rapidă și dezvoltare nativă în Python.
- Dashboards interactive cu reîmprospătare reactivă automată.
- Management simplificat al stărilor sesiunii prin `st.session_state`.
- Reducerea la zero a complexității codului de frontend (HTML/JavaScript).

---

### 13. What are Streamlit's limitations?
**Answer**
Fiecare interacțiune a utilizatorului reexecută scriptul de la început, ceea ce poate genera ineficiențe la volume masive de date dacă nu se folosește caching-ul corect. De asemenea, oferă un control limitat asupra personalizării avansate de CSS.

---

### 14. How does Streamlit update the UI?
**Answer**
Prin reexecutarea completă a scriptului Python de sus în jos de fiecare dată când o valoare (widget, slider, buton) este modificată în interfață, redesenând elementele pe baza noilor stări salvate în sesiune.

---

### 15. What are the key visual components of your dashboard?
**Answer**
- **Sidebar Configuration Panel:** Selector dinamic de limbă, ierarhie RBAC și parametri neonatali.
- **Real-Time Vital Parameters Grid:** Senzori vizuali colorați (coduri de alertă) pentru vitale (HR, Temp, SpO2).
- **Individualized Dose Calculation Panel:** Panel determinist izolat pentru protocoalele de antibiotice.
- **Integrated Audio Neurodevelopmental Player:** Simulator audio asincron pentru bătăile de inimă materne.
- **Active AI Decision Support Tabs:** Randează separat secțiunile validate XML (`<RAPORT>`, `<MEDICATIE>`, `<FCC>`).

---

## 🏥 Section 4 – Clinical Workflow

### 16. What telemetry parameters are monitored?
**Answer**
Sistemul procesează parametri fiziologici critici: Frecvența Cardiacă (HR), Temperatura, Saturația de Oxigen (SpO2), Tensiunea Arterială Medie, alături de valorile serice ale biomarkerilor inflamatori: Proteina C-Reactivă (CRP) și Procalcitonina (PCT).

---

### 17. Why is CRP important?
**Answer**
Proteina C-Reactivă este un biomarker sintetizat de ficat ca răspuns la stimuli infecțioși. Deși are o dinamică mai lentă (crește în 12-24 de ore), monitorizarea curbei sale este esențială pentru evaluarea răspunsului la antibioterapie.

---

### 18. Why is PCT important?
**Answer**
Procalcitonina este un biomarker timpuriu, înalt specific pentru infecțiile bacteriene sistemice severe și sepsis, înregistrând o creștere rapidă în primele 2-4 ore de la stimul.

---

### 19. What is considered a high-risk sepsis state?
**Answer**
Algoritmul determinist clasifică pacientul în **Protocol de Risc Critic** dacă valorile biologice depășesc pragurile stricte: **PCT ≥ 2.0 ng/mL** SAU **CRP ≥ 10.0 mg/L**, activând instantaneu schemele de intervenție de urgență.

---

### 20. What is considered a stable state?
**Answer**
Un nou-născut este considerat biochimic stabil când ambele condiții sunt îndeplinite simultan: **PCT < 0.5 ng/mL** ȘI **CRP < 5.0 mg/L**. Dacă orice parametru este încălcat, sistemul ocolește API-urile externe dependente de internet (precum Twilio) pentru a elimina riscul de *data leakage* și defectele de rețea. În schimb, declanșează un workflow de **CRITICAL ALERT** rutat direct în log-urile terminalului de fundal prin *Secured Runtime Logging*.

---

## 💊 Section 5 – Medication Engine

### 21. Why automate dosage calculations?
**Answer**
Automatizarea elimină complet erorile umane de calcul manual, care în neonatologie pot fi fatale din cauza indicelui terapeutic extrem de îngust al antibioticelor.

---

### 22. How is Ampicillin calculated?
**Answer**
Urmează protocolul clinic standard: **100 mg / kg corp / zi**, divizată în două prize administrate la interval strict de 12 ore. Matematica este executată rigid în codul Python nativ.

---

### 23. How is Gentamicin calculated?
**Answer**
Este calculată pe bază de masă corporală: **4 mg / kg corp / zi**, administrată ca doză unică zilnică (la 24 de ore), monitorizându-se constant funcția renală pentru a preveni oto- și nefrotoxicitatea.

---

### 24. Why use weight-based dosing?
**Answer**
Deoarece volumul de distribuție și rata de filtrare glomerulară la nou-născuți variază masiv și direct proporțional cu greutatea lor exprimată în grame, necesitând o personalizare milimetrică a dozelor.

---

### 25. What is the purpose of renal monitoring?
**Answer**
Identifică stadiile de Insuficiență Renală Acută (AKI - Mild sau Severe) bazate pe diureză și retenția de fluide. În caz de stadiu AKI Sever, sistemul modifică schema de administrare și blochează intervalele standard ca o barieră critică de siguranță farmacologică.

---

## 🧸 Section 6 – Family-Centered Care

### 26. What is Family-Centered Care?
**Answer**
Este o abordare terapeutică holistică ce recunoaște importanța nucleului familial în procesul de vindecare al nou-născutului, integrând părinții direct în fluxul de îngrijire din NICU pentru a sprijini neurodezvoltarea.

---

### 27. Why include Kangaroo Care?
**Answer**
Terapia Kangaroo (contactul piele-pe-piele) stabilizează clinic ritmul cardiac, îmbunătățește reglarea termică, reduce episoadele de apnee și scade nivelul de stres cortizolic al prematurului.

---

### 28. Why include Music Therapy?
**Answer**
Expunerea controlată la stimuli auditivi simulați (cum ar fi bătăile de inimă maternă integrate în player-ul asincron al dashboard-ului) reduce hiperexcitabilitatea neurologică și sprijină maturizarea cortexului auditiv.

---

### 29. How is FCC integrated into the system?
**Answer**
Indicatorii calitativi și cantitativi de FCC (minute de contact, sesiuni audio) sunt înregistrați în baza de date locală și pasați ca text securizat către LLM pentru a fi sintetizați într-o secțiune dedicată din raportul final.

---

### 30. Why track non-pharmacological interventions?
**Answer**
Deoarece prognosticul neurologic pe termen lung al unui prematur depinde în mod egal de eradicarea infecției prin antibiotice și de protecția mediului senzorial prin protocoale neurodezvoltamentale.

---

## 🤖 Section 7 – Artificial Intelligence

### 31. What is the role of AI in this project?
**Answer**
Rolul LLM-ului este exclusiv de interpretare contextuală, traducere bilingvă instantanee și generare de narațiuni clinice sintetizate. AI-ul acționează ca un asistent de comunicare, fiind complet izolat de zona deciziilor de diagnostic sau a calculelor matematice de dozaj.

---

### 32. Does AI make diagnoses?
**Answer**
Nu. Sistemul AI nu pune diagnostice și nu decide tratamente. El preia diagnosticul gata stabilit de logica deterministă Python și îl traduce într-o formă structurată, respectând un disclaimer legal strict.

---

### 33. Why use structured outputs?
**Answer**
Pentru a garanta că răspunsul generat de un model fundamental non-determinist poate fi parsat programatic de către aplicație fără erori, eliminând riscul ca AI-ul să returneze text liber sau Markdown invalid.

---

### 34. What output format is used?
**Answer**
Sistemul impune un contract structural rigid prin etichete XML personalizate: Răspunsul LLM-ului trebuie să conțină exclusiv blocurile `<RAPORT>`, `<MEDICATIE>` și `<FCC>`. Orice deviere în afara acestor tag-uri este respinsă de stratul de validare post-inferență.

---

### 35. Why is structured output important?
**Answer**
Permite validarea deterministă și testarea automată a datelor, asigurându-ne că nicio componentă de text generată de AI nu sparge structura bazei de date sau interfața utilizatorului.

---

### 36. How do you ensure the stability of these clinical logic overrides during updates?
**Answer**
Aplicația rulează sub o poartă de calitate MLOps severă: **17 / 17 de teste Pytest automate trecute cu succes** (ce acoperă calculele medicale, stadiile AKI și tranzacțiile bazei de date) combinate cu o matrice de **9 / 9 scenarii Promptfoo** care verifică automat rezistența la atacuri cibernetice și conformitatea tag-urilor XML.

  ## 🪤 Section 14 – Adversarial & Edge-Case Engineering (Intrebari Capcana)

### 37. Daca sistemul este 100% offline si izolat local, cum mai faci inferenta LLM prin Groq/Llama-3.1, din moment ce Groq necesita un API cloud extern? Nu este asta o contradictie in arhitectura ta?
**Answer**
Nu este o contradicție, ci o delimitare strictă a nivelurilor de risc critic (**Criticality Zoning**). Nucleul determinist al aplicației (calculele matematice, stadiile AKI, baza de date locală SQLite și alertele de urgență din consolă) funcționează complet izolat și offline, având dependență zero de internet. API-ul cloud Groq este utilizat exclusiv ca un serviciu asincron de optimizare și traducere pentru interfață. Dacă internetul pică complet, stratul AI devine indisponibil, dar sistemul CDSS continuă să ruleze stabil pe mașina locală, protejând viața pacientului prin afișarea dozelor corecte calculate în Python și declanșarea alertelor locale.

---

### 38. De ce ai ales SQLite pentru un proiect ce se doreste a fi enterprise-grade in mediul medical? SQLite nu suporta concurenta masiva la scriere (sufera de database locking).
**Answer**
SQLite a fost ales strategic ca o bază de date embedded pentru a demonstra principiul **Fail-Safe Locality** (autonomie completă pe un singur terminal medical de tip Edge Device, aflat fizic lângă incubator). Într-un scenariu real din NICU, fiecare monitor are propriul runtime izolat pentru a preveni un colaps generalizat al rețelei spitalului. Cu toate acestea, pentru a asigura scalabilitatea enterprise, am utilizat **SQLAlchemy ORM** și **Alembic**. Întregul backend este complet agnostic de baza de date: pentru a trece la un model centralizat cu mii de scrieri concurente, este suficientă schimbarea unei singure linii de cod (Connection String-ul) pentru a migra instantaneu pe un cluster PostgreSQL, fără a modifica nicio interogare din aplicație.

---

### 39. Daca un medic introduce un comentariu legitim, dar foarte lung si complex, cum te asiguri ca sistemul tau de aparare (Prompt Injection Defense) nu il clasifica gresit ca fiind un atac (False Positive) si blocheaza raportul?
**Answer**
Pentru a evita falsurile pozitive, sistemul nu se bazează pe blocarea simplistă a cuvintelor cheie. Textul introdus de medic este încapsulat în mod imuabil în interiorul unor tag-uri XML structurate (`<COMENTARIU_MEDIC>`). Layer-ul de analiză nu încearcă să modifice sau să cenzureze textul medicului, ci instruiește modelul prin meta-prompting riguros să trateze conținutul acelei etichete strict ca date de analizat (Data Plane), nu ca instrucțiuni de executat (Control Plane). În plus, suita de teste **Promptfoo** rulează scenarii specifice de text medical complex pentru a calibra barierele de securitate, asigurându-ne că doar payload-urile care încearcă în mod explicit să suprascrie comportamentul LLM-ului sunt neutralizate.

---

### 40. De ce ai folosit Streamlit pentru o aplicatie medicala critica? Streamlit reexecuta intregul script de sus in jos la fiecare interactiune, ceea ce este extrem de ineficient si poate duce la pierderi de performanta (lag) in timp real.
**Answer**
Streamlit a fost selectat ca un mediu de prototipare rapidă pentru a demonstra logica backend și pipeline-ul MLOps într-o interfață grafică funcțională. Pentru a combate ineficiența reexecuției, am implementat un management agresiv de stări prin **`st.session_state`** și am optimizat interogările bazei de date. Procesarea telemetriei grele și calculele clinice sunt decuplate în servicii Python pure, ceea ce înseamnă că logica de business rulează la viteză nativă. Într-o faza ulterioară de producție, prezentarea poate fi înlocuită cu un frontend dedicat în React sau Angular, însă nucleul arhitectural expus în acest proiect (serviciile, baza de date, securitatea și porțile MLOps) va rămâne complet neschimbat.

---

### 41. Ce se intampla daca baza de date SQLite locala se corupe in timpul unei scrieri tranzactionale din cauza unei pene de curent? Cum garantezi integritatea datelor pacientului?
**Answer**
Integritatea este garantată prin design-ul tranzacțional al bazei de date gestionat de SQLAlchemy, care operează sub reguli stricte **ACID**. SQLite folosește un mecanism nativ de tip *Rollback Journal* sau *WAL (Write-Ahead Logging)*. Dacă o scriere este întreruptă brutal la jumătate de o pană de curent, sistemul nu lasă datele într-o stare parțială sau coruptă. La următoarea repornire a aplicației, motorul bazei de date detectează automat tranzacția neterminată și face un rollback complet la ultima stare stabilă validă, asigurând că istoricul clinic și dozele rămân consistente din punct de vedere matematic.

## 🎯 Section 15 – Advanced Technical Blitz (Intrebari 42 - 50)

### 42. Cum gestionezi concurența în Streamlit dacă mai mulți utilizatori accesează dashboard-ul simultan?
**Answer**
Streamlit rulează nativ ca un server Flask/Tornado asincron și creează un thread izolat pentru fiecare sesiune de browser. Fiecare utilizator are propriul său `st.session_state` complet separat, ceea ce înseamnă că interacțiunile unui medic nu vor polua sau bloca stările sesiunii altui coleg.

---

### 43. De ce folosești SQLAlchemy ORM în loc de conexiuni brute cu `sqlite3`?
**Answer**
SQLAlchemy oferă un nivel de abstractizare (**Database Agnosticism**) și securitate automată. Previne nativ atacurile de tip SQL Injection prin parametrizarea interogărilor și ne permite să schimbăm motorul bazei de date (de la SQLite la PostgreSQL) doar modificând URL-ul de conexiune.

---

### 44. Ce este WAL (Write-Ahead Logging) în SQLite și de ce este critic în modul tău offline?
**Answer**
WAL este un mod de operare în care citirile nu blochează scrierile și invers. Este critic pentru reziliență: modificările sunt scrise mai întâi într-un jurnal separat, asigurând că o prăbușire bruscă a procesului nu corupe fișierul principal al bazei de date.

---

### 45. Cum garantezi idempotența în calculele de dozaj medical?
**Answer**
Funcțiile Python de calcul sunt pur matematice și **idempotente** (stateless). Rularea aceleiași funcții cu exact aceeași greutate a neonatoului va returna de fiecare dată miligramul identic, eliminând riscul de multiplicare accidentală a dozelor la reîmprospătarea paginii.

---

### 46. Ce rol joacă fișierul `.gitattributes` în managementul proiectului tău?
**Answer**
Acesta dictează cum clasifică GitHub Linguist tehnologiile din repository. Prin setarea regulilor potrivite, am forțat ignorarea fișierelor mari de date (CSV), a rapoartelor PDF și a testelor din statistica oficială, demonstrând vizual o dominanță reală de **Python 97%** pe profil.

---

### 47. De ce este Ruff o alegere mai bună decât Flake8 sau Black pentru analiza statică?
**Answer**
Ruff este scris în Rust și este de peste 10-100 de ori mai rapid decât linterele tradiționale scrise în Python. Acesta unifică regulile de la Flake8, Black și isort, reducând timpul de execuție al porților de calitate în pipeline-ul nostru de CI/CD (GitHub Actions).

---

### 48. Cum optimizezi Dockerfile-ul pentru a reduce timpul de build în CI/CD?
**Answer**
Prin utilizarea strategiei de **Layer Caching**. Am copiat și instalat fișierul de dependențe (`requirements.txt`) înainte de a copia restul codului sursă. Astfel, dacă codul se schimbă dar librăriile rămân aceleași, Docker sare peste descărcarea pachetelor, accelerând deployment-ul.

---

### 49. Ce se întâmplă dacă modelul LLM (Llama-3.1) refuză să returneze tag-urile XML cerute?
**Answer**
Layer-ul de validare post-inferență prinde excepția de parsare, blochează afișarea textului invalid și activează un **deterministic fallback**. Interfața va afișa automat un text predefinit, securizat, extras direct din logica Python, prevenind blocarea dashboard-ului.

---

### 50. Care este cel mai important indicator de performanță (KPI) al acestui pipeline MLOps?
**Answer**
Timpul de feedback la integrare. Datorită decuplării complete, rularea combinată a suitei de **17/17 teste Pytest** și a matricei **9/9 Promptfoo** durează sub 30 de secunde în GitHub Actions, asigurând o validare ultra-rapidă a fiecărui release de producție.

- **Automated MLOps Validation Panel:** Consolă integrată pentru declanșarea matricii Promptfoo.
- **Extensible PDF Document Service:** Gateway nativ pentru generarea rapoartelor clinice persistate.
