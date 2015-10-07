from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from .models import DeviceToken


@require_POST
@csrf_exempt
def register_device(request):
    if request.method == 'GET':
        # Just to make testing a little easier. Uncomment @require_POST above to use this
        return HttpResponse("""
<form action="/apns/register_device/" method="post">
    <input type="text" name="token">
    <input type="submit">
</form>
        """)

    if 'token' not in request.POST:
        return HttpResponse("Missing token", status=400)

    DeviceToken.objects.create(token=request.POST['token'])

    return HttpResponse()
