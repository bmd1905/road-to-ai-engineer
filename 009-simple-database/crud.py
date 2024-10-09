from sqlalchemy.orm import Session

from models import User


def get_user(db: Session, user_id: int):
    """Get a user by id"""
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 10):
    """Get all users"""
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: User):
    """Create a new user"""
    # Check if the user with the same email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise ValueError("A user with this email already exists.")

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user(db: Session, user_id: int, name, email):
    """Update a user by id"""
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.name = name
        user.email = email
        db.commit()
        db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    """Delete a user by id"""
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
