## 0x00 AirBnB Clone
![hbnb logo](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png)
First project in the AirBnB clone series is about laying the framework for a simple [AirBnB](http://airbnb.com/) clone.\
We have created some base classes for recieving, serializing and deserializtion of information along with creating a console using Class cmd for added control of handling the information.

## Environment
Creation and testing-
* Ubuntu 14.04.5 LTS
* Vagrant VirtualBox
* Python 3
* PEP8 styling

## Installation
This repository can be clones using the git provided url:\
``` $ git clone https://github.com/eightlimbed/AirBnB_clone.git ```\
To start the console:\
``` ~/AirBnB_clone$ ./console ```\

## Repository Contents
### Directories and Classes
| Directory   | Class         | Description                                                                         |
|-------------|---------------|-------------------------------------------------------------------------------------|
| Model       | BaseModel     | Defines all common attributes/methods for other classes                             |
|             | Amenity       | Defines amenities available                                                         |
|             | City          | Defines state id and name of the city                                               |
|             | Place         | Defines attributes like price by night, city id, number of rooms etc                |
|             | Review        | Defines attributes like place id, user id and text description                      |
|             | State         | Defines state name                                                                  |
|             | User          | Defines user attributes like email, password, first and last names                  |
| model/engine| FileStorage   | Class to create, save and reload instances                                          |
| console     | HBNBCommand   | Inherited from class cmd that will create, show, destroy, update and print instances|




