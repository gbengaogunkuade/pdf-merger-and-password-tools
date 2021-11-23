from django import forms
from django.core import validators
from django.utils import timezone
from django.contrib.auth.models import User
from pdf_tools.models import PDFtoMerge, PDFToPassword
from PIL import Image




# # ----------------------------------------------------------------------------------------------------------------------
# # form to use for uploading multiple files to a model field
# # ----------------------------------------------------------------------------------------------------------------------
# class PDFToMergeForm(forms.ModelForm):
#     pdf_file = forms.FileField(label='pdf_file', widget=forms.ClearableFileInput(attrs={'placeholder':'file', 'class':'form-control gbengaForm','multiple': True}))
# # ----------------------------------------------------------------------------------------------------------------------




class PDFToMergeForm(forms.ModelForm):
    pdf_file1 = forms.FileField(label='pdf_file1', widget=forms.ClearableFileInput(attrs={'placeholder':'pdf_file1', 'class':'form-control gbengaForm'}))
    pdf_file2 = forms.FileField(label='pdf_file2', widget=forms.ClearableFileInput(attrs={'placeholder':'pdf_file2', 'class':'form-control gbengaForm'}))
    pdf_file3 = forms.FileField(label='pdf_file3', widget=forms.ClearableFileInput(attrs={'placeholder':'pdf_file3', 'class':'form-control gbengaForm'}), required=False)
    pdf_file4 = forms.FileField(label='pdf_file4', widget=forms.ClearableFileInput(attrs={'placeholder':'pdf_file4', 'class':'form-control gbengaForm'}),required=False)
    pdf_file5 = forms.FileField(label='pdf_file5', widget=forms.ClearableFileInput(attrs={'placeholder':'pdf_file5', 'class':'form-control gbengaForm'}), required=False)
    pdf_file6 = forms.FileField(label='pdf_file6', widget=forms.ClearableFileInput(attrs={'placeholder':'pdf_file6', 'class':'form-control gbengaForm'}), required=False)


    class Meta:
        model = PDFtoMerge
        fields = [
            'pdf_file1',
            'pdf_file2',
            'pdf_file3',
            'pdf_file4',
            'pdf_file5',
            'pdf_file6',
        ]








class PDFToPasswordForm(forms.ModelForm):
    pdf_file = forms.FileField(widget=forms.ClearableFileInput(attrs={'placeholder':'pdf_file', 'class':'form-control gbengaForm'}))
    pdf_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password', 'class':'form-control gbengaForm'}), required=True)
    pdf_verify_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'verify password', 'class':'form-control gbengaForm'}), required=True)

    class Meta:
        model = PDFToPassword
        fields = [
            'pdf_file',
            'pdf_password',
            'pdf_verify_password',
        ]




