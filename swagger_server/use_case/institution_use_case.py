from swagger_server.models import RequestInstitutionAdd
from swagger_server.models.response_institution import ResponseInstitution
from swagger_server.models.response_institution_data import ResponseInstitutionData


class InstitutionUseCase:

    def __init__(self, institution_repository):
        self.institution_repository = institution_repository

    def get_institution(self):
        """
            Lista de instutition
        :return:
        """

        data_response = []
        institutions = self.institution_repository.get_institution()

        for i in institutions:
            data_response.append(
                ResponseInstitutionData(
                    id=i.id,
                    name=i.name,
                    description=i.description,
                    address=i.address,
                )
            )

        response = ResponseInstitution(
            code=0,
            message="proceso exitoso",
            data=data_response
        )

        return response

    def add_institution(self, institution_data):
        """
            Crea una institución
        :return:
        """

        institution = RequestInstitutionAdd(
            name=institution_data.name,
            description=institution_data.description,
            address=institution_data.address,
            created_user=institution_data.created_user
        )
        self.institution_repository.add_institution(institution)
        return ResponseInstitution(code=0, message="proceso satisfactorio")
