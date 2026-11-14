# CA System Monitor - Rendszererőforrás és Hardver Diagnosztika

## Hallgató
* **Név**: Czudor Attila
* **Monogram**: CA
* **Intézmény**: Dunaújvárosi Egyetem
* **Tantárgy**: Szkript nyelvek Python
* **Oktató**: Adamcsik János

---

## Feladat leírása
A **CA System Monitor** egy asztali rendszerfelügyeleti és hardverdiagnosztikai alkalmazás, amely valós időben követi és jeleníti meg a számítógép legfontosabb erőforrás-kihasználtsági mutatóit (processzorterheltség, rendszermemória/RAM használat, valamint háttértár kapacitás). Az alkalmazás grafikus felhasználói felületet (GUI) biztosít, és lehetőséget nyújt a pillanatnyi telemetria helyi fájlba történő mentésére (snapshot készítés).

---

## Modulok és felhasznált függvények

### 1. Tanult modul
* **`tkinter`**: Grafikus felhasználói felület kialakítása, ablakkezelés és időzített eseményvezérlés (`root.after`).

### 2. Bemutatandó modul
* **`psutil`**: Rendszer- és folyamatdiagnosztikai modul hardverinformációk lekérdezésére.
  * `psutil.cpu_percent()`: Processzor aktuális százalékos terheltségének mérése.
  * `psutil.virtual_memory()`: Rendszermemória (RAM) fizikai állapotának lekérdezése (összes, foglalt, szabad).
  * `psutil.disk_usage()`: Meghajtó vagy partíció tárterület-kihasználtságának elemzése.

### 3. Saját modul
* **`ca_system_service`** (`ca_system_service.py`): Telemetriai adatok összesítésére és formázására szolgáló saját modul.
  * `ca_format_metrics()`: Saját függvény a nyers bájtok emberi olvasásra optimalizált (GB) formázására és állapotjelzők számítására.

---

## Osztályok
* **`CASystemCollector`**: Saját osztály a hardveres adatok egységbe zárására és a vizsgálati eredmények strukturálására.

---

## Program indítása
* **Belépési pont**: `main.py`
```bash
python3 main.py
```
