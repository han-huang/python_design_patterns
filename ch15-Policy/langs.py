# coding: utf-8
import pprint # 美化输出
from collections import namedtuple
from operator import attrgetter # 生成按名称提取属性的函数
if __name__ == '__main__':
    ProgrammingLang = namedtuple('ProgrammingLang', 'name ranking')
    stats = (('Ruby', 14), ('Javascript', 8), ('Python', 7),
             ('Scala', 31), ('Swift', 18), ('Lisp', 23))
    lang_stats = [ProgrammingLang(n, r) for n, r in stats]
    print()
    pp = pprint.PrettyPrinter(indent=5)
    pp.pprint(sorted(lang_stats, key=attrgetter('name')))
    print()
    pp.pprint(sorted(lang_stats, key=attrgetter('ranking')))

    # class pprint.PrettyPrinter(indent=1, width=80, depth=None, stream=None, *, compact=False)
    # https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter

    # collections.namedtuple
    # https://docs.python.org/3/library/collections.html#collections.namedtuple
    print()
    print("for debug:")
    print()
    print(lang_stats)
    print()
    d = {}
    print([lang.ranking for lang in lang_stats])
    print()
    for lang in lang_stats: # use for loop
        print(lang)
        print(lang.name)
        print(lang.ranking)
        d[lang.name] = lang.ranking
    d2 = {lang.name: lang.ranking for lang in lang_stats} # use dict comprehension
    print()
    print(d)
    print()
    print(d2)
