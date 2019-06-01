from django.db import models

class hello_models(models.Model):
    Column1 = models.TextField(default="Column1_df")
    Column2 = models.TextField(default="Column2_df")
    Column3 = models.DateTimeField(auto_now=True)
    Column4 = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "APPppp"