from sqlalchemy import Column, Integer, String, Float
from server.models.base_case import base_case as Base
from server.logging_config import setup_logging  


logger = setup_logging()

class Supermarket(Base):
    __tablename__ = "supermarkets"
    supermarket_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    supermarket_name = Column(String(20), nullable=False)
    location = Column(String(40), unique=True, nullable=False)

    def __repr__(self):
        return f"supermarkets(ID = {self.supermarket_id}, Name = {self.supermarket_name}, Location = {self.location})>"

hardcoded_supermarkets = [
    {
        "supermarket_id": 101,
        "supermarket_name": "FreshMart",
        "location": "123 Main St, Springfield"
    },
    {
        "supermarket_id": 102,
        "supermarket_name": "GroMart",
        "location": "145 Main St, China"
    },
    {
        "supermarket_id": 103,
        "supermarket_name": "WMart",
        "location": "55 Main St, Dubai"
    }
]

logger.info("Hardcoded supermarket data defined.")

def add_supermarkets(session):
    logger.info("Adding hardcoded supermarkets to the database...")
    
    try:
        for supermarket in hardcoded_supermarkets:
            new_supermarket = Supermarket(
                supermarket_id=supermarket["supermarket_id"],
                supermarket_name=supermarket["supermarket_name"],
                location=supermarket["location"]
            )
            session.add(new_supermarket)
            logger.info(f"Supermarket {new_supermarket.supermarket_name} added with ID {new_supermarket.supermarket_id}.")
        
        session.commit()
        logger.info("Hardcoded supermarkets added successfully.")
    except Exception as e:
        logger.error(f"Error while adding supermarkets: {e}", exc_info=True)
        session.rollback()
