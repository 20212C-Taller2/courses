from app.adapters.http.subscriptions.subscriptions_service import SubscriptionsService
from app.db.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_subscriptions_service() -> SubscriptionsService:
    return SubscriptionsService()
