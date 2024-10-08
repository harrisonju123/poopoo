from rest_framework import serializers
from pooapp.models.poops import Poops


class PoopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poops
        fields = '__all__'

    def create(self, validated_data):
        # Custom logic before saving
        print("Creating a new Poop instance")

        # Create the Poop instance
        poop_instance = Poops.objects.create(**validated_data)

        # Custom logic after saving
        print("Poop instance created with ID:", poop_instance.id)

        return poop_instance

    def update(self, instance, validated_data):
        # Custom logic before updating
        print("Updating Poop instance with ID:", instance.id)

        # Update the Poop instance
        instance.date = validated_data.get('date', instance.date)
        instance.difficulty = validated_data.get('difficulty', instance.difficulty)
        instance.save()

        # Custom logic after updating
        print("Poop instance updated with ID:", instance.id)

        return instance