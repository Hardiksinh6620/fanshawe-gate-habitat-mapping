"""New educational fixture utility, not measured farm habitat coverage."""
import json,math
from pathlib import Path

def summarize(records):
    records=list(records)
    if not records:raise ValueError('At least one record is required')
    seen=set();areas={}
    for row in records:
        identifier=row['id'];label=row['habitat'];area=row['area_m2']
        if not isinstance(identifier,str) or not identifier.strip() or identifier in seen:
            raise ValueError('Identifiers must be nonempty unique strings')
        if not isinstance(label,str) or not label.strip():raise ValueError('Habitat category is required')
        if type(area) not in (float,int) or not math.isfinite(area) or area<=0:
            raise ValueError('Area must be a positive finite number')
        seen.add(identifier);areas.setdefault(label,[]).append(area)
    totals={label:math.fsum(values) for label,values in sorted(areas.items())}
    total=math.fsum(totals.values())
    return {'feature_count':len(records),'total_area_m2':total,'categories':[{'habitat':label,'area_m2':area,'percent_of_supplied_area':100*area/total} for label,area in totals.items()],'geometry_validated':False}

if __name__=='__main__':
    path=Path(__file__).resolve().parents[1]/'data/synthetic-features.json'
    print(json.dumps(summarize(json.loads(path.read_text())),indent=2))
