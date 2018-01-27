import RPi.GPIO as GPIO
import time
import sqlite3
import requests
import json
import pygame.mixer
import vlc
from pytz import timezone
from datetime import datetime
from beebotte import *
_accesskey  = 'fbabe9a5aa4d947d18b57a3e0296d724'
_secretkey  = '6421321cf8711279d041076edf1d737977a62a7792ffa9e0473fc5827128a536'
_hostname   = 'api.beebotte.com'
bbt = BBT( _accesskey, _secretkey, hostname = _hostname)
dbname = './db/development.sqlite3'
con = sqlite3.connect(dbname)
cur = con.cursor()
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.IN)
def json_data():
    response = requests.get('http://localhost:3000/users/1.json').text
    json_data = json.loads(response)
    return json_data
def alarm_music(song_name):
    player = vlc.MediaPlayer(song_name)
    player.audio_set_volume(100)
    player.play()
def measure_time(s_t,pin):
    print("OK")
    end_t = time.time()
    h_or_l = GPIO.input(pin)
    if h_or_l == GPIO.HIGH:
        return 1
    if end_t - s_t > 5:
        return 2
    return 0
def write_start():
    response = requests.get('http://localhost:3000/users/1.json').text
    json_data = json.loads(response)
    set_at = timezone('Asia/Tokyo').localize(datetime(2016, 1, 1,json_data["set_hour"],json_data["set_min"]))
    sleep_datum = (None,set_at,datetime.now(timezone('UTC')).strftime("%Y-%m-%d %H:%M:%S"),datetime.now(timezone('UTC')).strftime("%Y-%m-%d %H:%M:%S"))
    sql = 'insert into sleep_data (finished_at,set_at,created_at,updated_at) values (?,?,?,?)'
    cur.execute(sql,sleep_datum)
    con.commit()
    return datetime.now(timezone('UTC')).strftime("%Y-%m-%d %H:%M:%S")
def write_finish(created_at):
    print ("will write table")
    sql = "UPDATE sleep_data SET finished_at = '{0}' WHERE created_at = '{1}' ;".format(datetime.now(timezone('UTC')).strftime("%Y-%m-%d %H:%M:%S"),str(created_at))
    print(sql)
    cur.execute(sql)
    con.commit()
    print ("finish write table")
def is_wake():
    while search_wk() is True:
        vlc.MediaPlayer("meka_ge_tokei_den_aramu01.mp3").audio_set_volume(100).play()
        print("ring1")
    print("WAKE UP!!")
def sleeping(created_at):
    now = datetime.now()
    json_d = json_data()
    set_time = [json_d["set_hour"],json_d["set_min"]]
    if now.hour - set_time[0] > 0:
        bef_time = 24 * 60 - now.hour * 60 + now.minute
	aft_time = set_time[0] * 60 + set_time[1]
	ring_time = bef_time + aft_time
    elif now.hour == set_time[0] and now.minute > set_time[1]:
        bef_time = 24 * 60 - now.hour * 60 + now.minute
        aft_time = set_time[0] * 60 + set_time[1]
        ring_time = bef_time + aft_time
    else:
       ring_time = set_time[0] * 60 + set_time[1] - (now.hour * 60 + now.minute)
    pass_time = 0
    while not pass_time == ring_time:
       print("now:" +str(now.hour)+","+ str(now.minute))
       print("ringtime:"+ str(ring_time))
       print("passtime:"+ str(pass_time))
       print(created_at)
       time.sleep(60)
       pass_time += 1
       print("pass 1")
    print("Good Morning!!!!")
    # Wake UP??
    is_wake()

    write_finish(created_at)
    alarm_music("morning.mp3")
def search_sw(i):
    start_t = time.time()
    while num[i] == GPIO.LOW:
            if measure_time(start_t,i) == 1:
                break
            elif measure_time(start_t,i) == 2:
                print("OVERAAA")
                alarm_music("night.mp3")
                created_at = write_start()
                sleeping(created_at)
                break
def search_wk():
    num = { 22:GPIO.input(22), 27:GPIO.input(27), 17:GPIO.input(17), 4:GPIO.input(4) }
    if num[22] is GPIO.LOW or num[27] is GPIO.LOW or num[17] is GPIO.LOW or num[4] is GPIO.LOW:
        return True
    else:
        return False

while True:
    num = { 22:GPIO.input(22), 27:GPIO.input(27), 17:GPIO.input(17), 4:GPIO.input(4) }
    print(num[22])
    print(num[27])
    print(num[17])
    print(num[4])
    print("----")
    search_sw(22)
    search_sw(27)
    search_sw(17)
    search_sw(4)
    print("finish")
    time.sleep(1)
GPIO.cleanup()
