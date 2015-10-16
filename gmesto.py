__author__ = 'pika'
import random

glavna_mesta = {
    "nizozemska": "amsterdam",
    "slovenija": "ljubljana",
    "srbija": "beograd",
    "nemcija": "berlin",
    "svica": "bern",
    "francija": "paris"
}

def prestolnica(drzava):
    if drzava in glavna_mesta:
        return glavna_mesta[drzava] #vrne key iz sifranta - mesto, ki spada k drzavi
    else:
        return False

def preveri_glavno_mesto(glavno_mesto, drzava):
    if glavno_mesto == prestolnica(drzava): #poklices rezultat zgornje funkcije PRESTOLNICA
        return True
    else:
        return False

random = random.sample(glavna_mesta, 1)[0]
print random


tocke = 0
for drzava in glavna_mesta:
    gl_mesto = raw_input("Vnesi glavno mesto za drzavo %s " % drzava)
    uganil = preveri_glavno_mesto(gl_mesto, drzava)#zazenemo funkcijo PREVERI_GLAVNIO_MESTO, kjer je vnos gl_mesto
    if uganil == True:
        tocke += 1 #poveca toke za +1
    # print uganil #vrne samo True ali False

print "Bravo, uganil si %d krat" % tocke
