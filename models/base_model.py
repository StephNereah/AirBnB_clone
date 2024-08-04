#!/usr/bin/python3
"""
class BaseModel that defines all common attributes/methods for other classes
"""
from datetime import datetime
import uuid


class BaseModel:
    def __init__(self):
        """
        Initialize a new BaseModel instance.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        
    def __str__(self):
        """
        Return a string representation of the instance.
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
    
    def save(self):
        """
        Updates the public instance attribute updated_at with current datetime
        """
        self.updated_at = datetime.utcnow()
        
    def to_dict(self):
        """
        Return a dictionary containing all keys/values of __dict__ of the instance.
        Add a __class__ key with the class name of the object.
        Convert created_at and updated_at to string objects in ISO format.
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy


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
