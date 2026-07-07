"""
Módulo responsável pelo cálculo da taxa de entrega do LocalEats.

Regra de negócio:
- Taxa fixa base de R$ 5,00
- Adicional de R$ 1,50 por quilômetro de distância
- Frete grátis para pedidos com valor total igual ou superior a R$ 100,00
"""

TAXA_BASE = 5.0
TAXA_POR_KM = 1.5
VALOR_FRETE_GRATIS = 100.0


def calculate_delivery_fee(distance_km: float, order_total: float) -> float:
    """
    Calcula a taxa de entrega com base na distância e no valor do pedido.

    Args:
        distance_km: distância em quilômetros até o endereço de entrega.
        order_total: valor total do pedido.

    Returns:
        Valor da taxa de entrega (0.0 caso o pedido tenha direito a frete grátis).
    """
    if distance_km < 0:
        raise ValueError("A distância não pode ser negativa.")
    if order_total < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")

    if order_total >= VALOR_FRETE_GRATIS:
        return 0.0

    return round(TAXA_BASE + (TAXA_POR_KM * distance_km), 2)