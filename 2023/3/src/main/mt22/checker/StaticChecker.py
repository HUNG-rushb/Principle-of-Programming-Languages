# 1913652
# Trịnh Duy Hưng
from Visitor import Visitor


class StaticChecker(Visitor):
    pass

# def toJSON(data, place, typ = None) :
#     if typ == 't':
#         try:
#             print(json.dumps(data, sort_keys=False, indent=4))
#         except Exception as e:
#             print(e)
#     else:
#         f = open('./main/d96/checker/' + place + '.json', 'w', encoding='utf-8')
#         try:
#             f.write(json.dumps(data, sort_keys=False, indent=4))
#         except Exception as e:
#             f.write(e)
#         finally:
#             f.close()


class Type:
    def NONE(self): return "<3...None"

    def INT(self): return "<3...INT"

    def FLOAT(self): return "<3...FLOAT"

    def STRING(self): return "<3...STRING"

    def BOOLEAN(self): return "<3...BOOLEAN"

    def ARRAY(self, type, size): return "<3...ARRAY" + "**" + type + "**" + str(size)

    def CLASS(self, name): return "<3...CLASS " + name

    def VOID(self): return "<3...VOID"

    def NULL(self): return "<3...NULL"
