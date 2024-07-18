from django.db import models
#
#
# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     published_date = models.DateTimeField(auto_now_add=True, editable=True)
#     category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='books', null=True)
#
#     def __str__(self):
#         return self.title
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=60)
#     description = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name_plural = 'Categories'
#


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_card_number = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    group = models.ForeignKey('StudentGroup', on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class StudentGroup(models.Model):
    group_number = models.CharField(max_length=10, unique=True)
    motto = models.CharField(max_length=255)
    meeting_room = models.CharField(max_length=50)

    def __str__(self):
        return self.group_number


class LibraryCard(models.Model):
    student = models.OneToOneField('Student', on_delete=models.CASCADE, related_name='library_card')
    issue_date = models.DateField()
    expiry_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Library Card for {self.student.first_name} {self.student.last_name}"


class Literature(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    year = models.PositiveIntegerField()
    # year поле можна не додавати так, як вже є поле publication_date, але в дз воно було обов'язковим тому додав

    def __str__(self):
        return self.title


class BookBorrowingProcess(models.Model):
    library_card = models.ForeignKey(LibraryCard, on_delete=models.CASCADE, related_name='borrowings')
    literature = models.ForeignKey(Literature, on_delete=models.CASCADE, related_name='borrowings')
    borrow_date = models.DateField()
    librarian_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.literature.title} borrowed by {self.library_card.student}"

