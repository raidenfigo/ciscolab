# -*- coding: utf-8 -*-


import telnetlib
import time

tftp_server = b'10.124.113.69\n'
b12_gw = '10.74.43.22'
a12_gw = '10.74.43.6'
shn15_4f_gw = '10.74.43.50'
shn15_5f_gw = '10.74.43.46'
shn16_gw = '10.74.90.130'
shn4_15f_srg_gw = '10.74.46.74'
shn4_15f_ucbu_gw = '10.74.43.138'
shn4_13f_gw = '10.74.46.130'
shn7_12f_webex_gw = '10.140.106.178'


def do_tftp(tftp):
    tn.write(b'\ncopy running-config tftp:\n')
    time.sleep(1)
    tn.write(tftp)
    time.sleep(1)
    tn.write(b'\n')
    time.sleep(10)
    tn.write(b'\n')
    res = tn.read_very_eager()
    print(res, '\n')

    tn.close()


def telnet_b12():
    time.sleep(1)
    tn.read_until(b'Username:')
    time.sleep(1)
    tn.write(b'cisco\n')
    time.sleep(1)
    tn.read_until(b'Password: ')
    time.sleep(1)
    tn.write(b'cisco2017\n')
    time.sleep(1)


def telnet_a12():
    time.sleep(1)

    tn.read_until(b'Password: ')
    time.sleep(1)
    tn.write(b'cisco\n')
    time.sleep(1)
    tn.read_until(b'shn6-12f-gw>')
    time.sleep(1)
    tn.write(b'en\n')
    time.sleep(1)
    tn.read_until(b'Password: ')
    time.sleep(1)
    tn.write(b'cisco123!\n')
    time.sleep(1)


def telnet_shn15_4f():
    time.sleep(1)

    tn.read_until(b'Password: ')
    time.sleep(1)
    tn.write(b'cisco2017\n')
    time.sleep(1)
    tn.read_until(b'new_SHN15>')
    time.sleep(1)
    tn.write(b'en\n')
    time.sleep(1)
    tn.read_until(b'Password: ')
    time.sleep(1)
    tn.write(b'cisco2017\n')
    time.sleep(1)


def telnet_shn16():
    time.sleep(1)

    tn.read_until(b'Password: ')
    time.sleep(1)
    tn.write(b'cisco2017\n')
    time.sleep(1)
    tn.read_until(b'Podium-core-switch-new>')
    time.sleep(1)
    tn.write(b'en\n')
    time.sleep(1)
    tn.read_until(b'Password: ')
    time.sleep(1)
    tn.write(b'cisco123!\n')
    time.sleep(1)


def telnet_shn4_15f():
    time.sleep(1)
    tn.read_until(b'Username:')
    time.sleep(1)
    tn.write(b'sheli2\n')
    time.sleep(1)
    tn.read_until(b'Password: ')
    time.sleep(1)
    tn.write(b'cisco123!\n')
    time.sleep(1)


def telnet_shn4_15f_srg_gw():
    time.sleep(1)
    tn.read_until(b'Username:')
    time.sleep(1)
    tn.write(b'sheli2\n')
    time.sleep(1)
    tn.read_until(b'Password: ')
    time.sleep(1)
    tn.write(b'cisco123!\n')
    time.sleep(1)


def telnet_shn4_15f_ucbugw():
    time.sleep(1)
    tn.read_until(b'Username:')
    time.sleep(1)
    tn.write(b'zhennan\n')
    time.sleep(1)
    tn.read_until(b'password: ')
    time.sleep(1)
    tn.write(b'Lenovo5!\n')
    time.sleep(0.5)
    tn.read_until(b'SHN4-L15-GW-UCBU>')
    time.sleep(0.5)
    tn.write(b'en\n')
    time.sleep(0.5)
    tn.read_until(b'Password: ')
    time.sleep(0.5)
    tn.write(b'cisco123!\n')
    time.sleep(0.5)


def telnet_shn4_13f_gw():
    time.sleep(1)
    tn.read_until(b'Username:')
    time.sleep(1)
    tn.write(b'zhennan\n')
    time.sleep(1)
    tn.read_until(b'password: ')
    time.sleep(1)
    tn.write(b'Lenovo5!\n')
    time.sleep(0.5)
    tn.read_until(b'SHN4F13-GW-CABU>')
    time.sleep(0.5)
    tn.write(b'en\n')
    time.sleep(0.5)
    tn.read_until(b'Password: ')
    time.sleep(0.5)
    tn.write(b'greatcable!!\n')
    time.sleep(0.5)


def telnet_shn7_12f_webex_gw():
    time.sleep(1)
    tn.read_until(b'Username:')
    time.sleep(1)
    tn.write(b'zhennan\n')
    time.sleep(1)
    tn.read_until(b'password: ')
    time.sleep(1)
    tn.write(b'Lenovo5!\n')
    time.sleep(0.5)
    tn.read_until(b'SHN7-L12-GW-Webex>')
    time.sleep(0.5)
    tn.write(b'en\n')
    time.sleep(0.5)
    tn.read_until(b'Password: ')
    time.sleep(0.5)
    tn.write(b'cisco123!\n')
    time.sleep(0.5)


def telnet_shn15_5f_gw():
    time.sleep(1)
    tn.read_until(b'Username:')
    time.sleep(1)
    tn.write(b'zhennan\n')
    time.sleep(1)
    tn.read_until(b'password: ')
    time.sleep(1)
    tn.write(b'Lenovo5!\n')
    time.sleep(0.5)
    tn.read_until(b'S11-5F-lab-GW>')
    time.sleep(0.5)
    tn.write(b'en\n')
    time.sleep(0.5)
    tn.read_until(b'Password: ')
    time.sleep(0.5)
    tn.write(b'cisco123!\n')
    time.sleep(0.5)


tn = telnetlib.Telnet(b12_gw, port=23, timeout=20)
telnet_b12()
do_tftp(tftp_server)

tn = telnetlib.Telnet(shn15_4f_gw, port=23, timeout=20)
telnet_shn15_4f()
do_tftp(tftp_server)

tn = telnetlib.Telnet(shn16_gw, port=23, timeout=20)
telnet_shn16()
do_tftp(tftp_server)

tn = telnetlib.Telnet(shn4_15f_srg_gw, port=23, timeout=20)
telnet_shn4_15f_srg_gw()
do_tftp(tftp_server)

tn = telnetlib.Telnet(shn4_15f_ucbu_gw, port=23, timeout=20)
telnet_shn4_15f_ucbugw()
do_tftp(tftp_server)

tn = telnetlib.Telnet(shn4_13f_gw, port=23, timeout=20)
telnet_shn4_13f_gw()
do_tftp(tftp_server)

tn = telnetlib.Telnet(shn7_12f_webex_gw, port=23, timeout=20)
telnet_shn7_12f_webex_gw()
do_tftp(tftp_server)

tn = telnetlib.Telnet(shn15_5f_gw, port=23, timeout=20)
telnet_shn15_5f_gw()
do_tftp(tftp_server)

tn = telnetlib.Telnet(a12_gw, port=23, timeout=20)
time.sleep(1)
telnet_a12()
time.sleep(1)
do_tftp(tftp_server)

print('Finish')

# res = tn.read_very_eager()
# print(res,'\n')
# tn.close()