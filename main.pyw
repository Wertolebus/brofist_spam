import webbrowser as wb
import pyautogui as pgui
import keyboard as k
import dearpygui.dearpygui as dpg
import requests as req
from apscheduler.schedulers.background import BackgroundScheduler


from time import sleep

def get_browser():
    import winreg
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\\Microsoft\\Windows\\Shell\\Associations\\UrlAssociations\\http\\UserChoice") as key:
        browser = winreg.QueryValueEx(key, 'Progid')[0]
        return browser

def get_delay():
    return dpg.get_value('clickDelay')

ver = 'public version 1.0'

def cheat_panel():
    if get_browser() == 'ChromeHTML':
        pgui.moveTo(0, 150)
        sleep(get_delay())
        pgui.click(18, 207)
        sleep(get_delay())
        pgui.click(18, 260)
    if get_browser() == 'MSEdgeHTM':
        pgui.moveTo(0, 150)
        sleep(get_delay())
        pgui.click(18, 207)
        sleep(get_delay())
        pgui.click(18, 260)

def sandbox(region, room):
    if region == "ru":
        reg_coords = (1392, 816)
        if get_browser() == 'ChromeHTML':
            if room == 1:
                room_coords = (1420, 927)
            elif room == 2:
                room_coords = (1420, 967)
        if get_browser() == 'MSEdgeHTM':
            if room == 1:
                room_coords = (1420, 927)
            elif room == 2:
                room_coords = (1420, 967)
    elif region == "eng":
        reg_coords = (1440, 815)
        if get_browser() == 'ChromeHTML':
            reg_coords = (1440, 815)
            room_coords = (1420, 927)
        if get_browser() == 'MSEdgeHTM':
            if room == 1:
                room_coords = (1420, 927)
        
   
    room_button_coords = (1196, 887)
    
    sleep(get_delay())
    cheat_panel()
    sleep(get_delay())
    pgui.leftClick(reg_coords)
    sleep(get_delay())
    pgui.leftClick(room_button_coords)
    sleep(get_delay())
    pgui.leftClick(room_coords)

def _2pa(region, room):  
    wb.open_new_tab("http://brofist.io/modes/twoPlayer/c/index.html")
    if region == "ru":
        reg_coords = (1392, 816)
        if get_browser() == 'ChromeHTML':
            if room == 1:
                room_coords = (1420, 847)
            elif room == 2:
                room_coords = (1417, 882)
            elif room == 3:
                room_coords = (1422, 922)
            elif room == 4:
                room_coords = (1419, 957)
            elif room == 5:
                room_coords = (1427, 996)
        if get_browser() == 'MSEdgeHTM':
            if room == 1:
                room_coords = (1420, 813)
            elif room == 2:
                room_coords = (1417, 848)
            elif room == 3:
                room_coords = (1422, 885)
            elif room == 4:
                room_coords = (1419, 922)
            elif room == 5:
                room_coords = (1427, 958)
    if region == "eng":
        reg_coords = (1440, 815)
        if get_browser() == 'ChromeHTML':
            if room == 1:
                room_coords = (1420, 847)
            elif room == 2:
                room_coords = (1417, 882)
            elif room == 3:
                room_coords = (1422, 922)
            elif room == 4:
                room_coords = (1419, 957)
            elif room == 5:
                room_coords = (1427, 996)
        if get_browser() == 'MSEdgeHTM':
            if room == 1:
                room_coords = (1420, 813)
            elif room == 2:
                room_coords = (1417, 848)
            elif room == 3:
                room_coords = (1422, 885)
            elif room == 4:
                room_coords = (1419, 922)
            elif room == 5:
                room_coords = (1427, 958)
    
    room_button_coords = (1196, 887)
    
    sleep(get_delay())
    cheat_panel()
    sleep(get_delay())
    pgui.leftClick(reg_coords)
    sleep(get_delay())
    pgui.leftClick(room_button_coords)
    sleep(get_delay())
    pgui.scroll(-100)
    sleep(get_delay())
    pgui.leftClick(room_coords)

def hns(region, room):
    wb.open_new_tab("http://brofist.io/modes/hideAndSeek/c/index.html")
    if region == "ru":
        reg_coords = (1392, 816)
        if get_browser() == 'ChromeHTML':
            if room == 1: 
                room_coords = (1420, 930)
            elif room == 2:
                room_coords = (1419, 967)
            elif room == 3:
                room_coords = (1419, 1004)
        if get_browser() == 'MSEdgeHTM':
            if room == 1: 
                room_coords = (1420, 930)
            elif room == 2:
                room_coords = (1419, 967)
            elif room == 3:
                room_coords = (1419, 1004)
    
    if region == "eng":
        reg_coords = (1440, 815)
        if get_browser() == 'ChromeHTML':
            if room == 1: 
                room_coords = (1420, 930)
            elif room == 2:
                room_coords = (1419, 967)
            elif room == 3:
                room_coords = (1419, 1004)
        if get_browser() == 'MSEdgeHTM':
            if room == 1: 
                room_coords = (1420, 930)
            elif room == 2:
                room_coords = (1419, 967)
            elif room == 3:
                room_coords = (1419, 1004)
            
    room_button_coords = (1196, 887)
    
    sleep(get_delay())
    cheat_panel()
    sleep(get_delay())
    pgui.leftClick(reg_coords)
    sleep(get_delay())
    pgui.leftClick(room_button_coords)
    sleep(get_delay())
    pgui.leftClick(room_coords)



