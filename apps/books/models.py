from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import TextField, CharField, SlugField, DateField, TextChoices, IntegerField, ImageField, \
    URLField, ManyToManyField, ForeignKey, CASCADE

from apps.shared.models import AbstractModel


class LanguageChoice(TextChoices):
    ENGLISH = 'en', 'English'
    FRANCE = 'fr', 'French'
    RUSSIAN = 'ru', 'Russian'
    ARABIC = 'ar', 'Arabic'
    UZBEK = 'uz', 'Uzbek'


class Books(AbstractModel):
    title = CharField(max_length=128)
    slug = SlugField(unique=True)
    description = TextField()
    published = DateField()
    isbn = CharField(unique=True, max_length=18)
    language = CharField(max_length=7, choices=LanguageChoice.choices, default=LanguageChoice.ENGLISH)
    page = IntegerField()
    picture = ImageField(upload_to='media', default='media/book.png')
    genre = ManyToManyField('books.BookGenre', related_name='books')
    author = ManyToManyField('books.BookAuthor', related_name='books')


class BookAuthor(AbstractModel):
    first_name = CharField(max_length=128)
    last_name = CharField(max_length=128)
    birthdate = DateField()
    website = URLField()
    avatar = ImageField(upload_to='media', default='media/avatar.jpg')
    about = TextField()


class BookGenre(AbstractModel):
    name = CharField(max_length=128)


class BookReview(AbstractModel):
    book = ForeignKey("books.Books", CASCADE, "reviews")
    user = ForeignKey("users.User", CASCADE, "reviews")
    body = TextField()
    rating = IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    like_count = IntegerField(default=0)

    def __str__(self):
        return f"Review by {self.user.username}"

    def increment_like_count(self):
        self.like_count += 1
        self.save()
        return self.like_count