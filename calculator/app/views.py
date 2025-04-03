from django.shortcuts import render

def home(request):
    result = None  

    if request.method == "POST":
        try:
            num1 = float(request.POST.get("value1", 0))  
            num2 = float(request.POST.get("value2", 0))
            opr = request.POST.get("opr")

            if opr == "+":
                result = num1 + num2
            elif opr == "-":
                result = num1 - num2
            elif opr == "/":
                result = "Not Possible" if num2 == 0 else num1 / num2  
            elif opr == "*":
                result = num1 * num2
            else:
                result = "Invalid Operator"
        except ValueError:
            result = "Invalid Input"

    return render(request, "index.html", {"c": result}) 
