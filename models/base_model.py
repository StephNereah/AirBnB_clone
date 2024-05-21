#!/usr/bin/python3
"""class BaseModel that defines all common attributes/methods for other classes
"""

import uuid
from datetime import datetime


class BaseModel:
    """base model parent class for all other classes
       used in project
    """

    def __init__(self):
        """init method for base class used in instantiation
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """save method used for updating class so updated_at changes
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns the dictionary of our instance
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        """
        custom str method for str and print
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
