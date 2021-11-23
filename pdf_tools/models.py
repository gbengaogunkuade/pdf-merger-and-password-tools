from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image



# Create your models here.

class PDFtoMerge(models.Model):
    user_session_id = models.TextField(null=True, blank=True)
    pdf_file1 = models.FileField(upload_to='pdf_files_for_merging/', default='default.pdf')
    pdf_file2 = models.FileField(upload_to='pdf_files_for_merging/', default='default.pdf')
    pdf_file3 = models.FileField(upload_to='pdf_files_for_merging/', default='default.pdf', null=True, blank=True)
    pdf_file4 = models.FileField(upload_to='pdf_files_for_merging/', default='default.pdf', null=True, blank=True)
    pdf_file5 = models.FileField(upload_to='pdf_files_for_merging/', default='default.pdf', null=True, blank=True)
    pdf_file6 = models.FileField(upload_to='pdf_files_for_merging/', default='default.pdf', null=True, blank=True)


    # THE MODEL ADMIN "VERBOSE NAME PLURAL"
    class Meta:
        verbose_name_plural = "PDFtoMerge"


    # # Display the Title in the ADMIN page instead of the modelName
    def __str__(self):
        return self.user_session_id









class PDFToPassword(models.Model):
    user_session_id = models.TextField(null=True, blank=True)
    pdf_file = models.FileField(upload_to='pdf_files_for_passwording/', default='default.pdf')
    pdf_password = models.CharField(max_length=200)


    # THE MODEL ADMIN "VERBOSE NAME PLURAL"
    class Meta:
        verbose_name_plural = "PDFToPassword"


    # # Display the Title in the ADMIN page instead of the modelName
    def __str__(self):
        return self.user_session_id



