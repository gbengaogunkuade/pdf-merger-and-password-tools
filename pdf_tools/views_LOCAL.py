from django.shortcuts import render, get_object_or_404, redirect
from pdf_tools.models import PDFtoMerge, PDFToPassword
from pdf_tools.forms import PDFToMergeForm, PDFToPasswordForm
from django.contrib.auth.models import User

import PyPDF2
from pathlib import Path
import os


from django.core.files.storage import FileSystemStorage
from django.conf import settings        # import settings.py into views.py
import random



# Create your views here.


# # -------------------------------------------------------------------------
# # function to use for uploading MULTIPLE FILES UPLOAD AT ONCE to a model
# # -------------------------------------------------------------------------
# def merge_pdf(request):

#     # create/get current user session number
#     # ----------------------------------------------------------------------
#     # Get the current user session number
#     request.session.get('current_user_session_number')

#     if request.session.get('current_user_session_number'):
#         print(request.session.get('current_user_session_number'))

#     else:
#         # create a new current user session number
#         generated_Number = random.randrange(0, 1000000)
#         request.session['current_user_session_number'] = generated_Number
#         print(request.session.get('current_user_session_number'))

#     # ----------------------------------------------------------------------
#     # POST method
#     if request.method == 'POST':
#         form = PDFToMergeForm(request.POST, request.FILES)

#         files = request.FILES.getlist('pdf_file')  # where pdf_file is the field name in the model

#         if form.is_valid():
#             for f in files:
#                 PDFtoMerge.objects.create(user_session_id=request.session.get('current_user_session_number'), pdf_file=f)
#             return redirect('merge_pdf')

#     # GET method
#     else:
#         form = PDFToMergeForm()
#         context = {'form': form}
#         return render(request, 'pdf_tools/merge_pdf.html', context)

# ## -------------------------------------------------------------------------






# -------------------------------------------------------------------------------------------------------------
# home
# -------------------------------------------------------------------------------------------------------------
def home(request):
    # create/get current user session number
    # ----------------------------------------------------------------------
    # Get the current user session number
    request.session.get('current_user_session_number')

    if request.session.get('current_user_session_number'):
        print(request.session.get('current_user_session_number'))

    else:
        # create a new current user session number
        generated_Number = random.randrange(0, 1000000)
        request.session['current_user_session_number'] = generated_Number
        print(request.session.get('current_user_session_number'))

    # ----------------------------------------------------------------------


    # directory of previous merged pdf
    destination_path = settings.PDF_MERGE_URL_DESTINATION

    for item in destination_path.glob('*.pdf'):
        item.unlink()


    # directory of previous uploaded pdfs
    source_path = settings.PDF_MERGE_URL_SOURCE

    for item in source_path.glob('*.pdf'):
        item.unlink()



    # # directory of previous uploaded pdfs
    destination_dir = settings.PDF_PASSWORD_URL_DESTINATION

    for item in destination_dir.glob('*.pdf'):
        item.unlink()


    # # directory of previous uploaded pdfs
    source_dir = settings.PDF_PASSWORD_URL_SOURCE

    for item in source_dir.glob('*.pdf'):
        item.unlink()


    return render(request, 'pdf_tools/home.html')






# -------------------------------------------------------------------------
# function to use for uploading single files to a model field
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------
# merge pdf
# -------------------------------------------------------------------------------------------------------------
def merge_pdf(request):

    # create/get current user session number
    # ----------------------------------------------------------------------
    # Get the current user session number
    request.session.get('current_user_session_number')

    if request.session.get('current_user_session_number'):
        print(request.session.get('current_user_session_number'))

    else:
        # create a new current user session number
        generated_Number = random.randrange(0, 1000000)
        request.session['current_user_session_number'] = generated_Number
        print(request.session.get('current_user_session_number'))

    # ----------------------------------------------------------------------
    # POST method
    if request.method == 'POST':
        form = PDFToMergeForm(request.POST, request.FILES)

        existing_user_file, created = PDFtoMerge.objects.get_or_create(user_session_id=request.session.get('current_user_session_number'))

        if form.is_valid():
            pdf_file1 = form.cleaned_data['pdf_file1']
            pdf_file2 = form.cleaned_data['pdf_file2']
            pdf_file3 = form.cleaned_data['pdf_file3']
            pdf_file4 = form.cleaned_data['pdf_file4']
            pdf_file5 = form.cleaned_data['pdf_file5']
            pdf_file6 = form.cleaned_data['pdf_file6']

            if existing_user_file:
                existing_user_file.pdf_file1 = pdf_file1
                existing_user_file.pdf_file2 = pdf_file2
                existing_user_file.pdf_file3 = pdf_file3
                existing_user_file.pdf_file4 = pdf_file4
                existing_user_file.pdf_file5 = pdf_file5
                existing_user_file.pdf_file6 = pdf_file6
                existing_user_file.save()
            else:
                pass

        source_dir = settings.PDF_MERGE_URL_SOURCE

        destination_dir = settings.PDF_MERGE_URL_DESTINATION

        destination_file = open(Path(destination_dir, f'Merged_File.pdf'), 'wb')

        merger = PyPDF2.PdfFileMerger()

        for file in sorted(source_dir.glob('*.pdf'), key=os.path.getmtime):
            file = str(file)
            merger.append(file)

        merger.write(destination_file)
        merger.close()
        destination_file.close()
        return redirect('merge_pdf_complete')

    # GET method
    else:

        # directory of previous merged pdf
        destination_path = settings.PDF_MERGE_URL_DESTINATION

        for item in destination_path.glob('*.pdf'):
            item.unlink()


        form = PDFToMergeForm()

        # directory of previous uploaded pdfs
        source_path = settings.PDF_MERGE_URL_SOURCE

        for item in source_path.glob('*.pdf'):
            item.unlink()
        
        context = {'form': form}
        return render(request, 'pdf_tools/merge_pdf.html', context)

