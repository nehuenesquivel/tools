basic_salary_in_usd = float(input("basic salary in usd: "))

usd_value_in_ars = float(input("usd value in ars: "))

basic_salary_in_ars = basic_salary_in_usd * usd_value_in_ars

sijp = basic_salary_in_ars * 0.11

inssjp = basic_salary_in_ars * 0.03

osoc = basic_salary_in_ars * 0.03

deductions = sijp + inssjp + osoc

net_received = basic_salary_in_ars - deductions

net_received_in_ars = net_received * 0.3

net_received_in_usd = net_received * 0.7 / usd_value_in_ars

print("basic salary in ars: " + str(basic_salary_in_ars) + "\n")

print("sijp: " + str(sijp))

print("inssjp: " + str(inssjp))

print("osoc: " + str(osoc))

print("deductions: " + str(deductions) + "\n")

print("net received: " + str(net_received))

print("net received in ars: " + str(net_received_in_ars))

print("net received in usd: " + str(net_received_in_usd))
