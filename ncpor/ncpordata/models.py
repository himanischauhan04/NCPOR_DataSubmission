from django.db import models

# -------------------------------
# Dropdown choices (for select fields)
# -------------------------------
EXPEDITION_TYPE_CHOICES = [
    ('Antarctic', 'Antarctic'),
    ('Arctic', 'Arctic'),
    ('Southern Ocean', 'Southern Ocean'),
    ('Himalaya', 'Himalaya'),
]

ISO_TOPIC_CHOICES = [
    ('Environment', 'Environment'),
    ('Oceans', 'Oceans'),
    ('Climatology', 'Climatology'),
    ('Geoscientific Information', 'Geoscientific Information'),
    ('Biota', 'Biota'),
]

SCIENCE_CATEGORY_CHOICES = [
    ('Atmospheric Science', 'Atmospheric Science'),
    ('Biological Science', 'Biological Science'),
    ('Cryospheric Science', 'Cryospheric Science'),
    ('Geoscience', 'Geoscience'),
    ('Marine Science', 'Marine Science'),
]

SCIENCE_TOPIC_CHOICES = [
    ('Climate', 'Climate'),
    ('Oceanography', 'Oceanography'),
    ('Glaciology', 'Glaciology'),
    ('Ecology', 'Ecology'),
    ('Geology', 'Geology'),
]

COUNTRY_CHOICES = [
    ('India', 'India'),
    ('USA', 'USA'),
    ('UK', 'UK'),
    ('Australia', 'Australia'),
    ('Germany', 'Germany'),
]

STATE_CHOICES = [
    ('Maharashtra', 'Maharashtra'),
    ('Delhi', 'Delhi'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Karnataka', 'Karnataka'),
    ('Gujarat', 'Gujarat'),
]

DATASET_PROGRESS_CHOICES = [
    ('Complete', 'Complete'),
    ('In Progress', 'In Progress'),
    ('Planned', 'Planned'),
]

# -------------------------------
# Base models
# -------------------------------
class Institute(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

class Project(models.Model):
    title = models.CharField(max_length=300)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    year = models.IntegerField()

class Expedition(models.Model):
    number = models.IntegerField()
    year = models.IntegerField()

class Member(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    expedition = models.ForeignKey(Expedition, on_delete=models.CASCADE)

class Station(models.Model):
    name = models.CharField(max_length=100)

# -------------------------------
# Metadata form model
# -------------------------------

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.country.name})"

class ScienceCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ScienceTopic(models.Model):
    category = models.ForeignKey(ScienceCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Metadata(models.Model):
    # Expedition Details
    expedition_type = models.CharField(max_length=50, choices=EXPEDITION_TYPE_CHOICES)
    metadata_title = models.CharField(max_length=300)

    # Science Keywords
    science_category = models.ForeignKey(ScienceCategory, on_delete=models.SET_NULL, null=True)
    science_topic = models.ForeignKey(ScienceTopic, on_delete=models.SET_NULL, null=True)

    # ISO and Expedition
    iso_topic = models.CharField(max_length=100, choices=ISO_TOPIC_CHOICES)
    expedition_year = models.CharField(max_length=10)
    expedition_no = models.CharField(max_length=50, blank=True)

    # Project
    project_no = models.CharField(max_length=50)
    project_name = models.CharField(max_length=200)

    # Summary
    abstract = models.TextField()
    purpose = models.TextField()

    # Dataset Citation
    creator = models.CharField(max_length=100)
    editor = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    series_name = models.CharField(max_length=200)
    release_date = models.DateField()
    release_place = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    online_resource = models.URLField()

    # Scientist Info
    role = models.CharField(max_length=50)
    scientist_title = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)

    institute = models.TextField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    postal_code = models.CharField(max_length=20)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)

    # GPS
    gps = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')])

    # Dataset Progress
    dataset_progress = models.CharField(max_length=100, choices=DATASET_PROGRESS_CHOICES)

    # Instrument Details
    instrument_short_name = models.CharField(max_length=100, blank=True)
    instrument_long_name = models.CharField(max_length=100, blank=True)

    # Location
    location = models.CharField(max_length=100)
    subregion = models.CharField(max_length=100)

    # Data Resolution
    latitude_resolution_deg = models.CharField(max_length=10, blank=True)
    latitude_resolution_min = models.CharField(max_length=10, blank=True)
    latitude_resolution_sec = models.CharField(max_length=10, blank=True)

    longitude_resolution_deg = models.CharField(max_length=10, blank=True)
    longitude_resolution_min = models.CharField(max_length=10, blank=True)
    longitude_resolution_sec = models.CharField(max_length=10, blank=True)

    horizontal_resolution_range = models.CharField(max_length=100, blank=True)
    vertical_resolution = models.CharField(max_length=100, blank=True)
    vertical_resolution_range = models.CharField(max_length=100, blank=True)
    temporal_resolution = models.CharField(max_length=100, blank=True)
    temporal_resolution_range = models.CharField(max_length=100, blank=True)

    # Platform
    platform_short_name = models.CharField(max_length=100)
    platform_long_name = models.CharField(max_length=100)

    dataset_file = models.FileField(upload_to='datasets/', null=True, blank=True)
    old_data = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.metadata_title








    