## -------------------------------------------------------------------------







# -------------------------------------------------------------------------------------------------------------
# merge pdf complete
# -------------------------------------------------------------------------------------------------------------
def merge_pdf_complete(request):
    # create/get current user session number
    # ----------------------------------------------------------------------
    # Get the current user session number
    request.session.get('current_user_session_number')

    if request.session.get('current_user_session_number'):
        print(request.session.get('current_user_session_number'))

    else:
        # create a new current user session number
        generated_Number = random.randrange(0, 1000000)
        request.session['current_user_session_number'] = generated_Number
        print(request.session.get('current_user_session_number'))

    # ----------------------------------------------------------------------

    try:
        # directory of previous uploaded pdfs
        source_path = settings.PDF_MERGE_URL_SOURCE

        for item in source_path.glob('*.pdf'):
            item.unlink()


        link = f'/media/merged_pdf/Merged_File.pdf'

        mylocation = settings.PDF_MERGE_URL_DESTINATION

        for file in mylocation.glob('*.pdf'):
            if file:
                myfile = file
                context = {'link': link, 'myfile': myfile}

            else:
                pass
        
        return render(request, 'pdf_tools/merge_pdf_complete.html', context)
    
    except:
        return redirect('merge_pdf')











# def password_pdf(request):
#     # create/get current user session number
#     # ----------------------------------------------------------------------
#     # Get the current user session number
#     request.session.get('current_user_session_number')

#     if request.session.get('current_user_session_number'):
#         print(request.session.get('current_user_session_number'))

#     else:
#         # create a new current user session number
#         generated_Number = random.randrange(0, 1000000)
#         request.session['current_user_session_number'] = generated_Number
#         print(request.session.get('current_user_session_number'))

#     # ----------------------------------------------------------------------
#     # POST method
#     if request.method == 'POST':

#         source_dir = settings.PDF_PASSWORD_URL_SOURCE

#         destination_dir = settings.PDF_PASSWORD_URL_DESTINATION

#         form = PDFToPasswordForm(request.POST, request.FILES)

#         if form.is_valid():
#             pdf_file = form.cleaned_data['pdf_file']
#             pdf_password = form.cleaned_data['pdf_password']
#             pdf_verify_password = form.cleaned_data['pdf_verify_password']

#             if pdf_password == pdf_verify_password:
#                 newform = form.save(commit=False)
#                 newform.user_session_id=request.session.get('current_user_session_number')
#                 form.save()


#                 source_dir = settings.PDF_PASSWORD_URL_SOURCE.glob('*.pdf')

#                 destination_file = open(Path(destination_dir, f'Protected_{pdf_file}'), 'wb')

#                 for file in source_dir:

#                     source_file = open(file, mode='rb')

#                     reader = PyPDF2.PdfFileReader(source_file)
#                     writer = PyPDF2.PdfFileWriter()

#                     for page in range(reader.numPages):
#                         writer.addPage(reader.getPage(page))

#                     # destination_file = open(Path(destination_dir, f'Protected_{pdf_file}'), 'wb')
#                     writer.encrypt(pdf_password)
#                     writer.write(destination_file)
#                     destination_file.close()                
#                     return redirect('password_pdf_complete')

#             else:
#                 return redirect('password_pdf')

