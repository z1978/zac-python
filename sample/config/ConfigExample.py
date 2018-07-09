# -* - coding: UTF-8 -* -
import configparser

# 生成config对象
conf = configparser.ConfigParser()
# 用config对象读取配置文件
print("use RawConfigParser() read")
conf.read("test.cfg")
print(conf.get("portal", "url"))

# 写配置文件
print("use RawConfigParser() write")
# 增加新的section
conf.add_section('a_new_section')
conf.set('a_new_section', 'new_key', 'new_value')

# 更新既存设定
conf.set("portal", "port", "8080")
print(conf.get("portal", "port"))

# 写回配置文件
conf.write(open("test.cfg", "w"))