# Restaurant

Kleine Django-REST-API für eine Restaurantkarte (Gerichte und Getränke) mit Mittagsangebot.

- **Gerichte:** 40 % Rabatt im Mittagsangebot (10:00–14:00 Uhr), vegane Gerichte werden mit `(vegan)` gekennzeichnet.
- **Getränke:** 50 % Rabatt im Mittagsangebot, alkoholische Getränke werden mit `(Alkohol)` gekennzeichnet.

## Voraussetzungen

| Programm | Version                  |
| -------- | ------------------------ |
| Python   | 3.12 oder neuer          |
| Git      | beliebig aktuelle Version |

### Python und Git installieren

#### macOS

Mit [Homebrew](https://brew.sh) (falls noch nicht installiert, den Befehl von der Homebrew-Webseite ausführen):

```bash
brew install python git
```

Kontrolle:

```bash
python3 --version
git --version
```

#### Windows

1. Python von <https://www.python.org/downloads/> herunterladen und installieren.
   **Wichtig:** Im Installer unten den Haken bei **„Add python.exe to PATH“** setzen.
2. Git von <https://git-scm.com/download/win> herunterladen und installieren.

Alternativ mit `winget` in der PowerShell:

```powershell
winget install Python.Python.3.13
winget install Git.Git
```

Danach ein **neues** PowerShell-Fenster öffnen und prüfen:

```powershell
python --version
git --version
```

## Installation

### 1. Projekt holen

```bash
git clone <REPOSITORY-URL>
cd serializer-restaurant
```

### 2. Virtuelle Umgebung erstellen und aktivieren

#### macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Falls PowerShell die Ausführung von Skripten blockiert („running scripts is disabled“), einmalig ausführen:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

#### Windows (Eingabeaufforderung / cmd)

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

Ist die Umgebung aktiv, steht `(.venv)` vor der Eingabezeile.

### 3. Abhängigkeiten installieren

Die Abhängigkeiten stehen in der Datei `reuirements.tx` (Django, Django REST Framework, …).
Der Befehl ist auf macOS und Windows gleich:

```bash
pip install -r reuirements.tx
```

### 4. Datenbank anlegen

Es wird SQLite verwendet, die Datei `db.sqlite3` wird automatisch erzeugt.

macOS:

```bash
python3 manage.py migrate
```

Windows:

```powershell
python manage.py migrate
```

> Innerhalb der aktivierten virtuellen Umgebung funktioniert auf beiden Systemen auch `python manage.py …`.

### 5. (Optional) Admin-Benutzer anlegen

Damit lassen sich Gerichte und Getränke bequem im Admin-Bereich anlegen:

```bash
python manage.py createsuperuser
```

## Server starten

```bash
python manage.py runserver
```

Der Server läuft anschließend unter <http://127.0.0.1:8000/>. Beenden mit `Strg + C` (Windows) bzw. `Ctrl + C` (macOS).

Bei späteren Starts muss nur noch die virtuelle Umgebung aktiviert (Schritt 2, ohne `venv`-Befehl) und `runserver` ausgeführt werden.

## Routen

| Methode | Route                        | Beschreibung                |
| ------- | ---------------------------- | --------------------------- |
| GET     | `/api/card/dishes/`          | Alle Gerichte auflisten     |
| GET     | `/api/card/drinks/`          | Alle Getränke auflisten     |
| POST    | `/api/card/drinks/create`    | Neues Getränk anlegen       |
| —       | `/admin/`                    | Django-Admin                |

### Beispiele

Gerichte abrufen:

```bash
curl http://127.0.0.1:8000/api/card/dishes/
```

Getränk anlegen:

macOS / Linux / Git Bash:

```bash
curl -X POST http://127.0.0.1:8000/api/card/drinks/create \
  -H "Content-Type: application/json" \
  -d '{"name": "Bier", "price": 4.5, "lunch_action": true, "is_alcoholic": true}'
```

Windows (PowerShell):

```powershell
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/api/card/drinks/create `
  -ContentType "application/json" `
  -Body '{"name": "Bier", "price": 4.5, "lunch_action": true, "is_alcoholic": true}'
```

Alternativ lässt sich die API im Browser unter <http://127.0.0.1:8000/api/card/dishes/> ansehen (Django REST Framework Browsable API).

## Häufige Probleme

| Problem                                                    | Lösung                                                                                              |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `python: command not found` (macOS)                        | `python3` statt `python` verwenden oder die virtuelle Umgebung aktivieren.                          |
| `python` öffnet den Microsoft Store (Windows)              | Python installieren und beim Installer „Add python.exe to PATH“ aktivieren; neues Terminal öffnen. |
| `No module named 'django'`                                 | Virtuelle Umgebung ist nicht aktiv oder Schritt 3 wurde nicht ausgeführt.                           |
| Django lässt sich nicht installieren                       | Python-Version prüfen (mindestens 3.12).                                                            |
| `Error: That port is already in use`                       | Anderen Port nutzen: `python manage.py runserver 8001`                                              |
