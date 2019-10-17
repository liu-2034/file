import datetime,time

class ChackID:
    def __init__(self,id_number):
        self.id_number = id_number
        #切片身份证号
        self.area = id_number[:6]
        self.birthday = id_number[6:14]
        self.ea = id_number[14:17]
        self.exits = id_number[17:]
        self.lists = []
        self.lists.append(self.chack_birthday(self.birthday))
        self.lists.append(self.validate_check_number())
        self.lists.append(self.check_gender())
        self.lists.append(self.check_area())
        print(self.lists)

    def results(self):
        return self.lists

    def check_number(self):
        number = self.id_number[0:17]
        #系数
        si_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        check_up_number = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        #验证
        of_number = 0
        for index in range(len(number)):
            of_number += int(number[index]) * int(si_list[index])

        yu_number = of_number % 11
        return check_up_number[yu_number]

        # 校验码验证
    def validate_check_number(self):
        if self.check_number() == self.exits:
            return '有效'
        else:
            return False
    def check_gender(self):
        if int(self.ea) % 2 == 0:
            return '女'
        else:
            return '男'

    def chack_birthday(self,birthday):
        #时间戳从1970—1—1开始
        odate = datetime.datetime(1970,1,2)
        otime = time.mktime(odate.timetuple())

    #现在时间戳
        now = time.time()
        print(birthday)
        year = birthday[:4]
        month = birthday[4:6]
        day = birthday[6:]
        ymd = datetime.datetime(int(year), int(month), int(day))
        yearmd = time.mktime(ymd.timetuple())

        #判断
        if otime < yearmd and yearmd < now:
            return ymd.strftime("%Y-%m-%d")
        else:
            return False

        #返回结果

    def check_area(self):
        # 获取到所有的归属地
        f = open(file="身份证归属地.txt", mode='r', encoding="utf-8")
        all_area = f.readlines()
        res_area = ''
        for item in all_area:
            if self.area == item[:6]:
                res_area = item[6:-1]
        if res_area == '':
            return False
        else:
            return res_area



