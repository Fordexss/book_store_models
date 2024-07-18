from django.contrib import admin
from .models import Student, StudentGroup, LibraryCard, Literature, BookBorrowingProcess

admin.site.register(Student)
admin.site.register(StudentGroup)
admin.site.register(LibraryCard)
admin.site.register(Literature)
admin.site.register(BookBorrowingProcess)
