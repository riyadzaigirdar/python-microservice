import random
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from product import serializers, models, producer


class ProductView(viewsets.ViewSet):

    def find_product(self, id):
        try:
            product = models.Product.objects.get(id=id)
            return product
        except:
            return None

    def list(self, request):
        products = models.Product.objects.all()
        serializer = serializers.ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = serializers.ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            producer.publish_product(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'msg': 'bad request'}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        product = self.find_product(pk)
        if not product:
            return Response({'msg': 'product not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.ProductSerializer(instance=product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        product = self.find_product(pk)
        if not product:
            return Response({'msg': 'product not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ProductSerializer(
            instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({'msg': 'bad request', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        product = self.find_product(pk)
        if not product:
            return Response({'msg': "product not found"}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({'msg': 'product deleted'}, status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):

    def get(self, _):
        users = models.User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })
