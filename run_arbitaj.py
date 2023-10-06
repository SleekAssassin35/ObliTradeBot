from api import BinanceAPI
client = BinanceAPI('[API key]','[API secret]')
client.set_offset()
import time
from veri_kontrol import veri_kontrol
from fiyatmonitor import mon
from arbitraj import Trades
from log import log_c


dc = veri_kontrol()
mn = mon()
lg = log_c()
tr = Trades()
ready = False

t = str(time.time())[:10]
f = open('log' + t + '.txt', 'w')
f.write('log file for run starting at time ' + str(time.time()))
f.close()
f_name = 'log' + t + '.txt'

lg.set_file(f_name)
mn.setfile(f_name)
dc.setfile(f_name)
tr.setfile(f_name)

while not ready:
    a = tr.get_open_ords('XLMBNB')
    b = tr.get_open_ords('BNBETH')
    c = tr.get_open_ords('XLMETH')
    d = tr.get_open_ords('XLMBTC')
    e = tr.get_open_ords('BNBBTC')
    f = tr.get_open_ords('ADABTC')
    g = tr.get_open_ords('ADAETH')
    h = tr.get_open_ords('ADABNB')

    if a ==[] and b == [] and c == [] and d == [] and e == [] and f == [] and g == [] and h == []:
        ready = True
        print('Ready!')
    else:
        print('Trades open, waiting.')
        time.sleep(int(5))

if ready:
    client.set_offset()
    mn.monitor()