#         else:
#             return redirect('password_pdf')


#     # GET method
#     else:

#         # # directory of previous uploaded pdfs
#         source_dir = settings.PDF_PASSWORD_URL_SOURCE

#         for item in source_dir.glob('*.pdf'):
#             item.unlink()


#         # # directory of previous uploaded pdfs
#         destination_dir = settings.PDF_PASSWORD_URL_DESTINATION

#         for item in destination_dir.glob('*.pdf'):
#             item.unlink()

#         # # # directory of previous uploaded pdfs
#         # source_dir = settings.PDF_PASSWORD_URL_SOURCE

#         # for item in source_dir.glob('*.pdf'):
#         #     item.unlink()

#         form = PDFToPasswordForm()
#         context = {'form': form}
#         return render(request, 'pdf_tools/password_pdf.html', context)




# variable for created file
created_file = ''



# -------------------------------------------------------------------------------------------------------------
# password pdf
# -------------------------------------------------------------------------------------------------------------
def password_pdf(request):
    # create/get current user session number
    # ----------------------------------------------------------------------
    # Get the current user session number
    request.session.get('current_user_session_number')

    if request.session.get('current_user_session_number'):
        print(request.session.get('current_user_session_number'))

    else:
        # create a new current user session number
        generated_Number = random.randrange(0, 1000000)
        request.session['current_user_session_number'] = generated_Number
        print(request.session.get('current_user_session_number'))

    # ----------------------------------------------------------------------
    # POST method
    if request.method == 'POST':

        source_dir = settings.PDF_PASSWORD_URL_SOURCE

        destination_dir = settings.PDF_PASSWORD_URL_DESTINATION

        form = PDFToPasswordForm(request.POST, request.FILES)

        existing_user_file, created = PDFToPassword.objects.get_or_create(user_session_id=request.session.get('current_user_session_number'))

        if form.is_valid():
            pdf_file = form.cleaned_data['pdf_file']
            pdf_password = form.cleaned_data['pdf_password']
            pdf_verify_password = form.cleaned_data['pdf_verify_password']

            if pdf_password == pdf_verify_password:
                if existing_user_file:
                    existing_user_file.pdf_file = pdf_file
                    existing_user_file.pdf_password = pdf_password
                    existing_user_file.save()
                else:
                    pass

                source_dir = settings.PDF_PASSWORD_URL_SOURCE.glob('*.pdf')

                destination_file = open(Path(destination_dir, f'Passworded_{pdf_file}'), 'wb')

                global created_file
                created_file = f'Passworded_{pdf_file}'

                for file in source_dir:

                    source_file = open(file, mode='rb')

                    reader = PyPDF2.PdfFileReader(source_file)
                    writer = PyPDF2.PdfFileWriter()

                    for page in range(reader.numPages):
                        writer.addPage(reader.getPage(page))

                    writer.encrypt(pdf_password)
                    writer.write(destination_file)
                    destination_file.close()
                    source_file.close()     # close the source_file back         
                    return redirect('password_pdf_complete')

            else:
                return redirect('password_pdf')

        else:
            return redirect('password_pdf')


    # GET method
    else:

        # # directory of previous uploaded pdfs
        destination_dir = settings.PDF_PASSWORD_URL_DESTINATION

        for item in destination_dir.glob('*.pdf'):
            item.unlink()


        form = PDFToPasswordForm()
        context = {'form': form}
        return render(request, 'pdf_tools/password_pdf.html', context)






# -------------------------------------------------------------------------------------------------------------
# password pdf complete
# -------------------------------------------------------------------------------------------------------------
def password_pdf_complete(request):
    # create/get current user session number
    # ----------------------------------------------------------------------
    # Get the current user session number
    request.session.get('current_user_session_number')

    if request.session.get('current_user_session_number'):
        print(request.session.get('current_user_session_number'))

    else:
        # create a new current user session number
        generated_Number = random.randrange(0, 1000000)
        request.session['current_user_session_number'] = generated_Number
        print(request.session.get('current_user_session_number'))

    # ----------------------------------------------------------------------

    # # directory of previous uploaded pdfs
    source_dir = settings.PDF_PASSWORD_URL_SOURCE

    for item in source_dir.glob('*.pdf'):
        item.unlink()


    link = f'/media/passworded_pdf/{created_file}'
    print(link)

    destination_dir = settings.PDF_PASSWORD_URL_DESTINATION

    for file in destination_dir.glob('*.pdf'):
        if file:
            myfile = file
            context = {'link': link, 'myfile': myfile}

        else:
            pass
    
    return render(request, 'pdf_tools/password_pdf_complete.html', context)






