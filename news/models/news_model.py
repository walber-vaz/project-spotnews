from django.core.exceptions import ValidationError
from django.db import models


def validate_not_single_word(value):
    words = value.split()
    if len(words) <= 1:
        raise ValidationError(
            "O título deve conter pelo menos 2 palavras.",
        )


class News(models.Model):
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        validators=[validate_not_single_word],
    )
    content = models.TextField(null=False, blank=False)
    author = models.ForeignKey(
        "Users", on_delete=models.CASCADE, null=False, blank=False
    )
    created_at = models.DateField(null=False, blank=False)
    image = models.ImageField(upload_to="img/", null=True, blank=True)
    categories = models.ManyToManyField("Categories")

    def __str__(self):
        return self.title
