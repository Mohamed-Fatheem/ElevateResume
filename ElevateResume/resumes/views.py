from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Resume
import spacy
from xhtml2pdf import pisa

nlp = spacy.load("en_core_web_sm")

def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'resumes/resume_list.html', {'resumes': resumes})

def resume_form(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        doc = nlp(content)
        keywords = [token.text for token in doc if token.is_stop is False and token.is_punct is False]
        resume = Resume(content=content, keywords=keywords)
        resume.save()
        return redirect('resume_list')
    return render(request, 'resumes/resume_form.html')

def generate_pdf(request, id):
    resume = Resume.objects.get(id=id)
    template_path = 'resumes/resume_pdf.html'
    context = {'resume': resume}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors with code %s' % pisa_status.err)
    return response
