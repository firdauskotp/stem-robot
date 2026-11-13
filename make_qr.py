#!/usr/bin/env python3
"""Make a print-ready QR card for the *public* project website URL."""
import sys
from urllib.parse import urlparse
from pathlib import Path
import qrcode
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A5

def main():
 if len(sys.argv)!=2 or not sys.argv[1].startswith('https://'):
  raise SystemExit('Usage: python make_qr.py https://your-public-domain/stem-robot/')
 url=sys.argv[1].strip()
 if not urlparse(url).netloc: raise SystemExit('Invalid public website URL')
 qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=14,border=4)
 qr.add_data(url);qr.make(fit=True)
 qrim=qr.make_image(fill_color='#711b2d',back_color='white').convert('RGB')
 size=(1400,1850); card=Image.new('RGB',size,'#fffaf1');d=ImageDraw.Draw(card)
 # Standard fonts available on most computers; font fallback is safe.
 def font(n,bold=False):
  paths=['/usr/share/fonts/truetype/dejavu/DejaVuSans'+('-Bold' if bold else '')+'.ttf','arial.ttf']
  for p in paths:
   try:return ImageFont.truetype(p,n)
   except OSError:pass
  return ImageFont.load_default()
 crest=Path(__file__).parent/'assets/qosmo-crest.png'
 if crest.exists():
  logo=Image.open(crest).convert('RGB');logo.thumbnail((260,300));card.paste(logo,((size[0]-logo.width)//2,35))
 d.text((size[0]//2,365),'SMART RUBBISH DETECTION',font=font(53,True),fill='#651626',anchor='mm')
 d.text((size[0]//2,425),'QOSMO STEM PROJECT',font=font(33,True),fill='#91652f',anchor='mm')
 qrim.thumbnail((900,900));card.paste(qrim,((size[0]-qrim.width)//2,505))
 d.text((size[0]//2,1508),'SCAN TO EXPLORE',font=font(65,True),fill='#651626',anchor='mm')
 d.text((size[0]//2,1570),'How it works  •  Limitations  •  Future ideas',font=font(29),fill='#64545a',anchor='mm')
 # Don't print a misleading shortened address; small readable one-line URL if possible.
 safe=url if len(url)<65 else url[:62]+'…'
 d.text((size[0]//2,1702),safe,font=font(24),fill='#64545a',anchor='mm')
 out=Path(__file__).parent
 png=out/'Qosmo_STEM_QR.png';pdf=out/'Qosmo_STEM_QR.pdf';card.save(png)
 c=canvas.Canvas(str(pdf),pagesize=A5)
 w,h=A5;c.drawImage(ImageReader(card),0,0,width=w,height=h);c.showPage();c.save()
 print('Created:',png,'and',pdf)
if __name__=='__main__':main()
