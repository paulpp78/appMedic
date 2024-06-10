$BACK_DIR = "appMedicBack"
$FRONT_DIR = "appMedicFront"
$BACK_IMAGE = "app-medic-back"
$FRONT_IMAGE = "app-medic-front"
$BACK_CONTAINER = "app-medic-back"
$FRONT_CONTAINER = "app-medic-front"

function Setup-Back {
    python -m venv "$BACK_DIR/.venv"
    & "$BACK_DIR/.venv/Scripts/Activate.ps1"
    pip install -r "$BACK_DIR/requirements.txt"
}

function Setup-Front {
    cd $FRONT_DIR
    npm install
    cd ..
}

function Build-Back {
    Setup-Back
    docker build -t $BACK_IMAGE $BACK_DIR
}

function Build-Front {
    Setup-Front
    docker build -t $FRONT_IMAGE $FRONT_DIR
}

function Start-Back {
    docker run -d --name $BACK_CONTAINER -p 3000:3000 $BACK_IMAGE
}

function Start-Front {
    docker run -d --name $FRONT_CONTAINER -p 443:443 $FRONT_IMAGE
}

function Start {
    Start-Back
    Start-Front
}

function Stop {
    docker stop $BACK_CONTAINER, $FRONT_CONTAINER -ErrorAction SilentlyContinue
    docker rm $BACK_CONTAINER, $FRONT_CONTAINER -ErrorAction SilentlyContinue
}

function Pre-Commit {
    pre-commit run --all-files
}

function Clean {
    Stop
    docker rmi $BACK_IMAGE, $FRONT_IMAGE -ErrorAction SilentlyContinue
}

function All {
    Build-Back
    Build-Front
}

param (
    [Parameter(Mandatory=$true)]
    [ValidateSet("setup-back", "setup-front", "build-back", "build-front", "start-back", "start-front", "start", "stop", "pre-commit", "clean", "all")]
    [string]$task
)

switch ($task) {
    "setup-back" { Setup-Back }
    "setup-front" { Setup-Front }
    "build-back" { Build-Back }
    "build-front" { Build-Front }
    "start-back" { Start-Back }
    "start-front" { Start-Front }
    "start" { Start }
    "stop" { Stop }
    "pre-commit" { Pre-Commit }
    "clean" { Clean }
    "all" { All }
}
