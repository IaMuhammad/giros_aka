from rest_framework import serializers

from apps.models import Table, Meal, Order, OrderMeal


class TableModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('id', 'number', 'image')


class MealModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'name', 'type')


class OrderMealSerializer(serializers.Serializer):
    meal = serializers.IntegerField()
    quantity = serializers.IntegerField()


class OrderModelSerializer(serializers.ModelSerializer):
    meals = OrderMealSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = ('id', 'table', 'meals')

    def create_meals(self, meals, order):
        OrderMeal.objects.bulk_create([
            OrderMeal(
                order_id=order.pk,
                meal_id=item.get('meal'),
                quantity=item.get('quantity'),
            )
            for item in meals])

    def create(self, validated_data):
        meals = validated_data.pop('meals')
        order = super().create(validated_data)
        self.create_meals(meals, order)
        return order


class OrderDetailModelSerializer(OrderModelSerializer):
    table = serializers.SerializerMethodField()
    meals = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'table', 'meals')

    def get_table(self, obj: Order):
        return {
            'id': obj.table.pk,
            'number': obj.table.number,
        }

    def get_meals(self, obj: Order):
        meals = []
        for order_meal in obj.ordermeal_set.all():
            meals.append({
                'id': order_meal.id,
                'meal_id': order_meal.meal_id,
                'meal_name': order_meal.meal.name,
                'type': order_meal.meal.type,
                'quantity': order_meal.quantity
            })
        return meals
