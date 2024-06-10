BACK_DIR=appMedicBack
FRONT_DIR=appMedicFront
BACK_IMAGE=app-medic-back
FRONT_IMAGE=app-medic-front
BACK_CONTAINER=app-medic-back
FRONT_CONTAINER=app-medic-front

.PHONY: all setup-back setup-front build-back build-front start-back start-front start stop pre-commit clean

setup-back:
	python -m venv $(BACK_DIR)/.venv
	. $(BACK_DIR)/.venv/bin/activate && pip install -r $(BACK_DIR)/requirements.txt

setup-front:
	cd $(FRONT_DIR) && npm install

build-back: setup-back
	docker build -t $(BACK_IMAGE) $(BACK_DIR)

build-front: setup-front
	docker build -t $(FRONT_IMAGE) $(FRONT_DIR)

start-back:
	docker run -d --name $(BACK_CONTAINER) -p 3000:3000 $(BACK_IMAGE)

start-front:
	docker run -d --name $(FRONT_CONTAINER) -p 443:443 $(FRONT_IMAGE)

start: start-back start-front

stop:
	docker stop $(BACK_CONTAINER) $(FRONT_CONTAINER) || true
	docker rm $(BACK_CONTAINER) $(FRONT_CONTAINER) || true

pre-commit:
	pre-commit run --all-files

clean: stop
	docker rmi $(BACK_IMAGE) $(FRONT_IMAGE) || true

all: build-back build-front
