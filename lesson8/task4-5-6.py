class Stock:
    def __init__(self):
        self.__office_equipments = {'printers': [], 'scanners': [], 'xeroxes': []}

    def __str__(self) -> str:
        result_strings = []
        printers = '\n'.join([str(p) for p in self.__office_equipments['printers']])
        result_strings.append(f"Принтеры({self.printers_count} шт.): \n{'отсутствуют' if not printers else printers}")
        scanners = '\n'.join([str(s) for s in self.__office_equipments['scanners']])
        result_strings.append(f"Сканеры({self.scanners_count} шт.): \n{'отсутствуют' if not scanners else scanners}")
        xeroxes = '\n'.join([str(x) for x in self.__office_equipments['xeroxes']])
        result_strings.append(f"Ксероксы({self.xeroxes_count} шт.): \n{'отсутствуют' if not xeroxes else xeroxes}")
        return '\n\n'.join(result_strings)

    @property
    def printers_count(self):
        return len(self.__office_equipments['printers'])

    @property
    def scanners_count(self):
        return len(self.__office_equipments['scanners'])

    @property
    def xeroxes_count(self):
        return len(self.__office_equipments['xeroxes'])

    def store_office_equipment(self, office_equipment):
        for equipments in self.__office_equipments.values():
            for equipment in equipments:
                if equipment.inventory_num == office_equipment.inventory_num:
                    raise ValueError(f'Оборудование инвент. номером {office_equipment.inventory_num} '
                                     f'уже есть на складе!')
        if isinstance(office_equipment, Printer):
            self.__office_equipments['printers'].append(office_equipment)
        elif isinstance(office_equipment, Scanner):
            self.__office_equipments['scanners'].append(office_equipment)
        elif isinstance(office_equipment, Xerox):
            self.__office_equipments['xeroxes'].append(office_equipment)
        else:
            raise ValueError(f'Неизвестный тип офисного оборудования. {office_equipment}')


class OfficeEquipment:
    def __init__(self, name, inventory_num, price, start_using_date, using_duration_month):
        self.name = name
        self.inventory_num = inventory_num
        self.price = price
        self.start_using_date = start_using_date
        self.using_duration_month = using_duration_month

    def __str__(self) -> str:
        return f'наименование: {self.name}, ' \
               f'инвентарный номер = {self.inventory_num}, ' \
               f'стоимость = {self.price}, ' \
               f'дата начала эксплуатации: {self.start_using_date}, ' \
               f'срок эксплуатации(мес.): {self.using_duration_month}'


class Printer(OfficeEquipment):
    def __init__(self, inventory_num, price, start_using_date, using_duration_month, has_ink, colored=False):
        super().__init__('принтер', inventory_num, price, start_using_date, using_duration_month)
        self.colored = colored
        self.has_ink = has_ink

    def __str__(self) -> str:
        return f"{super().__str__()}, чернила: {'есть' if self.has_ink else 'нет'}, " \
               f"цветной принтер: {'да' if self.colored else 'нет'}"

    def __repr__(self) -> str:
        return f'Printer({self.inventory_num}, {self.price}, "{self.start_using_date}", ' \
               f'{self.using_duration_month}, {self.has_ink}, {self.colored})'


class Scanner(OfficeEquipment):
    def __init__(self, inventory_num, price, start_using_date, using_duration_month, colored=False):
        super().__init__('сканер', inventory_num, price, start_using_date, using_duration_month)
        self.colored = colored

    def __str__(self) -> str:
        return f"{super().__str__()}, цветной сканер: {'да' if self.colored else 'нет'}"

    def __repr__(self) -> str:
        return f'Printer({self.inventory_num}, {self.price}, "{self.start_using_date}", ' \
               f'{self.using_duration_month}, {self.colored})'


class Xerox(OfficeEquipment):
    def __init__(self, inventory_num, price, start_using_date, using_duration_month, has_ink, colored=False):
        super().__init__('ксерокс', inventory_num, price, start_using_date, using_duration_month)
        self.colored = colored
        self.has_ink = has_ink

    def __str__(self) -> str:
        return f"{super().__str__()}, чернила: {'есть' if self.has_ink else 'нет'}, " \
               f"цветной ксерокс: {'да' if self.colored else 'нет'}"

    def __repr__(self) -> str:
        return f'Printer({self.inventory_num}, {self.price}, "{self.start_using_date}", ' \
               f'{self.using_duration_month}, {self.has_ink}, {self.colored})'


printer = Printer(123, 15000, '05-12-2021', 36, True)
printer1 = Printer(124, 14000, '06-12-2021', 24, True)
scanner = Scanner(234, 5000, '12-05-2020', 36, True)
xerox = Xerox(1256, 7000, '30-11-2019', 36, False, True)
stock = Stock()
stock.store_office_equipment(printer)
stock.store_office_equipment(printer1)
stock.store_office_equipment(scanner)
stock.store_office_equipment(xerox)
print(stock)
