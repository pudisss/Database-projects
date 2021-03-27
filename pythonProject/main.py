import json
import os
from pathlib import Path
import random

class db(object):

    def show(self, filename):
        """

        :param filename: The file in the server
        :return: Json format data
        """

        try:
            with open(f"data/{filename}", "r") as file:
                data = json.load(file)
                print(data)
        except FileNotFoundError:
            print("There was no file in the server")
    def copy(self, targetfile, serverfile):
        """

        :param targetfile: The file that the user wanted to copy the data from
        :param serverfile: The file that was in the server
        :return: Process finished or errors
        """

        # All of the variable that will be used in the process


        homepath = Path.home()

        # To get the path to the file
        realpath = []

        for path, folder, file in os.walk(homepath):
           if targetfile in file:
               for i in range(len(file)):
                   if targetfile == file[i]:
                       rpath = os.path.join(path, targetfile)
                       realpath.append(rpath)

               break



        # To get the data from the file
        with open(realpath[0], "r") as newfile:
            oldfiledata = json.load(newfile)
            try:
                with open(f"data/{serverfile}", "w") as server:
                    json.dump(oldfiledata, server)
                    print("Process finished")
            except FileNotFoundError:
                print("There was no file in the server side you have to make a new file in the server")







    def save(self, filename): # To save the file in the server
        """

        :param filename: The file that the system will save in the server
        :return:
        """

        # To generate a token to access the file
        token = hex(random.randint(0, 10000000000))

        data = {
            "token": token
        }
        with open(f"data/{filename}.json", "a") as file:
            json.dump(data, file)
            print(f"Here is your token to access the file {token}")
            print("Process finished")






    def delete(self, filename):
        """

        :param filename: The file that the user wanted to delete it out of our server
        :return: True if no error occurs and False if not
        """
        try:
            os.remove(f"data/{filename}")
            print("Process finished")

        except FileNotFoundError:
            print("There was no file found in the server")
        except Exception:
            print("There was something wrong")


    def update(self, filename, data, token):
        """

        :param filename: The filename that the user had made already
        :param data: The data that the user wanted to update to
        :param token: The token to access to the file if you don't have the token you can't access the file
        :return:
        """

        # All of the variable that will be used in the process
        dicts = {}
        number = random.randint(0, 198759345)

        if type(data) == type(dicts):
            try:
                with open(f"data/{filename}", "r+") as file:
                    datas = json.load(file)

                    if datas["token"] == token:

                        datas[f"{number}"] = data

                        with open(f"data/{filename}", "w") as newfile:
                            json.dump(datas, newfile)
                            print("Process finished")

                    else:
                        pass
            except FileNotFoundError:
                print("There was no file in the server")
        else:
            print(False)
    def deletekey(self, filename, columnname, token):

        """

        :param filename: The file in the servevr
        :param columnname: The key of the dict in the json file
        :param token: The token to access the file

        :return:  True if no error occurs and False if not
        """
        try:
            # All of the variable that will be used in the process
            with open(f"data/{filename}", "r") as file:
                olddata = json.load(file)
                if olddata["token"] == token:
                    olddata.pop(columnname)

                    with open(f"data/{filename}", "w") as newfile:
                        json.dump(olddata, newfile)
                        print("Process finished")
                else:
                    print("You can access the file")


        except FileNotFoundError:
            print("There was not file in the server")

    def stores(self, path, data):
        """

        :param path: Path to store data in the user computer
        :param data: The data that the user wanted to store in his or her computer
        :return: Process finished
        """



        try:
            with open(path, "w") as file:
                json.dump(data, file)
                print("Process finished")
        except FileExistsError:
            print("There was a file in the computer already")








db =db()



