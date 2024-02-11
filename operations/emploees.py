from tables.database import Employees
from dto.model import Employee as employee
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, user_id:str):
    return db.query(Employees).filter(Employees.ID == user_id).first()

def create_task(db: Session, data: employee):
    try:
        exp = Employees(Full_Name = data.Full_Name, Phone = data.Phone, Addres = data.Address, Email = data.Email, Country = data.County, Login = data.Login, Password = data.Password)
        db.add(exp)
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def update_task(db: Session, data: employee, id: int):
    try:
        exp = db.query(Employees).filter(Employees.ID == id).first()
        exp.Full_Name = data.Full_Name
        exp.Phone = data.Phone
        exp.Addres = data.Address
        exp.Email = data.Email
        exp.Country = data.County
        exp.Login = data.Login
        exp.Password = data.Password
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(Employees).filter(Employees.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp
