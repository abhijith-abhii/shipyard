import hashlib,pytest
from core import analyze

def test_known_digest():assert analyze({'text':'hello'})['answer']==hashlib.sha256(b'hello').hexdigest()
def test_unicode_bytes():assert analyze({'text':'é'})['metrics']['UTF-8 bytes']==2
@pytest.mark.parametrize('text',['','x'*100001,None])
def test_invalid(text):
 with pytest.raises(ValueError):analyze({'text':text})
