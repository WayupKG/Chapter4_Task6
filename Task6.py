class Home:
    '''
    Расчет квадрат метр дома при мебели
    '''
    def __init__(self):
        self.width = int(input("Ширина - "))
        self.height = int(input("Длина - "))

    def Home_KV(self):
        self.kv = self.width * self.height
        print(f"Если в доме нет мебели то {self.kv} квадратный(х) метр(а)")

    def mebel_home(self):
        self.mebel = str(input("Имя мебели - "))
        self.width_mebel = int(input("Ширина - "))
        self.height_mebel = int(input("Длина - "))
        self.mebel_kv_res = self.height_mebel * self.width_mebel
        self.kv -= int(self.mebel_kv_res)
        print(f"{self.mebel} {self.mebel_kv_res} квадратный(х) метр(а). В доме осталься(лось) {self.kv} квадратный(х) метр(а) ")


My_Home = Home()
My_Home.Home_KV()

while 1:
    mebel = str(input("Есть ли у вас мебель? (Да или Нет) - "))
    if mebel.lower() == "да":
       My_Home.mebel_home()
    else:
        exit()