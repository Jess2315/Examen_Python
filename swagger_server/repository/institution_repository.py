import logging
from datetime import datetime

sql_select = "select * from institution where status = 'A'"
sql_insert = "insert into institution (name, description, address, created_user, status, created_at) values (:name, :description, :address, :created_user, :status, :created_at)"

class InstitutionRepository:

    def __init__(self, mysql_client):
        self.session_factory = mysql_client.session_factory

    def get_institution(self):
        with self.session_factory() as session:
            rows = session.execute(sql_select)
            return rows

    def add_institution(self, institution):
        with self.session_factory() as session:
            try:
                created_at = datetime.now()
                session.execute(sql_insert,
                    {
                        "name": institution.name,
                        "description": institution.description,
                        "address": institution.address,
                        "created_user": institution.created_user,
                        "created_at": created_at,
                        "status": "A"
                    })
                session.commit()
            except Exception as e:
                session.rollback()
                logging.error(f"No se pudo agregar la institución: {e}")
                raise ValueError("No se pudo agregar la institución. Por favor, inténtalo de nuevo.")