mkdir djangoadv <br />
git clone git@github.com:eng-renanmoura/gestao_clientes_django.git <br />
python3.6 -m venv venv <br />
. venv/bin/activate <br />
cd gestao_clientes_django/ <br />
pip install -r requirements-dev.txt <br />
criar arquivo .env com: <br />
 ->SECRET_KEY=dafaasdsadsadsadasd <br />
 ->DEBUG=True
python manage.py migrate <br />
python manage.py createsuperuser <br />
python manage.py runserver <br />
pip install django-debug-toolbar <br />
python manage.py collectstatic <br />
python manage.py startapp produtos <br />
python manage.py startapp vendas <br />