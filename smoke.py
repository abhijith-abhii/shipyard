import json,urllib.request,sys,time
url=sys.argv[1] if len(sys.argv)>1 else 'http://127.0.0.1:8080'
for _ in range(30):
 try:
  assert json.load(urllib.request.urlopen(url+'/health',timeout=2))['status']=='ok';break
 except Exception:time.sleep(1)
else:raise SystemExit('Service failed readiness check')
req=urllib.request.Request(url+'/api/run',data=json.dumps({'text':'hello'}).encode(),headers={'Content-Type':'application/json','X-Portfolio-Request':'1'})
d=json.load(urllib.request.urlopen(req,timeout=3));assert d['answer']=='2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
print('Readiness and known-digest smoke checks passed')
