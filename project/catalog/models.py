from django.db import models
from django.core.exceptions import ValidationError

Book_Categories = [
    ("PRODUCTIVITY_HABITS", "Productivity & Habits"),
    ("MINDSET_THINKING", "Mindset & Thinking"),
    ("PERSONAL_FINANCE", "Personal Finance"),
    ("BUSINESS_LEADERSHIP", "Business & Leadership"),
    ("MOTIVATION_MENTAL_TOUGHNESS", "Motivation & Mental Toughness"),
    ("SPIRITUALITY_MINDFULNESS", "Spirituality & Mindfulness"),
    ("HEALTH_SCIENCE", "Health & Science"),
    ("RELATIONSHIPS", "Relationships"),
]


class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=13, unique=True)
    category = models.CharField(
        max_length=30, choices=Book_Categories, default="PRODUCTIVITY_HABITS"
    )
    image = models.ImageField(upload_to="book_covers/", blank=True, null=True)
    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["available_copies"]

    def __str__(self):
        return self.title

    def clean(self):
        if self.available_copies > self.total_copies:
            raise ValidationError("Available copies must not exceed total copies.")
