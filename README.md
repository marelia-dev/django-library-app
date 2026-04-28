# Django Library App 📚

**Bibliotekos valdymo sistema, sukurta naudojant Django framework**

Pilnavertė Django web aplikacija, leidžianti valdyti bibliotekos knygas, vartotojus, rezervacijas ir skolinimą.

## Galimybės
- Knygų pridėjimas, redagavimas ir paieška
- Vartotojų registracija ir prisijungimas
- Knygų rezervavimas ir skolinimas
- Administravimo panelė (Django admin)
- Responsyvus dizainas

## Technologijos
- Python 3
- Django framework
- HTML, CSS, Bootstrap
- SQLite / PostgreSQL
- Git

## Kaip paleisti
```bash
git clone https://github.com/marelia-dev/django-library-app.git
cd django-library-app

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Autorius
**Marijanas Molis** — Python / Django Developer
