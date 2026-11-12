
class Supplier:
    def __init__(
        self,
        supplier_id: str,
        name: str,
        contact_email: str
    ) -> None:
        self.__supplier_id = supplier_id
        self.__name = name
        self.__contact_email = contact_email

    @property
    def supplier_id(self) -> str:
        return self.__supplier_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def contact_email(self) -> str:
        return self.__contact_email

    def display_information(self) -> None:
        print("Supplier ID:", self.__supplier_id)
        print("Supplier Name:", self.__name)
        print("Contact Email:", self.__contact_email)
