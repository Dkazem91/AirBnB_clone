# AirBnB Clone Project
## Part 1 - command interpreter
### This project will entail:
* Putting in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of future instances
* Creating a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* Creating all classes used for AirBnB (`User`, `State`, `City`, `Place…`) that inherit from `BaseModel`
* Create the first abstracted storage engine of the project: File storage.
* Create all unittests to validate all our classes and storage engine
### How to use it:
1. Start up the console by typing `./console`.
2. Type `help` to see what commands are available.
### Examples:
```
(hbnb)create BaseModel
22442c9d-2df8-4ad6-9877-fbebe5dc38eb
(hbnb)show BaseModel 22442c9d-2df8-4ad6-9877-fbebe5dc38eb
[BaseModel] (22442c9d-2df8-4ad6-9877-fbebe5dc38eb) {'updated_at': datetime.datetime(2018, 6, 13, 14, 39, 8, 949289), 'id': '22442c9d-2df8-4ad6-9877-fbebe5dc38eb', 'created_at': datetime.datetime(2018, 6, 13, 14, 39, 8, 949072)}
```
### Authors:
* Daniel Kazemian <274@holbertonschool.com>
* Andrew Suh <307@holbertonschool.com>