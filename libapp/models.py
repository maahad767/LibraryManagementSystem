from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name


class Book(models.Model):
    isbn = models.CharField(verbose_name='ISBN', max_length=256)
    title = models.CharField(max_length=512)
    cover = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    category = models.ManyToManyField(Category, related_name='books')
    pages = models.IntegerField()
    author = models.ForeignKey(Author, null=True, related_name='books', on_delete=models.SET_NULL)
    publisher = models.ForeignKey(Publisher, null=True, related_name='books', on_delete=models.SET_NULL)
    edition = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.title}({self.author})'


class Copy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='copies')
    copy = models.IntegerField(verbose_name='Copy Number')
    STATUS = [
        ('available', 'available'),
        ('borrowed', 'borrowed'),
    ]
    status = models.CharField(max_length=50, choices=STATUS)

    def __str__(self):
        return f'{self.book.title}(copy-{self.copy}, {self.status})'


class BookBorrowRecord(models.Model):
    copy = models.ForeignKey(Copy, on_delete=models.CASCADE, related_name='borrowed')
    # borrower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowed')
    borrower = models.CharField(max_length=256)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def return_book(self):
        self.return_date = timezone.now
    
    def __str__(self):
        return f'{self.copy.book} borrowed by {self.borrower}'


class BookSaleRecord(models.Model):
    copy = models.ForeignKey(Copy, on_delete=models.CASCADE, related_name='sold')
    customer = models.CharField(max_length=256)
    sale_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.copy.book} sold to {self.customer} at {self.sale_date}'


