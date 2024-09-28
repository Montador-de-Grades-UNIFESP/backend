import firebase_admin as fba
from firebase_admin import firestore_async as fs  # type: ignore


# Inicializa o app do Firebase e o banco de dados Firestore
_app = fba.initialize_app()
db = fs.client(_app)
