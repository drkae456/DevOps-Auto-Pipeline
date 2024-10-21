from sqlalchemy.orm import Session
from . import models, schemas

def get_inventory(db: Session, inventory_id: int):
    return db.query(models.Inventory).filter(models.Inventory.id == inventory_id).first()

def get_inventories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Inventory).offset(skip).limit(limit).all()

def create_inventory(db: Session, inventory: schemas.InventoryCreate):
    db_inventory = models.Inventory(**inventory.dict())
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory

def update_inventory(db: Session, inventory_id: int, inventory: schemas.InventoryCreate):
    db_inventory = db.query(models.Inventory).filter(models.Inventory.id == inventory_id).first()
    if db_inventory:
        db_inventory.item_name = inventory.item_name
        db_inventory.quantity = inventory.quantity
        db.commit()
        db.refresh(db_inventory)
    return db_inventory

def delete_inventory(db: Session, inventory_id: int):
    db_inventory = db.query(models.Inventory).filter(models.Inventory.id == inventory_id).first()
    if db_inventory:
        db.delete(db_inventory)
        db.commit()
    return db_inventory
