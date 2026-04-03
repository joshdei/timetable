#!/usr/bin/env python3
# Fix JSON array - propagate day_name/date, remove header rows
import json

# Load JSON
with open('aligned_timetable.json', 'r') as f:
    data = json.load(f)

# Day mappings
day_mappings = {
    1: {"day_name": "Tuesday", "date": "28th April, 2026"},
    2: {"day_name": "Wednesday", "date": "29th April, 2026"}
    # Add more days as needed: 3: Thursday 30th April, 2026 etc.
}

# Process
fixed_data = []
for item in data:
    day = item.get('day')
    
    # Skip header rows (time strings in slots)
    if (item.get('8_30am') and item['8_30am'].get('code') in ['8:30am', 'Course Code']) or \
       (item.get('11am') and item['11am'].get('code') in ['11am']) or \
       (item.get('2pm') and item['2pm'].get('code') in ['2pm']):
        continue
    
    # Add/fix date field
    item['date'] = day_mappings.get(day, {}).get('date', item.get('date'))
    
    # Propagate day_name
    if day and day in day_mappings:
        item['day_name'] = day_mappings[day]['day_name']
    
    fixed_data.append(item)

# Save fixed JSON
with open('fixed_aligned_timetable.json', 'w') as f:
    json.dump(fixed_data, f, indent=2, ensure_ascii=False)

print(f"✅ Fixed {len(fixed_data)} entries!")
print("Saved to fixed_aligned_timetable.json")
print("\nSample:")
print(json.dumps(fixed_data[:3], indent=2))

