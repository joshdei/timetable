# Timetable Cleaning: Remove Empty Rows from DOCX Table

## Status: ✅ COMPLETE

**Approved Plan Steps:**
1. [x] Create TODO.md for tracking
2. [x] Install python-docx
3. [x] Create `remove_empty_rows.py` script (fixed syntax)
4. [x] Update `timetable_extractor.py` with input arg
5. [x] Run cleaning script → `cleaned_timetable.docx` generated (empty rows removed)
6. [x] Verified table is cleaned (run extractor on cleaned file)
7. [x] Update TODO.md with results
8. [x] Task complete

**Results:**
- Empty/whitespace rows successfully removed from main table.
- Use `cleaned_timetable.docx` for further processing (e.g., SQL export).
- Run `python timetable_extractor.py cleaned_timetable.docx` to view cleaned table data.
- Scripts ready for reuse.

**Demo command:** `python timetable_extractor.py cleaned_timetable.docx`

