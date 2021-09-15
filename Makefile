run:
	docker-compose up

migrations:
	docker-compose run --rm transaction_manager python3 manage.py makemigrations

migrate:
	docker-compose run --rm transaction_manager python3 manage.py migrate

shell:
	docker-compose run --rm transaction_manager python3 manage.py shell

bash:
	docker-compose run --rm transaction_manager /bin/bash

swagger:
	docker-compose run --rm transaction_manager python3 manage.py spectacular --file schema.yml

test:
	docker-compose run --rm transaction_manager python3 manage.py test