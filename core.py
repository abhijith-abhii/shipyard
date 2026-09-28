import hashlib,os

def analyze(p):
 text=p.get('text','hello')
 if not isinstance(text,str) or not 1<=len(text)<=100000:raise ValueError('Payload must contain 1–100,000 characters')
 raw=text.encode('utf-8')
 return dict(metrics={'Release':os.environ.get('APP_VERSION','local-dev'),'UTF-8 bytes':len(raw),'Lines':len(text.splitlines())},answer=hashlib.sha256(raw).hexdigest(),details={'algorithm':'SHA-256','encoding':'UTF-8','purpose':'integrity fingerprint; not password hashing','release':os.environ.get('APP_VERSION','local-dev')})
