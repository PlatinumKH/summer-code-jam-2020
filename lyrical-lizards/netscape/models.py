class Category(models.Model):
 ###  
class Album(models.Model):   
    category = models.ForeignKey(Category, related_name='albums')
 ###
class Image(models.Model):
    album = models.ForeignKey(Album)
    image = models.ImageField(upload_to = 'images/albums/')