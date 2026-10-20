"""Real-browser checks against the self-contained file:// HTML. pip install playwright"""
from pathlib import Path
import json, hashlib
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,result):
 assert result,name
 checks.append(name)
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,args=['--no-sandbox'])
 context=browser.new_context(viewport={'width':1440,'height':1000},offline=True)
 page=context.new_page();errors=[];network=[]
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.on('request',lambda r:network.append(r.url) if r.url.startswith(('http:','https:')) else None)
 page.goto((ROOT/'Verdant-Flight.html').as_uri())
 snap=lambda:page.evaluate('verdantFlight.snapshot()')
 check('offline menu and title',page.title()=='Verdant Flight' and snap()['state']=='menu')
 page.locator('#start').click();page.wait_for_timeout(400)
 check('start flight',snap()['state']=='playing')
 check('embedded music plays',page.locator('#music').evaluate('(a)=>!a.paused && a.currentTime>0 && a.readyState>=2'))
 check('effects audio context running',snap()['audio']['effectsState']=='running')
 for key,coord,sign in [('ArrowLeft','x',-1),('ArrowRight','x',1),('ArrowUp','y',-1),('ArrowDown','y',1)]:
  before=snap()['ship'][coord];page.keyboard.down(key);page.wait_for_timeout(180);page.keyboard.up(key)
  check('movement '+key,(snap()['ship'][coord]-before)*sign>10)
 page.keyboard.down('z');page.wait_for_timeout(180)
 check('fire creates shots',snap()['shots']>0);page.keyboard.up('z')
 n=len(snap()['orbs']);page.keyboard.press('x');check('orb consumed',len(snap()['orbs'])==n-1)
 page.keyboard.press('p');before=snap()['stageTime'];page.wait_for_timeout(200)
 check('pause freezes simulation',snap()['state']=='paused' and snap()['stageTime']==before)
 check('pause stops music',snap()['audio']['musicPaused'])
 page.locator('#start').click();page.wait_for_timeout(100)
 check('resume restarts music',snap()['state']=='playing' and not snap()['audio']['musicPaused'])
 page.locator('#sound').click();check('mute stops music',snap()['audio']['muted'] and snap()['audio']['musicPaused'])
 page.locator('#sound').click();page.wait_for_timeout(100);check('unmute restarts music',not snap()['audio']['muted'] and not snap()['audio']['musicPaused'])
 page.screenshot(path=str(ROOT/'Verdant-Flight-navegador.jpg'),type='jpeg',quality=90)
 page.evaluate("window.dispatchEvent(new Event('blur'))")
 check('focus loss pauses',snap()['state']=='paused')
 check('no remote requests',not network);check('no desktop script errors',not errors)
 desktop=checks.copy();context.close()
 mobile=browser.new_context(viewport={'width':390,'height':844},is_mobile=True,has_touch=True,offline=True)
 page=mobile.new_page();page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto((ROOT/'Verdant-Flight.html').as_uri());page.locator('#start').tap();page.wait_for_timeout(100)
 check('touch controls visible',page.locator('#orbTouch').is_visible() and page.locator('#soundTouch').is_visible())
 check('mobile no horizontal overflow',page.evaluate('document.documentElement.scrollWidth<=innerWidth'))
 before=snap()['ship'];rect=page.locator('#game').bounding_box()
 x=rect['x']+rect['width']*.35;y=rect['y']+rect['height']*.6
 cdp=mobile.new_cdp_session(page);cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':[{'x':x,'y':y}]})
 page.wait_for_timeout(200);cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':[]})
 check('touch steering and autofire',snap()['ship']['x']<before['x']-10 and snap()['shots']>0)
 n=len(snap()['orbs']);page.locator('#orbTouch').tap();check('touch orb',len(snap()['orbs'])==n-1)
 page.locator('#soundTouch').tap();check('touch mute',snap()['audio']['muted'])
 page.locator('#pauseTouch').tap();check('touch pause',snap()['state']=='paused')
 page.set_viewport_size({'width':844,'height':390})
 check('landscape no overflow',page.evaluate('document.documentElement.scrollWidth<=innerWidth'))
 check('no browser script errors',not errors)
 report={'browser':'Chromium '+browser.version,'mode':'headless; file://; offline contexts','html_sha256':hashlib.sha256((ROOT/'Verdant-Flight.html').read_bytes()).hexdigest(),'passed':len(checks),'checks':checks,'errors':errors,'remote_requests':network,'scope':'Smoke tests of real input, audio playback and responsive layout. No full three-stage completion run. No Safari/Firefox or physical mobile device test. MP3 playback verified; perceived audio quality not assessed by automated tests.'}
 (ROOT/'pruebas-navegador.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 browser.close();print(json.dumps(report,ensure_ascii=False,indent=2))
