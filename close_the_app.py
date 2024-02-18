import os
from getallapps import list_of_software


def close_app(get_name):
    if os.name == 'nt':  # Windows
        list_of_softwarename=list_of_software()
        for i in list_of_softwarename:
            name_of_software = i
            i = i[:4]
            if i == get_name[:4]:
                name_of = "taskkill /f /im "+name_of_software + ".exe"
                os.system(name_of)
                break
    else:  # Linux or macOS
        os.system("pkill chrome")


 