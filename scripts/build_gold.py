import json, pathlib, re, collections, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from topics2 import is_english, CACHE
NEW={
 "Economics":{
  "National Income and Related Aggregates":[r'gross value added', r'net national product', r'\bfactor cost\b', r'gdp deflator', r'circular flow', r'net domestic product', r'consumption of fixed capital'],
  "Money and Banking":[r'cash reserve ratio', r'statutory liquidity', r'\brepo rate\b', r'reverse repo', r'money multiplier', r'high[- ]powered money', r'\bcredit creation\b', r'legal tender'],
  "Determination of Income and Employment":[r'investment multiplier', r'propensity to consume', r'propensity to save', r'deficient demand', r'excess demand', r'involuntary unemployment', r'\bex[- ]ante\b', r'break[- ]even'],
  "Government Budget and the Economy":[r'fiscal deficit', r'revenue deficit', r'primary deficit', r'revenue expenditure', r'capital receipts', r'government budget'],
  "Balance of Payments":[r'balance of payments', r'current account', r'capital account', r'foreign exchange rate', r'\bdevaluation\b', r'depreciation of.{0,12}currency', r'autonomous transactions'],
  "Current Challenges facing Indian Economy":[r'human capital formation', r'poverty line', r'self[- ]help group', r'sustainable development', r'\borganic farming\b', r'\binformal sector\b', r'disguised unemployment'],
 },
 "Psychology":{
  "I Variations in Psychological Attributes":[r'intelligence quotient', r'\biq\b', r'triarchic', r'multiple intelligences', r'\baptitude\b', r'psychometric', r'\bsternberg\b'],
  "II Self and Personality":[r'self[- ]efficacy', r'self[- ]esteem', r'trait theory', r'defence mechanism', r'projective techniq', r'big five', r'\bfreud', r'\bego\b'],
  "III Meeting Life Challenges":[r'\bcoping\b', r'\bburnout\b', r'\beustress\b', r'general adaptation syndrome', r'life skills', r'\bstressor'],
  "IV Psychological Disorders":[r'schizophrenia', r'\bphobia', r'obsessive[- ]compulsive', r'bipolar', r'\bautis', r'dissociative', r'anxiety disorder', r'\bdelusion'],
  "V Therapeutic Approaches":[r'psychotherapy', r'cognitive behaviour therapy', r'systematic desensitis', r'client[- ]cent', r'\brehabilitation\b', r'\bcatharsis\b'],
  "VI Attitude and Social Cognition":[r'cognitive dissonance', r'\bprejudice\b', r'\bstereotyp', r'attribution', r'attitude (change|formation)', r'\bschema\b'],
  "VII Social Influence and Group Processes":[r'\bconformity\b', r'\bobedience\b', r'group polaris', r'social loafing', r'\bbystander\b', r'\bin[- ]group\b'],
 }}
rows=[r for r in json.loads(pathlib.Path(CACHE).read_text()) if r.get("question") and is_english(r["question"]) and r.get("marks")]
by=collections.defaultdict(list)
for r in rows: by[r["subject"]].append(r)
HERE=pathlib.Path(__file__).parent
old=json.loads((HERE/"gold_patterns.json").read_text())
for subj,g in NEW.items():
    lab=collections.Counter(); amb=0
    for q in by[subj]:
        t=q["question"].lower()
        hit=[u for u,ps in g.items() if any(re.search(p,t) for p in ps)]
        if len(hit)==1: lab[hit[0]]+=1
        elif len(hit)>1: amb+=1
    tot=sum(lab.values())
    print(f"\n{subj}: {tot} gold from {len(by[subj])} questions ({tot/len(by[subj]):.0%}); {amb} ambiguous dropped")
    for u,n in lab.most_common(): print(f"   {n:5d}  {u}")
    if tot and min(lab.values() or [0])==0:
        print("   WARNING: some units have zero gold questions")
    for u in g:
        if lab[u]==0: print(f"   ZERO gold: {u}")
old.update(NEW)
(HERE/"gold_patterns.json").write_text(json.dumps(old, indent=1))
print("\ngold_patterns.json covers:", list(old))
