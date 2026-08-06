# Question-bank schema

Built locally by `scripts/build_bank.py`; the question text itself is CBSE copyright and is not redistributed here.


## `questions` — 960 rows

| column | type |
|---|---|
| subject | VARCHAR |
| qp_code | VARCHAR |
| paper_set | VARCHAR |
| architecture | VARCHAR |
| max_marks_paper | BIGINT |
| section | VARCHAR |
| block | VARCHAR |
| q_no | BIGINT |
| marks | BIGINT |
| block_answer_any | BIGINT |
| block_out_of | BIGINT |
| q_type | VARCHAR |
| has_figure | BOOLEAN |
| has_internal_choice | BOOLEAN |
| employability | BOOLEAN |
| question | VARCHAR |
| options | VARCHAR |
| full_text | VARCHAR |

## `papers` — 32 rows

| column | type |
|---|---|
| subject | VARCHAR |
| qp_code | VARCHAR |
| paper_set | VARCHAR |
| architecture | VARCHAR |
| max_marks_paper | BIGINT |
| questions_set | HUGEINT |
| questions_to_attempt | HUGEINT |
| attemptable_marks | HUGEINT |

## `past_paper_questions` — 30,734 rows

| column | type |
|---|---|
| subject | VARCHAR |
| source | VARCHAR |
| paper_id | VARCHAR |
| paper_file | VARCHAR |
| year | BIGINT |
| exam | VARCHAR |
| section | VARCHAR |
| q_no | BIGINT |
| marks | BIGINT |
| marks_source | VARCHAR |
| q_type | VARCHAR |
| has_figure | BOOLEAN |
| has_internal_choice | BOOLEAN |
| is_english | BOOLEAN |
| question | VARCHAR |
| options | VARCHAR |
| full_text | VARCHAR |

## `recurring_topics` — 56 rows

| column | type |
|---|---|
| subject | VARCHAR |
| phrase | VARCHAR |
| kind | VARCHAR |
| years | BIGINT |
| year_list | VARCHAR |
| papers | BIGINT |
| marks | BIGINT |
| example | VARCHAR |

## `subject_repetition` — 11 rows

| column | type |
|---|---|
| subject | VARCHAR |
| papers | BIGINT |
| questions | BIGINT |
| high_mark_questions | BIGINT |
| high_marks | BIGINT |
| repetition_index | DOUBLE |
| years | VARCHAR |
| n_recurring_topics | BIGINT |
| n_recurring_formulas | BIGINT |