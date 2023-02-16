### Desafio TDD

def caixinha_magica3(para1, para2):
    resp_caixinha = para1-para2
    if resp_caixinha >= 0:
        return resp_caixinha
    if resp_caixinha < 0:
        return 0

caixinha_magica3(1,5)

assert caixinha_magica3(20, 15) == 5
assert caixinha_magica3(20, 10) == 10
assert caixinha_magica3(10, 10) == 0
assert caixinha_magica3(10, 15) == 0
assert caixinha_magica3(30, 45) == 0