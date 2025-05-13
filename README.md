# Django Menu App

Приложение реализует древовидное меню с отрисовкой через template tag.

---

## 📌 Функциональность

- Хранение меню в БД
- Поддержка нескольких меню (по имени)
- Меню редактируется через стандартную Django админку
- Определение активного пункта по URL
- Разворачивается всё до активного + первый уровень под ним
- Поддержка `named url` и обычных ссылок
- Всего один запрос к БД при отрисовке

---

## 🚀 Установка

```bash
git clone https://github.com/Natanat2/UpTraderTest
cd uptrader
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
