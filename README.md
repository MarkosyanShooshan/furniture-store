# 🛋️ Furniture Store (Django Web Application)

[ 🇬🇧 English Version ](#english) | [ 🇦🇲 Հայերեն Տարբերակ ](#armenian)

---

<span id="english"></span>
## 🇬🇧 English

> A modern, responsive e-commerce web application built with Python and the Django framework. Designed as a digital furniture showroom, it provides an intuitive catalog for browsing, filtering, and managing furniture items.

### 📌 About the Project

The **Furniture Store** application provides an end-to-end shopping catalog experience. Users can explore various furniture categories (living room, bedroom, office, etc.), inspect detailed product specifications, view high-quality imagery, and check real-time pricing and availability.

The project highlights clean Django architectural practices, including relational database modeling (Categories & Products), custom Model managers, dynamic routing with SEO-friendly slugs, and a fully customized Django Admin dashboard for inventory tracking.

### ✨ Key Features

- **Product Catalog & Filtering:** Browse furniture pieces categorized by room, type, and material.
- **Detailed Product Pages:** Dynamic product view pages featuring detailed descriptions, price tags, dimensions, and image galleries.
- **SEO-Friendly URLs:** Dynamic routing powered by automated slug generation for clean and readable links.
- **Custom Django Admin Panel:** Robust back-office management for store owners to add, update, and manage inventory, categories, and stock.
- **Responsive Frontend:** Clean and modern UI built with Django Template Language (DTL), HTML5, and modular CSS.
- **Media Asset Pipeline:** Structured handling of uploaded product images using Django's media storage.

### 🛠 Tech Stack

- **Backend:** Python 3.x, Django
- **Database:** SQLite3 (Django ORM)
- **Frontend:** HTML5, CSS3, JavaScript, Django Templates
- **Image Processing:** Pillow

### 📂 Project Structure

```
furniture_store/
│
├── store/                  # Main application (Products, Categories, Views)
│   ├── models.py           # Database models (Category, Furniture, etc.)
│   ├── views.py            # Business logic (catalog, product details)
│   ├── urls.py             # Route routing rules
│   └── admin.py            # Admin panel configurations
│
├── templates/              # HTML templates (base.html, catalog, details)
├── static/                 # Static assets (CSS styles, JS, icons)
├── manage.py               # Django management script
├── requirements.txt        # Project dependencies
└── .gitignore              # Git ignored files
```


🚀 Installation & Setup


Clone the repository:

git clone https://github.com/MarkosyanShooshan/furniture-store.git
cd furniture-store

Create and activate a virtual environment:

Windows:

python -m venv venv
venv\Scripts\activate

macOS / Linux:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Apply database migrations:

python manage.py migrate

Create a superuser (for Admin access):

python manage.py createsuperuser

Run the development server:

python manage.py runserver

Open http://127.0.0.1:8000/ in your browser (or /admin for the admin portal).


<span id="armenian"></span>
🇦🇲 Հայերեն


Ժամանակակից և հարմարավետ վեբ-հավելված՝ ստեղծված Python-ով և Django ֆրեյմվորքով։ Նախագիծն իրենից ներկայացնում է կահույքի առցանց ցուցասրահ (կատալոգ), որը թույլ է տալիս զննել, ֆիլտրել և կառավարել կահույքի տեսականին։


📌 Նախագծի մասին


Furniture Store նախագիծը նպատակ ունի օգտատիրոջն ապահովել կահույք ընտրելու պարզ և հաճելի փորձառություն։ Հավելվածում իրականացված է ապրանքների բաժանում ըստ կատեգորիաների (հյուրասենյակ, ննջասենյակ, գրասենյակ և այլն), յուրաքանչյուր ապրանքի մանրամասն էջ՝ նկարներով, գնով, չափսերով և նկարագրությամբ։
Նախագիծը ցուցադրում է Django-ի կարևորագույն հնարավորությունները՝ տվյալների բազայի ռելյացիոն կառուցվածք (Categories & Products), slug-երով գեղեցիկ հասցեներ (SEO-friendly URLs), ինչպես նաև հզոր Django Admin վահանակ՝ ապրանքների քանակն ու տեսականին հեշտությամբ կառավարելու համար։

✨ Հիմնական հնարավորությունները


Ապրանքների Կատալոգ և Ֆիլտրացիա — Կահույքի տեսականու դիտում ըստ համապատասխան սենյակների և կատեգորիաների։
Ապրանքի Մանրամասն Էջ (Product Details) — Դինամիկ էջեր՝ գների, չափսերի, նկարագրության և լուսանկարների ցուցադրմամբ։
Հարմար URL-ներ (Slugs) — Ապրանքների անունների հիման վրա ավտոմատ ստեղծվող հասցեներ։
Ադմինիստրատիվ Վահանակ (Django Admin) — Խանութի տեսականու, կատեգորիաների և առկայության ամբողջական կառավարում։
Մոդուլային Շաբլոններ — Ճկուն HTML/CSS դիզայն՝ Django Template Language-ի (DTL) բազային շաբլոնների կիրառմամբ։
Մեդիա Ֆայլերի Կառավարում — Կահույքի նկարների ճիշտ պահպանում և արտապատկերում կայքում։


👤 Հեղինակ (Author)
- **Shooshan Markosyan** — [GitHub Profile](https://github.com/MarkosyanShooshan)