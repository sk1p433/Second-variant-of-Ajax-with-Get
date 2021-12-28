def simple_ajax(request):
    usernames = User.objects.all().values("username")
    return render(request, 'store/simple_ajax.html', {"usernames": usernames})

def simple_ajax_test(request):
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if request.method == "GET" and is_ajax:
        username = request.GET.get("username")
        user = User.objects.get(username=username)
        user_info = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "is_active": user.is_active,
            "joined": user.date_joined
            }
        return JsonResponse({"user_info": user_info}, status=200)
    else:
        return JsonResponse({"success": False}, status=400)
