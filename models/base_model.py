#!/usr/bin/python3
"""
class BaseModel that defines all common attributes/methods for other classes
"""
from datetime import datetime
import uuid


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        
    def __str__(self):
        """
         string - assign with an uuid when an instance is created:
         datetime -assign with the current datetime when an instance is created
         it will be updated every time you change your object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """
        updates the public instance attribute updated_at with current datetime
        """
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
