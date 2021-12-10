from django.db import models
from django.conf import settings
from django.utils.timezone import now

# Create your models here.
class Category(models.Model):
    NotionTypeChoice = (
        ('p', 'Page Type'),
        ('d', 'Database Type'),
        ('b', 'Block Type'),
    )
    name = models.CharField(max_length=30,unique=True)
    parent_category = models.ForeignKey('self', blank=True, null=True, related_name='child',on_delete=models.CASCADE)
    notion_id = models.CharField(max_length=60,blank=True,null=True)
    notion_type = models.CharField( 'Notion ID Type',
        max_length=1,
        choices=NotionTypeChoice,  default='d')
    is_enable = models.BooleanField('Enable', default=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(default='no-slug', max_length=60, blank=True)
    index = models.IntegerField(default=0, verbose_name="Higher index will be priority")
    created_time = models.DateTimeField('Created Time', default=now)
    last_modified_time = models.DateTimeField('Last Modified', default=now)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('index',)

# just creating first, not sure gonna add this feature or not        
class Post(models.Model):
    Publish_STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    title = models.CharField(max_length=55)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete= models.CASCADE)
    slug = models.SlugField(default='no-slug', max_length=60, blank= True)
    tags = models.ManyToManyField('Tag', verbose_name='All Tags', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    publish_status = models.CharField(
        'Post Publish Status',
        max_length=1,
        choices=Publish_STATUS_CHOICES,
        default='d')
    published_time = models.DateTimeField('Published Time', default= now)
    created_time = models.DateTimeField('Created Time', default=now)
    last_modified_time = models.DateTimeField('Last Modified', default=now)

    def __str__(self):
        return self.title + ' | By ' + str(self.author)



# just creating first, not sure gonna add this feature or not 
class Tag(models.Model):
    """Post's Tags"""
    name = models.CharField('Tag Name', max_length=30, unique=True)
    slug = models.SlugField(default='no-slug', max_length=60, blank=True)
    created_time = models.DateTimeField('Created Time', default=now)
    last_modified_time = models.DateTimeField('Last Modified', default=now)

    def __str__(self):
        return self.name

    def get_article_count(self):
        return Post.objects.filter(tags__name=self.name).distinct().count()

    class Meta:
        ordering = ['name']