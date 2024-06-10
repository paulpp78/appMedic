#!/bin/bash

BACK_DIR="appMedicBack"
FRONT_DIR="appMedicFront"
BACK_IMAGE="app-medic-back"
FRONT_IMAGE="app-medic-front"
BACK_CONTAINER="app-medic-back"
FRONT_CONTAINER="app-medic-front"

setup_back() {
    python -m venv "$BACK_DIR/.venv"
    source "$BACK_DIR/.venv/bin/activate"
    pip install -r "$BACK_DIR/requirements.txt"
}

setup_front() {
    cd $FRONT_DIR
    npm install
    cd ..
}

build_back() {
    setup_back
    docker build -t $BACK_IMAGE $BACK_DIR
}

build_front() {
    setup_front
    docker build -t $FRONT_IMAGE $FRONT_DIR
}

start_back() {
    docker run -d --name $BACK_CONTAINER -p 3000:3000 $BACK_IMAGE
}

start_front() {
    docker run -d --name $FRONT_CONTAINER -p 443:443 $FRONT_IMAGE
}

start() {
    start_back
    start_front
}

stop() {
    docker stop $BACK_CONTAINER $FRONT_CONTAINER || true
    docker rm $BACK_CONTAINER $FRONT_CONTAINER || true
}

pre_commit() {
    pre-commit run --all-files
}

clean() {
    stop
    docker rmi $BACK_IMAGE $FRONT_IMAGE || true
}

all() {
    build_back
    build_front
}

case "$1" in
    "setup-back")
        setup_back
        ;;
    "setup-front")
        setup_front
        ;;
    "build-back")
        build_back
        ;;
    "build-front")
        build_front
        ;;
    "start-back")
        start_back
        ;;
    "start-front")
        start_front
        ;;
    "start")
        start
        ;;
    "stop")
        stop
        ;;
    "pre-commit")
        pre_commit
        ;;
    "clean")
        clean
        ;;
    "all")
        all
        ;;
    *)
        echo "Usage: $0 {setup-back|setup-front|build-back|build-front|start-back|start-front|start|stop|pre-commit|clean|all}"
        exit 1
        ;;
esac