def GUI():
    dpg.create_context()
    dpg.create_viewport(width=600, x_pos=(1920-390)//2, y_pos=100, height=465, max_width=406, max_height=465, title='Brofist server spam bot', resizable=False, always_on_top=True)
    dpg.setup_dearpygui()
    
    with dpg.window(label='Brofist Servers Activity', no_close=True, width=193, height=425, max_size=(193, 425), no_move=True, no_resize=True, no_scrollbar=True):
        stats = dpg.add_text(parser(), tag='stats')
        def temp():
            dpg.set_value(stats, parser())
            
        updateStatistic = BackgroundScheduler()
        getDelay = BackgroundScheduler()
        updateStatistic.add_job(id='Sheduled task', func=temp, trigger='interval', seconds=0.25)
        getDelay.add_job(id='Sheduled task', func=get_delay, trigger='interval', seconds=0.25)
        updateStatistic.start()
        getDelay.start()
            
            
        # dpg.add_button(label="Update" ,callback=lambda: temp)
        
    with dpg.window(tag="Primary"):
        def start():
            i = dpg.get_value('tabs')
            mode = dpg.get_value('gamemode')
            reg = str(dpg.get_value('region')).lower()
            room = dpg.get_value('room')
            
            if i > 0:
                if mode == 'Sandbox':
                    dpg.disable_item('startButton')
                    dpg.disable_item('clickDelay')
                    for x in range(i):
                        if not k.is_pressed('q'):
                            dpg.show_item('loadingText')
                            dpg.show_item('loadingIndicator')
                            dpg.set_value('loadingText', str(i-x).zfill(3))
                            sandbox(reg, room)
                        else: break
                if mode == '2PA':
                    for x in range(i):
                        dpg.disable_item('clickDelay')
                        dpg.disable_item('startButton')
                        if not k.is_pressed('q'):
                            dpg.show_item('loadingText')
                            dpg.show_item('loadingIndicator')
                            dpg.set_value('loadingText', str(i-x).zfill(3))
                            _2pa(reg, room)
                        else: break
                if mode == 'Hide and Seek':
                    for x in range(i):
                        dpg.disable_item('startButton')
                        dpg.disable_item('clickDelay')
                        if not k.is_pressed('q'):
                            dpg.show_item('loadingText')
                            dpg.show_item('loadingIndicator')
                            dpg.set_value('loadingText', str(i-x).zfill(3))
                            hns(reg, room)
                        else: break
            dpg.hide_item('loadingText')
            dpg.hide_item('loadingIndicator')
            dpg.enable_item('startButton')
            dpg.enable_item('clickDelay')
            
        
        dpg.add_button(label='Start', pos=(275, 170), callback=lambda : start(), tag='startButton')
        dpg.add_text('Hold q to stop', pos=(245, 190))
        dpg.add_text(str(dpg.get_value('tabs')).zfill(3), pos=(283, 307), show=False, tag='loadingText')
        dpg.add_loading_indicator(pos=(270, 290), radius=5, style=1, show=False, tag='loadingIndicator')
        
        dpg.add_text(ver, pos=(250, 399), color=(67, 67, 67), )
    
    with dpg.window(label='Configuration', pos=(192, 0), width=214, height=165, no_close=True, max_size=(214, 175), no_move=True, no_resize=True):
        dpg.add_input_int(label='Tabs', pos=(70, 350-250), width=75, min_value=0, tag='tabs')
        dpg.add_input_int(label='Room', pos=(70, 325-250), width=75, min_value=0, tag='room')
        dpg.add_slider_float(label='Click Delay', width=100, min_value=0.3, max_value=1, pos=(10, 375-250), tag='clickDelay')   
        dpg.add_combo(('Ru', 'Eng'), label='Region', width=50, pos=(80, 300-250), tag='region')
        dpg.add_combo(('Sandbox', '2PA', 'Hide and Seek'), label='Gamemode', width=125, pos=(5, 275-250), tag='gamemode')
    
    dpg.set_primary_window('Primary', True)
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
    

def parser():
    # pass
    
    r = req.get('http://172.104.138.121/getGamingServersInfo')
    servers = eval(r.text.strip('][').replace("true", 'True').replace('false', 'False'))
    params = ['location', 'ip', 'mode', 'lan', 'rooms', 'connected', 'uptime', 'socketsCount']
    needed_params = ['mode','lan','rooms']
    result = ''
    for i in range(7):
        for j in range(len(needed_params)):
            temp = needed_params[j] + " : " + str(servers[i][needed_params[j]]).replace('[', '').replace(']', '')
            result = result + temp + "\n"
        result = result + '--------------------' + '\n'
    
    return result
    
GUI()