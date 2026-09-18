# DRF come - Library Management Project

Ushbu loyiha Django va Django REST Framework (DRF) asosida yaratilgan.

## Loyihaning asosiy tarkibi

1. **Virtual muhit (`venv`)**: Loyiha mustaqil virtual muhitda ishlaydi.
2. **Frameworklar**:
   - Django 6.1.1
   - Django REST Framework (DRF) 3.18.1
3. **Loyiha nomi**: `library`
4. **Ilova nomi**: `books`
5. **Sozlamalar**: `library/settings.py` faylida `rest_framework` va `books` ilovalari `INSTALLED_APPS` ro'yxatiga kiritilgan.
6. **Book modeli**:
   - `title`: Kitob nomi (`CharField`, max_length=255)
   - `author`: Muallif (`CharField`, max_length=150)
   - `price`: Narxi (`DecimalField`, max_digits=10, decimal_places=2)
   - `published_date`: Nashr etilgan sana (`DateField`)

---

## O'rnatish va ishga tushirish

### 1. Loyihani yuklab olish va papkaga kirish:
```bash
git clone <repo_url>
cd <repo_papka>
```

### 2. Virtual muhitni yaratish va faollashtirish:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Kutubxonalarni o'rnatish:
```bash
pip install django djangorestframework
```

### 4. Migratsiyalarni amalga oshirish:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Serverni ishga tushirish:
```bash
python manage.py runserver
```

Brauzeringizda quyidagi manzilni oching:
`http://127.0.0.1:8000/`
