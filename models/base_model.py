#!/usr/bin/python3
"""This is the base model class for AirBnB"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, DateTime, Column
import models


Base = declarative_base()


class BaseModel:
    """This class will defines all common attributes/methods
    for other classes
    """

    id = Column(String(60), unique=True, nullable=False,
                primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs.keys():
                setattr(self, "id", str(uuid.uuid4()))
            time = datetime.now()
            if "created_at" not in kwargs.keys():
                setattr(self, "created_at", time)
            if "updated_at" not in kwargs.keys():
                setattr(self, "updated_at", time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        dic = self.to_dict()
        # del dic['__class__']
        # dic['created_at'] = datetime.strptime(dic['created_at'],
        #                                       "%Y-%m-%dT%H:%M:%S")
        # dic['updated_at'] = datetime.strptime(dic['updated_at'],
        #                                       "%Y-%m-%dT%H:%M:%S")
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, dic)

    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_at to current
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        if '_sa_instance_state' in my_dict.keys():
            my_dict.pop('_sa_instance_state', None)
        return my_dict

    def delete(self):
        """Delete the current instance from the storage
        (models.storage) by calling the method delete"""
        models.storage.delete(self)

# #!/usr/bin/python3
# """BaseModel class."""
# import models
# from uuid import uuid4
# from datetime import datetime
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column
# from sqlalchemy import DateTime
# from sqlalchemy import String

# Base = declarative_base()


# class BaseModel:
#     """Defines the BaseModel class.
#     Attributes:
#         id (sqlalchemy String): The BaseModel id.
#         created_at (sqlalchemy DateTime): The datetime at creation.
#         updated_at (sqlalchemy DateTime): The datetime of last update.
#     """

#     id = Column(String(60), primary_key=True, nullable=False)
#     created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
#     updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

#     def __init__(self, *args, **kwargs):
#         """Initialize a new BaseModel.
#         Args:
#             *args (any): Unused.
#             **kwargs (dict): Key/value pairs of attributes.
#         """
#         self.id = str(uuid4())
#         self.created_at = self.updated_at = datetime.utcnow()
#         if kwargs:
#             for key, value in kwargs.items():
#                 if key == "created_at" or key == "updated_at":
#                     value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
#                 if key != "__class__":
#                     setattr(self, key, value)

#     def save(self):
#         """Update updated_at with the current datetime."""
#         self.updated_at = datetime.utcnow()
#         models.storage.new(self)
#         models.storage.save()

#     def to_dict(self):
#         """Return a dictionary representation of the BaseModel instance.
#         Includes the key/value pair __class__ representing
#         the class name of the object.
#         """
#         my_dict = self.__dict__.copy()
#         my_dict["__class__"] = str(type(self).__name__)
#         my_dict["created_at"] = self.created_at.isoformat()
#         my_dict["updated_at"] = self.updated_at.isoformat()
#         my_dict.pop("_sa_instance_state", None)
#         return my_dict

#     def delete(self):
#         """Delete the current instance from storage."""
#         models.storage.delete(self)

#     def __str__(self):
#         """Return the print/str representation of the BaseModel instance."""
#         d = self.__dict__.copy()
#         d.pop("_sa_instance_state", None)
#         return "[{}] ({}) {}".format(type(self).__name__, self.id, d)
