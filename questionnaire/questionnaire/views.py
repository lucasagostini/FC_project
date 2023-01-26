from django.shortcuts import render
from questionnaire.models import Answer, Question

def questionnaire(request):
    if request.method == "POST":
        # Collect answers and save to database
        for i in range(1, 6):
            question = Question.objects.get(order=i)
            answer = request.POST["answer-" + str(i)]
            a = Answer(question=question, answer=answer)
            a.save()
        return render(request, "thankyou.html")
    else:
        # Render questionnaire
        return render(request, "questionnaire.html")

def thankyou(request):
    return render(request, "thankyou.html")