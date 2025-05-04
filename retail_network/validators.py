from rest_framework import serializers


class DebtValidator:
    """
    Валидатор проверки задолженности. У завода (нулевого звена) не может быть задолженности.
    """

    def __init__(self, provider, debt):
        self.provider = provider
        self.debt = debt

    def __call__(self, value):
        provider_field = value.get(self.provider)
        debt_field = value.get(self.debt)

        if not provider_field and debt_field > 0.0:
            raise serializers.ValidationError(
                "Чтобы ввести размер задолженности, укажите поставщика"
            )
