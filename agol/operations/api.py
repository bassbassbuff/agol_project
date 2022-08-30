from django.shortcuts import get_object_or_404

from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SafetyChecklist
from customers.serializers import OrderSerializer
from .services import checklist_create, lab_create, loading_create, lab_results_create
from .selectors import order_list, checklist_details, labinspection_details, checklist_details_list, get_order
from .serializers import VehicleSerializer
class ChecklistCreateAPI(APIView):
    class InputSerializer(serializers.Serializer):
        order_id = serializers.CharField()
        question_id = serializers.IntegerField()
        checklist_choice = serializers.CharField()

    def post(self, request):
        # que = []
        # choices = []
        order = self.request.data['order']
        questions = self.request.data['questions']
        for index in range(len(questions)):
            question_list=list(questions[index].values())
            # print(question_list)
            checklist_choice = question_list[2]
            # print(checklist_choice)
            question = question_list[0]
            # que.append(question)
            # choices.append(checklist_choice)
            # print(choices)
            # print(que)
            serializer = self.InputSerializer(data={'order_id':order, 'question_id':question, 'checklist_choice':checklist_choice})
            serializer.is_valid(raise_exception=True)

            checklist_create(**serializer.validated_data)



        return Response(status=status.HTTP_201_CREATED)


class ChecklistListAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        trailer_details = VehicleSerializer(source="trailer", read_only=True)
        truck_details = VehicleSerializer(source="truck", read_only=True)


    def get(self, request):
        serializer = self.OutputSerializer(order_list('SAFETY'), many=True)
        print(serializer.data)
        return Response(serializer.data)


class ChecklistDetailAPI(APIView):
    
    class OutputSerializer(serializers.ModelSerializer):        
        class Meta:
            model = SafetyChecklist
            fields = ['question','checklist_choice', 'created_at']
            depth = 1


    def get(self, request, pk=None):
        serializer = self.OutputSerializer(checklist_details(pk), many=True)
        print(serializer.data)
        return Response(serializer.data)

# class ChecklistDetailApi(APIView):
#     def get(self, request, pk=None):
        

#         data = get_checklist_details(pk)

#         return Response(data)


class PrintSafetyListAPI(APIView):    
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        trailer_details = VehicleSerializer(source="trailer", read_only=True)
        truck_details = VehicleSerializer(source="truck", read_only=True)


    def get(self, request):
        serializer = self.OutputSerializer(checklist_details_list(), many=True)
        # serializer = SafetyChecklist.objects.filter().select_related().all()
        # print(serializer.data)
        return Response(serializer.data)


class LabInspectionListAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        trailer_details = VehicleSerializer(source="trailer", read_only=True)
        truck_details = VehicleSerializer(source="truck", read_only=True)


    def get(self, request):
        serializer = self.OutputSerializer(order_list('LAB'), many=True)
        print(serializer.data)
        return Response(serializer.data)

class LabInspectionCreateAPI(APIView):
    class InputSerializer(serializers.Serializer):
        pressure = serializers.IntegerField()
        oxygen = serializers.IntegerField()
        methane = serializers.IntegerField()
        order_id = serializers.IntegerField()

    def post(self, request):
        order = self.request.data['order']
        pressure = self.request.data['truck_pressure']
        oxygen = self.request.data['oxygen_content']
        methane = self.request.data['methane_content'] 
        serializer = self.InputSerializer(data={'order_id':order, 'pressure':pressure, 'oxygen':oxygen, 'methane':methane})
        serializer.is_valid(raise_exception=True)
        lab_create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

class LabResultsListAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        trailer_details = VehicleSerializer(source="trailer", read_only=True)
        truck_details = VehicleSerializer(source="truck", read_only=True)

    def get(self, request):
        serializer = self.OutputSerializer(order_list('LABRESULTS'), many=True)
        return Response(serializer.data)

class LabResultsCreateAPI(APIView):
    class InputSerializer(serializers.Serializer):
        order_status = serializers.CharField()        
        order_id = serializers.IntegerField()

    def post(self, serializer):
        order = self.request.data['order']
        order_status = self.request.data['status']
        serializer = self.InputSerializer(data={'order_id':order, 'order_status':order_status})
        serializer.is_valid(raise_exception=True)
        lab_results_create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

class LabInspectionDetailsAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        pressure = serializers.IntegerField()
        oxygen = serializers.IntegerField()
        methane = serializers.IntegerField()
        order_id = serializers.IntegerField()

    def get(self, serializer, pk=None):
        serializer = self.OutputSerializer(labinspection_details(pk), many=True)
        return Response(serializer.data)


class LabSealListAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        trailer_details = VehicleSerializer(source="trailer", read_only=True)
        truck_details = VehicleSerializer(source="truck", read_only=True)

    def get(self, request):
        serializer = self.OutputSerializer(order_list('SEAL'), many=True)
        return Response(serializer.data)

class LabVentListAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        trailer_details = VehicleSerializer(source="trailer", read_only=True)
        truck_details = VehicleSerializer(source="truck", read_only=True)

    def get(self, request):
        serializer = self.OutputSerializer(order_list('VENT'), many=True)
        return Response(serializer.data)

class LoadingListAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        trailer_details = VehicleSerializer(source="trailer", read_only=True)
        truck_details = VehicleSerializer(source="truck", read_only=True)

    def get(self, request):
        serializer = self.OutputSerializer(order_list('LOADING'), many=True)
        return Response(serializer.data)

class LoadingCreateAPI(APIView):
    class InputSerializer(serializers.Serializer):                
        order_id = serializers.IntegerField()
        net_weight = serializers.IntegerField()
        tare_weight = serializers.IntegerField()
        gross_weight = serializers.IntegerField()

    def post(self, serializer):
        order = self.request.data['order']
        net_weight = self.request.data['net_weight']
        tare_weight = self.request.data['tare_weight']
        gross_weight = self.request.data['gross_weight']    
        serializer = self.InputSerializer(data={'order_id':order, 'net_weight':net_weight, 'tare_weight':tare_weight, 'gross_weight':gross_weight})
        serializer.is_valid(raise_exception=True)
        loading_create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)
