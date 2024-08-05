#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()
        self.model.name = "My First Model"
        self.model.my_number = 89

    def test_id(self):
        self.assertIsInstance(self.model.id, str)

    def test_created_at(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        classname = self.model.__class__.__name__
        expected_str = "[{}] ({}) {}".format(classname, self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

    def test_to_dict_values(self):
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

    def test_init_with_kwargs(self):
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at.isoformat(), self.model.created_at.isoformat())
        self.assertEqual(new_model.updated_at.isoformat(), self.model.updated_at.isoformat())
        self.assertEqual(new_model.name, self.model.name)
        self.assertEqual(new_model.my_number, self.model.my_number)
        self.assertEqual(new_model.__class__.__name__, 'BaseModel')

    def test_dict_conversion_with_datetime(self):
        """
        Test that created_at and updated_at are converted back to datetime
        """
        self.model.save()
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
