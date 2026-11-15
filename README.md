# CA System Monitor - Rendszererőforrás és Hardver Diagnosztika

## Hallgatói adatok
* **Név**: Czudor Attila
* **Monogram**: CA
* **Intézmény**: Dunaújvárosi Egyetem
* **Tantárgy**: Szkript nyelvek Python Projektfeladat
* **Oktató**: Adamcsik János (adamcsik@uniduna.hu)

---

## 1. Feladat leírása
A **CA System Monitor** egy asztali rendszerfelügyeleti és hardverdiagnosztikai alkalmazás, amely valós időben követi a számítógép legfontosabb erőforrás-kihasználtsági mutatóit:
* **Processzorterheltség (CPU)**: pillanatnyi kihasználtság és terhelési állapotértékelés.
* **Rendszermemória (RAM)**: fizikai memória mérete, lefoglalt és szabad kapacitása gigabájtban, valamint százalékos értéke.
* **Háttértár (Disk)**: az elsődleges meghajtó / partíció összkapacitása, foglalt és szabad tárhelye.

Az alkalmazás grafikus felhasználói felületet (GUI), eseménykezelést (kézi frissítés, időzített automatikus ciklus), valamint fájlkezelést (pillanatkép exportálás JSON formátumba) biztosít.

---

## 2. Modulok és felhasznált függvények

A projekt a követelményeknek megfelelően három modultípust alkalmaz:

### A. Tanult modul: `tkinter`
A grafikus felhasználói felület elemeinek megjelenítése és az eseménykezelés megvalósítása:
* `tk.Tk()`: Az alkalmazás alapablakának (`root`) létrehozása.
* `tk.Frame()`, `tk.LabelFrame()`: Strukturált vezérlő- és információs kártyák elrendezése.
* `tk.Label()`, `tk.Button()`, `tk.Checkbutton()`: Szöveges adatközlők, műveleti gombok és állapotválasztók.
* `root.after()`: Nem-blokkoló, időzített eseményvezérlés az automatikus frissítési ciklushoz (2 másodpercenként).
* `messagebox.showinfo()`: Felugró visszajelzés a sikeres fájlexportálást követően.

### B. Bemutatandó modul: `psutil`
Rendszer- és hardverdiagnosztikai külső modul. A beadandóban **három függvénye** kerül részletes bemutatásra és alkalmazásra:
1. **`psutil.cpu_percent(interval=None)`**:
   * *Szerepe*: Lekéri az aktuális processzorterheltséget százalékos formában. Nem-blokkoló módban fut az eseményhurok folyamatosságának megőrzéséért.
2. **`psutil.virtual_memory()`**:
   * *Szerepe*: Részletes adatokat szolgáltat a fizikai rendszermemóriáról (összes, lefoglalt, szabad bájtok száma és százalékos aránya).
3. **`psutil.disk_usage(path)`**:
   * *Szerepe*: Megvizsgálja a paraméterként átadott meghajtó vagy gyökérkönyvtár (`/`) tárhelykapacitását és foglaltságát.

### C. Saját modul: `ca_system_service` (`ca_system_service.py`)
A modul nevében szerepel a hallgató monogramja (**CA**). Felelős az adatok lekérdezéséért, konverziójáért és fájlba írásáért:
* **`ca_format_metrics(raw_bytes, unit="GB", decimal_places=2)`**: Saját függvény a nyers bájtok emberi olvasásra optimalizált mértékegységekké (KB, MB, GB, TB) alakítására. A `main.py` és a `ca_system_service.py` is közvetlenül hívja.
* **`ca_evaluate_load_status(percent_value)`**: Segédfüggvény az állapotmeghatározáshoz (`NORMAL`, `WARNING`, `CRITICAL`).

---

## 3. Osztályok

A program objektumorientált szemléletben épül fel:

1. **`CASystemCollector`** (helye: `ca_system_service.py`):
   * Monogramos osztály a telemetriai adatok lekérdezésére és tárolására.
   * Főbb metódusai: `get_cpu_usage()`, `get_memory_usage()`, `get_disk_usage()`, `collect_all()`, `save_snapshot_to_file()`.
2. **`CASystemApp`** (helye: `main.py`):
   * A Tkinter grafikus felületet, elrendezést és felhasználói interakciókat kezelő osztály.
   * Főbb metódusai: `on_manual_refresh()`, `on_export_snapshot()`, `toggle_auto_refresh()`, `schedule_next_poll()`, `auto_poll_task()`.
3. **`CATestSystemCollector`** (helye: `ca_test_service.py`):
   * Automatikus egységteszteket megvalósító osztály (9 db teszteset).

---

## 4. Eseménykezelés
* **Kézi frissítés**: A `Frissítés most` gombra kattintás aktiválja az `on_manual_refresh` metódust, amely lekéri és frissíti az összes hardveradatot.
* **Automatikus időzítés**: A `root.after(2000, ...)` időzítő 2 másodpercenként automatikusan újraolvassa az értékeket a felület zárolása (fagyása) nélkül.
* **Fájlexport esemény**: A `Pillanatkép mentése` gomb aktiválja a helyi JSON fájl létrehozását és értesíti a felhasználót.

---

## 5. Választható feladat: Fájlkezelés
A program teljesíti a diasor 5. oldalán felsorolt választható feladatot (**Fájlkezelés**):
* A pillanatnyi rendszerállapot menthető a `ca_system_metrics_snapshot.json` fájlba strukturált formátumban (`save_snapshot_to_file` metódus).

---

## 6. Program futtatása és tesztelése

### Függőségek telepítése
```bash
pip3 install -r requirements.txt
```

### Alkalmazás indítása
A diasor 10. oldalának elvárása szerint a belépési pont a `main.py`:
```bash
python3 main.py
```

### Egységtesztek futtatása
```bash
python3 -m unittest ca_test_service.py
```
