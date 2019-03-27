import inspect
import yaml
import re

yaml.warnings({'YAMLLoadWarning': False})


def get_data(funcname):
    # 获取调用的测试用例文件名称
    fileInfo = inspect.stack()[1].filename
    filename = re.search(r'\\test_(.*?).py', fileInfo).group(1)
    with open('./data/data_{}.yaml'.format(filename), encoding='utf-8') as f:
        data = yaml.load(f)

    tmpdata = data[funcname]
    res_data = []
    for i in tmpdata.values():
        lis = []
        for j in i.values():
            lis.append(j)
        res_data.append(lis)
    return res_data
