#!/usr/bin/env python3
"""Validate WordLoop v4.1 CET-6 release files using only Python stdlib."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path


def fail(errors, message): errors.append(message)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--public',type=Path,default=Path('public'))
    a=p.parse_args(); root=a.public
    lex=json.loads((root/'data/cet6/cet6_lexicon.json').read_text(encoding='utf-8'))
    payload=json.loads((root/'data/cet6/cet6_cards_100.json').read_text(encoding='utf-8'))
    manifest=json.loads((root/'data/library_manifest.json').read_text(encoding='utf-8'))
    errors=[]
    entries=lex.get('entries',[]); cards=payload.get('cards',[])
    if len(entries)!=5407: fail(errors,f'Expected 5407 entries, got {len(entries)}')
    if len(cards)!=100: fail(errors,f'Expected 100 cards, got {len(cards)}')
    if len({e.get('id') for e in entries})!=len(entries): fail(errors,'Duplicate lexicon ids')
    if len({e.get('word','').lower() for e in entries})!=len(entries): fail(errors,'Duplicate lexicon words')
    by_word={e.get('word','').lower():e for e in entries}
    if len({c.get('id') for c in cards})!=len(cards): fail(errors,'Duplicate card ids')
    if len({c.get('word','').lower() for c in cards})!=len(cards): fail(errors,'Duplicate card words')
    required=['id','libraryId','word','pronunciation','partOfSpeech','meaningZh','sentenceEn','sentenceZh','clozePrefix','clozeAnswer','clozeSuffix','usageNotes']
    for c in cards:
        label=c.get('word') or c.get('id') or '<unknown>'
        for field in required:
            if not c.get(field): fail(errors,f'{label}: missing {field}')
        if c.get('libraryId')!='cet6': fail(errors,f'{label}: wrong libraryId')
        if c.get('clozePrefix','')+c.get('clozeAnswer','')+c.get('clozeSuffix','')!=c.get('sentenceEn',''):
            fail(errors,f'{label}: cloze does not reconstruct sentence')
        answer=c.get('clozeAnswer','')
        matches=re.findall(rf'(?<![A-Za-z]){re.escape(answer)}(?![A-Za-z])',c.get('sentenceEn',''),flags=re.I)
        if len(matches)!=1: fail(errors,f'{label}: answer occurrence count {len(matches)}')
        if answer not in c.get('acceptedAnswers',[]): fail(errors,f'{label}: target missing from acceptedAnswers')
        if not c.get('collocations'): fail(errors,f'{label}: no collocations')
        if not c.get('relatedExpressions'): fail(errors,f'{label}: no related expressions')
        if not c.get('wordFamily'): fail(errors,f'{label}: no word family')
        if not c.get('extraExamples'): fail(errors,f'{label}: no extra examples')
        base=by_word.get(c.get('word','').lower())
        if not base: fail(errors,f'{label}: not found in base lexicon')
        elif 'cet6' not in base.get('examTags',[]): fail(errors,f'{label}: base entry lacks cet6 tag')
    cet6=next((x for x in manifest.get('libraries',[]) if x.get('id')=='cet6'),None)
    if not cet6: fail(errors,'Manifest missing cet6')
    else:
        if cet6.get('baseEntryCount')!=5407: fail(errors,'Manifest baseEntryCount mismatch')
        if cet6.get('cardCount')!=100: fail(errors,'Manifest cardCount mismatch')
        if cet6.get('status')!='ready': fail(errors,'Manifest cet6 is not ready')
    if errors:
        print('\n'.join('ERROR: '+x for x in errors)); raise SystemExit(1)
    overlap=sum('cet4' in e.get('examTags',[]) for e in entries)
    print('PASS')
    print(f'Lexicon entries: {len(entries)}')
    print(f'CET-4 overlap: {overlap}')
    print(f'CET-6 entries without CET-4 tag: {len(entries)-overlap}')
    print(f'Curated cards: {len(cards)}')
    print('All card ids/words unique; cloze reconstruction and required fields passed.')

if __name__=='__main__': main()
