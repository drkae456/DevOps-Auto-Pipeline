from fastapi import FastAPI
from book_catalog.main import app as book_catalog_app
from inventory_management.main import app as inventory_management_app

app = FastAPI()

# Mounting each microservice's FastAPI app under different routes
app.mount("/book_catalog", book_catalog_app)
app.mount("/inventory_management", inventory_management_app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
