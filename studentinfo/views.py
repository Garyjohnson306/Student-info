from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def student_form(request):
    if request.method == "POST":
        student_name = request.POST.get("student_name")
        student_id = request.POST.get("student_id")

        if not student_name or not student_id:
            return HttpResponse("Please fill out student name and student ID to proceed.")
        
        else:
            major = request.POST.get("major")
            class_standing = request.POST.get("class_standing")
            graduation_year = request.POST.get("graduation_year")
            languages = request.POST.getlist("languages")
            comments = request.POST.get("comments")
    else:
        return render(request, "studentinfo/student_form.html")

    requested = {
        "student_name": student_name,
        "student_id": student_id,
        "major": major,
        "class_standing": class_standing,
        "graduation_year": graduation_year,
        "languages": languages,
        "comments": comments
    }

    return render(request, "studentinfo/results.html", requested)