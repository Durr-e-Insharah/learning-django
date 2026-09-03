from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='book_covers/', blank=True, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer_name} - {self.book.title}"


class Bookstore(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='stores')

    def __str__(self):
        return self.name

class Award(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='award')
    award_name = models.CharField(max_length=100)
    year_won = models.IntegerField()

    def __str__(self):
        return f"{self.award_name} for {self.book.title}"
    
    