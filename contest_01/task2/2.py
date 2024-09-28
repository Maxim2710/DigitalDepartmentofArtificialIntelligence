import math

oxygen_per_day = 0.5
days_in_year = 365
oak_oxygen_per_year = 20
poplar_oxygen_per_year = 32

oxygen_per_year_for_person = oxygen_per_day * days_in_year

required_oaks = oxygen_per_year_for_person / oak_oxygen_per_year
required_poplars = oxygen_per_year_for_person / poplar_oxygen_per_year

required_oaks_rounded = math.ceil(required_oaks)
required_poplars_rounded = math.ceil(required_poplars)

print(oxygen_per_year_for_person, required_poplars_rounded, required_oaks_rounded)
