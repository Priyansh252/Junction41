#!/usr/bin/env python3
"""Junction 41 — static site builder.
Usage:  python3 source/build.py --name "Your Name" --reg 24XXX0000 --email you@vitstudent.ac.in
Writes the .html files into the project root (one level above this folder)."""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(__file__))

ap = argparse.ArgumentParser()
ap.add_argument('--name', default='Aditya Varma')
ap.add_argument('--reg', default='24BCE0000')
ap.add_argument('--email', default='aditya.varma@vitstudent.ac.in')
ap.add_argument('--dept', default='School of Computer Science and Engineering')
cfg = ap.parse_args()
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

NAV = [('index.html', 'Home'), ('routes.html', 'Routes'), ('book.html', 'Book'),
       ('trips.html', 'My Trips'), ('status.html', 'Live'), ('journal.html', 'Journal'), ('about.html', 'About')]

def sub(s):
    return (s.replace('@@NAME@@', cfg.name).replace('@@REG@@', cfg.reg)
             .replace('@@EMAIL@@', cfg.email).replace('@@DEPT@@', cfg.dept))

def page(fname, title, body, nav=None, no=None, heading=None, blurb='', tags=(), css='', js=(), bare=False):
    """bare=True -> no site header/footer (pages that supply their own header)."""
    links = ''.join(f'<a href="{h}"{" class=on" if h == nav else ""}>{t}</a>' for h, t in NAV)
    head = f'''<div class="util"><div class="wrap"><span>Boarding from <strong>Chennai Central</strong></span>
  <span><a href="status.html">Helpline 1800-41-4141</a> · <a href="account.html">Sign in</a> · <a href="summary.html">Basket <b class="cnt">1</b></a></span></div></div>
<header class="site-head"><div class="wrap">
  <a class="logo" href="index.html"><span class="lamp"></span>Junction <b>41</b></a>
  <nav class="nav" id="nav">{links}</nav>
  <a class="btn" href="book.html">Book a seat</a>
  <button class="menu-btn" id="menuBtn" aria-label="Menu">MENU</button></div></header>'''
    plate = ''
    if heading:
        plate = f'''<div class="plate"><div class="wrap"><div class="pf-no">{no}</div><div>
  <span class="eyebrow">{title}</span><h1>{heading}</h1><p>{blurb}</p>
  <div>{''.join(f'<span class="tag">{t}</span>' for t in tags)}</div></div></div></div><div class="rails"></div>'''
    foot = '''<footer class="site-foot"><div class="wrap"><div><strong class="mono">Junction 41 · VIT Line</strong><br>
  Designed and built by @@NAME@@ (@@REG@@) · @@DEPT@@</div>
  <div class="mono">More: <a href="fest.html">Rail Fest</a> · <a href="careers.html">Careers</a> · <a href="assist.html">Assistance</a> · <a href="account.html">Sign in</a></div>
  <div class="mono">Mail the station master:<br><a href="mailto:@@EMAIL@@">@@EMAIL@@</a></div></div></footer>'''
    scripts = ''.join(f'<script src="js/{j}.js"></script>' for j in ['site'] + list(js))
    html = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · Junction 41</title><link rel="stylesheet" href="css/style.css">
<style>{css}</style></head><body>
{'' if bare else head}{plate}
{body}
{'' if bare else foot}{scripts}</body></html>'''
    with open(os.path.join(ROOT, fname), 'w', encoding='utf-8') as f:
        f.write(sub(html))

import pages_a, pages_b, pages_c
for mod in (pages_a, pages_b, pages_c):
    mod.build(page)
print('Built pages into', ROOT)
