from django.db import models


class Books(models.Model):
    GENRE = (
        ('Ужасы', 'Ужасы'),
        ('Дедективы', 'Дедективы'),
        ('Научная фантастика', 'Научная фантастика'),
        ('Романтика', 'Романтика'),
        ('Психология', 'Психология')
    )
    image = models.ImageField(upload_to='books/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=30, choices=GENRE)
    time = models.TimeField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
