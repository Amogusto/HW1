sec_in = int(input("Введите количество секунд"))

s = sec_in % 60
m_in = sec_in // 60
m = m_in % 60
h = m_in // 60
if h < 10:
    h = "0" + str(h)
if m < 10:
    m = "0" + str(m)
if s < 10:
    s = "0" + str(s)
print(f"{h}:{m}:{s}")
