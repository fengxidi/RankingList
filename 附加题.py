# _*_ coding: utf-8 _*_
__auther__ = 'guozheng'
__date__ = '2020-4-7 21:53'

def Fversion(version):
    vers = version.split('.')
    versions =[]
    for ver in vers:
        if len(ver)==1:
            versions.append(ver)
            continue
        ver = ver.lstrip('0')
        versions.append(ver)
    return versions

def fun(version1,version2):
    # version1 = "0.1"


    version1 = Fversion(version1)
    version2 = Fversion(version2)
    print('version1=',version1)
    print('version2=',version2)

    if len(version1) < len(version2):
        for i,version in enumerate(version1):
            if int(version) == int(version2[i]):
                continue
            else:
                if int(version) < int(version2[i]):
                    return -1
                else:
                    return 1
        for v in version2[i+1::]:
            if v !='0':
                return -1
        return 0
    elif len(version1) > len(version2):
        for i,version in enumerate(version2):
            if int(version) == int(version1[i]):
                continue
            else:
                if int(version) < int(version1[i]):
                    return 1
                else:
                    return -1
        for v in version1[i+1::]:
            if v !='0':
                return 1
        return 0
    else:
        for i,version in enumerate(version2):

            if int(version) == int(version1[i]):
                continue
            else:
                if int(version) < int(version1[i]):
                    return 1
                else:
                    return -1
        return 0


if __name__ == "__main__":
    # version1 = "1.01"
    # version2 = "1.001"
    # 0
    # version1 = "0.1"
    # version2 = "1.1"
    # -1
    # version1 = "7.5.2.4"
    # version2 = "7.5.3"
    # -1
    # version1 = "1.01"
    # version2 = "1.001"
    # 0

    version1 = input('version1=')
    version2 = input('version2=')
    # 0
    d =fun(version1,version2)
    print(d)

