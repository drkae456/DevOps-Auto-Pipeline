from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/inventories/", response_model=schemas.Inventory)
def create_inventory(inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    return crud.create_inventory(db=db, inventory=inventory)

@app.get("/inventories/", response_model=list[schemas.Inventory])
def read_inventories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    inventories = crud.get_inventories(db, skip=skip, limit=limit)
    return inventories

@app.get("/inventories/{inventory_id}", response_model=schemas.Inventory)
def read_inventory(inventory_id: int, db: Session = Depends(get_db)):
    db_inventory = crud.get_inventory(db, inventory_id=inventory_id)
    if db_inventory is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return db_inventory

@app.put("/inventories/{inventory_id}", response_model=schemas.Inventory)
def update_inventory(inventory_id: int, inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    return crud.update_inventory(db=db, inventory_id=inventory_id, inventory=inventory)

@app.delete("/inventories/{inventory_id}", response_model=schemas.Inventory)
def delete_inventory(inventory_id: int, db: Session = Depends(get_db)):
    return crud.delete_inventory(db=db, inventory_id=inventory_id)