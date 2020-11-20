# Li Ma: 95%
# Fan Lin: 5%
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import FileSerializer
from rest_framework import status
from vision_for_the_blind_2 import text as txt
from vision_for_the_blind_2 import caption_generator as capture
from os import path as path


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        try:
            file_serializer = FileSerializer(data=request.data)
            if file_serializer.is_valid():
                up_pic = request.FILES['file']
                new_path = path.dirname(path.abspath(__file__)) + up_pic.name
                destination = open(new_path,'wb+')
                for chunk in up_pic.chunks():
                    destination.write(chunk)
                destination.close()
                option = request.POST.get('option')
                if hasattr(request.POST, 'option'):
                    option = request.POST['option']
                if option and option == 'c':
                    print('image capturing...')
                    output = capture.capture_image(new_path)
                    return Response(output, status=status.HTTP_201_CREATED)
                else:
                    new_path = txt.image_bw(new_path)
                    output = txt.get_setence(new_path)
                    return Response(output, status=status.HTTP_201_CREATED)
            else:
                return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response("Something wrong", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
