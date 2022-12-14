# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

import random

random_nums = [random.randint(1, 50) for _ in range(20)]
print(f'Список пар, где сумма кортежа кратна 5 -> {list(filter(lambda x: (x[0]+x[1])%5==0, enumerate(random_nums)))}')