# -*- coding: UTF-8 -*-
# Author:Chao
import getpass

#访问用户文件,并把所有的用户名和密码用字典类型存储并返回这个列表
def user_all():
    user_dict = {}

    file_object = open("userinfo.txt")
    try:
        file_all_the_lines = file_object.readlines()

        for line in file_all_the_lines:
            user_dict[line.split(" ")[0]] = line.split(" ")[1].replace("\n", "")

    finally:
        file_object.close()

    return user_dict


def login(users, user_lo):
    username = input("username:")

    if username in user_lo:

            print("The user has benn locked!!!")

    else:

        if username in users:

            count = 0
            while count <3:
                passworld = input("passworld:")
                if users[username] == passworld:
                    print("Welcome", username)
                    break
                else:
                    print("Incorrect passworld!")
                    count +=1
                    continue
            else:
                print("Passworld input error more than three times, the user has locked!!!  ")

                file_object = open("locked.txt", 'a')
                try:
                    file_object.write(username + " ")
                finally:
                    file_object.close()
        else:
            print("User name error")

def user_lock():

    file_object = open("locked.txt")

    try:

        user_locked = file_object.readline()
        user_locked_list = user_locked.split(" ")

    finally:

        file_object.close()

    return user_locked_list

def main():

    user_locked = user_lock()
    user_list = user_all()
    login(user_list, user_locked)

if __name__ == '__main__':
    main()