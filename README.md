# StudentOverflow

Portal de preguntas y respuestas para estudiantes, inspirado en StackOverflow.

## Objetivo
Permitir que cualquier usuario publique preguntas sobre materias y que la comunidad aporte respuestas de calidad.

## Stack
- Python 3.11+
- Flask + Jinja2
- SQLAlchemy (SQLite en desarrollo)
- WTForms (opcional) para formularios

## Cómo correr en local
```bash
python -m venv .venv
source .venv/bin/activate  # en Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Estructura pensada
studentoverflow/
├─ app.py
├─ config.py
├─ requirements.txt
├─ README.md
├─ .gitignore
├─ studentoverflow/
│  ├─ __init__.py
│  ├─ models.py
│  ├─ routes/
│  │  ├─ __init__.py
│  │  ├─ main.py          # home/feed, búsqueda
│  │  ├─ auth.py          # login/registro
│  │  ├─ questions.py     # CRUD preguntas/respuestas, votos
│  │  └─ profile.py       # perfiles
│  ├─ services/
│  │  ├─ __init__.py
│  │  ├─ search.py        # búsqueda simple + filtros/tags
│  │  └─ notifications.py # stub para notificaciones
│  ├─ forms.py            # WTForms (opcional)
│  ├─ templates/
│  │  ├─ base.html
│  │  ├─ feed.html
│  │  ├─ question_detail.html
│  │  ├─ ask.html
│  │  ├─ login.html
│  │  ├─ register.html
│  │  ├─ profile.html
│  │  └─ tags.html
│  └─ static/
│     ├─ css/
│     │  └─ main.css
│     └─ js/
│        └─ main.js
└─ tests/
   └─ test_smoke.py
```