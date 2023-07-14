import locale
from decimal import Decimal


def formatar_em_kwanza(value: float, /, *, prefix=None, sufix=None) -> str:
    """Retorna o valor passado com o formato da moeda local"""
    if value != '' and value is not None:
        locale.setlocale(locale.LC_MONETARY, locale.getlocale())
        format_monetary = locale.currency(value, symbol=False, grouping=True)
        if prefix:
            return f'{prefix} {format_monetary}'
        elif sufix:
            return f'{format_monetary} {sufix}'
        return f'{format_monetary}'
    return str(Decimal('0.00')).replace(',', '.')
