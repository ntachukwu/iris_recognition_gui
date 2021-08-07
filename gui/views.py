
import os
import sys
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from subprocess import run, PIPE
from .models import EnrollModel
import json, ast
import tempfile


def home_view(request):
    return render(request, "home.html")


def eval_casia1_view(request):
    path = '//{}//{}'.format(settings.BASE_DIR, "enroll_casia1.py")

    out = run([sys.executable, path], shell=False, stdout=PIPE)



    evaluation_quary = EnrollModel.objects.all()
    context = {
        "evaluation_quary": evaluation_quary
    }
    return render(request, "home.html", context)


def command_view(request):
    # input_value = request.POST.get('image_file')
    input_value = request.POST.get('test_value')

    path = '//{}//{}'.format(settings.BASE_DIR, "test.py")

    out = run([sys.executable, path, input_value], shell=False, stdout=PIPE)

    print(out.stdout.decode("utf-8"))

    return render(request, 'home.html', {'output': out.stdout.decode("utf-8")})


def verification_view(request):
    image_upload = request.FILES['image']
    fs = FileSystemStorage()
    filename = fs.save(image_upload.name, image_upload)
    image_fullpath = fs.open(filename)
    media_location = fs.url(filename)

    path = '//{}//{}'.format(settings.BASE_DIR, "verify.py")

    path_to_image = '//{}//'.format(settings.BASE_DIR) + media_location

    out = run([sys.executable, path, path_to_image], shell=False, stdout=PIPE)

    result = out.stdout.decode("utf-8")
    result = ast.literal_eval(result)

    if len(result) == 1:
        return render(request, 'home.html', {'message': result['error']})
    
    image_context = {}
    image_context["image_to_verify"] = media_location
    image_context["number_of_results"] = result["number_of_results"]
    image_context["verification_time"] = result["verification_time"]
    image_locations = []
    for each_image in result["positive_results_path"]:
        each_name = each_image.split("/")[-1]
        each_name = each_name
        lf = tempfile.NamedTemporaryFile(dir=settings.MEDIA_ROOT)
        f = open(each_image, 'rb')
        lf.write(f.read())

        filename = fs.save(each_name, File(lf))
        image_locations.append(fs.url(filename))
        lf.close()

        
    image_context["images"] = image_locations
    print(image_context)
    image_contexture = {
        "image_context": image_context
    }
    return render(request, 'home.html', image_contexture)
