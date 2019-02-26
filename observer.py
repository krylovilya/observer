class Subject:
    """
    Объект наблюдения
    """
    def __init__(self, name, *args):
        """
        Конструктор объекта наблюдения

        :param name: Строковое представление объекта наблюдения
        :type name: str
        :param args: Перечисление объектов наблюдателей
        :type args: *Observer
        """
        self.name = name
        self.observers = list(args)
        self.status = ""

    def observe(self, observer):
        """
        Подключение наблюдателя

        :param observer: Объект наблюдателя, который необходимо подключить
        :type observer: Observer
        """
        observer.subject = self
        self.observers.append(observer)

    def detach(self, observer):
        """
        Отключение наблюдателя

        :param observer: Объект наблюдателя, который необходимо отключить
        :type observer: Observer
        """
        observer.subject = None
        self.observers.remove(observer)

    def notify(self, text_format):
        """
        Оповещение всех наблюдателей

        :param text_format: Текст, который должен содержать следующие переменные форматирования:
        observer_name: Строковое представление наблюдателя,
        subject_name: Строковое представление объекта наблюдения,
        status: Новый статус объекта наблюдения
        :type text_format: str
        """
        for observer in self.observers:
            observer.update(self, text_format)

    def get(self):
        """
        Получить статус объекта

        :return: статус
        :rtype: str
        """
        return self.status

    def set(self, new_status):
        """
        Установить статус

        :param new_status: Новый статус, который необходимо установить
        :type new_status: str
        """
        self.status = new_status


class Observer:
    """
    Наблюдатель
    """
    def __init__(self, name):
        """
        Конструктор наблюдателя

        :param name: Строковое представление наблюдателя
        :type name: str
        """
        self.name = name
        self.subject = None
        self.status = ""

    def update(self, subject, text_format):
        """
        Этот метод вызывается объектом наблюдения. Выводит на экран текст, который содержит переменные форматирования:
        observer_name, subject_name, status

        :param subject: Объект наблюдения
        :type subject: Subject
        :param text_format: Текст, который должен содержать переменные форматирования:
        observer_name, subject_name, status
        :type text_format: str
        """
        self.status = subject.get()
        print(text_format.format(observer_name=self.name, subject_name=subject.name, status=self.status))
