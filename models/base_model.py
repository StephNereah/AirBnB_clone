#!/usr/bin/python3
# models/base_model.py

"""class BaseModel that defines all common attributes/methods for other classes
"""

import uuid
from datetime import datetime


class BaseModel:
    """base model parent class for all other classes
       used in project
    """

    def __init__(self, *args, **kwargs):
        """init method for base class used in instantiation
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at


    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
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
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)
