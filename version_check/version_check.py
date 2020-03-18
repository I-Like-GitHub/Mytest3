import re


def version_check(v1="1.1.1", v2="1.2"):

    v1_list = v1.split(".")
    v2_list = v2.split(".")
    v1_len = len(v1_list)
    v2_len = len(v2_list)
    print(v1_list)
    print(v2_list)


    if v1_len > v2_len:
        for i in range(v1_len - v2_len): #v1=['1', '0', '1']  v2=['1',0,0]
            v2_list.append("0")
    elif v2_len > v1_len:
        for i in range(v2_len - v1_len):#
            v1_list.append("0")
    else:
        pass

    for i in range(len(v1_list)):
        if int(v1_list[i]) > int(v2_list[i]):
            return "1"
        if int(v1_list[i]) < int(v2_list[i]):
            return "-1"
    return "0"

print(version_check(v1="0.1", v2="1.1"))
print(version_check(v1="1.0.1", v2="1"))
print(version_check(v1="7.5.2.4", v2="7.5.3"))
print(version_check(v1="1.01", v2="1.001"))
print(version_check(v1="1.0", v2="1.0.0"))
