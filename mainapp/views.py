from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt

import datetime
from .models import Person
from .serializers import PersonSerializer


@api_view(["GET", "POST"])
@csrf_exempt
@permission_classes([AllowAny])
def person(request):
    iin = request.GET['iin']
    year = iin[:2]
    if int(year) >= 21:
        year = '19' + year
    else:
        year = '20' + year
    month, day = iin[2:4], iin[4:6]
    dob = day + '/' + month + '/' + year
    dob = datetime.datetime.strptime(dob, '%d/%m/%Y')
    age = (datetime.datetime.today() - dob) // datetime.timedelta(days=365.2425)
    if request.method == 'POST':
        person = PersonSerializer(data={'iin': iin, 'age': age})
        if person.is_valid():
            person.save()
            return Response({"iin": iin, "age": age}, status=201)
        else:
            return Response(status=400)

    return Response({"iin": iin, "age": age}, status=200)
