from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    technologies = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 scale

    def __str__(self):
        return self.name

class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} at {self.institution}"

class Internship(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company}"

class Experience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company}"

class Contribution(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class CocurricularActivity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

class ResearchBlog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateField()
    url = models.URLField()

    def __str__(self):
        return self.title

class Thought(models.Model):
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]

class SocialProfile(models.Model):
    PLATFORM_CHOICES = [
        ('linkedin', 'LinkedIn'),
        ('github', 'GitHub'),
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('other', 'Other'),
    ]
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()

    def __str__(self):
        return self.get_platform_display()

