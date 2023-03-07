import json
import os
import requests
from lxml import html


class LogIn:
    __headers_json = "headers.json"
    __login_json = "login.json"
    __main_link = "https://eos.pnu.edu.ru/"
    __login_link = "https://eos.pnu.edu.ru/login/index.php"
    __work_link = "https://eos.pnu.edu.ru/my/"
    __cookie_valid = False
    __session = None
    __headers = {}
    __tasks_list = []

    # def __init__(self):
    #     try:
    #         with open(self.__headers_json, "r", encoding="UTF-8") as F:
    #             self.__headers = json.load(F)
    #         assert self.test_for_login(), "Cookie not valid."
    #         print("Login succesfull by a cookie.")
    #         self.__cookie_valid = True
    #     except FileNotFoundError:
    #         self.__headers = {}
    #         self.__cookie_valid = self.login()
    #     except (OSError, AssertionError):
    #         self.__cookie_valid = self.login()

    # def test_for_login(self):
    #     """
    #     Check whether cookie refers to a valid session.\n
    #     Return true, if cookie is a valid session.\n
    #     Otherwise, return false.
    #     """
    #     page = requests.request("GET", self.__main_link, headers=self.__headers,
    #                             allow_redirects=False)
    #     return "Location" in page.headers and page.headers["Location"] == self.__work_link

    def login(self, username, password):
        """
        Enter the EOS system. Do not check whether the previous cookie was valid or not, it will be deleted.\n
        First check for a file "login.json" with login and password there.\n
        If not exists or information is incorrect, prompt from a console until KeyboardInterrupt or success.\n
        On success, return True. On interrupt, return False.
        """
        success_flag = False
        # print("Attempt to log in.")

        # clear cookies
        self.__headers["Cookie"] = ""

        # prepare login and password
        # with open(self.__login_json) as F:
        #     login_file = json.load(F)

        # refresh cookies
        page = requests.request("GET", self.__login_link,
                                headers=self.__headers, allow_redirects=False)
        if "Set-Cookie" in page.headers:
            self.__headers["Cookie"] = page.headers["Set-Cookie"].split(";")[0]

            # username = login_file["username"]
            # password = login_file["password"]
            # send a request to log in

        success_flag = self.__attempt_to_login(
            username, password)

        return success_flag

    def __attempt_to_login(self, username, password):
        """
        Hidden method required to test whether attempt to log in was succesfull.\n
        It is required by a login() function.\n
        Return true and change cookie if login was succesfull. Otherwise, return false.
        """
        # get logintoken
        page = requests.request("GET", self.__login_link,
                                headers=self.__headers, allow_redirects=False)
        logintoken = self.__get_login_token(page)
        # create request
        request = {"anchor": "", "username": username,
                   "password": password, "logintoken": logintoken}

        # send request
        page = requests.request("POST", self.__login_link, headers=self.__headers,
                                allow_redirects=False, data=request)
        # update cookie if login succesful and return true
        if "Set-Cookie" in page.headers:
            self.__headers["Cookie"] = page.headers["Set-Cookie"].split(";")[0]
            return True
        return False

    def __get_login_token(self, page):
        """
        Parse the logintoken value and return it from the given page.
        """
        login_token_value = None
        parsed_page = html.fromstring(page.text)
        all_inputs = parsed_page.xpath("//input")
        for input_line in all_inputs:
            name = input_line.xpath("@name")[0]
            if name == "logintoken":
                login_token_value = input_line.xpath("@value")[0]
                break
        return login_token_value
