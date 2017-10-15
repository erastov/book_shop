from django.db import models

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    fio = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)

    def __str__(self):
        return str(self.fio)


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    fio = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    salary = models.FloatField(default=0)

    def __str__(self):
        return str(self.fio)


class PublishingHouse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    SUBJECT_CHOICES = (
    ('ХУДОЖЕСТВЕННАЯ ЛИТЕРАТУРА', (
    ('Детектив', 'Детектив'),
    ('Поэзия. Драматургия', 'Поэзия. Драматургия'),
    ('Фантастика', 'Фантастика'),
    ('Зарубежная проза', 'Зарубежная проза'),
    ('Российская проза', 'Российская проза')
      )
    ),
    ('ДЕТСКАЯ ЛИТЕРАТУРА', (
    ('Детское творчество и досуг', 'Детское творчество и досуг'),
    ('Книги для самых маленьких', 'Книги для самых маленьких'),
    ('Художественная литература для детей', 'Художественная литература для детей')
      )
    ),
    ('БИОГРАФИИ. МЕМУАРЫ. ПУБЛИЦИСТИКА', (
    ('Биографии', 'Биографии'),
    ('Мемуары. Дневники. Письма', 'Мемуары. Дневники. Письма'),
    ('Публицистика, трэвелоги', 'Публицистика, трэвелоги')
      )
    ),
    ('КНИГИ ПО ИСКУССТВУ', (
    ('Архитектура. Градостроительство', 'Архитектура. Градостроительство'),
    ('Дизайн', 'Дизайн'),
    ('Живопись. Графика', 'Живопись. Графика'),
    ('Зрелищные виды искусств, кино', 'Зрелищные виды искусств, кино'),
    ('Мода', 'Мода'),
    ('Музыка', 'Музыка'),
    ('Фотоискусство', 'Фотоискусство')
      )
    ),
    ('ЛИТЕРАТУРА НА ИНОСТРАННЫХ ЯЗЫКАХ', (
    ('Книги на английском языке', 'Книги на английском языке'),
    ('Книги на немецком языке', 'Книги на немецком языке'),
    ('Книги на прочих языках мира', 'Книги на прочих языках мира'),
    ('Книги на французском языке', 'Книги на французском языке')
      )
    ),
    ('ИЗУЧЕНИЕ ИНОСТРАННЫХ ЯЗЫКОВ', (
    ('Английский язык', 'Английский язык'),
    ('Многоязычные словари, разговорники', 'Многоязычные словари, разговорники'),
    ('Немецкий язык', 'Немецкий язык'),
    ('Русский язык', 'Русский язык'),
    ('Русский язык для иностранцев', 'Русский язык для иностранцев')
      )
    ),
    ('unknown', 'Unknown'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    publishing_house = models.ForeignKey(PublishingHouse)
    author = models.CharField(max_length=100, null=True) 
    subject = models.CharField(
        max_length=100,
        choices=SUBJECT_CHOICES,
        default='unknown',
    )
    year = models.PositiveSmallIntegerField(null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField(null=True)
    image = models.ImageField(upload_to='static/image/book_covers', blank=True, null=True)

    def clean(self, *args, **kwargs):
        super(Book, self).clean(*args, **kwargs)
        if not self.image:
            raise ValidationError('Please provide an image')

    def __str__(self):
        return str(self.name + ' ' + self.author)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer)
    employee = models.ForeignKey(Employee)
    date = models.DateField(null=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return str(str(self.date) + ' ' + str(self.customer))


class MoreAboutOrder(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order)
    book = models.ForeignKey(Book)
    count = models.IntegerField(null=True)

    def __str__(self):
        return str(str(self.order) + ' ' + str(self.book))


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(null=True)
    customer = models.ForeignKey(Customer)
    book = models.ForeignKey(Book)
    text = models.TextField(null=True, max_length=500)

    def __str__(self):
        return str(str(self.book) + ' ' + str(self.customer))


